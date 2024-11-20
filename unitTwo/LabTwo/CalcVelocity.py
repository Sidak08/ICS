
def calcVelocity(intialVelocity, height):
    global GRAVITY
    return (intialVelocity**2 + 2*GRAVITY * height)**0.5

def convertMetersPerSecToKilometersPerSec(metersPerSec):
    return metersPerSec / 10000

GRAVITY = 9.8
height = float(input("Enter the height of the object in meters: "))
intialVelocity = float(input("Enter the initial velocity of the object in m/s: "))

finVelocityInMeters = calcVelocity(intialVelocity, height)
finVelocityInKiloMeters = convertMetersPerSecToKilometersPerSec(finVelocityInMeters)

print(f"The final velocity of the object is {finVelocityInMeters} m/s or {finVelocityInKiloMeters} km/s.")
