import json,os,urllib.request as u
U=os.getenv("MAKEFUN_ENV_URL")or exit()
V=(0,100,320,330,500,900,0);M=150000
P=[[0]*128 for _ in range(7)]
for s in range(128):
 if s&136:continue
 r,f=s>>4,s&7;c=min(f,7-f)+min(r,7-r)
 P[1][s]=r*r*(r<7)
 P[2][s]=6*c-20;P[3][s]=4*c-8;P[4][s]=15*(r==6);P[5][s]=2*c-6
 P[6][s]=-15*r+10*(r==0)*(f<2 or f>5)
Q=[s for s in range(128)if s&136==0]
N=(14,18,31,33,-14,-18,-31,-33);B=(15,17,-15,-17);R=(1,-1,16,-16);K=R+B
C={0:13,4:12,7:14,112:7,116:3,119:11}
b=[0]*128;S=1;A=0;W=[4,116];X=[0,0,0]
def uc(m):return "".join(chr(97+(n&7))+chr(49+(n>>4))for n in(m&127,(m>>7)&127))+("q" if m>>14 else "")
def pu(s):return 16*ord(s[1])+ord(s[0])-881|(16*ord(s[3])+ord(s[2])-881)<<7|(5<<14 if len(s)==5 else 0)
def pf(f):
 global b,S,A,W
 p=f.split();b=[0]*128;s=112
 for ch in p[0]:
  if ch=="/":s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   c=" PNBRQK".index(ch.upper())
   if ch.islower():c=-c
   b[s]=c
   if abs(c)==6:W[c<0]=s
   s+=1
 S=1 if p[1]=="w" else -1;A=sum((k in p[2])<<i for i,k in enumerate("KQkq"))
def at(s,y):
 for ds,pc in(((-15*y,-17*y),1),(N,2),(K,6),(B,3),(R,4)):
  for d in ds:
   t=s+d
   while not t&136:
    v=b[t]
    if v:
     if v==pc*y or pc>2 and v==5*y:return 1
     break
    if pc-3 and pc-4:break
    t+=d
 return 0
def mk(m):
 global S,A
 f=m&127;t=(m>>7)&127;w=m>>14;pc=b[f];cp=b[t];z=(m,cp,A)
 b[f]=0;n=w*(pc>0 or-1)if w else pc;b[t]=n
 if abs(pc)==6:
  W[pc<0]=t
  if abs(t-f)==2:
   rf=t+1 if t>f else t-2;rt=t-1 if t>f else t+1;b[rt]=b[rf];b[rf]=0
 A&=C.get(f,15)&C.get(t,15);S=-S;return z
def um(z):
 global S,A
 m,cp,A=z;f=m&127;t=(m>>7)&127;w=m>>14;pc=b[t]
 if abs(pc)==6:
  W[pc<0]=f
  if abs(t-f)==2:
   rf=t+1 if t>f else t-2;rt=t-1 if t>f else t+1;b[rf]=b[rt];b[rt]=0
 b[f]=(pc>0 or-1)if w else pc;b[t]=cp;S=-S
def gn(cp):
 ms=[];a=ms.append
 for s in Q:
  p=b[s]
  if not p or(p>0)!=(S>0):continue
  t=abs(p)
  if t==1:
   d=16*(p>0 or-1);l=7*(p>0);to=s+d
   if not b[to]:
    if to>>4==l:a(s|to<<7|5<<14)
    elif not cp:
     a(s|to<<7)
     if(s>>4)==6-5*(p>0) and not b[to+d]:a(s|(to+d)<<7)
   for to in(s+d-1,s+d+1):
    if to&136:continue
    v=b[to]
    if v and(v>0)!=(p>0):a(s|to<<7|(5<<14 if to>>4==l else 0))
  else:
   ds=N if t==2 else B if t==3 else R if t==4 else K;sl=2<t<6
   for d in ds:
    to=s+d
    while not to&136:
     v=b[to]
     if v:
      if(v>0)!=(p>0):a(s|to<<7)
      break
     if not cp:a(s|to<<7)
     if not sl:break
     to+=d
   if t==6 and not cp:
    for kf,kt,rf,bt in((4,6,7,1),(4,2,0,2),(116,118,119,4),(116,114,112,8)):
     if s==kf and A&bt and b[rf]==(4 if kf<16 else -4):
      d=1 if kt>kf else -1
      if not b[kf+d] and not b[kt] and(d>0 or not b[kt+d]) and not at(kf,-S) and not at(kf+d,-S) and not at(kt,-S):a(kf|kt<<7)
 return ms
def ev():
 return sum((V[t]+P[t][q if p>0 else q^112])*(p>0 or-1)for q in Q for p in[b[q]]for t in[abs(p)]if p)*(S>0 or-1)
def od(ms):
 return sorted(ms,key=lambda m:V[abs(b[(m>>7)&127])]if b[(m>>7)&127] else(9e3 if m>>14 else 0),reverse=1)
def sr(d,a,b2,p):
 X[0]+=1
 if X[0]>=X[2]>0:X[1]=1;return 0
 c=at(W[S<0],-S);be=-M-1
 if d<=0 and not c:
  s=ev()
  if s>=b2:return s
  be=s
  if s>a:a=s
 ms=od(gn(not c if d<=0 else 0))
 lg=0
 for m in ms:
  z=mk(m)
  if at(W[S>0],S):um(z);continue
  lg+=1
  s=-sr(max(d-1,0),-b2,-a,p+1)
  um(z)
  if X[1]:return 0
  if s>be:be=s
  if s>=b2:return s
  a=max(a,s)
 if not lg:return -M+p if c else(be if d<=0 else 0)
 return be
def rt(lg):
 ms=od(list(map(pu,lg)));X[0]=0
 for d in range(1,13):
  X[1]=0;X[2]=0 if d==1 else M;sc=[];A=sc.append
  for m in ms:
   z=mk(m)
   if at(W[S>0],S):um(z);continue
   s=-sr(d-1,-M-1,M+1,1);um(z)
   if X[1]:break
   A((s,m))
  if X[1]:break
  ms=[m for _,m in sorted(sc,reverse=1)]
 return ms[0]
def pt(a,b):
 try:return json.load(u.urlopen(u.Request(U+a,json.dumps(b).encode(),{"content-type":"application/json"})))
 except Exception as e:exit(a+str(e))
while 1:
 g=pt("/game",{})
 if g["status"][0]=="d":break
 while g["status"][0]=="y":
  pf(g["fen"])
  if not g["legal_moves"]:break
  g=pt("/move",{"game":g["game"],"move":uc(rt(g["legal_moves"]))})
