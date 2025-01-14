from translate_service import TranslatorService

def main():
    translator = TranslatorService()
    print("Customer Service Chatbot (Type 'exit' to quit)")

    while True:
        customer_message = input("Customer: ")
        if customer_message.lower() == "exit":
            break

        # Detect language and translate to English
        english_translation, detected_lang = translator.translate_to_english(customer_message)
        print(f"Translated to English for Agent: {english_translation}")

        # Simulate the agent's response
        agent_response = input("Agent (English): ")

        # Translate the agent's response back to the customer's language
        translated_response = translator.translate_to_original_language(agent_response, detected_lang)
        print(f"Translated back to Customer Language: {translated_response}")

if __name__ == "__main__":
    main()