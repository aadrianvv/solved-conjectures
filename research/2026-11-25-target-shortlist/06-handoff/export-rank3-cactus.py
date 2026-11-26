from pathlib import Path
import full_cactus as check

folder = Path(__file__).parent
check.normalize_arcs(check.cap_domains_with_petals(2))
caps=check.cap_domains_with_petals(4)
rows = []
for domain, shape in caps:
    values = [sum(symbol << (6*i) for i, symbol in enumerate(state)) for state in domain]
    rows.append(','.join(map(str,sorted(values))))
(folder/'rank3-arity4-cactus-domains.txt').write_text('\n'.join(rows)+'\n')
rows = []
for a in range(3*check.W):
    rows.append(','.join(str(sum(1<<m for m in check.MODES if check.permits(m,a,b)))
                         for b in range(3*check.W)))
(folder/'k4-cactus-edge-table.txt').write_text('\n'.join(rows)+'\n')
print('union',len(set().union(*(d for d,_ in caps))), 'largest cap',max(map(lambda item:len(item[0]),caps)),flush=True)
