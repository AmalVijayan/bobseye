# AI Code Linter (POC)

This repository contains a simple implementation of an AI-driven code linter that evaluates Python code snippets for cleanliness and adherence to best practices.

## Table of Contents

- [AI Code Linter (POC)](#ai-code-linter-poc)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Environment](#environment)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

The AI Code Linter (POC) uses a GPT-4 model to assess Python code snippets and provide feedback on their quality. It checks for best practices, clean code principles, and potential improvements.

## Installation

To install the necessary dependencies, use the following command:

```bash
pip install -r requirements.txt
```

## Environment

```bash
export OPENAI_API_KEY=<openai_api_key>
```

## Usage

Add the code snippets to lint to the inputs variable in main.py in the given format and run the following command.

```bash
python main.py
```

## Contributing
Contributions are welcome! Please create an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the [MIT](https://www.mit.edu/~amini/LICENSE.md) License. See the LICENSE file for details.