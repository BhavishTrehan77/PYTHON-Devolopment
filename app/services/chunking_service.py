def chunk_text(text,TextSize=500,overlap=50):
    res=[]
    for i in range(0,len(text),TextSize-overlap):
        data=text[i:i+TextSize]
        res.append(data)
    return res

def chunk_text_by_words(text,TextSize,overlap):
    words=text.split()
    res=[]
    for i in range(0,len(words),TextSize-overlap):
        data=words[i:i+TextSize]
        res.append(" ".join(data))
    return res