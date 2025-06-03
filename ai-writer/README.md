# AI Writer

A simple web application that generates text using a local LLM through Ollama. Write blog posts, stories, tweets, and more without relying on external APIs.

## Features

- Text generation using local LLM (Mistral)
- Multiple content types (blog, tweet, story, article)
- Temperature control for creativity adjustment
- Loading indicator during generation
- Clean, modern UI
- Local output logging

## Prerequisites

1. Install [Ollama](https://ollama.ai/)
2. Pull the Mistral model:
```bash
ollama pull mistral
```
3. Python 3.6+ installed

## Setup Instructions

1. Make sure Ollama is running and the Mistral model is installed
2. Start the Python server:
```bash
python server.py
```
3. Open your browser and navigate to `http://localhost:8080`

## Usage

1. Select the type of content you want to generate
2. Enter your prompt
3. Adjust the temperature if desired (higher = more creative, lower = more focused)
4. Click "Generate" and wait for the results
5. View your generated content
6. Check outputs.txt for a log of all generations

## Technical Details

- Frontend: HTML, CSS, JavaScript
- Local LLM: Ollama with Mistral model
- Server: Python HTTP Server
- Logging: Local file system (outputs.txt)

## Troubleshooting

1. Make sure Ollama is running:
   - Windows: Check Task Manager
   - Linux/Mac: `ps aux | grep ollama`

2. Verify Mistral model is installed:
```bash
ollama list
```

3. Common issues:
   - "Failed to generate text": Make sure Ollama is running
   - "Connection refused": Check if the server is running on port 8080
   - No output: Check browser console for errors

## Model Information

This app uses the Mistral model through Ollama for local inference. Mistral is a powerful open-source language model that offers a good balance between performance and resource usage. 