import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt



def wordclouding(text_df):

    text = text_df['word_freq'].str.cat(sep = ' ')

    text_df

    face_mask = np.array(Image.open("website/static/images/female-side-profile-silhouette-14.png"))
    face_mask

    transformed_face_mask = np.ndarray((face_mask.shape[0],face_mask.shape[1]), np.int32)
    transformed_face_mask = np.where(transformed_face_mask == 0, 255,0)

    plt.rcParams['figure.dpi'] = 50
    # Create a word cloud image
    wc = WordCloud(background_color="white", max_words=150, mask=transformed_face_mask,
                contour_width=0.01, contour_color='black', colormap='plasma', collocations=False)

    # Generate a wordcloud
    wc.generate(text)

    # store to file
    wc.to_file("website//static/images//wc.png")

