class Lightbulb:
    def __init__(self):
        self.status = False

    def turn_on(self):
        if self.status == False:
            print("ON!")
            self.status = True

    def turn_off(self):
        if self.status == True:
            print("OFF!")
            self.status = False



l1 = Lightbulb()
l2 = Lightbulb()
l3 = Lightbulb()
l4 = Lightbulb()


l1.turn_on()
l3.turn_on()

# This is a NOOP
l1.turn_on()









