# Holding Up in Noise

This chapter runs the experiment the
whole guide has been pointing at: bury
the FreeDV signal in noise and see what
the receiver makes of it. You finish
able to run the same test on any mode
you like, and — just as important — able
to say exactly what the test does and
does not prove. The lab's run is
transcript t06.

## The setup, stated precisely

The lab took the clean 700D signal from
chapter 5 and mixed in **Gaussian
noise** — the steady hiss kind — with a
seeded random generator, so the run can
be repeated exactly. Two mixtures were
made, measured by **signal-to-noise
ratio across the full 8 kHz band** of
the sample file:

```text
SNR 10 dB: signal RMS 5000, noise RMS 1581
SNR  2 dB: signal RMS 5000, noise RMS 3971
```

Two decibels needs translating. At that
point the noise is nearly two-thirds as
strong as the signal itself; if you
played the mixture as audio, you would
hear a faint warble under loud hiss. An
analogue voice recording treated this
way is not "hard to copy" — it is mostly
gone. (A fairness note: radio people
usually quote SNR inside a 2.5 kHz
receiver bandwidth, not a full sample
band, so do not carry this 2 dB onto
the air as a specification. It is a
laboratory mixture, measured the way
the transcript says.)

## The result

```text
freedv_rx 700D, clean signal:   frames decoded: 42
freedv_rx 700D, noise at 10 dB: frames decoded: 42
freedv_rx 700D, noise at 2 dB:  frames decoded: 42
```

All of them. And the decoded speech from
the 2 dB run still tracks the original
sentence's loud-and-quiet pattern with a
correlation of **0.87** — statistically
the same as the clean decode's 0.86.
The error correction and the modem's
design are doing precisely the job
chapter 3 promised: the voice either
arrives, or, past some worse threshold
the lab did not reach in these two
steps, it stops arriving. Nothing in
between sounds like a fading SSB signal,
because there is nothing in between —
that cliff edge is the digital bargain,
named again in chapter 12.

## What this does not prove

Noise is the politest thing the
ionosphere does. A real HF path also
**fades** (the signal rises and falls,
sometimes in slices of the band),
**bends** (multipath echoes smear the
signal in time), and shares the band
with other stations. The lab simulated
none of that: its channel was a file,
plus hiss. So the honest claim is
narrow and still worth having — 700D's
coding survives heavy steady noise with
no loss at all in this test — and the
wider claim, that 700D works paths SSB
cannot, rests on the project's design
and a decade of its users' logs, not on
this chapter. The 700E mode exists
precisely because fading is a different
enemy from noise; if your paths fade
fast, chapter 3's table says which
bargain to pick.
