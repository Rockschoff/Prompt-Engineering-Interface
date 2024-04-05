# Prompt Engineering Interface

This is a set of Python scripts that provide a Tkinter-based interface for working with large language models (LLMs), particularly for the purpose of prompt engineering.

## Features

The project consists of three main files:

1. `Iteration.py`: This file contains the main interface for the Prompt Engineering application. It provides the following features:

   - **Prompt Builder**: Allows users to construct and refine prompts for LLMs, with options to add task descriptions, specify instructions, include examples, and define input/output formatting.
   - **Prompt Evaluation**: Provides a way to test and evaluate the effectiveness of prompts, including generating sample outputs, analyzing output quality and coherence, and identifying potential improvements or refinements.
   - **Prompt Library**: Maintains a collection of pre-built, high-quality prompts that users can browse, customize, and use as a starting point for their own prompt engineering efforts.
   - **Prompt Sharing**: Enables users to share their prompts with the community, fostering collaboration and the creation of a shared knowledge base.

2. `guidelines.py`: This file contains a variety of functions for generating different types of prompts, such as summarizing prompts, JSON prompts, condition prompts, few-shot prompts, and marking prompts. These prompts can be used within the Prompt Engineering interface or in other applications.

3. `chatbot.py`: This file provides a simple Tkinter-based chatbot interface that uses the OpenAI API to generate responses to user input. It demonstrates how the prompt engineering capabilities can be integrated into a conversational application.

## Getting Started

1. Clone the repository: `git clone https://github.com/your-username/prompt-engineering-interface.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Obtain an OpenAI API key and set it as an environment variable (`OPENAI_API_KEY`).
4. Run the application: `python Iteration.py`
5. Access the interface at `http://localhost` in your web browser.

## Usage

The main usage of this project is to help users explore and refine prompts for large language models. Users can experiment with different prompt formats, evaluate the effectiveness of their prompts, and share their work with the community.

The `guidelines.py` file can also be used independently to generate prompts for various use cases, such as summarization, JSON formatting, condition satisfaction, few-shot learning, and student marking.

## Contributing

We welcome contributions to the Prompt Engineering Interface project. If you'd like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bug fix: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Create a new Pull Request

## License

This project is licensed under the [MIT License](LICENSE).

