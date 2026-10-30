# The Modes

This chapter gives you the mode table
and the one idea that organises it:
every FreeDV mode is a bargain between
**voice rate** and **survival**. The
check you can run right away needs no
radio: in a terminal, `freedv_tx` with
no arguments prints the modes the codec
tools support, and chapter 5's lab
measured two of them end to end.

## The modes the lab could touch

The Codec2 1.2.0 command-line tools —
and therefore this chapter's verified
core — support these modes:

| Mode | Voice rate | Character |
|------|-----------|-----------|
| 1600 | 1,600 bit/s | The original FreeDV mode. The clearest voice of the classic family, and the first to fail as the path worsens. |
| 700C | 700 bit/s | The low-rate codec carried by a simple robust modem. |
| 700D | 700 bit/s | The same 700 bit/s voice in a modern OFDM modem with strong error correction. The weak-signal workhorse, and this guide's lab mode. |
| 700E | 700 bit/s | A 700D relative tuned for fast fading — the path that will not sit still. |
| 800XA | 1,600 bit/s family | A wider-signal experiment in the 1600 family. |
| 2400A / 2400B | higher-rate family | Wider, fuller modes aimed at strong paths and FM-style use rather than desperate HF. |

Two of those rows are measurements in
this guide, not just descriptions. The
lab encoded the same sentence both ways
(transcripts t02 and t03). Mode 1600
produced a 6.80-second signal and got
6.40 seconds of speech back — the
receiver spent some early frames
locking on. Mode 700D produced 6.72
seconds and returned all of it, 42
frames of 42. Same voice, same file:
the tougher modem kept more of a
*perfect* signal, because locking on
and holding sync is part of its job
even before the path gets cruel.

## Reading the names

The number is roughly the voice rate in
bits per second, and that number is the
story of the mode. Halve the rate from
1,600 to 700 and the voice gets thinner
and more robotic — there is less
information to rebuild a person from.
In exchange, the modem around those
bits can spend more of its energy on
error correction and sync, and the
whole signal can be narrower and
repeated more insistently. Weak-signal
work is always this trade: say less,
but say it so it survives.

## The modes beyond the lab's reach

The FreeDV program offers more than the
command-line tools do, and this guide
labels the difference rather than
blurring it. The **2020** family keeps a
1,600-family channel but rebuilds the
voice with a small neural network
(LPCNet) instead of Codec2's classic
synthesis; its users report a markedly
more natural voice, at the cost of more
computer. The lab's source build had
LPCNet switched off — it is a separate
component — so no 2020 signal was built
or measured here, and nothing in this
guide claims otherwise. The project's
newest work, a machine-learning mode
called **RADEV** in FreeDV 2.x, is
likewise described from the project's
documentation only. If your interest is
the frontier, install the program
(chapter 4) and read the project's mode
page; if your interest is understanding,
700D teaches every idea the newer modes
also use.

## Choosing, in one paragraph

On a good path, or for a first contact,
use the newest mode both ends share —
in the current program that is usually
what the other station proposes. On a
path you can hear is struggling, drop
to 700D: it is the mode the community
reaches for when sideband has already
given up, and it is the mode this
guide's lab can vouch for — every frame
of it decoded through noise that buried
the original recording.
