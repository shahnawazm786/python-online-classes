class Test:
    def __hash__(self):
        return 1
    def __eq__(self, value):
        return False


t=Test()
t1=Test()
di={t:"Test",t1:"Test"}
print(id(t))
print(id(t1))
print(di)