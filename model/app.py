from flask import Flask, request
from flask_cors import CORS
import json
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.edmundson import EdmundsonSummarizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import translators as ts
from newspaper import Article
from langdetect import detect 

SENTENCES_COUNT = 2
LANGUAGES = ["english", "chinese", "spanish", "french"]
LANGUAGE_CODES = ["en", "zh", "es", "fr"]
PUNCT_CHARS = ['!', '.', '?', '։', '｡', '。']

tokenizers = []
summarizers = []
stop_words = []
for i, lang in enumerate(LANGUAGES):
  tokenizers.append(Tokenizer(lang))
  stemmer = Stemmer(lang)
  if lang == "chinese":
    summarizers.append(LsaSummarizer(stemmer))
  else:
    summarizers.append(EdmundsonSummarizer(stemmer))
  stop_words.append(get_stop_words(lang))

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Welcome to the rounce backend!'

@app.route('/parse')
def parse():

  args = request.args
  url = args["url"]

  article = Article(url)
  article.download()
  article.parse()

  if article.text == '':
    article = Article(url, language='zh')
    article.download()
    article.parse()

  title = clean(article.title)

  text = article.text
#   text = ' '.join([clean(x) for x in text.split('\n') if clean(x)[-1] in PUNCT_CHARS])

  summary = summarize(text)


  if type(summary) is tuple:
    return json.dumps(
    {
      'title': ts.sogou(title), 
      'trans_title': title, 
      'summary': summary[0],
    },
    ensure_ascii=False)

  return json.dumps(
    {
      'title': title, 
      'summary': summary,
    },
    ensure_ascii=False)


@app.route('/summarize')
def summarize(text, lang=-1):
  
  LANGUAGE = lang
  
  if LANGUAGE == -1:
    LANGUAGE = LANGUAGE_CODES.index(detect(text)[:2])

  parser = PlaintextParser.from_string(text, tokenizers[LANGUAGE])

  summarizer = summarizers[LANGUAGE]
  if lang == "chinese":
    summarizer.stop_words = stop_words[1]
  else:
    summarizer.null_words = stop_words[LANGUAGE]
    summarizer.bonus_words = parser.significant_words
    summarizer.stigma_words = parser.stigma_words

  sentences = [str(x) for x in summarizer(parser.document, SENTENCES_COUNT)]

  summary = ' '.join(sentences)

  if LANGUAGE != 0:
    return ( clean(ts.sogou(summary)), )
  return clean(summary)


def clean(str):
  return str.strip()