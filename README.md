# 🌿 Pattern Hunter

**An offline-first AI companion for discovering patterns hidden in nature.**

Pattern Hunter turns nature exploration into an interactive experience. It generates observation missions, analyzes photos of natural objects using local AI models, and helps users record their discoveries in a personal Nature Journal.

## ✨ Features

- 🤖 **AI-Generated Missions:** Generate creative nature observation missions using Llama 3.2 1B.
- 📸 **AI Image Analysis:** Analyze photos of leaves, flowers, and other natural objects using Moondream.
- 🌱 **Nature Journal:** Save AI analyses and personal observations in your browser.
- 🔒 **Local-First AI:** Run AI models locally through Ollama instead of relying on hosted AI APIs.
- 💻 **Simple Web Interface:** A lightweight interface built with HTML, CSS, and JavaScript.
- 🖼️ **Image Validation:** Supports JPG, JPEG, PNG, and WebP images up to 5 MB.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend logic |
| Flask | Web server and API routes |
| HTML | Page structure |
| CSS | Styling and layout |
| JavaScript | Frontend interactions |
| Ollama | Local AI model runtime |
| Llama 3.2 1B | Nature mission generation |
| Moondream | Image understanding |
| Browser localStorage | Nature Journal persistence |

## 🚀 Getting Started

### Prerequisites

Before running Pattern Hunter, install:

- [Python](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/download)
- [Git](https://git-scm.com/downloads) (optional)

### 1. Clone the Repository

```bash
git clone https://github.com/HarshrajNoob/pattern-hunter.git
cd pattern-hunter
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required Python packages:

```powershell
python -m pip install flask requests
```

### 3. Download the AI Models

Make sure Ollama is installed, then run:

```powershell
ollama pull llama3.2:1b
ollama pull moondream
```

The first download requires an internet connection and may take some time.

### 4. Run the Application

Start the Flask application:

```powershell
python app.py
```

Open the local URL displayed in your terminal. It is usually:

```text
http://127.0.0.1:5000
```

Keep Ollama running while using the AI-powered features.

## 🌳 How to Use Pattern Hunter

1. Open Pattern Hunter in your browser.
2. Generate a nature observation mission.
3. Explore your surroundings and find an interesting natural object.
4. Upload a photo in a supported image format.
5. Let the local AI model analyze visible details and patterns.
6. Save the analysis to your Nature Journal.
7. Add your own observations and revisit them later.

## 📴 Offline-First Design

Pattern Hunter is designed to run AI inference locally.

Once the dependencies and AI models have been downloaded:

- Mission generation can use the local Llama model.
- Image analysis can use the local Moondream model.
- Images can be analyzed without sending them to a hosted AI service.
- Journal entries remain stored in the browser's local storage.

**Important:** Initial setup requires internet access to download dependencies and models. Ollama must be running for AI features to work. Journal entries are tied to the browser and device, and clearing browser data may remove them.

If AI mission generation fails, the application can fall back to its built-in missions.

## 📁 Project Structure

```text
pattern-hunter/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── .gitignore
└── README.md
```

## 🔧 Troubleshooting

### Ollama command is not recognized

Check that Ollama is installed, reopen PowerShell, and run:

```powershell
ollama --version
```

### AI features are not responding

Check whether Ollama is running and the required models are available:

```powershell
ollama list
```

If a model is missing, download it using the commands in the setup section.

### Python dependencies are missing

Activate the virtual environment and run:

```powershell
python -m pip install flask requests
```

### Image analysis fails

- Confirm the image is JPG, JPEG, PNG, or WebP.
- Make sure the image is no larger than 5 MB.
- Confirm that the Moondream model is installed.
- Check that Ollama is running.

## 🔐 Privacy

Pattern Hunter is designed to process images through the local Ollama service on your machine. Nature Journal entries are stored in browser local storage rather than a remote database.

Avoid saving sensitive personal information, especially when using a shared device.

## 💡 Why Pattern Hunter?

Nature is full of fascinating patterns: branching networks in leaves, symmetry in flowers, spirals, repetition, and geometric structures.

Pattern Hunter encourages people to slow down, observe their surroundings, and use AI as a companion for curiosity and discovery—not as a replacement for their own observations.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome!

You can open an issue or submit a pull request through the [GitHub repository](https://github.com/HarshrajNoob/pattern-hunter).

## 📄 License

No license has been specified yet. Until a license is added, others should not assume they have permission to reuse, modify, or redistribute this project's code.

---

**Built with curiosity. 🌱**
