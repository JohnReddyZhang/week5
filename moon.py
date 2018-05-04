# Demo for SOLID.
from time import sleep
from random import randint


SEVERITY = 2

def ScreenLogger:
    def emit(msg):
        print(msg)

def FileLogger:
    def emit(msg):
        with open("moon.log", "w") as f:
            f.write(msg + "\n")

def log(msg):
    print(msg)

def log(msg, logger):
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
# * Duck typing? make sure objects have the same methods.
# * Dependency Inversion?
