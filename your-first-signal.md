# Your First Signal, No Radio Required

By the end of this chapter you have made
a genuine FreeDV 700D signal — the same
waveform a station would put on the air —
and decoded it back into speech, with a
check at every step. Nothing is
transmitted. The "path" between your
transmitter and receiver is a file on
your disk, which makes it the most
reliable HF path you will ever use, and
the right place to learn what the
receipts look like before noise enters
the story in chapter 7.

The lab's run of this chapter is
transcripts t01 and t02, and every
number below is from them.

## Step 1: get speech, at 8,000 Hz

FreeDV works on speech sampled **8,000
times a second**, mono, 16-bit — the
telephone standard. Any recording of a
voice can be converted to that; the lab
had no microphone, so it used a witness
that never complains: a speech
synthesiser, **espeak-ng**, reading a
stock sentence with a placeholder call
sign:

```bash
espeak-ng -w speech-native.wav \
  "CQ CQ, this is November Zero Call. \
   Free DV turns a voice into data, \
   and data back into a voice."
```

espeak-ng writes at 22,050 Hz, so the
lab resampled with a short Python script
(`freedv-lab/resample8k.py`) to
`speech-8k.wav`. The check, from
`freedv-lab/measure.py`:

```text
speech-8k.wav: 8000 Hz, 1 ch, 16-bit, 54698 samples, 6.84 s, RMS -20.9 dBFS, peak -0.0 dBFS, nonzero 79%
```

Read it like a receipt: 54,698 samples
at 8,000 a second is 6.84 seconds; the
loudness (RMS −20.9 dBFS) is a plausible
speech level; 79% nonzero means the file
is not accidentally silence. If you
record your own voice instead, this line
is how you know the take is good before
anything else touches it.

## Step 2: take the samples out, raw

Here is the trap the lab fell into, so
you don't have to: **the codec tools do
not read or write WAV files.** They read
and write **raw samples** — the numbers
themselves, no header. The tool's own
usage line says so (`InputRawSpeechFile
OutputModemRawFile`), but a file named
`.wav` will still be written, raw
samples and all, if you ask for one —
the lab's first modem file was a WAV in
name only, and `file` called it plain
"data". The fix is to be explicit:

```bash
# WAV body out as headerless raw (see t02 for the one-liner)
# 54,698 samples x 2 bytes = 109,396 bytes
ls -l speech-8k.raw
```

Check: the raw file is exactly twice the
sample count in bytes. 109,396 ✓.

## Step 3: transmit — into a file

```bash
freedv_tx 700D speech-8k.raw tx-700d.raw
```

Silence is normal; the check is the
output's size. The lab's was 107,520
bytes = 53,760 samples = **6.72
seconds** of modem signal at 8,000
samples a second. Slightly shorter than
the 6.84 seconds that went in: 700D
works in frames of 160 milliseconds
(1,280 samples), 42 of them fit, and the
part-frame at the end is dropped. A
modem signal also measures differently
from speech — wrapped in a header so
the measuring script could read it, it
showed RMS −16.3 dBFS and **100%
nonzero**: a modem waveform never sits
at zero, even between words.

## Step 4: receive, and read the receipt

```bash
freedv_rx 700D tx-700d.raw rx-700d.raw
```

```text
frames decoded: 42  output speech samples: 53760
```

That line is the receiver's whole
report, and it is a good one: 42 frames
sent (in the file), 42 decoded, and
53,760 samples of speech handed back —
the same count the transmitter made.
Wrapped and measured:

```text
decoded-700d.wav: 8000 Hz, 1 ch, 16-bit, 53760 samples, 6.72 s, RMS -22.5 dBFS, peak -1.0 dBFS, nonzero 100%
```

6.72 seconds, a speech-like level, no
long stretches of zeros. You have a
decoded voice. Whether it is *the same*
voice — the pattern of the same words,
in the same places — is a harder claim,
and it deserves better than a shrug.
That is chapter 6.
