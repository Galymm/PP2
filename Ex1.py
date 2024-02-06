class strManipulator():
    def __inti__(self):
        self.string=""
    def inpStr(self):
        self.string=input("Enter a string: ")
    def outStr(self):
        print("Original string: ", self.string)
        print("Operation output: ", self.string.upper())
    def outStrlower(self):
        print("Oringnial string: ", self.string)
        print("Operation output: ", self.string)
def main():
    manipulator=strManipulator()
    manipulator.inpStr()

    print("\nEnter the operation:")
    print("1. Output original string")
    print("2. Output uppercase of string")
    choise=input("Your choise: ")

    if choise=="1":
        manipulator.outStrlower()
    elif choise=="2":
        manipulator.outStr()
    else:
        print("Invalid syntax")
if __name__=="__main__":
    main()