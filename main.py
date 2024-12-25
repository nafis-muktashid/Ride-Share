from ride import RideRequest, Ride, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, MotorCycle

niye_jao = RideSharing("Niye Jao")

rahim = Rider("Rahim", "omuk@asdasd.com", 345266, "Badda", 500)
niye_jao.add_rider(rahim)

kolim = Driver("KolimBai", "tomuk@asff.com", 666463, "Notun Bazar")
niye_jao.add_driver(kolim)




rahim.request_ride(niye_jao, "Mirpur", "car")

kolim.reach_destination(rahim.current_ride)

rahim.show_current_ride()



# print(niye_jao)