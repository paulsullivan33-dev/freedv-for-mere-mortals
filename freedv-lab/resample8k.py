import sys, wave, struct, math

src, dst = sys.argv[1], sys.argv[2]
w = wave.open(src)
rate, n = w.getframerate(), w.getnframes()
frames = w.readframes(n)
samples = list(struct.unpack('<%dh' % n, frames))
target = 8000
out_n = int(n * target / rate)
out = []
for i in range(out_n):
    pos = i * rate / target
    j = int(pos)
    frac = pos - j
    a = samples[j]
    b = samples[j + 1] if j + 1 < n else a
    out.append(int(a + (b - a) * frac))
o = wave.open(dst, 'wb')
o.setnchannels(1); o.setsampwidth(2); o.setframerate(target)
o.writeframes(struct.pack('<%dh' % len(out), *out))
o.close()
print('in: %d Hz %d samples (%.2f s) -> out: %d Hz %d samples (%.2f s)'
      % (rate, n, n / rate, target, len(out), len(out) / target))
