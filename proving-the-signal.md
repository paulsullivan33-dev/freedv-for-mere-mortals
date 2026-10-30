# Proving the Signal

A decoder that fails can still write a
file. This chapter is the habit of not
taking the file's word for it: four
checks, each runnable, that together
make "it worked" a measured statement.
You finish able to prove a decode the
way this guide's lab proved its own —
transcript t05 is the worked example,
and it includes the check that *failed*
first, which is the most instructive
part.

## Check 1: the format is what you think

Digital-audio work is full of files
lying about what they are. This guide's
own lab produced the exhibit: a modem
file named `.wav` that was raw samples,
because `freedv_tx` writes raw whatever
you call the output. The check costs one
command:

```bash
file tx-700d.raw speech-8k.wav
```

```text
tx-700d.raw:   data
speech-8k.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, mono 8000 Hz
```

If a tool downstream behaves as if your
file is noise or silence, ask `file`
before you ask anyone else.

## Check 2: the durations add up

Speech went in at 6.84 s; the 700D
signal and its decode are 6.72 s — 42
whole frames of 160 ms, the tail
part-frame discarded by design. The
codec-only run (transcript t04) is
similarly accountable: 680 bytes of
700C bits is 171 frames × 4 bytes, and
171 × 40 ms is 6.84 s — the *whole*
sentence, because the bare codec keeps
shorter frames than the modem does.
When your durations reconcile like this,
the pipeline has no silent gaps in it:
nothing was dropped except what the
frame arithmetic predicts.

## Check 3: the levels are speech-like

A decoded file that is digital silence,
or a constant tone, still has a
duration. Its levels betray it. The
lab's measurements (chapter 5): original
speech RMS −20.9 dBFS, decoded −22.5
dBFS, peaks near full scale in both.
Real decoded speech lands within a few
dB of where ordinary speech sits; a
decode at −60 dB, or one pinned at
0 dB peak on every sample, is broken
however clean its frame count looks.

## Check 4: the pattern matches — after you align it

The strongest check asks whether the
decoded audio is loud and quiet *in the
same places* as the original — the shape
of the same words. The lab's script
(`freedv-lab/envelope.py`) compares the
loudness, averaged over 100 ms slices,
between the original and the decode, as
a correlation: 1.0 is a perfect match.

Run naively, the 700D decode scored
**−0.21** — worse than unrelated. The
decode was not wrong; the *check* was.
The file tools hold the decoded audio
back by a constant delay (about 350 ms
for 700D), so every loud moment was
being compared against the original's
quiet *next* moment. The script
therefore tries shifts up to two seconds
each way and reports the best:

```text
700D decoded:  best correlation 0.86 (shift -350 ms)
1600 decoded:  best correlation 0.89 (shift +200 ms)
700C codec only: best correlation 0.78 (shift -50 ms)
```

0.86 is what a heavily squeezed voice
should score: the words' rhythm and
weight survive; the fine detail, by
design, does not. Two lessons generalise.
Any store-and-forward comparison — file
tools, recordings of a live contact —
must align before it concludes. And a
negative result from a good check is
information, not embarrassment: it found
the delay, which chapter 12 lists among
FreeDV's real costs.
