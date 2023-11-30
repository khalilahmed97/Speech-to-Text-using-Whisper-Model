import whisper
from googletrans import Translator
import json

model = whisper.load_model("base")
result = model.transcribe("test.mp3", language="en", fp16=False)
json_data = json.dumps(result)
result_dict = json.loads(json_data)
print(result_dict["text"])

translator = Translator()
# Detect the language of the input text (optional)
# Translate the text to Urdu

try:
  translated_text = translator.translate(result_dict["text"], dest='ur')
  if translated_text is not None:
     print(translated_text.text)
  else:
     print("Translation result is None.")
except Exception as e:
  print(e)
