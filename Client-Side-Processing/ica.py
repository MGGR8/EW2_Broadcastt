# # import soundfile as sf
# # import numpy as np
# # from sklearn.decomposition import FastICA

# # file0 = 'mixed_audio.wav'

# # input_signal_0, sample_rate_0 = sf.read(file0)

# # print(input_signal_0.shape)

# # # input = np.reshape(input_signal_0, (len(input_signal_0), 1))
# # input = list(zip(input_signal_0, input_signal_0))

# # ica = FastICA(n_components=2)
# # components = ica.fit_transform(input)

# # c1 = components[:, 0]
# # c2 = components[:, 1]

# # sf.write('component1.wav', 50*c1, sample_rate_0)
# # sf.write('component2.wav', 50*c2, sample_rate_0)


import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="input value")
args = parser.parse_args()

output_name = 'input_file_1_' # replace with your desired output file name
number = args.input
format = '.wav'

output_file = output_name + str(number) + format
# print("ica.py")
# print(output_file)

# #processing



# # import subprocess
# # cmd = f'ffplay {output_file}'
# # subprocess.call(cmd, shell=True)

import soundfile as sf
import sounddevice as sd

# path to the audio file
audio_file_path = output_file

# read the audio file
data, sample_rate = sf.read(audio_file_path)

# play the audio file
sd.play(data, sample_rate)

# wait for playback to finish
sd.wait()

