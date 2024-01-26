# POLYMORPHISM : > Taking multiple forms > in built ex : len() -> can use to find length of any data type
class xyz():
    def websites(self):
        print("amazon.in is a wesite of many available on net. ")
    
    def topic(self):
        print("Python has many uses in technology.")

    def type(self):
        print("VIT is a college.")

class PQR():
    def websites(self):
        print("flutter.in is a wesite of many available on net. ")
    
    def topic(self):
        print("CPP has many uses in technology.")

    def type(self):
        print("MIT is a college.")


obj_itp = xyz()
obj_pvt = PQR()

for domain in (obj_itp,obj_pvt):
    domain.websites()
    domain.topic()
    domain.type()