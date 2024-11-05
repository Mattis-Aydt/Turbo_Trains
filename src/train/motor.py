class Motor:
    def __init__(self, efficiency_curve, energy_consumption_curve, energy_source):
        self.energy_consumption_curve = energy_consumption_curve
        self.efficiency_curve = efficiency_curve
        self.energy_source = energy_source

        self.throttle = 0

    def get_power_output(self, rpm):
        energy_consumption = self.energy_source.use(self.energy_consumption_curve(rpm, self.throttle))
        return energy_consumption * self.efficiency_curve(rpm, self.throttle)


