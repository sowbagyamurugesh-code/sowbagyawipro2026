class parent:
    def show(self):
        print("parent")
class child1(parent):
    def c1(self):
        print("child1")
class child2(parent):
    def c2(self):
        print("child2")

c1=child1()
c2=child2()
c1.show()
c1.c1()
c2.show()
c2.c2()