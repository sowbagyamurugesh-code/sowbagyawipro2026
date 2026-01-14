data=[1,2,3]
itr=iter(data)
print(next(itr))
print(next(itr))
print(next(itr))

for i in [3,2,1]:
    print(i)

# custom iterator that counts numbers from 1 up to a given limit.
class count:
    def __init__(self,limit):
        self.limit=limit
        self.current=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.limit:
            val=self.current
            self.current+=1
            return val
        else:
            raise StopIteration
obj=count(5)
for i in obj:
    print(i)
