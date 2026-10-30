# FreeDV for Mere Mortals

On a weak HF path — a voice signal fading
in and out across an ocean — ordinary
single sideband gives you fragments: a
word here, a syllable there, then noise.
**FreeDV** is digital voice for amateur
radio, built for exactly that path. It
takes your voice, squeezes it down to a
few hundred **bits per second** with an
open-source speech codec called
**Codec2**, and sends it as a modem
signal about as wide as a Morse signal
is tall next to a phone call. At the far
end, the same free software turns the
bits back into a voice. When the path is
too poor for sideband to survive, the
digital copy often still gets through —
not hi-fi, but *whole*.

This guide explains how FreeDV turns a
voice into data and back, what the modes
are and how they differ, and how to build
and decode a real FreeDV signal yourself
— with no radio, no licence, and nothing
transmitted. Then it covers connecting
an actual radio and getting on the air,
labelled honestly as the part the lab
could describe but not do.

The lab that wrote this guide had no
radio and no antenna. What it had was
the real thing underneath FreeDV: the
official **Codec2 1.2.0** tools, built
from source. Against them it spoke a
stock sentence with a speech synthesiser,
turned that speech into a genuine FreeDV
**700D** transmission file, decoded it
back, and measured everything: durations,
levels, frame counts, bit rates, and how
closely the decoded voice's loud-and-
quiet pattern tracks the original. It
then buried the signal in measured noise
— at a signal-to-noise ratio of 2 dB,
where a voice recording is mostly hiss —
and decoded all 42 frames anyway. Every
one of those runs is a transcript in
`freedv-lab/`.

What the lab could not do, it did not
fake. It never transmitted, never
connected a radio, and never *listened*
to the decoded audio — it has no ears.
Claims about how FreeDV *sounds* are the
project's and its users', and are
labelled as such. The parts of the hobby
that happen at a radio — sound-card
levels, PTT control, finding a QSO — are
taught from the FreeDV documentation and
marked documented-only wherever they
appear. `criteria.md` keeps the full
ledger of what was run and what was only
read.

One rule belongs up front, because it is
the reason FreeDV exists in the form it
does: **the codec is open**. Anyone with
the free software can decode anyone's
FreeDV transmission. That is deliberate.
Amateur radio in most countries forbids
transmissions that hide their meaning,
and FreeDV is built to comply by design —
it is a published codec, not a cipher.
You still identify your station the
usual way, under your own licence's
rules; chapter 9 covers the on-air
manners.

## What this guide covers

- [**What FreeDV is**](what-freedv-is.md) —
  the mental model: voice in, bits over
  the air, voice out — and why the codec
  being open is a feature, not a gap
- [**The moving parts**](the-moving-parts.md) —
  the FreeDV program, Codec2 the speech
  codec, the modem that carries the bits,
  and the radio treated as a sound card
- [**The modes**](the-modes.md) — 1600,
  700C, 700D and their neighbours: what
  each costs in bit rate and buys in
  survival on a bad path
- [**Installing FreeDV and the codec tools**](installing.md) —
  the program for your desktop, and the
  command-line tools this guide's lab
  actually ran, with the checks that
  prove they work
- [**Your first signal, no radio required**](your-first-signal.md) —
  speak a sentence, encode a real 700D
  signal, decode it back, and read the
  receipts at each step
- [**Proving the signal**](proving-the-signal.md) —
  how to know the file really carries a
  voice: headers and the raw-file trap,
  durations, levels, and the loud-and-
  quiet pattern test
- [**Holding up in noise**](noise-and-weak-signals.md) —
  the measured noise runs: what 2 dB of
  signal-to-noise does to a recording,
  and what it does to 700D
- [**Connecting the radio**](connecting-the-radio.md) —
  sound-card interfaces, levels, and
  PTT control, taught from the
  documentation (documented-only)
- [**On the air**](on-the-air.md) —
  where FreeDV lives on the bands, how a
  contact goes, spotting yourself on
  FreeDV Reporter, and the rules of the
  road (documented-only)
- [**Recipes**](recipes.md) — a test
  file in every mode, a noise ladder of
  your own, the codec without the modem,
  and a two-computer loopback to rehearse
  with
- [**The neighbours**](the-neighbours.md) —
  plain SSB, the VHF digital voice modes
  with their closed codec, FT8 and the
  sound-card data modes: what each does
  that FreeDV doesn't, and vice versa
- [**Limits**](limits.md) — the robotic
  voice, the delay, the computer and
  radio it still needs, and the parts of
  this guide that rest on documentation
- [**Troubleshooting**](troubleshooting.md) —
  the WAV that is really raw samples, the
  wrong sample rate, the receiver that
  decodes too few frames, and the traps
  this guide's lab fell into
- [**Glossary**](glossary.md) — the
  terms, collected in one place

## What it doesn't cover

Building or aligning radio hardware,
antenna work, and amplifier practice —
this guide treats the radio as a sound
device and stops there. The other
digital-voice worlds (DMR, D-Star,
Fusion) get a chapter-11 comparison, not
a course; they live on VHF and UHF
repeaters and use a different, closed
codec. Writing your own codec or modem
is out — Codec2's source is the place to
read, and this guide's lab builds it
unmodified. And nothing here transmits:
if you follow only the chapters the lab
verified, no RF leaves the room.

## How to use this guide

Read chapter 1 for the model and
chapter 2 before installing anything —
knowing which part holds what turns
later confusion into a named problem.
Chapters 4 and 5 build a real signal in
one sitting, with checks at every step;
chapters 6 and 7 are the ones to read
slowly, because their measurements are
how you learn to trust (or catch) a
digital-voice setup before it matters.
Chapters 8 and 9 take you to a real
radio and are marked documented-only:
follow them with your radio's manual
open. The lab's transcripts live in
`freedv-lab/transcripts/`; its measuring
scripts are `freedv-lab/measure.py`,
`freedv-lab/resample8k.py` and
`freedv-lab/envelope.py`.

---

## Part of the series

This guide is one of the [For Mere Mortals](https://paulsullivan33-dev.github.io/mere-mortals/) guides: plain-language guides to the tools programmers and makers use.

Related guides:

- [Ham Radio for Mere Mortals](https://paulsullivan33-dev.github.io/ham-radio-for-mere-mortals/)
- [WSJT-X for Mere Mortals](https://paulsullivan33-dev.github.io/wsjtx-for-mere-mortals/)
- [Fldigi for Mere Mortals](https://paulsullivan33-dev.github.io/fldigi-for-mere-mortals/)
- [Hamlib for Mere Mortals](https://paulsullivan33-dev.github.io/hamlib-for-mere-mortals/)

## License

The writing in this guide is licensed under [CC BY 4.0](https://github.com/paulsullivan33-dev/freedv-for-mere-mortals/blob/main/LICENSE). Code examples and lab scripts are licensed under the [MIT License](https://github.com/paulsullivan33-dev/freedv-for-mere-mortals/blob/main/LICENSE-CODE).
