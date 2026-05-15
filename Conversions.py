import math

fields = {}

def convert(field, value):
    if field in fields:
        return fields[field](value)
    return None

#Convert Degrees and Radians

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

fields['degrees-radians'] = degrees_to_radians

def radians_to_degrees(radians):
    return radians * (180 / math.pi)

fields['radians-degrees'] = radians_to_degrees

print(convert('degrees-radians', 90))