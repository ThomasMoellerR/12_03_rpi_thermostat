class thermostat:

    def __init__(self):
        self.state = "STATE_A"
        self.list = []
        self.valid = False


    def set_temperature(self, temperature):
        self.create_list(temperature)


    def create_list(self,temperature):
        self.list.clear()
        for i in range(120):
            self.list.append(self.state_machine(0)) # Herunterfahren

        for i in range(self.calculate_forward_steps(temperature)):
            self.list.append(self.state_machine(1)) # Hochfahren

        self.valid = True


    def valid_list(self):
        ret = False
        if self.valid:
            ret = True
            self.valid = False
        return ret


    def get_list(self):
        return self.list


    def calculate_forward_steps(self, fTemperature):
        imp = 0
        temp = 0
        ret = 0

        if fTemperature < 5.0: fTemperature = 0.0 # Begrenzung
        if fTemperature > 30.0: fTemperature = 30.0 # Begrenzung

        if fTemperature == 5.0:
            imp = 2 # Von Ausschalten auf 5 Grad braucht es zwei Impulse


        if fTemperature > 5.0:
            imp = 2 # Von Ausschalten auf 5 Grad braucht es zwei Impulse
            imp += int((fTemperature - 5.0) / 0.5) # Impulse Vorkomma berechnen
            temp = int((fTemperature * 2) % 2) # Nachkomma ?
            if temp: ret += 1 # Für Nachkommastelle einen Impuls mehr

        ret = imp * 2 # * 2 weil ein Encoder-Schritt aus zwei Teilschritten besteht

        return ret


    def state_machine(self, dir):
        a = 0
        b = 0

        while True:

            if self.state == "STATE_A":
                a = 0
                b = 0
                if dir: self.state = "STATE_D"
                else: self.state = "STATE_E"
                break

            if self.state == "STATE_B":
                a = 1
                b = 1
                if dir: self.state = "STATE_C"
                else: self.state = "STATE_F"
                break

            if self.state == "STATE_C":
                a = 0
                b = 1
                self.state = "STATE_A"
                break

            if self.state == "STATE_D":
                a = 1
                b = 0
                self.state = "STATE_B"
                break

            if self.state == "STATE_E":
                a = 0
                b = 1
                self.state = "STATE_B"
                break

            if self.state == "STATE_F":
                a = 1
                b = 0
                self.state = "STATE_A"
                break

            break

        return a, b
