from sys import argv

def main(argv):
    if len(argv) != 4:
        print("Usage: bilesik_faiz.py <amount> <%_groth_rate> <iter_time> ")
        exit(1)


    result = float(argv[1]) * (1 + float(argv[2]) * .01) ** float(argv[3])
    print(result)
    exit(0)



if __name__ == "__main__":
    main(argv)

