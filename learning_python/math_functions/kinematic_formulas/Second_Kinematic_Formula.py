# Solve for time, acceleration, final velocity or initial velocity
# by using First Kinematic Formula.
# Usage: enter the known values. Enter 'x' for unknown value.
#
def second_kinematic_formula(initial_velocity, final_velocity,
                            displacement, time):

    if initial_velocity == 'x':
        solve_for_initial_velocity(float(final_velocity), float(displacement), float(time))

    if final_velocity == 'x':
        solve_for_final_velocity(float(initial_velocity), float(displacement), float(time))

    if displacement == 'x':
        solve_for_displacement(float(initial_velocity), float(final_velocity), float(time))

    if time == 'x':
        solve_for_time(float(initial_velocity), float(final_velocity),
                       float(displacement))

    else:
        exit(1)


def solve_for_initial_velocity(final_velocity, displacement, time):
    initial_velocity = ((2 * displacement) / time) - final_velocity
    print("\nInitial Velocity is: ", initial_velocity)
    exit(0)


def solve_for_final_velocity(initial_velocity, displacement, time):
    final_velocity = ((2 * displacement) / time) - initial_velocity
    print("\nFinal Velocity is: ", final_velocity)
    exit(0)


def solve_for_displacement(initial_velocity, final_velocity, time):
    displacement = ((final_velocity + initial_velocity) / 2) * time
    print("\nDisplacement is: ", displacement)
    exit(0)


def solve_for_time(initial_velocity, final_velocity, displacement):
    time = displacement / ((initial_velocity + final_velocity) / 2)
    print("\nTime is: ", time)
    exit(0)


