import pandas as pd, numpy as np, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from pathlib import Path
def evaluate(pred,gold):
    assert pred.qid.is_unique and set(pred.qid)==set(gold.qid), 'IDs incompletos o duplicados'
    z=gold.merge(pred,on='qid',suffixes=('_gold','_pred'))
    exact=(z.answer_gold.astype(str).str.strip().str.lower()==z.answer_pred.astype(str).str.strip().str.lower())
    def hit(r):
        g=set(str(r.evidence_ids).split('|'))-{'','nan'}; p=set(str(r.citations).split('|'))-{'','nan'}
        return bool(g&p) if g else not p
    h=z.apply(hit,axis=1)
    return {'EM':float(exact.mean()),'evidence_hit':float(h.mean()),'joint':float((exact&h).mean()),'by_kind':exact.groupby(z.kind).mean().to_dict()}
