global girlfriend_anger
global in_public
global is_horny
girlfriend_anger=0
in_public=False
is_horny=False

class boobs:

    def __init__(self):
        self.girlfriend_anger = 0
    
    def touch(self, in_public, is_horny):
        if in_public == True:
            girlfriend_anger += 40
        else:
            girlfriend_anger += 20
        if is_horny == True:
            girlfriend_anger -= 20

    def slap(self):
        girlfriend_anger += 50

    def stare(self):
        girlfriend_anger += 10

    def kiss(self, is_horny):
        if is_horny == True:
            girlfriend_anger -= 20
        else:
            girlfriend_anger += 20

    def suck(is_horny):
        if is_horny == True:
            girlfriend_anger -= 30
        else:
            girlfriend_anger += 50

    def is_dead(self):
        if girlfriend_anger >= 100:
            print("You are dead")

    def is_horny(self, is_horny):
        is_horny = input("Is Horny? (True/False)")

    def is_public(self, in_public):
        in_public = input("In Public? (True/False)")
    

while True:
    global girlfriend_anger
    global in_public
    global is_horny
    girlfriend_anger=0
    in_public=False
    is_horny=False
    boobs = boobs()
    boobs.is_horny(is_horny)
    boobs.is_public(in_public)
    boobs.touch(in_public, is_horny)
    boobs.slap()
    boobs.stare()
    boobs.kiss(is_horny)
    boobs.suck(is_horny)
    boobs.is_dead(girlfriend_anger)