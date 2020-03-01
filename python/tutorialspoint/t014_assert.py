#!/usr/bin/python

def KelvinToFahrenheit(kelvin) :
    assert(kelvin >= 0), "Colder than absolute 0!"
    return 32 + (kelvin - 273.15) * 9 / 5

print KelvinToFahrenheit(273.15)
print KelvinToFahrenheit(0)
print KelvinToFahrenheit(-5)

