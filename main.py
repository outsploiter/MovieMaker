import argparse
import utils.clip_editor as clipper


def manual_mode():
    print('Enter the file location with forward slashes(/) example (file/path/video.mp4)\n\n\tEnter here: ')
    video_path = input()
    print('Enter the no of scenes in number: ')
    num = int(input())
    time_dict = {}
    for i in range(num):
        scene_temp = input('Enter the scene name: ')
        time_dict[scene_temp] = {}
        print('Enter the start time(hh:mm:ss)\n\n\tEnter here: ')
        start_time = input()
        time_dict[scene_temp]['from'] = start_time
        print('Enter the start time(hh:mm:ss)\n\n\tEnter here: ')
        end_time = input()
        time_dict[scene_temp]['to'] = start_time
        print('Enter the tag\n\n\tEnter here: ')
        end_time = input()
        time_dict[scene_temp]['tag'] = start_time

    clips, tags = clipper.get_short_clips(time_dict, video_path)
    print('Completed trimming to short video')
    print('Would you like to upload? : ')


def auto_mode():
    import json
    f = open('config.json')
    control_dict = json.load(f)
    video_path = control_dict['file_location'].replace('\\', '/')
    time_dict = control_dict['scenes']
    clips, tags = clipper.get_short_clips(time_dict, video_path)
    print('Completed trimming to short video')

    # unique_tags = list(set(tags))
    # clipper.merge_clips(clips, tags, unique_tags)


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
