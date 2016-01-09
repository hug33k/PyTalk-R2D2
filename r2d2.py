#!/usr/local/bin/python3.5

import wave
import time
import pyaudio
import sys

if __name__ == '__main__':
	if len(sys.argv) == 2:
		word = sys.argv[-1].lower()
	elif len(sys.argv) == 1:
		word = ["a","b","c","c1","d","e","f","g","g1","h","i","j","k","l","m","n","o","o1","p","q","r","s","s1","t","u","u1","v","w","x","y","z"]
	else:
		print("Usage : ./r2d2.py (string)")
		sys.exit(-1)
	root = "sounds/{0}.wav"
	p = pyaudio.PyAudio()
	stream = p.open(format = p.get_format_from_width(2),
		channels = 1,
		rate = 22050,
		output = True)
	data = b""
	chunk = 1024
	for letter in word:
		if not letter.isalpha():
			continue
		try:
			with wave.open(root.format(letter), "rb") as f:
				data += f.readframes(f.getnframes())
		except Exception as e:
			print(e)
	stream.write(data)
	wf = wave.open("out.wav", 'wb')
	wf.setnchannels(1)
	wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
	wf.setframerate(22050)
	wf.writeframes(data)
	wf.close()
	p.terminate()
