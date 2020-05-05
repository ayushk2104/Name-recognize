import speech_recognition as sr

text = ""
text_detected = []
last_name = "quit quit"

print("Please enter the names")

while text != last_name:
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:            
        text = r.recognize_google(audio)
        print("The name is {}".format(text))
        text_detected.append("{}".format(text))
    except:
        print("Couldn't get the text")