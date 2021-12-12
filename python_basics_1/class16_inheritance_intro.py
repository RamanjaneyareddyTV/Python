#class example
#mobile
class Mobile:
    def __init__(self,name,ram,display,version,price):
        self.name=name
        self.ram=ram
        self.display=display
        self.version=version
        self.price=price
    def dis(self):
        print("mobile-name:",self.name)
        print("Ram:",self.ram)
        print("display:",self.display)
        print("version:",self.version)
        print("price:",self.price)       
obj=Mobile("apple",4,6,'ios',90000)
obj1=Mobile("mi",4,6,'android',10000)
obj.dis()
obj1.dis()
#inheritance
'''kcr parent,base,super
   ktr dervied,child,sub-class
  
parent-class
child-class
  

  
    
Types
1.single inheritance
2.multiple
3.multilevel
4.hierarichal
'''