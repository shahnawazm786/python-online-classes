import pickle

def writing_data(data):
    with open("11Feb2026/file.pk1","wb+") as wf:
        pickle.dump(data,wf)
        wf.close()
    
my_data = {'username': 'alex', 'theme': 'dark', 'notifications': True}
writing_data(dict(my_data))