import math


def fuelneed(mass):
    return int(math.floor(int(mass)/3))-2
fuel_counter_upper = 0

temp = input()
while temp != '':
    if temp != '':
        print('DEBUG: {}'.format(fuelneed(temp)))
        remaining_fuel = fuelneed(temp)
        while fuelneed(remaining_fuel) >= 0:
            fuel_counter_upper += remaining_fuel
            print('DEBUG: Counter:{}'.format(fuel_counter_upper))
            remaining_fuel = fuelneed(remaining_fuel)
            print('DEBUG: Remaini:{}'.format(remaining_fuel))
        fuel_counter_upper += remaining_fuel
    temp = input()

print('Total required fuels: '+str(fuel_counter_upper))