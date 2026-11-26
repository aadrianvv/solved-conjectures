"use strict";

const fs = require("node:fs");
const vm = require("node:vm");
const source = fs.readFileSync("C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/check_03_conflict_free_colouring.js", "utf8");
const {verifyColouring} = vm.runInNewContext(source.slice(0, source.indexOf("\ncheckExamples();"))
    + "\n({verifyColouring});", {process: {argv: []}});
let seed = Number(process.argv[2] ?? 937001);
function random(n) {
    seed ^= seed << 13; seed ^= seed >>> 17; seed ^= seed << 5;
    return (seed >>> 0) % n;
}
const clone = g => g.map(row => [...row]);
const has = (g,u,v) => g[u].includes(v);
const link = (g,u,v) => {g[u].push(v); g[v].push(u);};
const unlink = (g,u,v) => {g[u].splice(g[u].indexOf(v),1); g[v].splice(g[v].indexOf(u),1);};
const newGraph = n => Array.from({length:n}, ()=>[]);
function permute(n) {
    const p=Array.from({length:n},(_,i)=>i);
    for(let i=n-1;i>0;i--){const j=random(i+1);[p[i],p[j]]=[p[j],p[i]];}
    return p;
}
function cycleUnion(n){
    for(;;){
        const g=newGraph(n), p=permute(n);
        for(let i=0;i<n;i++) link(g,i,(i+1)%n);
        if(p.some((v,i)=>has(g,v,p[(i+1)%n]))) continue;
        for(let i=0;i<n;i++) link(g,p[i],p[(i+1)%n]);
        return g;
    }
}
function chainOfOctahedra(n){
    const g=newGraph(n);
    for(let k=0;k<n;k+=6) for(let i=0;i<6;i++) for(let j=i+1;j<6;j++){
        if((i>>1)!==(j>>1)) link(g,k+i,k+j);
    }
    for(let k=6;k<n;k+=6) for(const [a,b,c,d] of [[0,3,0,2],[1,5,1,4]]){
        unlink(g,k-6+a,k-6+b); unlink(g,k+c,k+d);
        link(g,k-6+a,k+d); link(g,k-6+b,k+c);
    }
    return g;
}
function switched(g){
    const out=clone(g);
    for(let tries=0;tries<60;tries++){
        const a=random(g.length), b=g[a][random(g[a].length)];
        const c=random(g.length), d=g[c][random(g[c].length)];
        if(new Set([a,b,c,d]).size!==4 || has(g,a,c) || has(g,b,d)) continue;
        unlink(out,a,b); unlink(out,c,d); link(out,a,c); link(out,b,d);
        return out;
    }
    return out;
}
function removeMatching(g){
    const out=clone(g);
    for(const i of permute(g.length)){
        if(out[i].length!==4 || random(10)>=6) continue;
        const choices=out[i].filter(v=>out[v].length===4);
        if(choices.length) unlink(out,i,choices[random(choices.length)]);
    }
    return out;
}
const bit=Array.from({length:5},(_,i)=>1<<i);
const multiplicities=Array.from({length:32},(_,m)=>m.toString(2).replaceAll("0","").length);
function search(g, cap){
    const phi=Array(g.length).fill(-1);
    let nodes=0;
    function available(v){
        let excluded=0, completed=0;
        for(const u of g[v]){
            if(phi[u]!==-1) excluded|=bit[phi[u]];
            let once=0, twice=0, uncoloured=0;
            for(const x of g[u]){
                if(x===v) continue;
                if(phi[x]===-1){uncoloured++; continue;}
                const mark=bit[phi[x]];
                twice|=once & mark; once|=mark;
            }
            if(uncoloured) continue;
            completed++;
            const singletons=once & ~twice;
            if(singletons && !(singletons & (singletons-1))) excluded|=singletons;
            else if(!singletons) excluded|=once;
        }
        return [31 & ~excluded, completed];
    }
    function descend(left, used){
        if(!left) return true;
        if(++nodes>cap) return null;
        let winner=-1, domain=0, min=6, highest=-1;
        for(let v=0;v<g.length;v++){
            if(phi[v]!==-1) continue;
            const [allowed, completed]=available(v);
            const size=multiplicities[allowed];
            if(!size) return false;
            if(size<min || (size===min && completed>highest)){
                winner=v; domain=allowed; min=size; highest=completed;
            }
        }
        const choices=domain & ((1<<Math.min(5,used+1))-1);
        for(let c=0;c<5;c++){
            if(!(choices & bit[c])) continue;
            phi[winner]=c;
            const result=descend(left-1,Math.max(used,c+1));
            if(result!==false) return result;
        }
        phi[winner]=-1;
        return false;
    }
    const result=descend(g.length,0);
    if(result && !verifyColouring(g,phi,5)) throw new Error("Invalid certificate");
    return {result,nodes};
}

const budget=Number(process.argv[3]??150);
for(const n of [18,24,30,42,60,90,120,180]){
    let best=0, hardest, restricted=0, touched=0;
    for(const kind of ["regular","irregular","octahedra"]){
        let original=kind==="octahedra"?chainOfOctahedra(n):cycleUnion(n);
        let current=original, rating=0;
        for(let trial=0;trial<budget;trial++){
            if(trial%30===0 && kind!=="octahedra") original=cycleUnion(n);
            const start=trial%30===0?original:current;
            const trialGraph=switched(start);
            const graph=kind==="irregular"?removeMatching(trialGraph):trialGraph;
            if(graph.some((row,u)=>row.length<3 || row.length>4 || new Set(row).size!==row.length
                || row.some(v=>u===v || !graph[v].includes(u)))) throw new Error("Invalid graph");
            const {result,nodes}=search(graph,20000);
            if(result===false){console.log(JSON.stringify({counterexample:graph,n,kind,trial,nodes})); process.exitCode=2; break;}
            if(!result) restricted++;
            if(nodes>best){best=nodes;hardest=graph;}
            if(nodes>=rating||random(10)===0||trial%30===0){rating=nodes;current=trialGraph;}
            touched++;
        }
    }
    console.log(JSON.stringify({n,touched,best,restricted,seed:seed>>>0}));
    if(hardest) fs.writeFileSync(`C:/Users/USER/AppData/Local/Temp/pcf-hardest-${n}.json`,JSON.stringify(hardest));
}
