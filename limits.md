# Limits

What FreeDV cannot do, and what this
guide could not do with it — the two
lists a reader deserves before trusting
either.

## The tool's limits

**The voice is a model, not a copy.**
At 700 bits per second there is not
enough information to carry *you* — your
warmth, your accent's fine grain, the
difference between you tired and you
fresh. What survives is intelligibility:
words, call signs, intent. Anyone
promised a natural voice at these rates
is being sold something; the 2020 and
RADEV modes (chapter 3) narrow the gap
with neural synthesis, and their cost is
computation, and their evidence in this
guide is documented-only.

**There is delay.** Codec plus modem
plus buffering held this guide's decoded
audio back by roughly a third of a
second in the file tools (chapter 6),
and a live path adds its own. Fine for
HF conversation, wrong for anything
that must interlock in real time —
singing together, interrupting
gracefully, some contest exchanges.

**The failure is a cliff.** Analogue
voice degrades by degrees and invites
you to lean in. FreeDV decodes until it
cannot, then gives silence and a lost-
sync indicator. The error correction
that makes chapter 7's result possible
is the same mechanism that makes the
edge abrupt.

**It still needs the whole station.**
FreeDV is software; the radio, the
antenna, the propagation, the computer,
the sound devices, and the operator's
level discipline are all still load-
bearing. It rescues marginal paths; it
does not repeal physics, and it does
nothing at all the moment the path
falls below even its generous floor.

**Weak-signal is a comparison, not a
promise.** Chapter 7's noise runs are
one artificial channel, two ratios, one
sentence. Fading, multipath and
interference were not simulated, and
the numbers must not be quoted as
on-air specifications.

## This guide's limits

**Nothing was transmitted.** The lab
had no radio, no antenna, and no
licence to use in this context; the
verified chapters are a file pipeline.
Chapters 8 and 9 — radio connection and
operating — are documentation and
community practice, carefully labelled,
and they will be wrong somewhere your
own radio's manual is right.

**Nothing was heard.** The lab has no
ears. Every audio claim herein is a
measurement (durations, levels, frame
counts, pattern correlations); every
claim about how a mode *sounds* is
attributed to the project and its
users. The decoded files the lab made
are consistent with speech in every
measurable way; a human listener's
verdict is the one check this guide
could not run, and chapter 6 says what
would settle it.

**One version, one voice, one mode
family.** Codec2 1.2.0, one synthesised
witness voice (a robot judging robots
is a limitation, honestly noted), and
modes the command-line tools support.
The program's newer machinery — 2020,
RADEV, the reporter integration as
actually used — is described, not
exercised. The shelf this guide stands
on will move; the checks in chapters 5
to 7 are written to be re-run against
whatever replaces them.
