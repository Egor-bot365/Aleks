import speech_recognition as sr 

r = sr.Recognizer()
with sr.Microphone(device_index=6) as sourse:
	print("Я тебя слушаю")
	audio = r.listen(sourse)

query = r.recognize_google(audio, language='ru-RU', show_all=True)
print("Ты сказал" + query.lower())
