# Audio Recorder with Python 🎤🎶

This project is a simple yet powerful **Audio Recorder** developed using **Python**, **sounddevice**, and **Tkinter**. It allows users to record high-quality audio and save it as a WAV file effortlessly. 

## Features 🚀

- 🎙 **Record Audio**: Capture high-quality sound from your microphone.
- 💾 **Save Recordings**: Choose a location and save your recording as a WAV file.
- ⚙️ **Customizable Duration**: Set the recording duration as needed.
- 🖥 **User-Friendly Interface**: Uses Tkinter's file dialog for a smooth experience.
- 🔊 **High-Quality Audio**: 44.1 kHz sample rate with stereo channels.

## Technologies and Libraries 🛠️

- **Python 3.x**: The core programming language.
- **sounddevice**: For recording audio.
- **scipy.io.wavfile**: For saving the recorded audio as a WAV file.
- **Tkinter**: For handling file dialogs.

## Installation and Setup 📥

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- pip package manager for Python

### Install Required Libraries

Run the following commands in your terminal or command prompt:

```bash
pip install sounddevice 
```

```bash
pip install scipy
```

```bash
pip install Tkinter
```

## Documentation 📖

### sounddevice:

- Official Documentation: [Python SoundDevice Docs](https://python-sounddevice.readthedocs.io/)

### SciPy (wavfile):

- Official Documentation: [SciPy Wavfile Docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html)

### Tkinter:

- Official Python Docs: [Tkinter (GUI Programming)](https://docs.python.org/3/library/tkinter.html)

## Code Overview 📝

### `record(duration, fs)`
- Records audio for the given duration and sample rate.
- Returns the recorded data.

### `main()`
- Calls `record()` to capture audio.
- Opens a save file dialog.
- Saves the recording in WAV format.

## Running the Application ▶️

To run the application, execute the Python file:

```bash
python recorder.py
```

### How to Use 🎬

1. **Run the script**: Start the Python file.
2. **Recording starts**: It will record for the set duration (default: 20 seconds).
3. **Save the file**: A file dialog will appear for saving the WAV file.
4. **Enjoy your recording!** 🎧

## Important Notes ⚠️

- Ensure that your microphone is working properly.
- Adjust the duration and sample rate as needed.
- If you encounter issues, check your Python environment and installed libraries.

## SEO Keywords 🔍

**Python**, **Audio Recorder**, **Sounddevice**, **WAV File**, **Microphone Recording**, **Python Project**, **GUI Development**, **Tkinter**, **Python Tutorial**, **HiTech**, **Audio Processing**

## Conclusion 🏁

This project is a great way to explore **Python audio processing** and **desktop application development**. Whether you're a beginner or an experienced developer, it's a valuable project for learning and building practical applications. 

🚀 **If you found this project helpful, give it a ⭐ on GitHub and subscribe to my YouTube channel for more tutorials!**  

🔗 **Subscribe Here:**  
👉 [Click Here](https://www.youtube.com/channel/UCBc3aSf54eyrl46RUWqIOIg?sub_confirmation=1)

