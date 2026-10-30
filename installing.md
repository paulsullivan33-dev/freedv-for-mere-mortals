# Installing FreeDV and the Codec Tools

By the end of this chapter you have two
things, each with a check: the **FreeDV
program** on your machine (the check is
its version and its opening screen,
described from the project's
documentation), and the **Codec2
command-line tools** (the check is one
this guide ran: `freedv_tx` with no
arguments printing its usage). The tools
matter beyond the lab: they are the
engine room of the program itself, and
they are how you rehearse everything in
chapters 5 to 7 with no radio attached.

## The program

FreeDV is a free download from
**freedv.org**, with installers for
Windows and macOS and packages or build
instructions for Linux. On Ubuntu 24.04,
the archive the lab's machine uses
carries it directly:

```bash
sudo apt install freedv
```

The lab's transcript t00 records that
package: `freedv` version **1.8.11**,
described by the archive as "Digital
Voice mode for ham radio". Installing
and opening the program is the whole of
this section's procedure; configuring
its sound devices and radio control is
chapter 8's subject, and is
documented-only in this guide because
the lab had no radio and did not run
the graphical program at all. What the
documentation promises on first run is a
main window with a waterfall, a mode
list, and *Tools → Options* holding the
sound-card and PTT settings — if your
install shows that much, you have the
program.

## The codec tools, the distro way

The command-line tools live in a
different package:

```bash
sudo apt install codec2
```

Here the lab can be exact, because it
took the package apart (transcript
t00). Ubuntu 24.04's `codec2` **1.2.0**
package ships `c2enc` and `c2dec` — the
bare codec, speech to bits and back —
plus the older FDMDV modem utilities.
It does **not** ship `freedv_tx` or
`freedv_rx`, the tools that build a
complete FreeDV signal. A reader who
installs the package and can run

```bash
c2enc 700C speech.raw speech.bit
```

has verified the codec half of this
guide's lab. For the modem half, build
from source — which is also what the
project's own developers expect Linux
users to be able to do.

## The codec tools, built from source

The lab built the official Codec2
**1.2.0** source release (the same
version as the distro package) on
Ubuntu 24.04 with the ordinary build
tools installed:

```bash
tar xzf codec2-1.2.0.tar.gz
mkdir build && cd build
cmake ../codec2-1.2.0 -DCMAKE_BUILD_TYPE=Release -DLPCNET=OFF
make -j2 freedv_tx freedv_rx c2enc c2dec
```

Two build choices are worth naming.
`LPCNET=OFF` skips the separate neural
vocoder component: smaller build, and
the price is the 2020 modes, which this
guide does not use (chapter 3 says why,
and criteria.md lists the omission in
the open). Nothing else was patched or
trimmed; the tools are the project's own.

The check that the build worked is the
one printed in transcript t00 — run the
transmitter with no arguments:

```bash
./freedv_tx
```

It answers with usage — `usage:
freedv_tx [options] 1600|700C|700D|700E|
2400A|2400B|800XA InputRawSpeechFile
OutputModemRawFile` — and exits with an
error status, which is correct behaviour
for a tool complaining. That mode list
is the table of chapter 3, straight
from the tool's own mouth. If your
`freedv_tx` prints that, chapters 5 to 7
will work for you exactly as written.
