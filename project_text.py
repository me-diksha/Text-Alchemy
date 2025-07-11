import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text="""Soft computing is an umbrella term used to describe types of algorithms that produce approximate solutions to unsolvable high-level problems in computer science. Typically, traditional hard-computing algorithms heavily rely on concrete data and mathematical models to produce solutions to problems. Soft computing was coined in the late 20th century.During this period, revolutionary research in three fields greatly impacted soft computing. Fuzzy logic is a computational paradigm that entertains the uncertainties in data by using levels of truth rather than rigid 0s and 1s in binary. Next, neural networks which are computational models influenced by human brain functions. Finally, evolutionary computation is a term to describe groups of algorithm that mimic natural processes such as evolution and natural selection.

In the context of artificial intelligence and machine learning, soft computing provides tools to handle real-world uncertainties. Its methods supplement preexisting methods for better solutions. Today, the combination with artificial intelligence has led to hybrid intelligence systems that merge various computational algorithms. Expanding the applications of artificial intelligence, soft computing leads to robust solutions. Key points include tackling ambiguity, flexible learning, grasping intricate data, real-world applications, and ethical artificial intelligence."""

def summarizer(input):
    stopwords=list(STOP_WORDS)
    # print(stopwords)
    nlp= spacy.load('en_core_web_sm')
    doc=nlp(input)
    # print(doc)
    tokens= [token.text for token in doc]
    # print(tokens)
    # for frequency of each word
    word_f={}
    for word in doc :
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_f.keys():
                word_f[word.text]=1
            else:
                word_f[word.text]+=1
            
# print(word_f)     
    max_f= max(word_f.values())
# print(max_f)
    for word in word_f.keys():
        word_f[word]=word_f[word]/max_f
# print(word_f)

    sent_tokens= [sent for sent in doc.sents]
# print(sent_tokens)

    sent_score={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_f.keys():
                if sent not in sent_score.keys():
                    sent_score[sent]=word_f[word.text]
                else:
                    sent_score[sent]+=word_f[word.text]
# print(sent_score)

    select_len=int(len(sent_tokens)*0.5)
    print(select_len)
    summary = nlargest(select_len,sent_score,key = sent_score.get)
# print(summary)
    final_summary= [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(input) # main text
    # print(summary) #summary
    # print( "length of original text :" , len(text.split(' ')))
    # print( "length of summary text :" , len(summary.split(' ')))
    
    return summary,doc,len(input.split(' ')),len(summary.split(' '))