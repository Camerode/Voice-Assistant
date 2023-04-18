from Skills.Acore import speak, recognize_speech, record_action
from deep_translator import GoogleTranslator
from langdetect import detect

# German
def translate_to_german():
    try:
        speak('What would you like to translate into German?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='de').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: German')
    except Exception as e:
        print("An error has occurred in the translate to German command, output has been sent to errors.log")
        speak("An error has occurred in the translate to German command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# Hindi
def translate_to_hindi():
    try:
        speak('What would you like to translate into Hindi?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='hi').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Hindi')
    except Exception as e:
        print("An error has occurred in the translate to Hindi command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Hindi command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# Spanish
def translate_to_spanish():
    try:
        speak('What would you like to translate into Spanish?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='es').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Spanish')
    except Exception as e:
        print("An error has occurred in the translate to Spanish command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Spanish command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# French
def translate_to_french():
    try:
        speak('What would you like to translate into French?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='fr').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: French')
    except Exception as e:
        print("An error has occurred in the translate to French command, output has been sent to errors.log")
        speak("An error has occurred in the translate to French command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# Russian
def translate_to_russian():
    try:
        speak('What would you like to translate into Russian?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='ru').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Russian')
    except Exception as e:
        print("An error has occurred in the translate to Russian command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Russian command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# Japanese
def translate_to_japanese():
    try:
        speak('What would you like to translate into Japanese?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='ja').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Japanese')
    except Exception as e:
        print("An error has occurred in the translate to Japanese command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Japanese command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# Italian
def translate_to_italian():
    try:
        speak('What would you like to translate into Italian?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='it').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Italian')
    except Exception as e:
        print("An error has occurred in the translate to Italian command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Italian command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# Greek
def translate_to_greek():
    try:
        speak('What would you like to translate into Greek')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='el').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Greek')
    except Exception as e:
        print("An error has occurred in the translate to Greek command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Greek command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

# Swedish
def translate_to_swedish():
    try:
        speak('What would you like to translate into Swedish?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='sv').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Swedish')
    except Exception as e:
        print("An error has occurred in the translate to Swedish command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Swedish command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")

def translate_to_hungarian():
    try:
        speak('What would you like to translate into Hungarian?')
        text = recognize_speech()
        # Detect language
        detected_language = detect(text)
        # Translate
        language_translation = GoogleTranslator(source=detected_language, target='hu').translate(text)
        print(language_translation)
        speak(language_translation)
        record_action('Translated: ' + text + ' | into: Hungarian')
    except Exception as e:
        print("An error has occurred in the translate to Hungarian command, output has been sent to errors.log")
        speak("An error has occurred in the translate to Hungarian command, output has been sent to errors.log")
        with open("Skills/CoreFiles/errors.log", "a") as f:
            f.write(str(e) + "\n")