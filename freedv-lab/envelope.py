import sys, struct, math

def load(path):
    d = open(path, 'rb').read()
    return list(struct.unpack('<%dh' % (len(d) // 2), d))

WIN = 800  # 100 ms at 8 kHz

def env(s, n):
    return [math.sqrt(sum(x * x for x in s[i:i + WIN]) / WIN)
            for i in range(0, n - WIN, WIN)]

def corr_at(orig, dec, lag_samples):
    if lag_samples >= 0:
        a_s, b_s = orig[lag_samples:], dec
    else:
        a_s, b_s = orig, dec[-lag_samples:]
    n = min(len(a_s), len(b_s))
    a, b = env(a_s, n), env(b_s, n)
    m = min(len(a), len(b))
    a, b = a[:m], b[:m]
    ma, mb = sum(a) / m, sum(b) / m
    cov = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    va = math.sqrt(sum((x - ma) ** 2 for x in a))
    vb = math.sqrt(sum((y - mb) ** 2 for y in b))
    return cov / (va * vb) if va and vb else 0.0

orig = load(sys.argv[1])
dec = load(sys.argv[2])
print('unaligned correlation: %.2f' % corr_at(orig, dec, 0))
best = None
for lag_ms in range(-2000, 2001, 50):
    r = corr_at(orig, dec, lag_ms * 8)
    if best is None or r > best[1]:
        best = (lag_ms, r)
print('best correlation %.2f with decoded shifted by %+d ms'
      % (best[1], best[0]))
