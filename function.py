def plane_ride_cost(city):
     if city == 'charlotte':
          return 220
     elif city == 'pittsburgh':
          return 222
     elif city == 'los Angles':
          return 475

def rental_car_cost(days):
     day_rate = 40
     total_cost = day_rate * days

     if days >= 7:
          total_cost = total_cost - 50
     elif days >= 3:
          total_cost = total_cost - 20
     return total_cost

def trip_cost(city, days):
     return rental_car_cost(days)  + plane_ride_cost(city)


print(plane_ride_cost('charlotte'))
print(rental_car_cost(20))
print(trip_cost('charlotte',7))
     
