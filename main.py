import os
from lib.ham_ho_tro import save_obj, load_obj
from models import lstm, cnn
from app import Realtime


cwd = os.getcwd()

if 'speech emotion recognition' not in cwd:
    raise Exception('open sai thư mục. vui lòng open thư mục speech emotion recognition')



# =================================================================

# audio_features = ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel']
# a = cnn('TESS', '2d', audio_features)
# a.run(50)
# save_obj(a)

# -----------------------------------------------------------------

# audio_features = ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel']
# a = cnn(['vi/1','vi/2', 'vi/3', 'vi/4', 'vi/5', 'vi/6', 'vi/7', 'vi/8'], '1d', audio_features)
# a.select_audio_preprocessing['sequentially'] =False
# a.run(70)
# save_obj(a)

# =================================================================

# b = lstm(['TESS',  'Emotion', 'RAVDESS', 'SAVEE'], 'frequency', ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel'], True)
# b.select_audio_preprocessing['sequentially'] = False
# b.run(50)
# save_obj(b)

# -----------------------------------------------------------------

# việc build model phụ thuộc vào số tính chất cần học. nên cân nhắc hàm  build_model
# b = lstm('TESS', 'time', 'mfcc', False)
# b.run(50)
# save_obj(b)

# -----------------------------------------------------------------
# dt = [ 'vi/1','vi/2', 'vi/3', 'vi/4', 'vi/5', 'vi/6', 'vi/7', 'vi/8']
# dt = ['Emotion']+5*dt
# b = lstm(dt, 'time', ['zcr', 'chroma_stft', 'mfcc', 'rms', 'mel'], False)
# b.run(50)
# save_obj(b)

# =================================================================

# c = Realtime(path_cnn='storage/CNN/2 cnn.nht', path_lstm='storage/LSTM/2 lstm.nht')
# c.start()

# c = Realtime()
# c.start()





