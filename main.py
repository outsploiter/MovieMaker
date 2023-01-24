import argparse
import utils.clip_editor as clipper


def manual_mode():
    pass


def auto_mode():
    import json
    f = open('config.json')
    control_dict = json.load(f)
    video_path = control_dict['file_location'].replace('\\', '/')
    time_dict = control_dict['scenes']
    clips, tags = clipper.get_short_clips(time_dict, video_path)
    unique_tags = list(set(tags))
    clipper.merge_clips(clips, tags, unique_tags)


def main():
    parser = argparse.ArgumentParser()
    MODE_MESSAGE = '''
    Two Modes ->
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
        auto_mode()
    else:
        print("No such options available in modes. check the spelling of the mode you entered")


if __name__ == '__main__':
    main()
