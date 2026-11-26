
"use strict";
const Q=[0,1,2,3,4], P=[0,1,2], V=[0,1,2,3];
const e3=(i,j)=>i===0?1<<(j-1):4, e4=(i,j)=>1<<([0,3,5][i]+j-i-1);
const fac=P.map(i=>V.filter(j=>j!==i));
const good=(r,d)=>d===4||r.slice(1).includes(1);
function decode(s){return Array.from({length:s.length/6},(_,i)=>[...s.slice(i*6,i*6+6)].map(Number));}
function norm(R,D){
 for(let i=0;i<R.length;i++)if(D[i]===4){
   if(R[i].slice(1).some(x=>x!==0)&&!R[i].slice(1).includes(1))return null;
   R[i]=[R[i][0],0,0,0,0,0];
 }
 const p=[];for(const r of R)if(!p.includes(r[0]))p.push(r[0]);const q=Q.filter(x=>!p.includes(x));
 q.sort((a,b)=>{for(const r of R)if(r[a+1]!==r[b+1])return r[a+1]-r[b+1];return 0;});p.push(...q);
 return R.map(r=>[p.indexOf(r[0]),...p.map(c=>r[c+1])].join("")).join("");
}
function eDeg(mask,n){
 const d=Array(n).fill(0);for(let i=0;i<n;i++)for(let j=i+1;j<n;j++)if(mask&(n===3?e3:e4)(i,j)){d[i]++;d[j]++;}
 return d;
}
function masks(mask,L){
 let e=0;for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)if(mask&e4(L[i],L[j]))e|=e3(i,j);
 return e;
}
function base(E,D){
 const ans=new Set;
 for(let a of Q)for(let b of Q)for(let c of Q)for(let d of Q){const w=[a,b,c,d], R=w.map(h=>[h,0,0,0,0,0]);let ok=true;
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)if(E&e4(i,j)){if(w[i]===w[j])ok=false;else{R[i][w[j]+1]++;R[j][w[i]+1]++;}}
 if(ok)ans.add(norm(R,D));}
 return ans;
}
function permute(A){if(!A.length)return [[]];return A.flatMap(a=>permute(A.filter(x=>x!==a)).map(B=>[a,...B]));}
const maps=new Map;
function mapColours(H,C){
 const key=H.join("")+C.join("");if(maps.has(key))return maps.get(key);
 const a=new Map,b=new Set;let ok=true;
 for(let i=0;i<3;i++){
 if(a.has(C[i])){if(a.get(C[i])!==H[i])ok=false;}
 else{if(b.has(H[i]))ok=false;a.set(C[i],H[i]);b.add(H[i]);}}
 const M=ok?permute(Q.filter(c=>!b.has(c))).map(B=>Q.map(c=>a.has(c)?a.get(c):B.shift())):[];
 maps.set(key,M);return M;
}
function extra(S,E){
 const groups=new Map;
 for(const A of S){
 const R=A.map(x=>x.slice());for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)if(E&e3(i,j)){R[i][R[j][0]+1]--;R[j][R[i][0]+1]--;}
 const k=R.map(x=>x[0]).join("");if(!groups.has(k))groups.set(k,[]);groups.get(k).push(R);
 }
 return [...groups].map(([k,g])=>[[...k].map(Number),g]);
}
function merge(A,B,L,D){
 const S=new Set;
 for(const a of A){const H=L.map(i=>a[i][0]);for(const [k,G] of B){const M=mapColours(H,k);
 for(const b of G)for(const p of M){
 const R=a.map(x=>x.slice());
 for(let i=0;i<3;i++)for(let j=0;j<5;j++)R[L[i]][p[j]+1]+=b[i][j+1];
 const key=norm(R,D);if(key!==null)S.add(key);
 }
 }}
 return S;
}

const patterns = ["000","001","010","011","012"];
const contextLists = new Map, rowCache = new Map;
function circumstances(hue,degree){
 const key=hue+":"+degree;if(contextLists.has(key))return contextLists.get(key);
 const A=Q.filter(x=>x!==hue), sets=[];
 function build(remaining,next,row){if(!remaining){sets.push(row.slice());return;}
 for(let j=next;j<A.length;j++){row[A[j]]++;build(remaining-1,j,row);row[A[j]]--;}}
 for(let count=Math.max(0,3-degree);count<=4-degree;count++)build(count,0,[0,0,0,0,0]);
 contextLists.set(key,sets);return sets;
}
function rowChoices(colour,counts,degree){
 const k=[colour,degree,...counts].join("");if(rowCache.has(k))return rowCache.get(k);
 const hits=[];
 for(const [i,outside] of circumstances(colour,degree).entries()){
 if(outside.some((n,h)=>n+counts[h]===1))hits.push(i);
 }
 rowCache.set(k,hits);return hits;
}
function profile(S,D){
 const sizes=D.map(d=>circumstances(0,d).length), block=sizes.reduce((a,b)=>a*b);
 const raw=new Uint32Array(Math.ceil(patterns.length*block/32)), n=Array(patterns.length).fill(0);
 for(const code of S){
 const R=decode(code), H=R.map(r=>r[0]), i=patterns.indexOf(H.join(""));
 if(n[i]===block)continue;
 for(const permutation of mapColours(H,H)){
 const A=R.map((r,j)=>{
 const counts=[0,0,0,0,0];for(let h=0;h<5;h++)counts[permutation[h]]=r[h+1];
 return rowChoices(r[0],counts,D[j]);
 });
 for(const q of A[0])for(const r of A[1])for(const s of A[2]){
 const bit=i*block+(q*sizes[1]+r)*sizes[2]+s;
 const word=bit>>>5,b=1<<(bit&31);
 if(!(raw[word]&b)){raw[word]|=b;n[i]++;}
 }
 }
 }
 return raw;
}
function profileSubset(left,right){
 return left.every((x,i)=>(x&~right[i])===0);
}

function explore(cap){
 const Qs=[],A3=new Map,A4=new Map,matching4=Array.from({length:8},()=>[]),matching3=Array.from({length:8},()=>[]);
 let processed=0,term=0,j4=0,j3=0,max=0,projs=0,count4=0,count3=0;
 const record=()=>({processed,seen:Qs.length,j4,j3,term,max,projs,count4,count3,live:Qs.filter(x=>x.live).length});
 function state(A,k,meta,S){
 const list=A.get(k)||[];
 if(S.size===0)throw Error("empty signatures: "+JSON.stringify(meta));
 const acceptance=meta.four?null:profile(S,meta.D);
 const existingDominates=x=>meta.four
   ? x.raw.size<=S.size&&[...x.raw].every(v=>S.has(v)) : profileSubset(x.acceptance,acceptance);
 const newDominates=x=>meta.four
   ? x.raw.size>=S.size&&[...S].every(v=>x.raw.has(v)) : profileSubset(acceptance,x.acceptance);
 if(list.some(x=>x.live&&existingDominates(x)))return;
 for(const x of list)if(x.live&&newDominates(x))x.live=false;
 const s={...meta,acceptance,raw:S,S:[...S].map(decode),live:true};list.push(s);A.set(k,list);Qs.push(s);max=Math.max(max,S.size);if(meta.four)count4++;else count3++;
 }
 function add3(E,D,num,S){
 const ext=eDeg(E,3).map((d,i)=>D[i]-d);
 if(ext.some(d=>d<1)||num>=2&&ext.reduce((a,b)=>a+b)<4)return;
 if(D.every(d=>d>=3)){term++;if(![...S].some(s=>decode(s).every((r,i)=>good(r,D[i]))))throw Error("bad terminal "+JSON.stringify({E,D,num,S:S.size}));}
 if(D.includes(4))return;
 state(A3,[E,...D].join(""),{E,D,num,four:false},S);
 }
 function project(E,D,last,S){
 if(D[3]<3)return;
 const D3=D.slice(0,3), out=new Set([...S].map(decode).filter(R=>good(R[3],D[3])).map(R=>norm(R.slice(0,3),D3)));
 projs++;add3(masks(E,P),D3,last<0?1:2,out);
 }
 function add4(E,D,last,S){
 if(!S.size)throw Error("no proper partial coloring "+JSON.stringify({E,D,last}));
 const available=P.filter(i=>i>last&&fac[i].every(j=>D[j]<4));
 if(!available.length){project(E,D,last,S);return;}
 const border=eDeg(masks(E,P),3);
 if(P.some(i=>D[i]===border[i]&&!available.some(j=>fac[j].includes(i))))return;
 state(A4,[E,...D,last].join(""),{E,D,last,four:true},S);
 }
 for(let E=0;E<63;E++){const D=eDeg(E,4);add4(E,D,-1,base(E,D));}
 function attach(a,b,i){
 const L=fac[i], D=a.D.slice(), E=b.E;
 const e=eDeg(E,3);
 for(let k=0;k<3;k++){D[L[k]]+=b.D[k]-e[k];if(D[L[k]]>4)return;}
 j4++;const r=merge(a.S,b.extra,L,D);
 add4(a.E,D,i,r);
 }
 function join(a,b){
 const e=eDeg(a.E,3),D=a.D.map((d,i)=>d+b.D[i]-e[i]);
 if(D.some(d=>d>4))return;
 j3++;add3(a.E,D,2,merge(a.S,b.extra,P,D));
 }
 for (const s of Qs){
 if(!s.live)continue;
 if(processed%100===0)console.log(JSON.stringify(record()));
 if(processed++===cap)return {...record(),limit:cap};
 if(s.four){
 project(s.E,s.D,s.last,s.raw);
 for(let i=s.last+1;i<3;i++){const E=masks(s.E,fac[i]);
 for(const b of matching3[E])if(b.live)attach(s,b,i);
 matching4[E].push([s,i]);}
 }else{
 s.extra=extra(s.S,s.E);
 for(const a of matching3[s.E])if(a.live)join(a,s);
 join(s,s);
 for(const [a,i] of matching4[s.E])if(a.live)attach(a,s,i);
 matching3[s.E].push(s);
 }
 }
 return {...record(),complete:true};
}
console.log(JSON.stringify(explore(Number(process.argv[2]||100000))));

