def cars(make, model, **add_ons):
    car_dict = {
        'make': make.title(), 
        'model': model.title(),}

    for add, value in add_ons.items():
        car_dict[add] = value

    return car_dict

print('\n')
passat = cars('volts wagon', 'Passat', trany="8 gear", drive_train='fwd')
print(passat)
print('\n')
ranger = cars('ford', 'ranger', color='cement gray', package='lariut')
print(ranger)
print('\n')
nine_eleven = cars('911', 'porshe', engine='3.8L 6 cylinder', zeroToSixty='2.7 seconds')
print(nine_eleven)
print('\n')