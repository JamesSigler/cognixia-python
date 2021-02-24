def circ_area(rad):
    return 3.14*rad**2

def circ_vol(area, height):
    return area*height

c_area = circ_area(4)
c_vol = circ_vol(c_area, 10)

print (c_area)
print (c_vol)