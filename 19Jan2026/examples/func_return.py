def area_cal(radius,PIE=3.141): # PIE is constant
    result = PIE * (radius ** 2)
    return result

print('Calling the function area_cal()')
print(area_cal(15)) #print value  or message 
print('Calling the function area_cal()')
ret=area_cal(25)
print(f'area of circle is {ret}')
