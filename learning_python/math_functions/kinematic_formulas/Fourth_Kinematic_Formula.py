# Solve for displacement, acceleration, final velocity or initial velocity
# by using First Kinematic Formula.
# Usage: enter the known values. Enter 'x' for unknown value.
#
def fourth_kinematic_formula(initial_velocity, final_velocity,
                            displacement, acceleration):

    if initial_velocity == 'x':
        solve_for_initial_velocity(float(final_velocity), float(acceleration),
                                   float(displacement))

    if final_velocity == 'x':
        solve_for_final_velocity(float(initial_velocity), float(displacement),
                                 float(acceleration))

    if displacement == 'x':
        solve_for_displacement(float(initial_velocity), float(final_velocity),
                               float(displacement))

    if acceleration == 'x':
        solve_for_acceleration(float(initial_velocity), float(final_velocity),
                       float(displacement))

    else:
        exit(1)


def solve_for_initial_velocity(final_velocity, acceleration, displacement):
    from math import sqrt
    initial_velocity = sqrt((final_velocity**2) -
                            (2 * acceleration * displacement))
    print("\nInitial Velocity is: ", initial_velocity)
    exit(0)


def solve_for_final_velocity(initial_velocity, acceleration, displacement):
    from math import sqrt
    final_velocity = sqrt((initial_velocity**2) +
                          (2 * acceleration * displacement))
    print("\nFinal Velocity is: ", final_velocity)
    exit(0)


def solve_for_displacement(initial_velocity, final_velocity, acceleration):
    displacement = ((final_velocity**2) - (initial_velocity**2)) / (2*acceleration)
    print("\nDisplacement is: ", displacement)
    exit(0)


def solve_for_acceleration(initial_velocity, final_velocity, displacement):
    acceleration = ((final_velocity**2) - (initial_velocity**2)) / (2*displacement)
    print("\nAcceleration is: ", acceleration)
    exit(0)
