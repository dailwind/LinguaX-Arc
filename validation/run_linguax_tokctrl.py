# Runs the LinguaX Arc engine (www/index.html, v6.0.2) headlessly on the validation corpus
import asyncio, json, glob, os, time
from playwright.async_api import async_playwright
C='/home/claude/corpus/LinguaX_Validation_Corpus'
OUT='/home/claude/paper/linguax_tokctrl'
tgt=[{'name':os.path.basename(f),'text':open(f,encoding='utf-8').read()} for f in sorted(glob.glob(C+'/1_Target_Austen/*.txt'))]
ref=[{'name':os.path.basename(f),'text':open(f,encoding='utf-8').read()} for f in sorted(glob.glob(C+'/2_Reference_Fiction/*.txt'))]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto('file:///home/claude/linguax-arc/www/index.html'); await pg.wait_for_timeout(2000)
        await pg.evaluate('''([t,r])=>{ window.persistFileToStorage=async()=>{}; window.tokenize=(text)=>{const re=/\p{L}+/gu; const toks=[]; let m; while((m=re.exec(text))) toks.push({w:m[0],l:m[0].toLowerCase(),s:m.index}); return toks;}; S.files=[];S.ref=[];
            addTexts(t,'corpus'); addTexts(r,'ref'); }''',[tgt,ref])
        info=await pg.evaluate('()=>({tgt:corpusTotals(S.files), ref:corpusTotals(S.ref)})')
        print('totals',info)
        async def run(tool, opts, fn, q=None):
            t0=time.time()
            rows=await pg.evaluate('''([tool,opts,fn,q])=>{ go(tool);
                window.gselVal=(id)=> (id in opts)? String(opts[id]) : null;
                if(q!==null){ const el=document.querySelector('#q'); if(el) el.value=q; }
                window[fn](); return S.lastRows; }''',[tool,opts,fn,q])
            return rows, time.time()-t0
        res={}
        res['wordlist'],_=await run('wordlist',{'wsort':'freq'},'runWordList')
        res['collocates'],_=await run('collocate',{'cl':5,'cr':5,'comin':5,'cstat':'LL'},'runColl','time')
        res['keywords_pos'],_=await run('keyword',{'kwMetric':'LL','kwSig':'all','kwMinFreq':1},'runKeyword')
        res['ngram2'],_=await run('ngram',{'nsize':2,'nmin':5,'nsort':'freq'},'runNgram')
        res['ngram3'],_=await run('ngram',{'nsize':3,'nmin':5,'nsort':'freq'},'runNgram')
        kw=[]
        for w in ['time','love','said','never','house']:
            n=await pg.evaluate('(w)=>getHits(w,false,false).length',w); kw.append([w,n])
        res['kwic_counts']=kw
        # negative keywords
        res['keywords_neg']=await pg.evaluate('''()=>{ S.kw.show='neg'; runKeyword(); return S.lastRows; }''')
        for k,v in res.items():
            json.dump(v,open(f'{OUT}/{k}.json','w'))
            print(k, len(v), v[:3] if k!='kwic_counts' else v)
        json.dump(info,open(f'{OUT}/totals.json','w'))
        await b.close()
asyncio.run(main())
