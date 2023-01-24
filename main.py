import argparse


def manual_mode():
    pass


def auto_mode():
    pass


def main():
    parser = argparse.ArgumentParser()
    MODE_MESSAGE = '''
    Mode can of two types
    1.Manual - which takes continues user inputs in runtime and
    2.Auto - which takes input from the config json(edit the file accordingly before running in this mode).
    '''
    parser.add_argument("-m", "--mode", help=MODE_MESSAGE)
    args = parser.parse_args()
    if args.mode.lower() == 'manual':
        print("Running in manual mode")
        manual_mode()
    elif args.mode.lower() == 'auto':
        print("Running in Auto mode from the config json")
    else:
        print("No such options available in modes. check the spelling of the mode you entered")


if __name__ == '__main__':
    main()
