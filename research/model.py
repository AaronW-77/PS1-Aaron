"""Synthetic ticket decision model. No human data or actual AI predictions."""
import math, random, csv, json
from pathlib import Path

def risk(Q,N):
    if not math.isfinite(Q) or not math.isfinite(N) or Q < 1 or N < 0:
        raise ValueError('Q must be positive; N must be nonnegative')
    return min(.98, N/(N+8*Q+1))

def posterior(p,r,advice):
    if not (0<=p<=1 and 0<=r<=1) or advice not in ('buy','wait'):
        raise ValueError('invalid probability or advice')
    # Symmetric noisy signal of sale-out state; not an empirical accuracy claim.
    a,b=(r,1-r) if advice=='buy' else (1-r,r)
    denom=p*a+(1-p)*b
    return None if denom==0 else p*a/denom

def values(P,V,p):
    if not (math.isfinite(P) and math.isfinite(V) and 0<P<V and 0<=p<=1):
        raise ValueError('analysis restricts to 0 < P < V and p in [0,1]')
    return V-P,(1-p)*(V-.9*P)

def action(P,V,p):
    b,w=values(P,V,p)
    return 'buy' if b>=w else 'wait'

def expected(P,V,p,r,policy):
    total=0.
    for sold in (True,False):
        for advice in ('buy','wait'):
            prob=(p if sold else 1-p)*(r if ((advice=='buy')==sold) else 1-r)
            if prob==0: continue
            post=posterior(p,r,advice)
            choice=advice if policy=='follow' else action(P,V,p if policy=='ignore' else post)
            reward=V-P if choice=='buy' else (0 if sold else V-.9*P)
            total+=prob*reward
    return total

def run(outdir):
    outdir=Path(outdir);outdir.mkdir(parents=True,exist_ok=True)
    rows=[]
    for N in (10,50,100,500,900):
      for r in (.3,.5,.6,.8,1.):
        p=risk(40,N)
        row={'N':N,'Q':40,'P':150,'V':220,'reliability':r,'risk':p}
        for policy in ('ignore','follow','bayes'):
            row[policy]=expected(150,220,p,r,policy)
        row['follow_regret']=row['bayes']-row['follow']
        rows.append(row)
    with (outdir/'policy_comparison.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
    p=risk(40,500);r=.8
    rng=random.Random(206); totals={k:0. for k in ('ignore','follow','bayes')}
    trials=100000
    for _ in range(trials):
        sold=rng.random()<p;correct=rng.random()<r
        advice='buy' if sold==correct else 'wait'
        for policy in totals:
            choice=advice if policy=='follow' else action(150,220,p if policy=='ignore' else posterior(p,r,advice))
            totals[policy]+=70 if choice=='buy' else (0 if sold else 85)
    result={'evidence':'synthetic exact enumeration and Monte Carlo; not human behavior',
      'seed':206,'trials':trials,'risk':p,'no_advice_threshold':15/85,
      'posterior_buy':posterior(p,r,'buy'),'posterior_wait':posterior(p,r,'wait'),
      'exact':{k:expected(150,220,p,r,k) for k in totals},
      'monte_carlo':{k:v/trials for k,v in totals.items()},
      'grid_cases':len(rows)}
    (outdir/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    return result

if __name__=='__main__':
    print(json.dumps(run(Path(__file__).parent/'outputs'),indent=2))
