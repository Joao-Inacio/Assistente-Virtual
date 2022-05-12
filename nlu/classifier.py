from tensorflow.python.keras.models import load_model
import numpy as np

model = load_model('model.h5')

labels = open('labels.txt', 'r', encoding='utf8').read().split('\n')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label


def classify(text):
    x = np.zeros((1, 48, 256), dtype='float32')

    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()
    return idx2label[idx]


"""while True:
    text = input('Digite algo: ')
    print(classify(text))"""
