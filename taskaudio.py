import librosa
import jupyter
import numpy
import time
import os
import warnings
warnings.filterwarnings('ignore')
#cd C:\Users\klise\Downloads\vox2_test_aac (1)\test

t=time.time()
fn=os.getcwd()
res=fn+'res'
os.mkdir(res)
for f1 in os.listdir(fn):
    os.mkdir(res+"\\"+f1)
    for f2 in os.listdir(fn+"\\"+f1):
        os.mkdir(res+"\\"+f1+"\\"+f2)
        for el in os.listdir(fn+"\\"+f1+"\\"+f2):
            y,sr=librosa.core.load(fn+"\\"+f1+"\\"+f2+"\\"+el)
            mfcc=numpy.empty(0)
            mfcc=librosa.feature.mfcc(y,sr)
            numpy.save(res+"\\"+f1+"\\"+f2+"\\"+el[:-4],mfcc)
                
        
print(time.time()-t)





