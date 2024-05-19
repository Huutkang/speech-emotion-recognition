import matplotlib.pyplot as plt
import sounddevice as sd
import librosa


data, sr = librosa.load('test/Hello Viet Nam.mp3')

sd.play(data, sr)

data = data[12*sr:17*sr]


zcr = librosa.feature.zero_crossing_rate(y=data)
print("zcr:", zcr.shape)


stft = librosa.stft(data)
chroma_stft = librosa.feature.chroma_stft(S=stft, sr=sr)
print("chroma_stft:", chroma_stft.shape)


mfcc = librosa.feature.mfcc(y=data, sr=sr)
print('mfcc:', mfcc.shape)


rms = librosa.feature.rms(y=data)
print('rms:', rms.shape)


mel = librosa.feature.melspectrogram(y=data, sr=sr)
print('mel:', mel.shape)


xdb = librosa.amplitude_to_db(mfcc)
librosa.display.specshow(xdb, sr=sr, x_axis='time')
plt.colorbar()
plt.show()

sd.wait()
