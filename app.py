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

article_image_url = article.images
image_url = 'https://cdn.arstechnica.net/wp-content/uploads/2018/04/shiny_merlin_edited-760x380.jpg'

# Getting the size of an image
image_blob = requests.get(image_url)
with Image(blob=image_blob.content) as img:
    image_dims = img.size

# Ideal size for instagram stories
dims = (1080, 1920)
ideal_height = dims[0]
ideal_width = dims[1]
ideal_aspect = ideal_width / ideal_height 

width = image_dims[0]
height = image_dims[1]
aspect = width / height

if aspect > ideal_aspect:
    # Crop the left and right edges
    new_width = int(ideal_aspect * height)
    offset = (width - new_width) / 2
    resize = (
        (0, 0, int(new_width), int(height)),
        (int(width-new_width), 0, int(width), int(height))
    )
else:
    # ... then crop the top and bottom edge
    new_height = int(width / ideal_aspect)
    offset = (height - new_height) / 2
    resize = (
        (0, 0, int(width), int(new_height)),
        (0, int(height-new_height), int(width), int(height))
    )

with Image(blob = image_blob.content) as img:
    img.crop(*resize[0])
    img.save(filename='croped_1.jpg')

with Image(blob = image_blob.content) as img:
    img.crop(*resize[1])
    img.save(filename='croped_2.jpg')

# for sentence in summarizer(parser.document, SENTENCES_COUNT):
#     print(sentence)


# print(article.keywords)
# print(article.summary)