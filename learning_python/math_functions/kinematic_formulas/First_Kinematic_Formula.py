# According to given values decide which function to use
# and returns the result and exit

def first_kinematic_formula(initial_velocity, final_velocity,
                            acceleration, time):

    if initial_velocity == 'x':
        solve_for_initial_velocity(float(final_velocity), float(acceleration), float(time))

    if final_velocity == 'x':
        solve_for_final_velocity(float(initial_velocity), float(acceleration), float(time))

    if acceleration == 'x':
        solve_for_acceleration(float(initial_velocity), float(final_velocity), float(time))

    if time == 'x':
        solve_for_time(float(initial_velocity), float(final_velocity), float(acceleration))

    else:
        main()


def solve_for_initial_velocity(final_velocity, acceleration, time):
    initial_velocity = final_velocity - (acceleration * time)
    print("\nInitial Velocity is: ", initial_velocity)
    exit(0)


def solve_for_final_velocity(initial_velocity, acceleration, time):
    final_velocity = initial_velocity + (acceleration * time)
    print("\nFinal Velocity is: ", final_velocity)
    exit(0)


def solve_for_acceleration(initial_velocity, final_velocity, time):
    acceleration = (final_velocity - initial_velocity) / time
    print("\nAcceleration is: ", acceleration)
    exit(0)


def solve_for_time(initial_velocity, final_velocity, acceleration):
    time = (final_velocity - initial_velocity) / acceleration
    print("\nTime is: ", time)
    exit(0)
