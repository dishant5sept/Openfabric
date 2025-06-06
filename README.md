# Openfabric AI Agent  
# AI Developer Challenge Submission

## Overview

This repository contains my submission for the Openfabric AI Developer Challenge. It features an AI agent built using the `openfabric-pysdk`. The agent performs intelligent processing based on input data and serves as a proof-of-concept for building decentralized AI applications.

## Project Structure

The project is organized into the following main parts:

1. **`agent/main.py`**: Main entry point for the AI agent.
2. **`agent/brain.py`**: Core AI logic and processing logic.
3. **`requirements.txt`**: Python dependencies.
4. **`start.sh`**: Shell script to run the agent locally.

## Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- (Optional but recommended) `virtualenv` or `pyenv`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/openfabric-ai-agent.git
   ```

2. Navigate into the project directory:

   ```bash
   cd openfabric-ai-agent
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

No additional configuration is needed. The default settings in the `agent/` directory are sufficient to run the agent locally.

## Running the Application

To start the AI agent locally, use:

```bash
./start.sh
```

Make sure the script is executable:

```bash
chmod +x start.sh
```

This will run the agent and begin listening for inputs on the configured local endpoint.

## Files Description

### `agent/main.py`
- Initializes the Openfabric agent
- Sets up request handling and dispatch to the brain logic

### `agent/brain.py`
- Implements the core logic of the AI agent
- Processes incoming queries and generates intelligent responses

### `start.sh`
- A shell script that launches the agent using Python

### `requirements.txt`
- Specifies all required Python libraries for the project, including:
  - `openfabric-pysdk`
  - `gevent`
  - Any additional project-specific dependencies

## API Usage

This project doesn't expose REST endpoints directly. Instead, it runs as part of the Openfabric decentralized AI infrastructure and is designed to process input through event-driven callbacks via Openfabric's runtime.

## Contributing

Contributions are welcome! If you'd like to enhance the agent, feel free to fork this repository and submit a pull request. For major changes, open an issue to discuss improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Openfabric
- Openfabric Python SDK
- Gevent
