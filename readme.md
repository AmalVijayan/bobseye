# AI Code Linter (POC WITH RAG)

This repository contains a simple implementation of an AI-driven code linter that evaluates Python code snippets for cleanliness and adherence to best practices.

## Table of Contents

- [AI Code Linter (POC WITH RAG)](#ai-code-linter-poc-with-rag)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Environment](#environment)
  - [Usage](#usage)
      - [To create a new index in vectorDB](#to-create-a-new-index-in-vectordb)
      - [To run the linter](#to-run-the-linter)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

The AI Code Linter (POC) uses a GPT-4 model and RAG to assess Python code snippets and provide feedback on their quality. It checks for best practices, clean code principles, and potential improvements.

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Environment

```bash
export OPENAI_API_KEY=<openai_api_key>
export PINECONE_API_KEY=<pinecone_api_key>
export PINECONE_INDEX_NAME=<index_name>
export DATA_SOURCE_FILE_NAME=<data_source_file_name>
export OPENAI_EMBEDDING_MODEL=<openai_embedding_model_name>
```

## Usage

Add the code snippets to lint to the inputs variable in main.py in the given format and run the following command.

#### To create a new index in vectorDB
```bash
 python main.py build_vector_db
```

#### To run the linter
```bash
 python main.py lint_code
```

## Contributing
Contributions are welcome! Please create an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the [MIT](https://www.mit.edu/~amini/LICENSE.md) License. See the LICENSE file for details.