# Troubleshooting

Sorted by part — program, codec, modem,
radio — because a fault fixed in the
wrong part stays fixed nowhere. The
first three entries are traps this
guide's lab fell into itself, in its
own transcripts.

## The file that will not play (modem/tools)

**Symptom:** a file named `.wav` from
`freedv_tx` or `freedv_rx` opens as
noise, static, or nothing in players
and editors.
**Cause:** the tools write **raw
samples** whatever the file is called.
There is no header; players guess wrong.
**Check:** `file the-file` says "data",
not "WAVE audio" (chapter 6, check 1).
**Fix:** work in `.raw` names end to
end, and wrap a copy in a real header
(8,000 Hz, mono, 16-bit) only when a
player or measuring tool needs one —
exactly as transcript t02 does.

## The speech that encodes to mush (codec)

**Symptom:** plenty of frames decode,
but the envelope check of chapter 6
scores near zero at *every* shift.
**Cause:** the input was not 8,000 Hz
mono speech. The tools do not resample:
a 22,050 Hz file fed as raw samples is
a voice slowed and pitched down past
recognition, and it will still "work"
in every superficial way.
**Check:** measure the source (chapter
5, step 1). 8,000 Hz, 1 channel, and a
duration that matches the sentence.
**Fix:** resample first; the lab's
`freedv-lab/resample8k.py` is one honest
way, any audio editor is another.

## The missing frames (modem)

**Symptom:** *frames decoded* comes
back well short of what was sent, on a
clean file path.
**Causes, in the order the lab would
check them:** the input file is shorter
than a whole number of frames and the
comparison forgets the dropped tail
(700D keeps 160 ms frames — chapter 5's
6.84 s in, 6.72 s out is *correct*);
the wrong mode on the receive side
(the modes share no sync with each
other); the signal was clipped on
transmit until its shape lied (chapter
7's mixtures were deliberately *not*
clipped — check your peak measurement);
or the level is so low the receiver's
sync never engages, which on a file
shows up as a decode that starts late.
**Check:** run recipe 1 (a test file in
every mode) to separate tool faults
from file faults.

## The receiver that hears nothing (program/radio — documented-only)

**Symptom:** the waterfall is dead or
the program decodes nothing on air.
**First checks:** the two sound devices
(chapter 8) are the radio's, not the
laptop's own microphone and speakers;
the radio is in the mode and sideband
chapter 9 describes, with any noise
reduction, notch, or speech processing
*off* — DSP that improves a voice
mangles a modem; and the receive level
leaves the waterfall alive but not
saturated. Most "FreeDV doesn't work"
reports are one of these three.

## The transmitter everyone complains about (radio — documented-only)

**Symptom:** contacts decode you
poorly, or neighbours report width.
**Cause:** level. ALC driven hard
distorts the warble; the cure is less
audio drive, not more power (chapter
8). A monitor receiver and a dummy load
find this in a minute, before the band
does.

## The mode that will not build (codec)

**Symptom:** a source build lacks the
2020 modes, or the GUI lacks a mode
the web page describes.
**Cause:** 2020 needs the separate
LPCNet component; this guide's build
set `LPCNET=OFF` on purpose
(transcript t00), so its tools are the
chapter-3 table and no more. Version
skew explains the rest — check the
program's version against the
documentation's, and prefer the
project's current release.
