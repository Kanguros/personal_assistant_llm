# Personal CLI Assistants

**Personal CLI Assistants** is a command-line application derived from the `phidata` Python library. This project
simplifies and customizes the original library to create a versatile personal assistant powered by large language
models.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Development](#development)

## Features

- **Custom Assistants**: Define your own assistants to accomplish specific tasks.
- **SQLite Storage**: Uses SQLite by default for assistant memory and storage.
- **ChromaDB Vector Database**: Utilizes ChromaDB for vector database storage.
- **Configuration Files**: Load configurations from YAML files.

## Installation

To install, clone the repository and install the required dependencies:

```bash
git clone https://github.com/Kanguros/personal_assistant_llm
cd personal_assistant_llm
poetry install
```

## Usage

Run the following command:

```bash
pas [OPTIONS] [PROMPT]
```

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

If you encounter issues, ensure that all dependencies are installed correctly. Check the configuration file for any
errors. For detailed logs, run the CLI with the `--verbose` option.

## Development

```shell
pre-commit install --install-hooks
poetry install --with=dev --with=webtool --with=openai --with=files
```

## Background

