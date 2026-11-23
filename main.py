import json as j,urllib.request as u
from os import environ
U=environ["MAKEFUN_ENV_URL"]
Y=[0,100,320,330,500,900,0]
KN=[33,31,18,14,-14,-18,-31,-33]
BD=[15,17,-15,-17]
RD=[1,-1,16,-16]
KI=BD+RD
L=30000;W=10**6
o=lambda a:0<=a<128 and not a&136
def A(q,y):
 if any((o(a:=q+32*y-16+s) and B[a]==1+(y<<3)) for s in(-1,1)):return 1
 if any((o(a:=q+w) and B[a]==d+(y<<3)) for n,d in((KN,2),(KI,6)) for w in n):return 1
 for n,d in((BD,(3,5)),(RD,(4,5))):
  for w in n:
   a=q+w
   while o(a):
    p=B[a]
    if p and p>>3==y and p&7 in d:return 1
    if p:break
    a+=w
 return 0
def G(cp=0):
 ms=[];ap=ms.append;pp=lambda a:[ap(s+a*128+q*16384)for q in(5,4,3,2)]
 for s in range(128):
  p=B[s]
  if not p or p>>3!=S:continue
  t=p&7;f=s&7;r=s>>4
  if t==1:
   d=16-32*S;e=s+d;pr=r==6-5*S
   if not B[e]:
    if pr:pp(e)
    elif not cp:
     ap(s+e*128)
     if r==1+5*S and not B[e+d]:ap(s+(e+d)*128)
   for w in(-1,1):
    a=e+w
    if not o(a):continue
    v=B[a]
    if v and v>>3!=S:
     if pr:pp(a)
     else:ap(s+a*128)
  else:
   for n in(KN,BD,RD,KI,KI)[t-2]:
    a=s+n
    while o(a):
     v=B[a]
     if v:
      if v>>3!=S:ap(s+a*128)
      break
     if not cp:ap(s+a*128)
     if t==2 or t==6:break
     a+=n
  if t==6 and not cp and s==4+112*S:
   for dt,ro,k in((2,3,0),(-2,-4,1)):
    t2=s+dt
    if C&(1+k)<<2*S and not B[s+dt//2] and not B[t2] and B[s+ro]==4+8*S and not any(A(x,1-S) for x in(s,s+dt//2,t2)) and (dt>0 or not B[s-3]):ap(s+t2*128)
 return ms
def R(c,f,t,d):
 if (c&7)==6 and abs(t-f)==2:
  a,b=(t+1,t-1) if t>f else(t-2,t+1)
  B[b],B[a]=(B[a],0)if d>0 else(0,B[b])
def K(m):
 global S,C,H,J
 f=m&127;t=m>>7&127;pr=m>>14&7
 c=B[f];v=B[t]
 T.append((f,t,c,v,C,H,J))
 if c==6:H=t
 elif c==14:J=t
 R(c,f,t,1)
 for q,bt in((0,2),(7,1),(112,8),(119,4),(4,3),(116,12)):
  if f==q or t==q:C&=~bt
 B[f]=0;B[t]=pr+(S<<3) if pr else c
 S^=1
def Z():
 global S,C,H,J
 f,t,c,v,C,H,J=T.pop()
 S^=1;B[f]=c;B[t]=v
 R(c,f,t,-1)
def E():
 s=0
 for i,p in enumerate(B):
  if not p:continue
  t=p&7;f=i&7;r=i>>4;w=p>>3;rr=r+(7-2*r)*w;g=1-2*w;v=Y[t]
  if t==1:v+=8*rr
  elif t in(2,3):v+=(7-abs(2*f-7)-abs(2*rr-7))*(5-t)
  s+=g*v
 s+=14*((H in(2,6))-(J in(114,118)))
 return s
def N(a,be,d,py):
 global g,F
 g+=1
 if g>=L:F=1;return 0
 if d<=0:
  st=E()*(1-2*S)
  if st>=be:return be
  if st>a:a=st
  for m in G(1):
   K(m)
   if A(H if S==1 else J,S):Z();continue
   s=-N(-be,-a,0,py+1)
   Z()
   if F:return 0
   if s>=be:return be
   a=max(a,s)
  return a
 k=(bytes(B),S,C);tm=O.get(k,0)
 ms=G()
 ms.sort(key=lambda m:(m==tm,B[m>>7&127]),reverse=True)
 bs=-W;bm=0
 for m in ms:
  K(m)
  if A(H if S==1 else J,S):Z();continue
  s=-N(-be,-a,d-1,py+1)
  Z()
  if F:return 0
  if s>bs:bs=s;bm=m
  a=max(a,s)
  if a>=be:break
 if bs==-W:return -100000+py if A(H if S==0 else J,1-S) else 0
 if bm:O[k]=bm
 return bs
def D(f):
 global B,S,C,H,J,T
 B=[0]*128;T=[];a=f.split();i=112
 for ch in a[0]:
  if ch=="/":i-=24
  elif ch.isdigit():i+=int(ch)
  else:B[i]="PNBRQK".find(ch)+1 or "pnbrqk".find(ch)+9;i+=1
 S=a[1]!="w"
 C=sum((ch in a[2])<<i for i,ch in enumerate("KQkq"))
 H=B.index(6);J=B.index(14)
h=lambda m:f"{chr(97+m%8)}{(m>>4)%8+1}{chr(97+(m>>7)%8)}{(m>>11)%8+1}{'nbrq'[(m>>14)-2] if m>>14 else ''}"
def b(fen,legal):
 global g,F,O
 D(fen);ms=[]
 for m in G():
  K(m)
  if not A(H if S==1 else J,S):ms.append(m)
  Z()
 if not ms:return legal[0]
 if len(ms)==1:return h(ms[0])
 O={};g=0;F=0;bm=ms[0]
 for d in range(10):
  if F:break
  a=-W;cur=0
  for m in ms:
   K(m)
   if A(H if S==1 else J,S):Z();continue
   s=-N(-W,-a,d,1)
   Z()
   if F:break
   if s>a:a=s;cur=m
  if not F and cur:bm=cur;ms.remove(cur);ms.insert(0,cur)
 return h(bm)
def post(p,y):
 try:return j.load(u.urlopen(u.Request(U+p,j.dumps(y).encode(),{"Content-Type":"application/json"})))
 except Exception:return{"error":1}
while (q:=post("/game",{})).get("status")!="done":
 if "error" in q:break
 while q.get("status")=="your_move":
  w=post("/move",{"game":q["game"],"move":b(q["fen"],q["legal_moves"])})
  if "error" in w:w=post("/move",{"game":q["game"],"move":q["legal_moves"][0]})
  q=w
