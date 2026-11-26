"use strict";
const fs=require("node:fs"),vm=require("node:vm");
const reference="C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/check_03_conflict_free_colouring.js";
const source=fs.readFileSync(reference,"utf8");
const {enumerate,bits}=vm.runInNewContext(source.slice(0,source.indexOf("\ncheckExamples();"))+"\n({enumerate,bits});",{process:{argv:[]}});
const perm=(a)=>a.length?a.flatMap((v,i)=>perm(a.filter((_,j)=>i!==j)).map(r=>[v,...r])):[[]];
const permutations=perm([0,1,2,3]);
const countBits=Array.from({length:32},(_,x)=>x.toString(2).replaceAll("0","").length);
function forbidden(c, g, vertex){
    let used=0, repeat=0;
    for(const w of g[vertex]){
        const b=1<<c[w]; repeat|=used&b;used|=b;
    }
    const singular=used&~repeat;
    if(countBits[singular]>=2)return -1;
    return Math.log2(singular||used);
}
function signature(colours,g,ports){
    const temp=[...ports.map(v=>colours[v]),...ports.map(v=>forbidden(colours,g,v))];
    const labels=new Map();
    return temp.map(c=>{
        if(c<0)return -1;
        if(!labels.has(c))labels.set(c,labels.size);
        return labels.get(c);
    });
}
function collect(g,ports){
    const c=Array(g.length).fill(-1);
    const checks=Array.from({length:g.length},()=>[]);
    const states=new Map();
    let complete=0;
    g.forEach((row,v)=>{if(!ports.includes(v)&&row.length)checks[Math.max(...row)].push(v);});
    function visit(i,used){
        if(i===g.length){
            complete++;
            const s=signature(c,g,ports);
            states.set(s.join(","),s);
            return;
        }
        let available=(1<<Math.min(5,used+1))-1;
        for(const other of g[i]) if(other<i) available&=~(1<<c[other]);
        for(let choices=available;choices;choices&=choices-1){
            const bit=choices&-choices;
            c[i]=Math.log2(bit);
            if(checks[i].every(v=>{
                let present=0,repeat=0;
                for(const w of g[v]){const flag=1<<c[w];repeat|=present&flag;present|=flag;}
                return Boolean(present&~repeat);
            }))visit(i+1,Math.max(used,c[i]+1));
        }
    }
    visit(0,0);
    return {g,ports,sets:[...states.values()],complete};
}
function glue(a,b){
    const lists=[31,31,31,31,31];
    for(let i=0;i<4;i++){
        lists[b[i]]&=~(1<<a[i]);
        if(a[i+4]!==-1) lists[b[i]]&=~(1<<a[i+4]);
        if(b[i+4]!==-1) lists[b[i+4]]&=~(1<<a[i]);
    }
    lists.sort((a,b)=>countBits[a]-countBits[b]);
    function visit(i,used){
        if(i===5)return true;
        for(let open=lists[i]&~used;open;open&=open-1){
            if(visit(i+1,used|(open&-open)))return true;
        }
        return false;
    }
    return visit(0,0);
}

const top=[];
let candidateCount=0, sigMin=Infinity, biggest=0, flexible=0, fewBad=0, noBad=0, hallLoads=0, firstRigid;
let twinFreeRigid=0, firstTwinFree;
const left=[[0,0,1,1,-1,2,2,2],[0,1,0,2,2,2,1,-1]];
const right=[[0,1,0,2,1,2,2,1],[0,1,2,3,3,2,1,2],[0,1,0,2,2,2,1,-1]];
const exclusions=[0,0], firstFilter=[null,null];
function consider(g,ports){
    const entry=collect(g,ports);
    if(!entry.sets.length)throw new Error("Unexpected empty fragment");
    candidateCount++; sigMin=Math.min(sigMin,entry.sets.length);biggest=Math.max(biggest,entry.sets.length);
    const second=entry.sets.some(s=>new Set(s.slice(0,4)).size===4&&s.slice(4).filter(c=>c>=0).length<=1);
    const first=entry.sets.some(s=>{
        if(s.slice(4).some(c=>c>=0))return false;
        const c=s.slice(0,4);
        return new Set(c).size!==2||c.filter(v=>v===c[0]).length!==2;
    });
    const load=entry.sets.some(s=>{
        const counts=[0,0,0,0,0];
        for(const number of s.slice(0,4))counts[number]+=2;
        for(const number of s.slice(4))if(number>=0)counts[number]++;
        return [1,2,3,4].every(k=>counts.filter(c=>c<k).length>=k);
    });
    if(load)hallLoads++;
    if(second)fewBad++;
    if(first)noBad++;
    if(first||second||load)flexible++;
    else {
        firstRigid??={graph:g,ports,states:entry.sets.length};
        if(new Set(g.map(row=>row.join(","))).size===g.length){
            twinFreeRigid++;
            firstTwinFree??={graph:g,ports,states:entry.sets.length};
        }
    }
    for(const p of permutations){
        const relabelled=entry.sets.map(t=>[...p.map(k=>t[k]),...p.map(k=>t[k+4])]);
        for(const [which,witness] of [[0,left],[1,right]]){
            if(witness.some(s=>relabelled.some(t=>glue(s,t))))continue;
            exclusions[which]++;
            firstFilter[which]??={graph:g,ports,p,states:entry.sets};
        }
    }
    if(top.length<40||entry.sets.length<top.at(-1).sets.length){
        top.push(entry);top.sort((a,b)=>a.sets.length-b.sets.length);
        if(top.length>40)top.pop();
    }
}
for(let n=6;n<=9;n++){
    let seen=0;
    enumerate(n,n,adj=>{
        if(++seen>60)return;
        const g=Array.from(adj,bits);
        for(let v=0;v<n;v++){
            const ports=g[v].map(w=>w<v?w:w-1);
            const remaining=g.filter((_,i)=>i!==v).map(row=>row.filter(w=>w!==v).map(w=>w<v?w:w-1));
            consider(remaining,ports);
        }
        const edges=g.flatMap((row,i)=>row.filter(j=>i<j).map(j=>[i,j]));
        for(let i=0;i<Math.min(3,edges.length);i++){
            const [a,b]=edges[i], other=edges.find(([c,d])=>!([a,b].includes(c)||[a,b].includes(d)));
            if(!other)continue;
            const [c,d]=other;
            const h=g.map((row,u)=>row.filter(v=>![[a,b],[b,a],[c,d],[d,c]].some(([x,y])=>u===x&&v===y)));
            consider(h,[a,b,c,d]);
        }
    });
}
let checked=0;
for(let i=0;i<top.length;i++)for(let j=i;j<top.length;j++){
    const a=top[i],b=top[j];
    for(const p of permutations){
        if(!a.sets.some(s=>b.sets.some(t=>glue(s,[...p.map(k=>t[k]),...p.map(k=>t[k+4])])))){
            console.log(JSON.stringify({counterexampleCandidate:{i,j,a,b,p}}));
            process.exit(2);
        }
        checked++;
    }
}
console.log(JSON.stringify({candidateCount,sigMin,biggest,checked,flexible,fewBad,noBad,hallLoads,firstRigid,
    twinFreeRigid,firstTwinFree,exclusions,firstFilter,topCounts:top.map(t=>t.sets.length)}));
