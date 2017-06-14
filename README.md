## Synth Test

This project provides classes for producing music notes and monophonic
music. It is for learning and educational purpose.

The music output can be stored in a WAV file and can be played by this
software and other music players. It can also plot the waveform on the
GUI, generate scales and notes frequencies tables.

### Music info

Musical notes represents sounds with definite pitches (sound
frequency). Definite pitches come from instruments like piano,
guitar, vocals, etc. Notes often come from the chromatic scale,
with 12 pitches, each a semitone above or below another. The notes
are:

`C, C#, D, D#, E, F, F#, G, G#, A, A#, B`

In this class each of this notes are represented by a number from 0
(C note) to 11 (B note). This 12 notes represents an octave. Each
octave ends in a B note, then a new octave starts (C note).

For example: as we said, the the note number 11 is a B so the number
12 will be another C. This C will be one octave higher the other C.
So we can call the first C, C0, the second C will be C1 and so on.
The letter is the note name and the number is the octave.

Each note in this class can be represented as a number or by the
note name followed by the octave number. Example:

| Note | Name | Frequency (Hz) | Wavelength (m)|
|:----:|:----:|---------------:|--------------:|
|    0 |   C0 |      16.351597 |     21.098855 |
|    1 |  C#0 |      17.323914 |     19.914667 |
|    2 |   D0 |      18.354047 |     18.796943 |
|...   |      |                |               |
|   12 |   C1 |      32.703195 |     10.549427 |
|   13 |  C#1 |      34.647828 |      9.957333 |
|...   |      |                |               |

We can see that the C1 is twice C0 frequency. Although C1 is more
acute, it produces a harmonic sound to C0. C2 will be twice the
frequency of C1, and it keeps doubling. The human ear can listen to
frequencies from 20 to 20000 Hz.

### Installing and running

Anaconda distribution has all packages needed except pyaudio. I used
Anaconda3 (which comes with python 3 interpreter).

Anaconda download: https://www.continuum.io/downloads

To install pyaudio on Windows:
```
python -m pip install pyaudio
```

On Linux:
```
pip install pyaudio
```

More pyaudio installation instructions at:
http://people.csail.mit.edu/hubert/pyaudio/

### License
Synth Test is licensed under the
[Apache 2 License](http://www.apache.org/licenses/LICENSE-2.0.html),
meaning you can use it free of charge, without strings attached in
commercial and non-commercial projects. I would like to get
(non-mandatory) credit in case you use this code in your project.