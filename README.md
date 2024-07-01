
# Personal CLI Assistants

**Personal CLI Assistants** is a command-line application derived from the `phidata` Python library. This project
simplifies and customizes the original library to create a versatile personal assistant powered by language models. 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)

## Installation

To install, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/phidata-cli.git
cd phidata-cli
pip install -r requirements.txt
```

## Usage

To use the PHIDATA CLI, run the following command:

```bash
pas [OPTIONS] [PROMPT]
```

## Features

- **Custom Assistants**: Input your own prompts to interact with the assistant.
- **SQLite Storage**: Uses SQLite by default for assistant memory and storage.
- **ChromaDB Vector Database**: Utilizes ChromaDB for vector database storage.
- **Configuration Files**: Load configurations from YAML files.

## Configuration

Configuration is managed through a YAML file. The default configuration file is `config.yaml` located in the application
directory. You can specify a different configuration file using the `--config` option.

Example `config.yaml`:

```yaml
name: "Helpful Assistant"
description: "You are a helpful assistant."
instructions:
  - "Assist the user with their queries."
  - "Provide detailed and accurate responses."
model: "llama3"
markdown: true
add_storage: true
```

## Examples

Run the default assistant with a prompt:

```bash
pas "Tell me a joke."
```

Run the assistant with a custom configuration:

```bash
pas --config custom_config.yaml "What's the weather like today?"
```

## Troubleshooting

If you encounter issues, ensure that all dependencies are installed correctly. Check the configuration file for any
errors. For detailed logs, run the CLI with the `--verbose` option.
