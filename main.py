import whisper
from googletrans import Translator

model = whisper.load_model("base")
result = model.transcribe("test.mp3", language="en", fp16=False)

translator = Translator()
# Detect the language of the input text (optional)
# Translate the text to Urdu

try:
  translated_text = translator.translate(str(result), dest='ur')
  print(translated_text.text)
except Exception as e:
  print(e)
