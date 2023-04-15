from Skills.Acore import speak, recognize_speech, record_action
from deep_translator import GoogleTranslator
from langdetect import detect

# German
def translate_to_german():
    speak('What would you like to translate into German?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='de').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: German')

# Hindi
def translate_to_hindi():
    speak('What would you like to translate into Hindi?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='hi').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Hindi')

# Spanish
def translate_to_spanish():
    speak('What would you like to translate into Spanish?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='es').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Spanish')

# French
def translate_to_french():
    speak('What would you like to translate into French?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='fr').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: French')

# Russian
def translate_to_russian():
    speak('What would you like to translate into Russian?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='ru').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Russian')

# Japanese
def translate_to_japanese():
    speak('What would you like to translate into Japanese?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='ja').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Japanese')

# Italian
def translate_to_italian():
    speak('What would you like to translate into Italian?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='it').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Italian')

# Greek
def translate_to_greek():
    speak('What would you like to translate into Greek')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='el').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Greek')

# Swedish
def translate_to_swedish():
    speak('What would you like to translate into Swedish?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='sv').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Swedish')

def translate_to_hungarian():
    speak('What would you like to translate into Hungarian?')
    text = recognize_speech()
    # Detect language
    detected_language = detect(text)
    # Translate
    language_translation = GoogleTranslator(source=detected_language, target='hu').translate(text)
    print(language_translation)
    speak(language_translation)
    record_action('Translated: ' + text + ' | into: Hungarian')