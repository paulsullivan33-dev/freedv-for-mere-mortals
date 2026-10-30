# The Moving Parts

By the end of this chapter you can name
the four parts of a FreeDV station and
say which one a given problem lives in —
the skill that turns "it doesn't work"
into a checkable question. The check to
hold in mind: in chapter 5 you will run
two of the four parts alone, as programs,
and hear (well, measure) them work with
no radio involved at all.

## 1. The FreeDV program

The program you install and look at is
**FreeDV** (often called the FreeDV GUI).
It is the conductor. It takes audio from
a microphone, hands it to the codec,
takes the modem signal to the radio,
and does the same in reverse for
received audio, showing you a waterfall,
a signal-to-noise estimate, and a text
box where stations can send their call
sign and a short message alongside the
voice. It also talks to **Hamlib**, the
radio-control library in this series'
Hamlib guide, to key the transmitter and
read the frequency. Everything in this
chapter except this program can be — and
in the lab, was — run without it.

## 2. Codec2, the speech codec

Codec2 is the part that makes FreeDV
possible. It turns 8,000 speech samples
a second into a trickle of bits, and the
trickle back into speech. Its rates run
from 3,200 bits per second down to a few
hundred; FreeDV's working modes use the
range from 1,600 down to 700. Codec2
does not work like a tape recorder or
like the MP3 format: it builds a model
of the vocal tract many times a second
and transmits the model's settings,
which is why so few bits suffice — and
why the result sounds *synthesised*
rather than *recorded*, because it is.

Codec2 also exists on its own, as
command-line tools (`c2enc`, `c2dec`)
that convert speech to bits and back
with no radio anything involved. The lab
ran them: transcript t04 is the codec
alone, producing 680 bytes of bits for
a 6.84-second sentence.

## 3. The modem

Bits do not cross a radio path by
themselves; something has to turn them
into sound the transmitter can send and
survive the trip. That is the **modem**
inside FreeDV. The mode names you will
meet — 1600, 700D, 700E — are mostly
modem designs: different arrangements of
carriers, error correction, and sync
signals, each trading bandwidth and
toughness differently. (700D, for
instance, uses an **OFDM** waveform —
many small carriers side by side, each
carrying a little of the data, so losing
a slice of the band to a fade does not
lose the message.) The command-line
tools `freedv_tx` and `freedv_rx` are
this modem with a file going in and a
file coming out — a transmitter and
receiver whose "path" is a disk. Chapter
5 puts a signal through them;
`freedv_rx`'s receipt, *frames decoded*,
is the number the rest of the guide
keeps reading.

## 4. The radio, as a sound card

The fourth part is the one this guide's
lab did not have: an ordinary SSB
transceiver, connected to the computer
as an audio device — microphone socket
in, speaker socket out, plus some way to
key the transmitter (**PTT**). Modern
rigs offer this as one USB cable;
older ones use an interface box. The
radio's job is deliberately dumb: carry
a roughly one-kilohertz-wide audio
signal faithfully, at the power and
frequency the operator chose. Chapter 8
covers the connection from the FreeDV
manual, and flags it documented-only.

## Who holds what

A useful way to keep the parts straight:
the **program** holds the settings, the
**codec** holds the voice's recipe, the
**modem** holds the bits while they are
sound, and the **radio** holds the
frequency and the power. A distorted
voice with strong signals is a codec or
levels question; a clean voice that
keeps dropping out is a modem or path
question; a signal on the wrong
frequency is the program or the rig.
Chapter 13's troubleshooting is organised
on exactly this split.
