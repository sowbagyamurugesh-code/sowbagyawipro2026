class animal:
    def speak(self):
        print("animal makes sound")
class dog(animal):
    def bark(self):
        print("dog barks")

d=dog()
d.bark()
d.speak()