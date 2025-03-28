import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',150)
engine.setProperty('volume',3.0)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #Index 0 for male, 1 for female
engine.say("jaya is an lazy bitch who have fake dream to show other but will naiver change because people never change")
engine.runAndWait()