# LLM Projects with OpenAI API

Welcome to the **LLM Projects with OpenAI API** repository! This collection showcases five distinct projects that leverage Large Language Models (LLMs) and OpenAI's powerful APIs to solve diverse problems ranging from applicant tracking to image generation and video transcription. Each project is designed to demonstrate different aspects of AI and machine learning, providing practical examples of how LLMs can be integrated into various applications.

![Repository Banner](https://your-banner-image-link.com)

---

## Table of Contents

- [Overview](#overview)
- [Projects](#projects)
  - [1. ATS Tracking System](#1-ats-tracking-system)
  - [2. Chatbot Model](#2-chatbot-model)
  - [3. SQL Data Retriever](#3-sql-data-retriever)
  - [4. Vision Model](#4-vision-model)
  - [5. YouTube Transcriber](#5-youtube-transcriber)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

This repository encompasses five innovative projects that utilize OpenAI's APIs to create intelligent applications:

1. **ATS Tracking System**: An Applicant Tracking System that evaluates resumes against job descriptions using LLMs.
2. **Chatbot Model**: A conversational chatbot built with OpenAI's ChatGPT.
3. **SQL Data Retriever**: A tool that converts natural language queries into SQL commands to retrieve data from a SQLite database.
4. **Vision Model**: An image generation application using OpenAI's DALL-E.
5. **YouTube Transcriber**: A system that transcribes YouTube videos and generates detailed notes using LLMs.

Each project is self-contained and demonstrates different capabilities of LLMs, offering valuable insights into their practical applications.

---

## Projects

### 1. ATS Tracking System

![ATS System](https://your-ats-system-image-link.com)

#### Description

The **ATS Tracking System** is designed to streamline the recruitment process by evaluating resumes against job descriptions. Leveraging OpenAI's GPT-4, this system provides professional evaluations and matching percentages to help HR professionals make informed decisions.

#### Features

- **Resume Evaluation**: Analyzes resumes in PDF format against job descriptions.
- **Matching Percentage**: Calculates the percentage match between resumes and job requirements.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.
- **Automated Responses**: Generates insightful feedback using GPT-4.

#### Technologies Used

- **Streamlit**: For the web interface.
- **OpenAI GPT-4**: For generating evaluations and matching percentages.
- **PyPDF2**: For extracting text from PDF resumes.
- **Python-dotenv**: For managing environment variables.

#### Setup and Usage

1. **Navigate to the ATS System Directory**:

    ```bash
    cd OpenAI_models_Demo/ATS_system
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r ../../requirements.txt
    ```

3. **Set Up Environment Variables**:

    Create a `.env` file in the `ATS_system` directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

---

### 2. Chatbot Model

![Chatbot](https://your-chatbot-image-link.com)

#### Description

The **Chatbot Model** is a simple yet effective conversational agent built using OpenAI's GPT-3.5-turbo. It provides a responsive chat interface where users can interact with the chatbot to get answers, assistance, or just have a conversation.

#### Features

- **Conversational Interface**: Engages users in real-time conversations.
- **Chat History**: Maintains a history of interactions for context.
- **Customizable UI**: Styled with custom CSS for an enhanced user experience.

#### Technologies Used

- **Streamlit**: For the web interface.
- **OpenAI GPT-3.5-turbo**: For generating conversational responses.
- **HTML/CSS**: For styling the chat interface.

#### Setup and Usage

1. **Navigate to the Chat Model Directory**:

    ```bash
    cd OpenAI_models_Demo/Chat_model
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r ../../requirements.txt
    ```

3. **Set Up Environment Variables**:

    Create a `.env` file in the `Chat_model` directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

---

### 3. SQL Data Retriever

![SQL Retriever](https://your-sql-retriever-image-link.com)

#### Description

The **SQL Data Retriever** converts natural language queries into SQL commands, enabling users to interact with a SQLite database effortlessly. This tool is perfect for those who are not well-versed in SQL but need to retrieve specific data from databases.

#### Features

- **Natural Language to SQL**: Translates user queries into executable SQL commands using GPT-4.
- **Database Interaction**: Retrieves and displays data from a SQLite database.
- **Error Handling**: Manages scenarios where transcripts or data are unavailable.

#### Technologies Used

- **Streamlit**: For the web interface.
- **OpenAI GPT-4**: For generating SQL queries.
- **SQLite3**: For database management.
- **YouTube Transcript API**: For extracting video transcripts.

#### Setup and Usage

1. **Navigate to the SQL Data Retriever Directory**:

    ```bash
    cd OpenAI_models_Demo/Retriev_SQL_data_project
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r ../../requirements.txt
    ```

3. **Initialize the Database**:

    ```bash
    python sqlite.py
    ```

4. **Set Up Environment Variables**:

    Create a `.env` file in the `Retriev_SQL_data_project` directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

5. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

---

### 4. Vision Model

![Vision Model](https://your-vision-model-image-link.com)

#### Description

The **Vision Model** utilizes OpenAI's DALL-E to generate images based on textual descriptions. Users can input prompts, and the model will create corresponding images, making it a powerful tool for creative and design applications.

#### Features

- **Image Generation**: Creates images from text prompts using DALL-E.
- **Download Option**: Allows users to download the generated images.
- **User-Friendly Interface**: Built with Streamlit for easy interaction.

#### Technologies Used

- **Streamlit**: For the web interface.
- **OpenAI DALL-E**: For generating images from text prompts.
- **Python-dotenv**: For managing environment variables.
- **PIL**: For image processing.

#### Setup and Usage

1. **Navigate to the Vision Model Directory**:

    ```bash
    cd OpenAI_models_Demo/Vision_model
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r ../../requirements.txt
    ```

3. **Set Up Environment Variables**:

    Create a `.env` file in the `Vision_model` directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application**:

    ```bash
    streamlit run vision.py
    ```

---

### 5. YouTube Transcriber

![YouTube Transcriber](https://your-youtube-transcriber-image-link.com)

#### Description

The **YouTube Transcriber** extracts transcripts from YouTube videos and generates detailed notes using OpenAI's GPT-4. This tool is ideal for content creators, educators, and researchers who need summaries of video content.

#### Features

- **Transcript Extraction**: Retrieves transcripts from YouTube videos using the YouTube Transcript API.
- **Detailed Notes Generation**: Summarizes transcripts into concise notes using GPT-4.
- **Error Handling**: Manages cases where transcripts are unavailable.
- **User-Friendly Interface**: Built with Streamlit for seamless interaction.

#### Technologies Used

- **Streamlit**: For the web interface.
- **OpenAI GPT-4**: For generating detailed notes from transcripts.
- **YouTube Transcript API**: For extracting video transcripts.
- **Python-dotenv**: For managing environment variables.

#### Setup and Usage

1. **Navigate to the YouTube Transcriber Directory**:

    ```bash
    cd OpenAI_models_Demo/YouTube-Transcriber
    ```

2. **Install Dependencies**:

    ```bash
    pip install -r ../../requirements.txt
    ```

3. **Set Up Environment Variables**:

    Create a `.env` file in the `YouTube-Transcriber` directory and add your OpenAI API key:

    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

4. **Run the Application**:

    ```bash
    streamlit run app.py
    ```

---

## Technologies Used

- **OpenAI API**: For leveraging GPT-3.5-turbo and GPT-4 models.
- **Streamlit**: For building interactive web applications.
- **Langchain**: For managing conversational chains and embeddings.
- **PyPDF2**: For extracting text from PDF documents.
- **FAISS**: For efficient similarity search and clustering of dense vectors.
- **SQLite3**: For lightweight database management.
- **Python-dotenv**: For environment variable management.
- **PIL (Pillow)**: For image processing.
- **YouTube Transcript API**: For extracting transcripts from YouTube videos.
- **DALL-E**: For generating images from textual descriptions.

---

## Installation

### Prerequisites

- **Python 3.8+**: Ensure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
- **OpenAI API Key**: Obtain your API key from [OpenAI](https://platform.openai.com/account/api-keys).

### Clone the Repository

```bash
git clone https://github.com/yourusername/LLM-projects-OpenAI-API.git
cd LLM-projects-OpenAI-API
```
