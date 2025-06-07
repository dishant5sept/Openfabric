# Openfabric AI Agent

## 🧠 AI Developer Challenge Submission

### 🔍 Overview

This repository presents my official submission for the **Openfabric AI Developer Challenge**. It showcases a working AI agent built using the `openfabric-pysdk`, capable of intelligent processing and output generation, with support for local LLM inference and object/image generation. The project is structured to be extensible and serves as a proof-of-concept for building decentralized AI applications.

### 🗂️ Project Structure

The repository is organized as follows:

| Path/File              | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| `main.py`              | Entry point that initializes and starts the AI agent. |
| `local_llm.py`         | Handles local LLM interactions and inference logic.   |
| `memory.py`            | Manages the agent's memory and knowledge base.        |
| `memory_gui.py`        | GUI-based memory visualization using `tkinter`.       |
| `test_tk.py`           | Auxiliary test script for GUI-related logic.          |
| `memory.db`            | SQLite database file used for memory persistence.     |
| `start.sh`             | Shell script for launching the agent locally.         |
| `requirements.txt`     | Lists all required Python dependencies.               |
| `Dockerfile`           | Dockerfile for containerizing the application.        |
| `sdk/schema/`          | Schema definition and data validation logic.          |
| `sdk/helper.py`        | Utility functions to support agent logic.             |
| `sdk/wrapper.py`       | Wrapper logic around SDK tools for integration.       |
| `generated/model.obj`  | Generated 3D model output.                            |
| `generated/output.png` | Generated image output.                               |

---

### 🚀 Getting Started

#### 📋 Prerequisites

Ensure the following tools are installed:

* Python **3.10 or higher**
* `pip` (Python package manager)
* (Optional) `virtualenv` or `pyenv` for environment management

#### 🔧 Installation Steps

```bash
# Clone your project repository (replace URL with your actual repo)
git clone (https://github.com/dishant5sept/Openfabric).git
cd <Openfabric>

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

### ⚙️ Configuration

No additional configuration is required. All components and modules are self-contained. The SQLite memory DB (`memory.db`) is automatically managed by `memory.py`.

---

### ▶️ Running the Agent

To run the application locally:

```bash
./start.sh
```

If the script is not executable:

```bash
chmod +x start.sh
./start.sh
```

Alternatively, you can start the agent directly:

```bash
python main.py
```

---

### 📄 File Highlights

#### `main.py`

* Launches the AI agent.
* Interfaces with the Openfabric SDK and internal components.

#### `local_llm.py`

* Handles local large language model inference.
* Acts as the backbone for NLP-related processing.

#### `memory.py`

* Stores, updates, and retrieves contextual memory from `memory.db`.

#### `memory_gui.py`

* Offers a visual frontend to explore memory contents.

#### `sdk/schema/schema.py`

* Defines schemas and validation for incoming/outgoing data.

#### `Dockerfile`

* Used for containerized deployments.

---

### 📡 Runtime Architecture

The AI agent operates as a local event-driven process. It does not expose REST APIs directly but listens and responds via Openfabric’s internal message-passing and SDK callback mechanisms.

---

### 🤝 Contributing

Feel free to contribute to this project:

* Fork the repo
* Create a feature branch
* Submit a Pull Request

For large changes, please open an issue first.

---


### 🙏 Acknowledgments

* **Openfabric** for hosting the challenge and platform
* **Python SDK** for enabling LLM integration
* **Gevent**, **SQLite**, and **Tkinter** for various runtime utilities
