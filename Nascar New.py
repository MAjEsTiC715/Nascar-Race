#========================================================  Documentation(FINISHED)  ==================================================================================
#Define a class called Car with the following attributes:
    #Total Odometer Miles
    #Speed in miles per hour
    #Driver Name
    #Sponsor
#The total odometer miles and speed should be initialized to zero.
#Create a list of 20 unique vehicles with random (or real (Links to an external site.)Links to an external site.) driver and sponsor names.
#Your main program should simulate the progress of the vehicles in the race. Every simulated minute, the vehicles pick a new random speed between 1 and 120,
#and their odometer miles are updated every minute using this equation:
    #odometer_miles = odometer_miles + speed * time 
#Since speed is in miles per hour, time should be in hours as well (1 minute is 1/60th of an hour).
#The first car to reach 500 miles should be declared the winner by printing the driver name and sponsor name.
#Include any useful methods in your class definition that you see fit.
#Be sure to use comments for both structure of the program and documentation of the code.
#All code must completely be your own individual work product.
#===========================================================================================================================================================

from random import randint #import randint from random

class Car:
    #initialize d_name and sponsor
    def __init__(self, d_name, sponsor):
        self.odometer = 0
        self.speed = 0
        self.driver_name = d_name
        self.sponsor = sponsor

    #set speed
    def set_speed(self, speed):
        self.speed = speed

    #set odometer which adds on the speed to the previous odometer
    def set_odometer(self):
        self.odometer += self.speed
        return self.odometer

    #get speed
    def get_speed(self):
        return self.speed

    #get odometer
    def get_odometer(self):
        return self.odometer 

    #get driver
    def get_driver(self):
        return self.driver_name

    #get sponsor
    def get_sponsor(self):
        return self.sponsor

def main():
    #Create 1 list called car_list
    car_list = []
    #create 20 instances of the object car called v[i]
    v = Car('John','Target')
    v2 = Car('Smith','Walmart')
    v3 = Car('Alex','must Cisco')
    v4 = Car('Travis','Costco')
    v5 = Car('James','Albertson')
    v6 = Car('Dan','LumberCo')
    v7 = Car('David','Exxon')
    v8 = Car('Mike','Wonder Bread')
    v9 = Car('Cody','Taco Bell')
    v10 = Car('Matt','Taco John')
    v11 = Car('Austin','McDonalds')
    v12 = Car('Ty','Burger King')
    v13 = Car('Dale','Safeway')
    v14 = Car('Jeffrey','Wendys')
    v15 = Car('Chase','Town Pump')
    v16 = Car('Gray','Dodge')
    v17 = Car('Denny','Ford')
    v18 = Car('Kevin','Porshe')
    v19 = Car('Professor Gose','Ruby')
#append each instance that we have created into car_list
    car_list.append(v)
    car_list.append(v2)
    car_list.append(v3)
    car_list.append(v4)
    car_list.append(v5)
    car_list.append(v6)
    car_list.append(v7)
    car_list.append(v8)
    car_list.append(v9)
    car_list.append(v10)
    car_list.append(v11)
    car_list.append(v12)
    car_list.append(v13)
    car_list.append(v14)
    car_list.append(v15)
    car_list.append(v16)
    car_list.append(v17)
    car_list.append(v18)
    car_list.append(v19)

    race(car_list) #execute the race function
    
def race(car_list):
    
    Race = True #set Race to true this will be the sentinal
    while Race == True:
        for n in range(len(car_list)):
            rand = randint(1,120) #rand is a variable that generates a random number each time the loop is iterated
            car_list[n].set_speed(rand) #access the attibute speed and asign a random number
            car_list[n].set_odometer() #we execute the method set_odometer which adds on the speed to the previous odometer
            odom = car_list[n].get_odometer() #odom is the argument to getting the odometer for that driver
            print(car_list[n].driver_name, odom)   #print the drivers name and the odometer associated with it 
            if car_list[n].odometer >= 500: #print the winner when the odom is over 500
                print('\nThe winner is:', car_list[n].get_driver(), '\tSponserd by', car_list[n].get_sponsor()) 
                input('\nPress Enter to do another race\n\n\n\n\n\n\n')
                del car_list[:] #deleted the car list
                main() #execute the main function again
                break
            else:
                print('')
                 

main()
