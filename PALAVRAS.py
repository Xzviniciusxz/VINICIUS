import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

Caminho = sg.popup_get_file('Chosse a CSV file:')
CSV = pd.read_csv(Caminho)
CSV_DT = pd.DataFrame(CSV)

summary = CSV_DT.dropna(subset=["42. Escreva algumas linhas sobre sua história e seus sonhos de vida."], axis = 0) ["42. Escreva algumas linhas sobre sua história e seus sonhos de vida."]

all_summary = " ".join(s for s in summary)

print("Quantidade de Palavras; {}".format(len(all_summary)))

stopwords = set(STOPWORDS)
stopwords.update(["da", "meu", "em", "voce", "de", "Um", "uma","eu","que","na","o","como"])

wordcloud = WordCloud(stopwords=stopwords,
                background_color= "black", width=1600, height=800).generate(all_summary)

fig, ax = plt.subplots(figsize=(10,6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.set_axis_off()

plt.imshow(wordcloud);
wordcloud.to_file("FATEC_123.png")