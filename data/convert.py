import random
import os
import librosa
import soundfile as sf
import time

# files = os.listdir('41000_data')
# for file in files:
#     # if 'heyditto' in file:
#     os.system(f'ffmpeg -y -i "41000_data/{file}" -ar 16000 "raw_data/{file}"')

# files = os.listdir('48000_data')
# for file in files:
#     # if 'heyditto3' in file:
#     os.system(f'ffmpeg -y -i "48000_data/{file}" -ar 16000 "raw_data/{file}"')

# files = os.listdir('synthetic_data/')
# for file in files:
#     os.system(f'ffmpeg -y -i "synthetic_data/{file}" -ar 16000 "raw_data/{file}.wav"')

# files = os.listdir('mp3_data/')
# for ndx,file in enumerate(files):
#     stamp = int(time.time())+ndx+1
#     os.system(f'ffmpeg -y -i "mp3_data/{file}" -ar 16000 "raw_data/heyditto-{stamp}-{file}.wav"')

# for i in range(3):
#     files = os.listdir(f'gtts_session{i+1}/')
#     for ndx,file in enumerate(files):
#         stamp = int(time.time())+ndx+1
#         os.system(f'ffmpeg -y -i "gtts_session{i+1}/{file}" -ar 16000 "raw_data/heyditto-{stamp}-{file}.wav"')

# for i in range(13):
#     files = os.listdir(f'gtts_session{i+1}_background/')
#     for ndx,file in enumerate(files):
#         stamp = int(time.time())+ndx+1
#         os.system(f'ffmpeg -y -i "gtts_session{i+1}_background/{file}" -ar 16000 "raw_data/background-{stamp}-{file}.wav"')


# for i in range(12):
# session_num = i + 1
# session_num = 13
# folder = f'gtts_session{session_num}_background/'
# files = os.listdir(folder)
# for ndx,file in enumerate(files):
#     stamp = int(time.time())+ndx+1
#     os.system(f'ffmpeg -y -i "{folder}/{file}" -ar 16000 "raw_data/background-{stamp}-{file}.wav"')


# files = os.listdir('common_voice_dataset/data/')
# for ndx,file in enumerate(files):
#     stamp = int(time.time())+ndx+1
#     os.system(f'ffmpeg -y -i "common_voice_dataset/data/{file}" -ar 16000 "common_voice_dataset/wav_data/{file}.wav"')


# files = os.listdir('Hospital noise original/')
# size = len(files)
# print('converting hospital ambient noise to background dataset')
# for ndx,file in enumerate(files):
#     y, s = librosa.load(f'Hospital noise original/{file}',sr=16000, mono=True)
#     chunk_size = int(y.size/5) # each sample is 5 seconds, so to get 1 second chunks, divide by 5
#     for i in range(0, int(y.size), chunk_size): # iterate through each second
#         sf.write(f'raw_data/background_{file}_{i}.wav', y[i:i+chunk_size], 16000)

# y, s = librosa.load(f'background_data/background-horns.wav',sr=16000, mono=True)
# chunk_size = int(y.size/(y.size/16000)) # each sample is 1 second, so to get 1 second chunks, divide by RATE
# for i in range(0, int(y.size), chunk_size): # iterate through each second
#     sf.write(f'raw_data/background_horns_{i}.wav', y[i:i+chunk_size], 16000)

# files = list(os.listdir('background_data/'))
# random.shuffle(files)
# for file in files:
#     print(f'loading {file}')
#     y, s = librosa.load(f'background_data/{file}', sr=16000, mono=True)
#     # each sample is 1 second, so to get 1 second chunks, divide by RATE
#     chunk_size = int(y.size/(y.size/16000))
#     for i in range(0, int(y.size), chunk_size):  # iterate through each second
#         sf.write(
#             f'raw_data/background_music_{file}_{i}.wav', y[i:i+chunk_size], 16000)

# y, s = librosa.load(f'background_data/omar-talking-2.wav',sr=16000, mono=True)
# chunk_size = int(y.size/(y.size/16000)) # each sample is 1 second, so to get 1 second chunks, divide by RATE
# for i in range(0, int(y.size), chunk_size): # iterate through each second
#     sf.write(f'raw_data/background-omar-talking-2-{i}.wav', y[i:i+chunk_size], 16000)

# files = os.listdir('common_voice_dataset/wav_data/')
# # size = len(files)
# print('converting common voice dataset to background dataset')
# for ndx,file in enumerate(files):
#     stamp = int(time.time())+ndx+1
#     if ndx>500:
#         print(f'converting {file}')
#         y, s = librosa.load(f'common_voice_dataset/wav_data/{file}',sr=16000, mono=True)
#         seconds = y.size / 16000
#         chunk_size = int(y.size/seconds) # get size of 1 second chunk by dividing total size by sample rate
#         for i in range(0, int(y.size), chunk_size): # iterate through each second
#             sf.write(f'raw_data/background_{file}_{i}_{stamp}.wav', y[i:i+chunk_size+1], 16000)

session_num = 14
files = os.listdir(f'elvenlabs_samples/session{session_num}/')
for ndx, file in enumerate(files):
    stamp = int(time.time())+ndx+1
    os.system(
        f'ffmpeg -y -i "elvenlabs_samples/session{session_num}/{file}" -ar 16000 "raw_data/heyditto-{stamp}-{file}.wav"')

# session_num = 9
# files = os.listdir(f'elvenlabs_samples/session{session_num}-background/')
# num_files = len(files)
# print(f'converting {num_files} elevenlabs files to background dataset')
# for ndx, file in enumerate(files):
#     print(f'converting {file}')
#     stamp = int(time.time())+ndx+1
#     y, s = librosa.load(
#         f'elvenlabs_samples/session{session_num}-background/{file}', sr=16000, mono=True)
#     seconds = y.size / 16000
#     # get size of 1 second chunk by dividing total size by sample rate
#     chunk_size = int(y.size/seconds)
#     for x in range(0, int(y.size), chunk_size):  # iterate through each second
#         sf.write(
#             f'raw_data/background_{file}_{x}_{stamp}.wav', y[x:x+chunk_size+1], 16000)

# files = os.listdir('soundscape_audio/')
# num_files = len(files)
# print(f'converting {num_files} soundscape files to background dataset')
# for ndx, file in enumerate(files):
#     print(f'converting {file}')
#     y, s = librosa.load(
#         f'soundscape_audio/{file}', sr=16000, mono=True)
#     seconds = y.size / 16000
#     # get size of 1 second chunk by dividing total size by sample rate
#     chunk_size = int(y.size/seconds)
#     N = 3000  # sample N seconds of audio from soundscape
#     # iterate through each second
#     for count, i in enumerate(range(0, int(y.size), chunk_size)):
#         if count+1 > N:
#             break
#         sf.write(
#             f'raw_data/background_music_{file}_{i}_.wav', y[i:i+chunk_size+1], 16000)
#         count += 1

# files = os.listdir(f'music/')
# num_files = len(files)
# print(f'converting {num_files} music files to background dataset')
# for ndx, file in enumerate(files):
#     print(f'converting {file}')
#     stamp = int(time.time())+ndx+1
#     y, s = librosa.load(
#         f'music/{file}', sr=16000, mono=True)
#     seconds = y.size / 16000
#     # get size of 1 second chunk by dividing total size by sample rate
#     chunk_size = int(y.size/seconds)
#     N = 25  # sample N seconds of audio per music file
#     for count, x in enumerate(range(0, int(y.size), chunk_size)):  # iterate through each second
#         if count+1 > N:
#             break
#         sf.write(
#             f'raw_data/background_music_{file}_{x}_{stamp}.wav', y[x:x+chunk_size+1], 16000)
