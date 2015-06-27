import os
import re
#from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = os.path.dirname(__file__)
text_files = os.path.join(d, 'text_files')
images = os.path.join(d, 'images')

paths = [fn for fn in next(os.walk(text_files))[2]]


for path in paths:
    png_filename = re.sub(r'\.txt$', '.png', path)
    text = open(os.path.join(text_files, path)).read()
    # generate word cloud
    wc = WordCloud(width=1000, height=500, margin=10).generate(text)
    wc.generate(text)
    # store to file
    wc.to_file(os.path.join(images, png_filename))
