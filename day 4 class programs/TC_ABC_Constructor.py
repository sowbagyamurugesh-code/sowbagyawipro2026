from abc import ABC, abstractmethod
class emp(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def salary(self):
        pass
class manager(emp):
    def salary(self):
        print(self.name, "salary 1000")
ob=manager("david")
ob.salary()