from abc import ABC, abstractmethod
class bank(ABC):
    def interest(self):
        pass
    def loan(self):
        pass

class SBI(bank):
    def interest(self):
        print("interest")
    def loan(selfself):
        print("loan")
obj=SBI()
obj.interest()
obj.loan()