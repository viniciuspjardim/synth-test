"""
Author: Vinícius Jardim
Email: viniciuspjardim@gmail.com
Date: 3/2016
"""

import math
import random
import re
import wave

import matplotlib.pyplot as plt
import numpy as np
import pyaudio as pa
from scipy.io.wavfile import write

from src.musics import *


class Notes:
    """Musical notes represents sounds with definite pitches (sound
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
    """

    names = [
        # 0   1     2    3     4    5    6     7    8     9    10    11
        'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    """Notes names"""

    notes_dict = {
        'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6,
        'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}
    """Notes name dictionary. We can get the number of the note by
    passing the note name
    """

    scales = [

        {
            'name': 'Major Diatonic',
            'notes': [0, 2, 4, 5, 7, 9, 11]},

        {
            'name': 'Minor Diatonic',
            'notes': [0, 2, 3, 5, 7, 8, 10]},

        {
            'name': 'Major Pentatonic',
            'notes': [0, 2, 4, 7, 9]},

        {
            'name': 'Minor Pentatonic',
            'notes': [0, 3, 5, 7, 10]},

        {
            'name': 'Major Hexatonic',
            'notes': [0, 2, 3, 4, 7, 9],
            'blue_note': 3},

        {
            'name': 'Minor Hexatonic',
            'notes': [0, 3, 5, 6, 7, 10],
            'blue_note': 6}
    ]
    """A list of scales with C as the tonic note.
    Each scale is a dictionary itself, with name, notes and blue note
    when applicable.
    """

    note_rgx = re.compile(r"^([CDEFGAB]{1}[#]?)([0-9]*)$")
    """Matches a string note like C, G#, B4, D#3
    More about regex can be found on
    https://docs.python.org/3/library/re.html
    """

    @staticmethod
    def get_note_name(note_num, octave_num=True):
        octave = str(note_num // 12)
        note_name = Notes.names[note_num % 12]
        if octave_num:
            return note_name + octave
        else:
            return note_name

    @staticmethod
    def get_note_num(note_name):

        if isinstance(note_name, int):
            return note_name

        match = Notes.note_rgx.match(note_name)

        if not match:
            raise ValueError("note_name arg is not a valid note name")

        note = match.group(1)
        octave_str = match.group(2)

        if not octave_str:
            octave_str = "0"

        octave = int(octave_str)

        return Notes.notes_dict[note] + (octave * 12)

    @staticmethod
    def print_notes(notes, octave_num=True, scale_tonic=0):

        tonic = Notes.get_note_num(scale_tonic)

        for i, item in enumerate(notes):
            print("%s" % Notes.get_note_name(
                            item + tonic, octave_num), end="")

            if i < len(notes)-1:
                print(", ", end="")

    @staticmethod
    def print_scale(scale, scale_tonic):

        print("%s in %s: " % (scale['name'], scale_tonic), end="")

        Notes.print_notes(scale['notes'], False, scale_tonic)

        tonic = Notes.get_note_num(scale_tonic)

        if 'blue_note' in scale:
            print(". Blue note: %s" % Notes.get_note_name(
                        scale['blue_note'] + tonic, False))

    @staticmethod
    def print_guitar(tune=None, scale=None, scale_tonic=None,
                     octave_num=False, fret_num=12):

        fret_num += 1

        if tune is None:
            tune = [28, 33, 38, 43, 47, 52]

        if scale is not None:
            Notes.print_scale(scale, scale_tonic)
            print()

        for y in range(0, fret_num):
            print("%4d  " % y, end="")
        print()

        for x in range(len(tune)-1, -1, -1):
            for y in range(0, fret_num):
                note = tune[x] + y
                fret_divisor = "|"

                if y == 0:
                    fret_divisor = "||"

                if scale is None:
                    print(" %3s " %
                        Notes.get_note_name(note, octave_num), end="")
                    print(fret_divisor, end="")
                else:
                    tonic = Notes.get_note_num(scale_tonic)
                    has_note = False

                    for scale_note in scale['notes']:
                        if note % 12 == (scale_note + tonic) % 12:
                            has_note = True
                            break

                    if has_note:
                        print(" %3s " % Notes.get_note_name(
                            note, octave_num), end="")
                        print(fret_divisor, end="")
                    else:
                        print(" --- ", end="")
                        print(fret_divisor, end="")

            print()

    @staticmethod
    def print_guitar_scales():

        print("All notes in guitar neck")
        Notes.print_guitar(fret_num=22, octave_num=True)
        print()

        for tonic in Notes.names:
            for scale in Notes.scales:
                Notes.print_guitar(
                        scale=scale, scale_tonic=tonic,
                        fret_num=22, octave_num=True)
                print()

    @staticmethod
    def volume(time, max_time, shape):

        if time > max_time:
            return 0

        # Max volume all time - causes glitches in sound
        if shape == 0:
            r = 1

        # -(x-1)^2 + 1 from 0 to 2
        elif shape == 1:
            x = time / max_time * 2
            r = -(x-1) ** 2 + 1

        # interpolate{{0, 0}, {1, 0.98}, {2, 0.5}, {3, 0.3}, {4, 0}}
        # -0.0883333 x^4+0.82 x^3-2.57167 x^2+2.82 x
        elif shape == 2:
            x = time / max_time * 4
            r = - 0.0883333 * x ** 4 + 0.82 * x ** 3 - 2.57167 *\
                x ** 2 + 2.82 * x

        elif shape == 3:
            x = time / max_time

            # interpolate{{0, 0}, {0.1, 1}}
            if x <= 0.1:
                r = 10 * x
            elif 0.1 < x <= 0.9:
                r = 1
            # interpolate{{0.9, 1}, {1, 0}}
            else:
                r = 10 - 10 * x

        return r

    def __init__(self, a4_tune=440, sound_speed=345):
        self.a4Tune = a4_tune
        self.sound_speed = sound_speed

    def frequency(self, note_num):
        """Returns the note frequency of the note represented by note
        num. The math formula is T * 2 ^((N -15/12)), where T is the A4
        default tune (usually 440 Hz) and N is the number of the note
        (starting from C0 = 0).
        """

        if note_num is None:
            return 0

        return self.a4Tune * 2 ** ((note_num - 57) / 12)

    def wavelength(self, note_num):
        return self.sound_speed / self.frequency(note_num)

    def print_notes_table(self, start=0, end=120):
        cont = 0

        print('| Note | Name | Frequency      | Wavelength')

        for x in range(start, end):
            print("| %4d | %4s | %14.8f | %11.8f " % (
                cont, Notes.get_note_name(x), self.frequency(x),
                self.wavelength(x)))
            cont += 1


class WavFile:

    # length of data to read.
    chunk = 1024

    def __init__(self, duration):

        self.duration = duration
        self.samplesPerSecond = 44100
        self.samples = self.duration * self.samplesPerSecond
        self.data = np.ones(self.samples)
        self.scaled = None
        self.it = np.nditer(self.data, flags=['f_index'],
                            op_flags=['readwrite'])

    def scale(self):

        max_val = np.max(np.abs(self.data))

        if max_val == 0:
            max_val = 1

        self.scaled = np.int16(self.data/max_val * 32767)

    def write(self, file_name):
        write(file_name, self.samplesPerSecond, self.scaled)

    def play(self, file_name):

        # open the file for reading.
        wf = wave.open(file_name, 'rb')

        # create an audio object
        p = pa.PyAudio()

        # open stream based on the wave object which has been input.
        stream = p.open(format=p.get_format_from_width(
                            wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        # read data (based on the chunk size)
        data = wf.readframes(self.chunk)

        # play stream (looping from beginning of file to the end)
        while len(data) > 0:
            # writing to the stream is what *actually* plays the sound.
            stream.write(data)
            data = wf.readframes(self.chunk)

        # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()


class Music:

    def __init__(self, notes, music, def_time=4, bpm=120, tone_shift=0):

        self.notes = notes
        self.music = music
        self.fileName = None

        self.bpm = bpm
        self.defTime = def_time
        self.toneShift = tone_shift
        self.randomShifts = [tone_shift]

        self.duration = 0
        self.duration_calc()
        self.wav = WavFile(self.duration)

    def duration_calc(self):
        # Beat time in seconds
        b_time = 60 / self.bpm

        for note in self.music:
            if isinstance(note, list):
                max_tone_time = b_time * self.defTime / note[1]
            else:
                max_tone_time = b_time

            self.duration += max_tone_time

    def parse(self):

        tone_start = 0
        # tone index in the music array
        i = 0

        # Beat time in seconds
        b_time = 60 / self.bpm

        for x in self.wav.it:

            music_time = self.wav.it.index / self.wav.samplesPerSecond
            tone_time = music_time - tone_start

            if isinstance(self.music[i], list):
                tone = Notes.get_note_num(self.music[i][0]) +\
                       self.toneShift if self.music[i][0]\
                       is not None else None

                max_tone_time = b_time * self.defTime / self.music[i][1]

            else:
                tone = Notes.get_note_num(self.music[i]) +\
                       self.toneShift if self.music[i]\
                       is not None else None

                max_tone_time = b_time

            volume = Notes.volume(tone_time, max_tone_time, 3)

            par = self.wav.it.index * 2 * math.pi /\
                  self.wav.samplesPerSecond

            x[...] = math.sin(par * self.notes.frequency(tone)) * volume

            # x[...] = signal.square(par * self.notes.frequency(tone))\
            #          * volume

            # x[...] = signal.sawtooth(
            #          par * self.notes.frequency(tone), 0) * volume

            # If the tone time has ended go to the next tone
            if tone_time >= max_tone_time and i < len(self.music) - 1:
                i += 1  # increment tone index
                tone_start = music_time
                self.toneShift = random.choice(self.randomShifts)

    def save(self, file_name):
        self.fileName = file_name
        self.wav.scale()
        self.wav.write(self.fileName)

    def play(self):
        self.wav.play(self.fileName)

    @staticmethod
    def random():

        scale = Notes.scales[0]['notes']
        scale.append(None)
        times = [4/1.5, 4, 8, 4, 8, 4]
        octaves = [4]

        music = []

        for i in range(60):
            note = random.choice(scale)
            note = note + (12 * random.choice(octaves))\
                   if note is not None else None

            time = random.choice(times)
            music.append([note, time])

        return music


def main():

    notes = Notes()

    # This notes come from the file musics.py that contain notes samples
    music_notes = smoke_on_the_water

    music = Music(notes, music_notes, bpm=112, tone_shift=44)
    music.parse()
    music.save('generated\music1.wav')

    print('Playing...')
    music.play()
    print('End Playing')

    plt.plot(music.wav.data)
    plt.ylabel('Air Pressure')
    plt.xlabel('Time')
    plt.show()


if __name__ == "__main__":
    main()
