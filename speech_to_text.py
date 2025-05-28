# Importing the speech recognition library
import speech_recognition as sr

def listen_and_recognize():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        # Calibrate the recognizer to ambient noise for 1 second
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening... Please speak something!")
        # Listen and capture the audio from the microphone
        audio_data = recognizer.listen(source)

        print("Recognizing speech...")
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError:
            # Handle case when speech was unintelligible
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            # Handle connection errors or API issues
            print(f"Could not request results; check your internet connection. {e}")

# Main execution starts here
if __name__ == "__main__":
    listen_and_recognize()
