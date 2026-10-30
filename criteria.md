# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's sentence uses a placeholder call sign (N0CALL,
   read aloud as "November Zero Call") precisely so it belongs
   to nobody.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** Chapter 12 names what the tool
   cannot do: the modelled (not copied) voice, the delay, the
   cliff-edge failure, the whole station it still needs, and
   the narrowness of this guide's own noise evidence.
8. **The ethics rule is in the text, early.** FreeDV's rule
   shapes the tool itself — the codec is published, nothing is
   obscured, and station identification remains the operator's
   duty under their own licence — so chapter 1 and the README
   state it before any procedure: openness by design, identify
   the usual way, and no using the mode to hide a meaning.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a shared Ubuntu 24.04 sandbox with **no
radio, no antenna, no sound device, and no display**. The lab
therefore worked at the layer that needs none of those: the
official **Codec2 1.2.0**, obtained two ways and compared.
Ubuntu's `codec2` package (1.2.0-2build1) was downloaded and
taken apart; it ships `c2enc`/`c2dec` and the FDMDV utilities
but **not** `freedv_tx`/`freedv_rx`. The same-version official
source release was then built unmodified (`cmake
-DCMAKE_BUILD_TYPE=Release -DLPCNET=OFF -DUNITTEST=OFF`; only
the four lab tools were compiled) to obtain the full modem
tools. The Ubuntu archive also carries the FreeDV GUI as
package `freedv` 1.8.11-1build4 — recorded in transcript t00,
**not installed or run**: the GUI cannot run headless here,
and this guide never pretends it did. The test voice was
**espeak-ng 1.51** (Ubuntu packages extracted, not installed),
speaking one stock sentence; espeak-ng's data ended up behind
a prefix quirk (its data lives in the library directory on
Ubuntu, and a symlink in the sandbox pointed there), which
chapter 13's spirit covers without burdening the reader. All
transcripts live in `freedv-lab/transcripts/`; the lab
scripts are `freedv-lab/measure.py`,
`freedv-lab/resample8k.py` and `freedv-lab/envelope.py`.

The lab had **no way to listen**. Every claim about the audio
is a measurement — format, duration, sample-level RMS/peak,
frame counts, and a loudness-envelope correlation against the
original — and the guide never grades how a decode *sounds*.

Run for real, with transcripts as evidence:

- Tools: the distro package's contents listed tool by tool;
  the source build's four tools built; `freedv_tx` run with
  no arguments, printing its usage and the mode list
  (1600, 700C, 700D, 700E, 2400A, 2400B, 800XA) (t00).
- Speech: the stock 20-word sentence synthesised at 22,050 Hz
  (6.84 s), resampled to FreeDV's 8,000 Hz (54,698 samples,
  RMS −20.9 dBFS, peak −0.0 dBFS, 79% nonzero) (t01).
- 700D round trip: raw speech in, 53,760 modem samples out
  (6.72 s, RMS −16.3 dBFS, peak −6.0 dBFS, 100% nonzero);
  `freedv_rx` reports **frames decoded: 42** of 42, returning
  53,760 speech samples at RMS −22.5 dBFS. The shorter
  duration is whole-frame arithmetic (42 × 160 ms), shown,
  not hidden (t02).
- 1600 round trip: 6.80 s of modem signal in, 6.40 s of
  speech back (RMS −21.6 dBFS) — the receiver spends early
  frames locking on, and the guide says so where it quotes
  the mode (t03).
- The codec alone: `c2enc 700C` turns the sentence into a
  680-byte bit file (171 frames × 4 bytes × 40 ms) against
  109,396 bytes of raw speech; `c2dec` returns 6.80 s of
  speech samples (t04).
- The pattern check: loudness-envelope correlation between
  original and decoded, over 100 ms slices. Unaligned, the
  700D comparison scores −0.21 — the decode trails by a
  constant ~350 ms in the file tools, and the naive check
  fails for that reason alone. Aligned by a shift search:
  700D **0.86**, 1600 **0.89**, 700C **0.78** (t05).
- Noise: the 700D signal mixed with seeded Gaussian noise at
  measured full-band SNRs of 10 dB and 2 dB decodes **42 of
  42 frames at both levels**, and the 2 dB decode's envelope
  correlation is 0.87 — with the method (full-band ratio,
  steady noise only, no fading or multipath) stated in the
  chapter so the number cannot be over-read (t06).

Documented only — described from the project's documentation
and community practice, not run, and the text says so at the
chapter head:

- The FreeDV GUI itself: its windows, waterfall, options
  layout, and Reporter integration (chapters 4, 8, 9).
- Everything at a radio: sound-card and interface cabling,
  level and ALC discipline, PTT by CAT/VOX/serial, dummy-load
  and on-air checks (chapter 8).
- Operating: activity centres (14.236 MHz USB named as the
  best-known, with the current list deliberately left to the
  project), FreeDV Reporter's use, contact procedure,
  identification practice (chapter 9).
- The 2020 family (LPCNet neural synthesis — the component
  this lab's build deliberately omitted) and the RADEV mode
  of FreeDV 2.x: characterised, never encoded or measured
  here (chapter 3).
- The neighbour systems of chapter 11 (SSB practice, the
  AMBE-based VHF/UHF modes, WSJT-X modes, the sound-card
  data modes): characterised, not run or benchmarked.
- How any mode *sounds* to a human ear, including whether
  the lab's decoded files are intelligible — every proxy
  measurement says the speech pattern survives; the
  listening check is named in chapter 6 as the one the lab
  could not run.

Fixtures are this guide's own and deliberately generic: one
stock sentence about FreeDV itself, spoken by a synthesiser,
carrying the placeholder call sign N0CALL. No real call
signs, people, stations, or organisations appear anywhere in
the lab or the text.
