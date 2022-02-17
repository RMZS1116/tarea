# Python program to generate WordCloud

# importing all necessary modules
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
# Reads 'Youtube04-Eminem.csv' file
df = pd.read_csv(r"Youtube04-Eminem.csv", encoding ="latin-1")
#generar stopwords
stop_wordsunicos = ['Ã', 'Â', 'ð','ðŸ', 'Ÿ', '€','@', '¢' ,'https', 'âœ' 'âœˆï','ˆ','Ÿ','â','œ','ï', 'estÃ','dÃ','mÃ', 'ä', 'https://t.co/', 't', 'co', 'í', 'n' ]
stop_words = stopwords.words('spanish')
stop_words.extend(stop_wordsunicos)
comment_words = ''
stopwords = set(STOPWORDS)

# iterate through the csv file
for val in df.CONTENT:
	
	# typecaste each val to string
	val = str(val)

	# split the value
	tokens = val.split()
	
	# Converts each token into lowercase
	for i in range(len(tokens)):
		tokens[i] = tokens[i].lower()
	
	comment_words += " ".join(tokens)+" "

wordcloud = WordCloud(width = 800, height = 800,
				background_color ='white',
				stopwords = stopwords,
				min_font_size = 10).generate(comment_words)

# plot the WordCloud image					
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

plt.show()
