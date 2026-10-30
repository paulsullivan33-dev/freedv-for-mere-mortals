import sys, wave, struct, math

for path in sys.argv[1:]:
    w = wave.open(path)
    rate, n, ch, width = w.getframerate(), w.getnframes(), w.getnchannels(), w.getsampwidth()
    data = w.readframes(n)
    s = struct.unpack('<%dh' % (len(data) // 2), data)
    peak = max(abs(x) for x in s) if s else 0
    rms = math.sqrt(sum(x * x for x in s) / len(s)) if s else 0
    def db(v):
        return -99.0 if v <= 0 else 20 * math.log10(v / 32767.0)
    nonzero = sum(1 for x in s if x != 0)
    print('%s: %d Hz, %d ch, %d-bit, %d samples, %.2f s, RMS %.1f dBFS, peak %.1f dBFS, nonzero %d%%'
          % (path, rate, ch, width * 8, n, n / rate, db(rms), db(peak),
             round(100 * nonzero / len(s)) if s else 0))
