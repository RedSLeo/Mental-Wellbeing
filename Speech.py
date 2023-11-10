import speech_recognition as sr

rec = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("Adjusting for ambient noise. Please wait . . .")
    rec.adjust_for_ambient_noise(source, duration = 5)
    print("Ambient noise adjustment complete.")

timeout_duration = 1

with mic as source:
    print("What is on your mind. . .")
    audio = rec.listen(source)
    try:
        audio = rec.listen(source, timeout=timeout_duration)
        print("Recording complete.")

        # The recording audio is saved as a .wav file
        with open("recorded_audio.wav", "wb") as f:
            f.write(audio.get_wav_data())

        result = rec.recognize_google(audio)
        print("Recognized text:", result)
    except sr.WaitTimeoutError:
        print("I have not heard anything from you. Lemme know when you are ready.")
