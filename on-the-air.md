# On the Air

> **Documented-only.** This chapter is
> written from the FreeDV project's
> documentation and community practice.
> The lab transmitted nothing. Your
> licence, your band plan, and the
> project's current pages outrank
> anything here.

You finish this chapter knowing where
FreeDV stations gather, how a contact
typically goes, and the three duties
that come with the mode.

## Where it lives

FreeDV lives in the voice parts of the
HF bands, as an SSB-width guest. The
best-known centre of activity is
**14.236 MHz USB** on 20 metres, with
smaller gatherings on other bands that
move as versions and seasons change —
the project maintains the current list,
and this guide deliberately points
there rather than printing a table that
would age. Two habits matter more than
any frequency: FreeDV follows the
*sideband convention of the band* (USB
on the higher HF bands, as for voice),
and it is found by listening — the
warble is unmistakable once heard, a
bubbling, musical buzz nothing like a
voice.

Because a digital signal gives a
listener's ear nothing to identify,
FreeDV stations also spot themselves on
**FreeDV Reporter**, the project's live
map and list (in the program and on the
web): who is on, on what frequency, in
what mode, and who is hearing whom, with
signal-to-noise figures. For a mode
whose whole problem is finding the other
end of a marginal path, the reporter is
half the operating technique — check it
before concluding a band is empty.

## How a contact goes

A FreeDV contact is a voice contact,
with a digital handshake. Call CQ (or
answer one) in the mode both ends
share; the program shows sync, an SNR
estimate, and usually the other
station's call sign, carried in the
signal's small text channel (the same
channel the program's message box uses,
and the command-line tool's
`--reliabletext` option writes). Then
talk, in short overs. The digital
differences are three: there is a
noticeable **delay** (the codec and
modem hold audio briefly; this guide
measured a few hundred milliseconds in
the file tools), the signal is either
*there* or *not there* rather than
fading gracefully, and when it drops,
the honest report is "lost sync" — the
numbers the program shows (SNR,
frames decoded) are the signal report
that replaces the voice operator's
"weak but readable".

## The three duties

1. **Identify.** FreeDV's text channel
   carrying your call sign is a
   convenience, not a discharge of your
   licence's identification rules —
   identify as your regulations require,
   in a mode the rules accept, at the
   intervals they specify.
2. **Stay decodable.** The mode is open
   by design (chapter 1). Using any
   setting or side channel to obscure a
   transmission's meaning is against the
   spirit and, in most jurisdictions,
   the letter of amateur law.
3. **Mind the width and the power.**
   A FreeDV signal is narrow; a badly
   driven one is not. Chapter 8's level
   discipline — ALC barely stirring — is
   an obligation to the neighbours you
   cannot hear, on a band you are
   sharing.

Work one contact and the mode stops
being an article you read. The chapters
before this one were written so that,
when sync is lost over the Pacific, you
can tell whether the codec, the modem,
the levels, or the ionosphere did it.
