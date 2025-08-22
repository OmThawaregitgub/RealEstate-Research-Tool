# 🏙️ **RealEstate Research Tool** We are going to build a user-friendly news research tool designed for effortless information retrieval. Users can input article URLs and ask questions to receive relevant insights from the real-estate domain. (But its features can be extended to any domain.)

### Features

  - Load URLs to fetch article content.
  - [cite\_start]Process article content using **LangChain's UnstructuredURL Loader**[cite: 1].
  - [cite\_start]Construct an embedding vector with **HuggingFace embeddings** and use **ChromaDB** as the vector store for quick and effective information retrieval[cite: 1].
  - Interact with a local LLM (**Llama 3 via Ollama**) to get answers and source URLs from the articles by inputting queries.

-----

### **Set-up**

1.  [cite\_start]**Install dependencies:** Run the following command to install all necessary packages[cite: 1].

    ```bash
    pip install -r requirements.txt
    ```

2.  **Download Ollama and a model:** Install Ollama and then pull a model like Llama 3 from your terminal. For example:

    ```bash
    ollama pull llama3
    ```

3.  [cite\_start]**Run the Streamlit app:** Start the application by running this command[cite: 1].

    ```bash
    streamlit run main.py
    ```

-----

### **Usage/Examples**

[cite\_start]The web app will open in your browser after the setup is complete[cite: 1].

  - [cite\_start]Enter URLs directly into the sidebar[cite: 1].
  - [cite\_start]Click **"Process URLs"** to start loading and processing the data[cite: 1].
  - [cite\_start]The system will perform text splitting and generate embedding vectors using **HuggingFace's Embedding Model**[cite: 1].
  - [cite\_start]These embeddings will be stored in **ChromaDB**[cite: 1].
  - [cite\_start]You can now ask questions to get answers based on the provided news articles[cite: 1].
  - [cite\_start]The tutorial uses the following news articles as examples[cite: 1]:
      - `https://www.cnbc.com/2024/12/21/how-the-federal-reserves-rate-policy-affects-mortgages.html`
      - `https://www.cnbc.com/2024/12/20/why-mortgage-rates-jumped-despite-fed-interest-rate-cut.html`
      - `https://www.cnbc.com/2024/12/17/wall-street-sees-upside-in-2025-for-these-dividend-paying-real-estate-stocks.html`

-----

### **Live Web App**

https://realestate-research-tool-g7hwzvsm6ecv7nko9sftxs.streamlit.app/

-----

[cite\_start]*Copyright (C) Codebasics Inc. All rights reserved. [cite: 1]*

*Additional Terms: This software is licensed under the MIT License. However, commercial use of this software is strictly prohibited without prior written permission from the author. [cite\_start]Attribution must be given in all copies or substantial portions of the software[cite: 1].*
