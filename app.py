import requests

# Wand - work with iamge and ovaerlaying texts over image
from wand.image import Image

# Sumy - summirizing artciles
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.reduction  import ReductionSummarizer  as summarize
from sumy.nlp.stemmers import Stemmer

# Newspaper - parsing articles
from newspaper import Article

url = "https://arstechnica.com/science/2018/06/first-space-then-auto-now-elon-musk-quietly-tinkers-with-education/"

# Parsing the articles
article = Article(url)
article.download()
article.parse()

# Summarizing articles with Natural Language Processing AI
article.nlp()

# Summarizing articles with Sumy
LANGUAGE = "english"
SENTENCES_COUNT = 10
parser = PlaintextParser.from_string(article.text, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)
summarizer = summarize(stemmer)

image_url = 'https://cdn.arstechnica.net/wp-content/uploads/2018/04/shiny_merlin_edited-760x380.jpg'
image_blob = requests.get(image_url)
with Image(blob=image_blob.content) as img:
    print(img.size)




# for sentence in summarizer(parser.document, SENTENCES_COUNT):
#     print(sentence)


# print(article.keywords)
# print(article.summary)