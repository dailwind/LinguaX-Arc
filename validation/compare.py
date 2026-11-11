import json, csv, math
import numpy as np
from scipy.stats import spearmanr, pearsonr
A='antconc/'
def tsv(f): 
    r=list(csv.reader(open(A+f,encoding='utf-8'),delimiter='\t')); return r[0],r[1:]
def L(d,k): return json.load(open(f'{d}/{k}.json'))
out={}
for cond in ['linguax','linguax_tokctrl']:
    R={}
    # word list
    h,ac=tsv('1_wordlist.txt'); acf={r[0]:int(r[4]) for r in ac if r[0]}
    lx=L(cond,'wordlist')[1:]; lxf={r[1]:int(r[2]) for r in lx}
    common=set(acf)&set(lxf); exact=sum(acf[w]==lxf[w] for w in common)
    x=[acf[w] for w in common]; y=[lxf[w] for w in common]
    top=lambda d,n: [w for w,_ in sorted(d.items(),key=lambda t:(-t[1],t[0]))[:n]]
    R['wordlist']=dict(ac_types=len(acf),lx_types=len(lxf),common=len(common),exact_pct=100*exact/len(common),
        pearson=pearsonr(x,y)[0],spearman=spearmanr(x,y)[0],top100_overlap=len(set(top(acf,100))&set(top(lxf,100))),
        top1000_overlap=len(set(top(acf,1000))&set(top(lxf,1000))))
    # collocates
    h,ac=tsv('3_collocates.txt'); acc={r[0]:r for r in ac if r[0]}
    lx=L(cond,'collocates')[1:]; lxc={r[1]:r for r in lx}
    cm=sorted(set(acc)&set(lxc))
    fr=sum(int(acc[w][3])==int(lxc[w][2]) for w in cm)
    mi_a=[float(acc[w][8]) for w in cm]; mi_l=[float(lxc[w][6]) for w in cm]
    ll_a=[float(acc[w][7]) for w in cm]; ll_l=[float(lxc[w][7]) for w in cm]
    R['collocates']=dict(ac_n=len(acc),lx_n=len(lxc),common=len(cm),freq_exact_pct=100*fr/len(cm),
        mi_pearson=pearsonr(mi_a,mi_l)[0],mi_mae=float(np.mean(np.abs(np.array(mi_a)-mi_l))),mi_maxdiff=float(np.max(np.abs(np.array(mi_a)-mi_l))),
        ll_spearman=spearmanr(ll_a,ll_l)[0],ll_pearson=pearsonr(ll_a,ll_l)[0],
        top10_ac=[r[0] for r in ac[:10]], top10_lx=[r[1] for r in sorted(lx,key=lambda r:-float(r[7]))[:10]])
    # keywords (positive)
    h,ac=tsv('4_keywords.txt'); ack={r[0]:r for r in ac if r[0]}
    lx=L(cond,'keywords_pos')[1:]; lxk={r[1]:r for r in lx}
    cm=sorted(set(ack)&set(lxk))
    fa=sum(int(ack[w][4])==int(lxk[w][2]) and int(ack[w][5])==int(lxk[w][4]) for w in cm)
    ll_a=np.array([float(ack[w][12]) for w in cm]); ll_l=np.array([float(lxk[w][6]) for w in cm])
    ac_top=[r[0] for r in ac[:100]]; lx_top=[r[1] for r in lx[:100]]
    R['keywords']=dict(ac_n=len(ack),lx_n=len(lxk),common=len(cm),freq_exact_pct=100*fa/len(cm),
        ll_pearson=pearsonr(ll_a,ll_l)[0],ll_spearman=spearmanr(ll_a,ll_l)[0],ll_mae=float(np.mean(np.abs(ll_a-ll_l))),
        ll_max_absdiff=float(np.max(np.abs(ll_a-ll_l))),
        top20_overlap=len(set(ac_top[:20])&set(lx_top[:20])),top50_overlap=len(set(ac_top[:50])&set(lx_top[:50])),top100_overlap=len(set(ac_top)&set(lx_top)),
        top10_ac=ac_top[:10],top10_lx=lx_top[:10])
    # ngrams
    for n in ['2','3']:
        h,ac=tsv(f'5_ngram_{n}.txt'); acn={r[0]:int(r[2]) for r in ac if r[0]}
        lx=L(cond,f'ngram{n}')[1:]; lxn={r[1]:int(r[2]) for r in lx}
        cm=set(acn)&set(lxn); ex=sum(acn[g]==lxn[g] for g in cm)
        x=[acn[g] for g in cm]; y=[lxn[g] for g in cm]
        R[f'ngram{n}']=dict(ac_n=len(acn),lx_n=len(lxn),common=len(cm),exact_pct=100*ex/len(cm),pearson=pearsonr(x,y)[0],
            top50_overlap=len(set(top(acn,50))&set(top(lxn,50))))
    R['kwic']=L(cond,'kwic_counts')
    out[cond]=R
json.dump(out,open('comparison_results.json','w'),indent=1,default=float)
for c,R in out.items():
    print('=====',c)
    for k,v in R.items(): print(k, {a:(round(b,4) if isinstance(b,float) else b) for a,b in v.items()} if isinstance(v,dict) else v)
