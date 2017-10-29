def main():
    # ask user name
    user_name = input("type your name: ")

    # capitilize user name's first letter
    user_name = user_name[0].upper() + user_name[1:]

    # prompt greeting to user
    print("Hello %s" % user_name)


if __name__ == "__main__":
    main()
