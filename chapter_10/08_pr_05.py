class Train :
    
    def __init__(self , name , fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    
    def getInfo(self):
         print(f"The name of the train is {self.name} and available seats are {self.seats}")
        
    def fareInfo(self):
        print(f"The ticket price is {self.fare} Taka")
        
    def bookTicket(self):
        if(self.seats > 0):
            print(f"You seats is booked . Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("No sit available")

chandonaExpress = Train('chandonaExpress' , 200 , 2 )
chandonaExpress.getInfo()
chandonaExpress.fareInfo()
chandonaExpress.bookTicket()
