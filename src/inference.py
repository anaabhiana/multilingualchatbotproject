from translate_service import TranslatorService

def run_inference():
    translator = TranslatorService()
    test_message = input("Enter a test message for translation: ")
    detected_lang = translator.detect_language(test_message)
    english_translation = translator.translate_to_english(test_message, detected_lang)
    print(f"Detected Language: {detected_lang}")
    print(f"Translated to English: {english_translation}")

if __name__ == "__main__":
    run_inference()