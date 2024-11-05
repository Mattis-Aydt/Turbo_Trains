# Turbo_Trains
A 2d train game

# Calculation of power
Calculation is triggered by the Train requesting the acceleration of each of its railcars
It is propagated through all the components, until reaching the motor
The motor has a efficiency and fuel consumption function, where he inputs rpm and throttle, receives efficiency and consumption and calculates power
This consumption is always calculated in Joules(Watt seconds) and has to be transfered to liters of gasoline etc if needed
