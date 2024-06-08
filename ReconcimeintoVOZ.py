
import speech_recognition as sr

# Crear un objeto reconocedor
recognizer = sr.Recognizer()

# Escuchar el audio del micrófono
with sr.Microphone() as source:
    print("Di algo:")
    audio = recognizer.listen(source)

# Convertir audio a texto
try:
    text = recognizer.recognize_google(audio, language="es-ES")
    print("Has dicho:", text)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print("Error al solicitar resultados; {0}".format(e))