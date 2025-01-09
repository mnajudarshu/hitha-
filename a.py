import nltk
from nltk.probability import FreqDist
import pandas as p 
import matplotlib.pyplot as m 
from nltk.tokenize import word_tokenize
f=open(r'C:\Users\admin\Desktop\da.txt')
t=f.read()
w=word_tokenize (t)

print("before removal stopwords:",len(w))
st_w=nltk.corpus.stopwords.words('english')
rm_st=[]
for i in w:
    if i not in st_w:
        rm_st.append(i)
print("after remova stopwords:",len(rm_st))
freq=FreqDist(rm_st)
freqs=p.Series(dict(freq))
m.figure(figsize=(18,10))
freqs.plot(kind='bar')
m.title('distribution of stopword removal')
m.show()
