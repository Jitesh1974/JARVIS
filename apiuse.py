import google.generativeai as genai

genai.configure(api_key="    API KEY    ")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content('     PROMT    ')

print(response.text)

