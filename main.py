import whisper
from googletrans import Translator

# Loading the model and Transcribing the speech into English
model = whisper.load_model("base")
result = model.transcribe("test.mp3", language="en", fp16=False)
print(result["text"])

translator = Translator()

# Translate the text to Urdu
try:
  translated_text = translator.translate(result["text"], dest='ur')
  if translated_text is not None:
     print(translated_text.text)
  else:
     print("Translation result is None.")
except Exception as e:
  print(e)
