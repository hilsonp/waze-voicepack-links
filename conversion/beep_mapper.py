"""
I like listening podcast on my commute.
I hate announcements to cut/pause the podcast for all directions I know...
... still, hate missing a redirection or a hazard announcement.

The idea is therefore to generate a voice pack with short and soft beeps (like in an airplane cabin).

This scripts uses the prompt_names.csv to map prompt_names to beep sounds.
The beep mp3 inputs are in the input folder.
The prompt mp3 are "generated" in the output folder.
"""

import csv
import shutil

input_dir='input'
output_dir='output'
beep={
    'silence': '1ms_silence.mp3',
    'notice': 'airplane-dong.mp3',
    'alert': 'airplane-ding.mp3'
}

with open('prompt_names.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    for prompt_name, type in csvreader:
        input_filename="input/{}".format(beep[type])
        output_filename="output/{}".format(prompt_name)
        print('{} = {} => copy {} to {}'.format(prompt_name, type, input_filename, output_filename))
        shutil.copyfile(input_filename, output_filename)
