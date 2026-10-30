# Recipes

Four jobs, end to end. The first three
use only the command-line tools and were
run by this guide's lab in substance —
the transcripts are the receipts. The
fourth is the rehearsal for a real
station and is documented-only, like
chapters 8 and 9.

## 1. A test file in every mode

Goal: a pocket library of known signals,
for testing a receiver, a program
install, or a friend's setup.

Take one `speech-8k.raw` (chapter 5,
steps 1–2) and run the transmitter once
per mode from transcript t00's list:

```bash
for mode in 1600 700C 700D 700E 2400A 2400B 800XA; do
  freedv_tx $mode speech-8k.raw test-$mode.raw
  freedv_rx $mode test-$mode.raw out-$mode.raw
done
```

Check: every `freedv_rx` prints a
*frames decoded* line, and chapter 6's
measure step shows decoded durations
within a frame or two of the source.
Where a mode decodes materially fewer
samples on a *perfect* file path, you
have found a build or usage problem,
not a propagation problem — that is
what the library is for.

## 2. Your own noise ladder

Goal: find where a mode breaks, instead
of stopping where this guide stopped.

Repeat chapter 7's mixture at a ladder
of ratios — 10, 6, 2, 0, −4 dB — using
the seeded noise recipe in transcript
t06, and record *frames decoded* and
the envelope correlation at each rung.
Check: the frames hold, then fall; the
rung where they fall is your mode's
cliff edge in steady noise. Compare two
modes on the same ladder and you have
done, on a bench, the comparison
chapter 3's table only asserts.

## 3. The codec without the modem

Goal: hear the voice rates themselves,
with no radio anything — the quickest
way to learn what 700 bit/s costs a
voice.

```bash
c2enc 1600 speech-8k.raw speech-1600.bit
c2enc 700C speech-8k.raw speech-700c.bit
c2dec 1600 speech-1600.bit back-1600.raw
c2dec 700C speech-700c.bit back-700c.raw
```

Check the bit files' sizes (transcript
t04): the 700C file is well under half
the 1600 file for the same sentence.
Wrap the outputs and run chapter 6's
envelope check on each: the correlation
gap between the two *is* the rate
trade-off, measured instead of argued.

## 4. The two-computer loopback (documented-only)

Goal: rehearse a whole station — program,
levels, PTT behaviour — before any of it
touches an antenna.

Put FreeDV on two computers (or two
sound devices on one), join transmit
audio out to receive audio in with a
cable or a virtual audio device, and
hold a contact with yourself across the
desk, exactly as chapter 9 describes.
Check: sync locks, the text channel
shows the call sign you typed, the
delay is audible and expected, and
stopping talking drops the far end's
squelch. Everything after this is
chapter 8's cabling and chapter 9's
manners; everything before it, you
have already proven at a command line.
