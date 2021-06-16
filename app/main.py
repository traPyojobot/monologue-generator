import markovify
import MeCab
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)

wakati = MeCab.Tagger('-Owakati')
parsed_text = ''
with open('data.tsv', 'r') as f:
  text = f.readlines()
  for line in text:
    parsed_text += wakati.parse(line)
text_model = markovify.NewlineText(parsed_text, state_size=3)


@app.post('/api')
async def api_text():
  text = text_model.make_short_sentence(100, 20, tries=100).replace(' ', '')
  return {'text': text}
