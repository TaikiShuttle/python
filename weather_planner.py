distance_mi = 5
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = False

if distance_mi == False:
    print("False")
elif distance_mi <= 1 and is_raining == False:
    print("True")
elif distance_mi > 1 and distance_mi <= 6 and not is_raining and has_bike:
    print('True')
elif distance_mi > 6 and has_ride_share_app:
    print("True")
elif distance_mi > 6 and has_car:
    print("True")
else:
    print("False") 
