# Solve for time, acceleration, final velocity or initial velocity
# by using First Kinematic Formula.
# Usage: enter the known values. Enter 'x' for unknown value.
#


def main():
    print("Usage: enter known values, enter 'x' for missing value" + \
          ", enter '-' for irrelavent value.")
    initial_velocity = input("initial velocity: ")
    final_velocity = input("final velocity: ")
    acceleration = input("constant acceleration: ")
    time = input("time interval: ")
    displacement = input("displacement: ")


    if final_velocity == '-':
        from Third_Kinematic_Formula import third_kinematic_formula as tkf

        tkf(initial_velocity, acceleration, displacement, time)

    if acceleration == '-':
        from Second_Kinematic_Formula import second_kinematic_formula as skf

        skf(initial_velocity, final_velocity, displacement, time)

    if time == '-':
        from Fourth_Kinematic_Formula import fourth_kinematic_formula as fkf

        fkf(initial_velocity, final_velocity, acceleration, displacement)

    if displacement == '-':
        from First_Kinematic_Formula import first_kinematic_formula as ftk

        ftk(initial_velocity, final_velocity, acceleration, time)

    else:
        main()


if __name__ == "__main__":
    main()
