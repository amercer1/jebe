from os import path
#from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)
text_files = path.join(d, 'text_files')
images = path.join(d, 'images')

text = open(path.join(text_files, 'game_1.txt')).read()


# generate word cloud
wc = WordCloud().generate(text)
wc.generate(text)

# store to file
wc.to_file(path.join(images, "game_1.png"))
