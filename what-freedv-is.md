# What FreeDV Is

You finish this chapter able to say, in
one sentence, what happens to a voice
between two FreeDV stations — and able to
check the claim at the heart of it
yourself: that a voice can be squeezed
into about **700 bits per second** and
still come back out as a voice. Chapter 5
runs that check for real; this chapter
draws the map.

**FreeDV is digital voice for HF amateur
radio.** HF — the shortwave bands, where
signals bounce off the ionosphere and
cross oceans — is a hard place for a
voice. The signal fades, static crashes
roll through, and a path that was fine a
minute ago can fall apart mid-sentence.
Single sideband, the analogue voice mode
hams have used for generations, degrades
the way an old cassette does: gracefully,
but downhill all the way. FreeDV takes
the other bargain. It converts the voice
to data first, so what crosses the ocean
is not a picture of the sound but the
*recipe* for it — and recipes either
arrive intact or not at all.

The recipe-writer is **Codec2**, an
open-source speech **codec** (coder-
decoder) written by David Rowe and
released freely, like FreeDV itself.
Codec2 does not record your voice; it
*models* it. Twenty times a second or
more, it measures the pitch and the
shape of the sound your mouth is making,
and writes down just those numbers. At
its famous lowest rates that is about
**700 bits every second** — against
128,000 bits per second for the ordinary
uncompressed speech file this guide's
lab started with. The lab's arithmetic,
from files you will see in chapter 5: a
20-word sentence took 109,396 bytes as
raw speech samples, and **680 bytes** as
Codec2 700C bits. Same sentence. That
squeeze — roughly 180 to 1 — is the
whole trick, and everything else in
FreeDV exists to carry those bits across
a hostile radio path and rebuild a voice
from them at the far end.

Because the bits are so few, the radio
signal that carries them can be narrow
and tough. FreeDV's modern modes wrap
the bits in a **modem** signal — a
carefully designed warble about a
kilohertz wide — with error correction
woven in, so some of the signal can be
damaged and the message still decode.
Chapter 7 shows the lab's version of the
miracle: the 700D signal mixed with
noise until the mixture measured a
signal-to-noise ratio of 2 dB, and the
receiver still decoded every frame.

## The open part is the point

A commercial digital-voice radio hides
its codec. The one inside DMR and D-Star
radios (chapter 11) is patented and
licensed; you may use it, but you may
not read it, build it, or fix it. FreeDV
was written in reaction to exactly that.
Codec2 is published source code. The
specification is public. Anyone can
build a FreeDV station from the same
software, and anyone can *decode* one:
there are no keys, and there is nothing
to unlock.

That openness is also a legal shape, not
just a philosophy. Amateur licences in
most countries forbid transmissions
intended to obscure their meaning.
FreeDV complies by construction — its
meaning is published. What it does not
do is excuse you from the ordinary
duties: you identify your station under
your own licence's rules (chapter 9),
you obey your band plan, and you are
responsible for what your station sends,
same as on phone or CW.

## What it is not

FreeDV is not a repeater mode. It lives
on HF, point to point, in the same parts
of the bands where SSB voice lives, and
it uses your ordinary SSB transceiver —
the radio neither knows nor cares that
the "voice" in its microphone socket is
a computer's modem signal. It is not a
data mode in the FT8 sense: there is a
person talking, in real time, at both
ends; the computer is doing the voice's
packaging, not having the conversation.
And it is not hi-fi. A voice rebuilt from
700 bits a second sounds like what it
is — a tireless robot doing an impression
of you. Call signs, names and signal
reports come through clearly; warmth
does not. Chapter 12 is plain about the
rest of the costs.

## Who it is for

The HF operator whose paths are marginal
and who loses contacts to fading that a
digital copy would have survived. The
experimenter who likes that the whole
stack — codec, modem, program — can be
read, built and measured on a bench,
which is what chapters 5 to 7 do. The
club demonstrating that amateur radio
still invents things. And the newcomer
who wants to understand digital voice
*before* spending money, because FreeDV's
whole toolchain is free and, as this
guide shows, most of it can be run with
no radio at all.
