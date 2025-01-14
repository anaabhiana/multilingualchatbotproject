from transformers import pipeline
from langdetect import detect

class TranslatorService:
    def __init__(self):
        """Initialize translators with corrected models for Bengali, Hindi, and French."""
        self.translators_to_english = {
            "fr": pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en"),
            "bn": pipeline("translation", model="csebuetnlp/banglat5_nmt_bn_en"),
            "hi": pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en"),
            "default": pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")
        }
        
        self.translators_from_english = {
            "fr": pipeline("translation", model="Helsinki-NLP/opus-mt-en-fr"),
            "bn": pipeline("translation", model="csebuetnlp/banglat5_nmt_en_bn"),
            "hi": pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi"),
            "default": pipeline("translation", model="Helsinki-NLP/opus-mt-en-mul")
        }

    def detect_language(self, text):
        """Detect the language of the input text."""
        try:
            lang = detect(text)
            print(f"Detected language: {lang}")
            return lang
        except Exception as e:
            print(f" Error detecting language: {e}")
            return "default"

    def translate_to_english(self, text):
        """Translate input text to English based on detected language."""
        source_lang = self.detect_language(text)
        translator = self.translators_to_english.get(source_lang, self.translators_to_english["default"])
        try:
            result = translator(text)
            if isinstance(result, list) and "translation_text" in result[0]:
                translated_text = result[0]["translation_text"]
            else:
                translated_text = str(result)
            #print(f" Translated to English: {translated_text}")
            return translated_text, source_lang
        except Exception as e:
            print(f" Error translating to English: {e}")
            return text, source_lang

    def translate_to_original_language(self, text, target_lang):
        """Translate English text back to the original language."""
        translator = self.translators_from_english.get(target_lang, self.translators_from_english["default"])
        try:
            result = translator(text)
            if isinstance(result, list) and "translation_text" in result[0]:
                translated_text = result[0]["translation_text"]
            else:
                translated_text = str(result)
            #print(f" Translated back to {target_lang}: {translated_text}")
            return translated_text
        except Exception as e:
            print(f" Error translating back to {target_lang}: {e}")
            return text