
# Multilingual Chatbot using BERT and Transformers

## Project Overview
This project enables a multilingual customer-agent conversation where:
- Customers can write messages in any language.
- Messages are automatically translated into English for the agent.
- Agent responses are translated back into the customer's language.

### Key Features:
- **BERT Transformer Models** for translation
- **Automatic Language Detection** using `langdetect`
- **Supports English, Spanish, French, German**

## Setup Instructions:
1. Clone the repository.
2. Create a virtual environment and install dependencies:


3. Install the Hugging Face Hub Library
pip install huggingface_hub

4. Generate a Hugging Face Token (If Not Already Done)
	1.	Go to Hugging Face Profile.
	2.	Click New Token.
	3.	Choose the Write access level for downloading and uploading models.
	4.	Copy the generated token.


5. Log in to Hugging Face CLI 
huggingface-cli login

python3 -m venv venv
source venv/bin/activate
pip install -r src/requirements.txt

pip install pycountry 

pip install sentencepiece

python -c "import sentencepiece; print('sentencepiece is installed!')"

3. Run the chatbot:
python src/main.py

4. Run inference tests:
python src/inference.py





multilingual_chatbot_project/
├── src/
│   ├── main.py                      # Main entry point for the chatbot
│   ├── translate_service.py         # Translation service using Hugging Face models
│   ├── inference.py                 # Language detection and response handling
│   └── requirements.txt             # Required packages for the project
├── models/
│   └── translation_model/           # Pretrained translation models (optional)
├── data/
│   └── sample_conversations.csv     # Sample conversations for testing
├── README.md                        # Instructions and project overview
├── .gitignore                       # Ignore unnecessary files for version control
└── config.py                        # Configurations (like model names and languages)