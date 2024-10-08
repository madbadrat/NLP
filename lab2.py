# безделушка, комод

import gensim

pos = ["вещица_NOUN", "шкапчик_NOUN"] # вещица
neg = [] # шкапчик, шкафчик, сундук, ящик
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format("cbow.txt", binary=False)
dist = word2vec_model.most_similar(positive=pos, negative=neg)

for i in dist:
    print(i)
