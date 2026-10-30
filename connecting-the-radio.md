# Connecting the Radio

> **Documented-only.** The lab that
> wrote this guide had no radio. This
> chapter teaches the connection from
> the FreeDV manual and standard
> sound-card practice, and labels it as
> such: nothing here was run, and your
> radio's own manual outranks it.

By the end you can name the three wires
FreeDV needs between computer and radio —
audio out, audio in, and a way to key
the transmitter — and your first three
checks once they are plugged in.

## The shape of the connection

The radio stays an ordinary SSB
transceiver. FreeDV asks it for exactly
what a microphone and a speaker offer:

- **Computer → radio:** the modem signal
  (that ~1 kHz warble) goes in where a
  microphone's audio would, ideally via
  the rig's data or accessory socket,
  which bypasses microphone processing.
- **Radio → computer:** received audio
  comes back the same way, from a data
  socket or the speaker/headphone line.
- **PTT:** something must tell the radio
  to transmit. The usual ways are the
  radio's **CAT** control over USB or
  serial (FreeDV speaks to rigs through
  Hamlib — the subject of this series'
  Hamlib guide), a serial-port line
  wired to the PTT pin, or, least
  preferred, VOX.

Many recent transceivers fold all three
into **one USB cable**: the rig appears
as a USB sound card plus a serial port.
Older rigs use an interface box (the
same species of hardware sold for Fldigi
and the other sound-card modes — this
series' Fldigi guide covers that world).
If you already run any sound-card mode,
you already own FreeDV's cabling.

## The settings that matter

Inside FreeDV's options, the manual has
you choose **two sound devices**, not
one: the radio's (for the modem audio)
and your own (microphone and speakers
for your voice). Swapping them is the
classic first-run fault — the symptom
is a program that hears your room and
sends your voice's *recording* nowhere
near the radio.

Levels are the second classic. The
receive side wants the radio's audio
steady and unremarkable — the waterfall
alive but not blazing. The transmit
side wants restraint: drive the radio
so its **ALC** meter barely stirs.
Overdriving a digital signal splatters
it across the band exactly as it does
an overdriven voice, and the far end's
decoder gets a distorted warble no
amount of error correction asked for.

## Your first three checks

1. **Receive-only first.** With PTT
   control disabled or the radio on a
   dummy load, tune to a FreeDV signal
   (chapter 9 names where). The check:
   the program's sync indicator and SNR
   display wake up. Receive working
   proves half the cabling and all of
   the decode chain.
2. **Transmit into a dummy load, at low
   power.** Key up and speak. The check:
   the radio's power meter shows a
   steady digital signal while you talk
   and drops when you stop — and your
   monitor receiver (or the rig's own
   monitor) hears a warble, not your
   voice and not silence.
3. **Only then, the antenna.** Same
   checks, real frequency, low power,
   and a call (chapter 9).

If a check fails, chapter 13 sorts the
faults by part — program, codec, modem,
radio — rather than by symptom alone.
