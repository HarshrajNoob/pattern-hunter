#🌿 Pattern Hunter
An offline-first AI companion for discovering patterns hidden in
nature.
Pattern Hunter turns a walk outdoors into a small exploration mission.
It uses locally running AI models to suggest what to observe, analyze a
photo of a natural object, and help you save discoveries in a personal
Nature Journal.
✨ Features
AI-generated missions: Creative, beginner-friendly nature
observation missions powered by Llama 3.2 1B.
Photo pattern analysis: Upload a nature photo and ask Moondream
to describe visible details and patterns.
Nature Journal: Save observations and AI analysis in your
browser.
Local-first AI: After setup, AI inference runs locally through
Ollama.
Simple web interface: Built with HTML, CSS, and JavaScript.
Image validation: JPG/JPEG, PNG, and WebP support; maximum
upload size is 5 MB.
> **Note:** AI descriptions are suggestions to support observation, not
> scientific verification.
🧰 Tech Stack
Backend: Python, Flask
Frontend: HTML, CSS, JavaScript
Local AI runtime: Ollama
Mission generation: `llama3.2:1b`
Image understanding: `moondream`
Journal storage: Browser `localStorage`
🚀 Getting Started
Prerequisites
Python 3.10 or newer
Ollama
Git (optional)
1. Clone the repository
``` powershell
git clone https://github.com/HarshrajNoob/pattern-hunter.git
cd pattern-hunter
```
You can also download the repository as a ZIP and extract it.
2. Create and activate a virtual environment
On Windows PowerShell:
``` powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install flask requests
```
If PowerShell blocks activation, run the environment's Python directly:
``` powershell
.\.venv\Scripts\python.exe -m pip install flask requests
```
3. Download the local AI models
``` powershell
ollama pull llama3.2:1b
ollama pull moondream
```
The initial downloads require internet access and may take a while. Keep
Ollama installed and running when you use the app.
4. Start Pattern Hunter
With the virtual environment activated:
``` powershell
python app.py
```
Or, without activating it:
``` powershell
.\.venv\Scripts\python.exe app.py
```
Open the local address printed by Flask---usually
`http://127.0.0.1:5000`.
🪴 How to Use It
Open Pattern Hunter in your browser.
Generate a nature mission.
Find a natural object such as a leaf, flower, or tree.
Choose a JPG/JPEG, PNG, or WebP image up to 5 MB.
Upload it and review the AI's description of visible patterns.
Save the analysis to your Nature Journal and add your own
observation.
Revisit your journal in the same browser.
📴 Offline Behavior
After Ollama and both models have been installed and downloaded, AI
mission generation and image analysis can run locally without sending
images to a hosted AI service.
Internet is needed initially to install dependencies and download
models.
Ollama must be running for AI-powered features.
The Nature Journal uses browser `localStorage`; entries are tied to
that browser and device. Clearing browser data may remove them.
If local AI mission generation fails, the app may use its built-in
fallback missions.
🗂️ Project Structure
``` text
pattern-hunter/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .gitignore
└── README.md
```

🧪 Troubleshooting
`ollama` is not recognized
Make sure Ollama is installed. Restart PowerShell and check:
``` powershell
ollama --version
```
An AI feature does not respond
Check that Ollama is running and both models are installed:
``` powershell
ollama list
```
If needed, run `ollama pull llama3.2:1b` or `ollama pull moondream`.
Flask dependencies are missing
``` powershell
python -m pip install flask requests
```
Image analysis fails
Check the image format and 5 MB limit, and confirm that `moondream` is
installed and Ollama is running.
🔒 Privacy
Image analysis is designed to use the local Ollama service on your
machine. The Nature Journal is stored in browser local storage. Avoid
saving sensitive personal information on a shared device.
🎯 Why Pattern Hunter?
Nature is full of branching networks, symmetry, spirals, repetition, and
geometry. Pattern Hunter encourages people to slow down, look closer,
and use AI as a companion for curiosity---not a replacement for their
own observation.
🤝 Contributing
Ideas, bug reports, and improvements are welcome. Open an issue or
submit a pull request on GitHub.
📄 License
No license has been specified yet. Until a license is added, others
should not assume they have permission to reuse, modify, or redistribute
this project's code.
---
Built with curiosity 🌱
