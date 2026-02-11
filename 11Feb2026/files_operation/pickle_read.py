import pickle

def reading_data():
    with open("11Feb2026/file.pk1","rb+") as fb:
        content=pickle.load(fb)
        print(content)
        fb.close()
    
reading_data()