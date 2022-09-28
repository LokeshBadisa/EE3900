import soundfile as sf
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

#read .wav file 
input_signal,fs = sf.read('codes/Sound_Noise.wav') 

#sampling frequency of Input signal
sampl_freq=fs

#order of the filter
order=4   

#cutoff frquency 4kHz
cutoff_freq=4000.0  

#digital frequency
Wn=2*cutoff_freq/sampl_freq  

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order,Wn, 'low') 

#filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a, input_signal)

file=open('codes/input_signal.dat','w')

#Generating Samples 
for i in range(0,len(output_signal)):
         file.write(str(output_signal[i])+'\n')

file.close()

file=open('codes/signal_length.dat','w')
file.write(str(len(output_signal)))
file.close()

#plt.plot(np.arange(len(input_signal)),output_signal)
#plt.savefig('figs/input_signal.eps')
#plt.show()

#plt.plot(np.arange(len(input_signal)),input_signal)
#plt.savefig('figs/output_signal.eps')
#plt.show()


#write the output signal into .wav file
sf.write('Sound_With_ReducedNoise.wav', output_signal, fs) 

