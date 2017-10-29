# Solve for time, acceleration, final velocity or initial velocity
# by using First Kinematic Formula.
# Usage: enter the known values. Enter 'x' for unknown value.
#
def third_kinematic_formula(initial_velocity, acceleration,
                            displacement, time):

    if initial_velocity == 'x':
        solve_for_initial_velocity(float(displacement),
                                   float(displacement), float(time))

    if acceleration == 'x':
        solve_for_acceleration(float(initial_velocity),
                                        float(displacement), float(time))

    if displacement == 'x':
        solve_for_displacement(float(initial_velocity),
                               float(displacement), float(time))

    if time == 'x':
        solve_for_time(float(initial_velocity), float(acceleration),
                       float(displacement))
        exit(0)

    else:
        exit(1)


def solve_for_initial_velocity(acceleration, displacement, time):
    initial_velocity = (displacement - (.5 * acceleration * (time**2))) / time
    print("\nInitial Velocity is: ", initial_velocity)
    exit(0)


def solve_for_displacement(initial_velocity, acceleration, time):
    displacement = (initial_velocity * time) + (.5 * acceleration * (time**2))
    print("\nDisplacement Velocity is: ", displacement)
    exit(1)


def solve_for_time(initial_velocity, acceleration, displacement):
    from Quadratic_Formula import quadratic_formula as qf
    acceleration = acceleration * 0.5
    displacement = -1 * displacement
    print(acceleration, initial_velocity, displacement)
    qf(acceleration, initial_velocity, displacement)
    exit(0)


def solve_for_acceleration(initial_velocity, time, displacement):
    acceleration = (displacement - (initial_velocity*time)) / (.5 * (time**2))
    print("\nAcceleration is: ", acceleration)
    exit(0)


