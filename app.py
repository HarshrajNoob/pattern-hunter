
import base64
import requests
from flask import Flask, jsonify, render_template, request

import random
import json

app = Flask(__name__)

MISSIONS = [
    {
        "title": "Find Nature's Symmetry",
        "pattern": "Symmetry",
        "description": "Find a leaf, flower, or other natural object "
                       "whose two sides look similar.",
        "question": "If you divide it down the middle, what looks similar?"
    },
    {
        "title": "Hunt for Spirals",
        "pattern": "Spiral",
        "description": "Look for a spiral-like pattern in a plant, "
                       "shell, or another natural object.",
        "question": "Where does the spiral begin, and how does it curve?"
    },
    {
        "title": "Spot Repeating Patterns",
        "pattern": "Repetition",
        "description": "Find repeated shapes or lines in leaves, "
                       "tree bark, grass, or seed heads.",
        "question": "Which shape or feature repeats most often?"
    },
    {
        "title": "Discover Fractals",
        "pattern": "Branching",
        "description": "Look for a branching structure in a tree, "
                       "fern, or leaf veins.",
        "question": "Do the smaller branches resemble the larger ones?"
    },
    {
        "title": "Follow the Lines",
        "pattern": "Lines",
        "description": "Find natural lines in leaf veins, tree bark, "
                       "or the shadows cast by plants.",
        "question": "Which direction do the lines travel?"
    },
    {
        "title": "Find Nature's Geometry",
        "pattern": "Geometry",
        "description": "Look for approximate circles, triangles, "
                       "or other geometric shapes in nature.",
        "question": "What makes you recognize that shape?"
    }
]


def generate_ai_mission():
    prompt = """
Create ONE creative, beginner-friendly nature observation mission.

Choose an interesting pattern such as symmetry, spirals, branching,
repetition, geometry, or lines.

Make the mission practical for someone observing plants, leaves,
flowers, trees, clouds, or other natural objects.

Return ONLY valid JSON with these exact keys:
{
  "title": "Short, interesting mission title",
  "pattern": "Pattern category",
  "description": "One or two sentences describing what to find",
  "question": "One question to help the observer think"
}

Make the mission different and creative. Avoid generic wording.
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.9
            }
        },
        timeout=120
    )

    response.raise_for_status()
    result = response.json()
    mission = json.loads(result["response"])

    required_keys = {"title", "pattern", "description", "question"}
    if not required_keys.issubset(mission):
        raise ValueError("AI returned an incomplete mission.")

    return {key: str(mission[key]) for key in required_keys}

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/api/mission")
def get_mission():
    try:
        mission = generate_ai_mission()
        mission["source"] = "AI"
        return jsonify(mission)

    except (requests.RequestException, ValueError, KeyError, TypeError):
        app.logger.exception("AI mission generation failed")

        mission = random.choice(MISSIONS).copy()
        mission["source"] = "fallback"
        return jsonify(mission)



app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

@app.route("/api/analyze-image", methods=["POST"])
def analyze_image():
    uploaded_file = request.files.get("image")

    if not uploaded_file or not uploaded_file.filename:
        return jsonify({"error": "Please select an image."}), 400

    allowed_types = {
        "image/jpeg",
        "image/png",
        "image/webp"
    }

    if uploaded_file.mimetype not in allowed_types:
        return jsonify({
            "error": "Please upload a JPG, PNG, or WebP image."
        }), 400

    image_bytes = uploaded_file.read()

    if not image_bytes:
        return jsonify({"error": "The selected image is empty."}), 400

    encoded_image = base64.b64encode(image_bytes).decode("utf-8")

    prompt = """
    Analyze the actual image provided to you.

First, describe 3 specific visual details that are clearly visible
in this image. Focus on shapes, lines, textures, repetition,
symmetry, branching, spirals, or geometric structures.

Then answer these questions:
1. What natural object or structure is visible?
2. What pattern can you identify, if any?
3. What visual evidence supports your conclusion?
4. What details are uncertain or difficult to identify?

Be specific to this particular image. Do not invent details.
If no clear pattern is visible, say so honestly.
Use simple English and keep the answer under 120 words.
    """

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "moondream",
                "prompt": prompt,
                "images": [encoded_image],
                "stream": False
            },
            timeout=180
        )

        response.raise_for_status()
        result = response.json()
        analysis = result.get("response", "").strip()

        if not analysis:
            raise ValueError("The model returned an empty response.")

        return jsonify({"analysis": analysis})

    except (requests.RequestException, ValueError, KeyError):
        app.logger.exception("Image analysis failed")
        return jsonify({
            "error": (
                "Image analysis failed. Check that Ollama is running "
                "and the moondream model is available."
            )
        }), 503


if __name__ == "__main__":
    app.run(debug=True)
