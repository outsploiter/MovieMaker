from moviepy.editor import VideoFileClip, concatenate_videoclips, ImageClip, CompositeVideoClip
import os


def get_short_clips(time_dict, video_path):
    clips = []
    tags = []
    main_clip = VideoFileClip(video_path)
    for i in time_dict.keys():
        clip_title = time_dict[i]
        store_location = str(video_path[:video_path.rindex('/')]) + '/clips/'
        if not os.path.exists(store_location):
            os.makedirs(store_location)
        file_name = f'{i}.mp4'
        temp = main_clip.subclip(t_start=clip_title['from'], t_end=clip_title['to'])
        print(f'Rendering Clip - {file_name}')
        temp.write_videofile(store_location + file_name,
                             fps=20, threads=32, logger=None,
                             codec="mpeg4", preset="slow",
                             ffmpeg_params=['-b:v', '20000k'])
        clips.append(store_location + file_name)
        tags.append(clip_title['tag'])
        temp.close()
    main_clip.close()
    return clips, tags


def merge_clips(clip_list, tag_list, tag_types=None):
    print('Merging clips')
    final_location = str(clip_list[0][:clip_list[0].rindex('/')]) + '/final/'
    if not os.path.exists(final_location):
        os.makedirs(final_location)
    for tag in tag_types:
        print('Working on tag - ', tag)
        current_tag_clips = []
        for i in range(len(clip_list)):
            if tag_list[i] == tag:
                temp = VideoFileClip(clip_list[i])
                current_tag_clips.append(temp)
        if len(current_tag_clips) > 1:
            print(f'Concatenating clips from the tag - {tag}')
            no_logo_clip = concatenate_videoclips(current_tag_clips)
            logo = (ImageClip("artifacts/logo.png")
                    .set_duration(no_logo_clip.duration)
                    .resize(height=80)  # if you need to resize...
                    .margin(right=10, top=10, opacity=0)  # (optional) logo-border padding
                    .set_pos(("right", "top")))
            final = CompositeVideoClip([no_logo_clip, logo])
            print(f'Rendering final video - final_{tag}.mp4')
            final.write_videofile(final_location + f'final_{tag}.mp4',
                                  fps=24, threads=32, logger=None,
                                  codec="mpeg4", preset="slow",
                                  ffmpeg_params=['-b:v', '20000k'])
        else:
            print("only one video found not merging")
            print(current_tag_clips)