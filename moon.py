# Demo for SOLID.
from time import sleep
from random import randint

def log(msg):
    print(msg)

def perform(manuever):
    # pretend we are performing it
    log(manuever)

    # simulate a hard-to-find bug:
    # if randint(1,5) == 1:
    #     raise Exception("Crashed during " + manuever)

def land_on_moon():
    phases = ["Liftoff!", "Low-Earth Orbit Insertion", "Orbiting Earth",
              "Going to Moon Orbit", "Moon Orbit Insertion", "Oribiting Moon",
              "Descending to Surface", "Landed!"]

    try:
        for phase in phases:
            perform(phase)
            sleep(0.5)
    except Exception as e:
        print(e)

land_on_moon()


# Requirements have changed:
# * log based on severity level
# * log to file
# * log with timestamp (datetime.datetime.now())

# Ideas:
# * Parameters?
# * Polymorphism?
# * Duck typing?
# * Dependency Inversion?
