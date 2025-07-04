import pyttsx3
import speech_recognition as sr
import webbrowser
import music
import apps
import pyaudio
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):#fn to speak the output
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
     #to open any app or website
    if  c.lower().startswith('open'):
        app_name = c.lower().split(' ')[1]
        webbrowser.open(apps.apps[app_name])
        speak(f'Opening {app_name}')

      #to play music
    elif c.lower().startswith('play'):
         song= c.lower().split(' ')[1]
         webbrowser.open(music.music[song])

      #using AI model to process command
    else:
         genai.configure(api_key="PASTE_YOUR_API_KEY_HERE")

         model = genai.GenerativeModel("gemini-1.5-flash")

         response = model.generate_content(c)
         print(response.text)
         speak(response.text)
         print('')
#MAIN PROG
if __name__ == '__main__':
    print('INITIALIZING JARVIS ........')  
    speak('INITIALIZING JARVIS')#using speak fn
    print('')
    while True:
    
      r=sr.Recognizer()
      try:
          #wait for word "jarvis" 
          with sr.Microphone() as source:
             print('Listening......')
             audio = r.listen(source,timeout=2)
             word = r.recognize_google(audio)#analizing the word

          if word.lower() == 'jarvis':
               speak('Yes, how can I help you?')

               #wait for main command
               with sr.Microphone() as source:
                   print('Listening for command...')
                   audio = r.listen(source,timeout=5)
                   command = r.recognize_google(audio)#anlizing the command

                   #proces fn call
                   processCommand(command)
            
          elif word.lower() == 'terminate':
              print('')
              speak('Terminating the program')
              print('Terminating the program')

              print('Deinitializing JARVIS.........')
              speak('Deinitializing JARVIS.........')

              print('JARVIS terminated successfully')

              break
              
     
      except  Exception as e:
          print('ERROR:{0}'.format(e))
          speak('try again please') 
