from tkinter import filedialog
import sounddevice as sd
from scipy.io.wavfile import write


def record(duration, fs):  
    print("Start recording...")
    # ضبط صدا
    my_record = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='int16')
    sd.wait()
    
    print("Recording finished!")
    return my_record

def main():
    duration = 20  
    fs = 44100     
    
    
    my_record = record(duration, fs)  # Fixed: Added call to record function
    
    output_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    write(output_file, fs, my_record)
    print(f"Your file has been saved successfully as {output_file}")
    

main()



