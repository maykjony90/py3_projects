def main():
    # Get user inputs for prior probabilities
    prior_positive_prob = float(input("What is prior probability of: "))
    sensitivity = float(input("What is sensitivity: "))
    specitivity = float(input("What is the specitivity: "))

    # Find negative probability
    prior_negative_prob = 1-prior_positive_prob

    # Calculate positive joint
    joint_positive = (prior_positive_prob*sensitivity) + \
                    (prior_negative_prob)*(1-specitivity)
    print("\nJoint of positive probability: " + str(joint_positive) + "\n")

    # Calculate negative joint
    joint_negative = (prior_positive_prob)*(1-sensitivity) + \
                    (specitivity*prior_negative_prob)
    print("Joint of negative probability: " + str(joint_negative) + "\n")

    # Find Posterior Positive Probability of prior positive probability
    posterior_pos_prob = (prior_positive_prob*sensitivity) / joint_positive
    print("Posterior Positive Result of Prior Positive Probability: " +
          str(posterior_pos_prob) + "\n")

    # Find Posterior Negative Probability of prior negative probabilty
    posterior_neg_prob = (prior_positive_prob*(1-sensitivity)) / joint_negative
    print("Posterior negative probability of prior negative probability: "
          + str(posterior_neg_prob) + "\n")


if __name__ == "__main__":
    main()
