class computer:
    def __init__(self,brand,ram,rom):
        self.brand=brand
        self.ram=ram
        self.rom=rom
    def info(self):
        print(self.brand,self.ram,self.rom)

comp1=computer('Asus','16gb','512gb')
comp2=computer('acer','4gb','2tb')

comp1.info()
comp2.info()
comp1.brand="hp"
print(comp1.brand)