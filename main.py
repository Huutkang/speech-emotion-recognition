import os
from lib.ham_ho_tro import save_obj, load_obj
from models import lstm, cnn
from app import Realtime


cwd = os.getcwd()

if 'speech emotion recognition' not in cwd:
    raise Exception('open sai thư mục. vui lòng open thư mục speech emotion recognition')



# =================================================================

# a = cnn(['TESS',  'Emotion', 'RAVDESS', 'SAVEE'], '1d', ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel'])
# a.select_audio_preprocessing['sequentially'] = False
# a.run(50)
# save_obj(a)

# -----------------------------------------------------------------

# a = cnn(['TESS',  'Emotion', 'RAVDESS', 'SAVEE'], '2d', ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel'])
# a.continue_studying = True
# a.run(5)
# save_obj(a)

# -----------------------------------------------------------------

# a = cnn(['phim_viet',  'Emotion', 'SAVEE'], '2d', ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel'])
# a.continue_studying = True
# a.run(10)
# save_obj(a)

# =================================================================

# b = lstm(['TESS',  'Emotion', 'RAVDESS', 'SAVEE'], 'frequency', ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel'], True)
# b.run(50)
# save_obj(b)

# -----------------------------------------------------------------

# b = lstm(['phim_viet',  'Emotion', 'SAVEE'], 'time', ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel'], False)
# b.continue_studying = True
# b.run(10)
# save_obj(b)

# =================================================================

# a = load_obj('storage/CNN/cnn 512 emo sav 10.nht')
# del a.X_train, a.Y_train
# del a.X_test, a.Y_test
# save_obj(a)

# b = load_obj('storage/LSTM/2 lstm.nht')
# b.resume_training(50)
# b.results()
# save_obj(b)

# =================================================================

c = Realtime(path_cnn='storage/CNN/cnn.nht', path_lstm='storage/LSTM/lstm.nht')
c.start()

# c = Realtime()
# c.start()



