import speech_recognition as sr

def listen_and_recognize():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # calibrate for ambient noise

        print("Listening... Please speak something!")
        audio_data = recognizer.listen(source)  # listen for the first phrase and extract audio data

        print("Recognizing speech...")
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; check your internet connection. {e}")

if __name__ == "__main__":
    listen_and_recognize()
