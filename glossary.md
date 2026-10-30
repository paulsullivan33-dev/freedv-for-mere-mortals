# Glossary

**ALC** — Automatic Level Control, the
transmitter circuit that holds audio
drive down. For digital modes the rule
of thumb is to keep it barely moving.

**Bit rate** — how many bits per second
a codec produces. FreeDV's working
rates run from 1,600 down to 700 bit/s,
against 128,000 bit/s for uncompressed
telephone-rate speech samples.

**CAT** — Computer Aided Transceiver
control: the radio's serial or USB
control channel, used for frequency
reading and keying.

**Codec** — coder-decoder. Software
that turns a signal into a compact
representation and back. In FreeDV, the
representation is a model of the voice,
not a recording of it.

**Codec2** — the open-source speech
codec at FreeDV's heart, written by
David Rowe; also the name of its
command-line tools (`c2enc`, `c2dec`,
`freedv_tx`, `freedv_rx`).

**Correlation (envelope)** — this
guide's pattern check: whether two
recordings are loud and quiet in the
same 100 ms places. 1.0 is a perfect
match of shape, whatever the fine
detail.

**dBFS** — decibels relative to full
scale, the largest number a digital
audio file can hold. Levels in this
guide are quoted in dBFS.

**Dummy load** — a resistor that
absorbs a transmitter's output safely,
for tests that must not radiate.

**Envelope** — a recording's
loudness-over-time outline: the words'
rhythm and weight, abstracted from the
sound itself.

**FEC** — Forward Error Correction:
extra bits woven into a signal so the
receiver can repair damage without
asking for a repeat.

**Frame** — the modem's unit of work.
In 700D, 160 ms of signal: 1,280 samples
at 8,000 Hz.

**FreeDV** — the open digital-voice
system for HF amateur radio: program,
modes, and community, at freedv.org.

**FreeDV Reporter** — the project's
live web service showing who is on the
air in FreeDV, where, in what mode, and
hearing whom.

**HF** — high frequency, 3–30 MHz: the
bands where signals refract off the
ionosphere and travel intercontinental
distances.

**LPCNet** — a small neural network
that synthesises speech for Codec2's
2020 modes; a separate component from
Codec2 itself.

**Modem** — modulator-demodulator: the
part that turns bits into a sendable
audio signal and back.

**OFDM** — Orthogonal Frequency Division
Multiplexing: many small carriers side
by side, each carrying a little data,
so a fade across part of the band
damages only part of the message.

**PTT** — Push To Talk: the signal that
keys a transmitter.

**RADEV** — FreeDV 2.x's
machine-learning mode, described in
this guide from documentation only.

**Raw samples** — audio as bare numbers
with no header: the format the Codec2
command-line tools read and write, at
an agreed 8,000 Hz, mono, 16-bit.

**SNR** — signal-to-noise ratio, in
decibels. Chapter 7 states the band its
ratios were measured across, because
the number means nothing without it.

**SSB** — single sideband: the analogue
voice mode of HF, and FreeDV's host —
FreeDV's signal travels inside an SSB
transmitter's audio passband.

**Sync** — the receiver's lock on the
modem signal's structure. Lose it, and
decoding stops; the cliff of chapter
12.

**Waterfall** — the scrolling display of
frequency against time that sound-card
programs use to show signals.
