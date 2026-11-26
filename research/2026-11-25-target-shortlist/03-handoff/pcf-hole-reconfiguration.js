"use strict";
const fs=require("node:fs"),vm=require("node:vm");
const filepath="C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/check_03_conflict_free_colouring.js";
const source=fs.readFileSync(filepath,"utf8");
const {enumerate,bits}=vm.runInNewContext(source.slice(0,source.indexOf("\ncheckExamples();"))+"\n({enumerate,bits});",{process:{argv:[]}});
const palette=[0,1,2,3,4];
function canon(colours){
    const map=new Map();
    return colours.map(c=>{
        if(c<0)return -1;
        if(!map.has(c))map.set(c,map.size);
        return map.get(c);
    });
}
function valid(g,c,hole){
    return g.every((neighbours,i)=>{
        if(i===hole)return true;
        if(neighbours.some(j=>c[j]===c[i]))return false;
        if(neighbours.includes(hole)||!neighbours.length)return true;
        const old=neighbours.map(j=>c[j]);
        return old.some(c=>old.indexOf(c)===old.lastIndexOf(c));
    });
}
function states(g){
    const seen=new Set();
    for(let hole=0;hole<g.length;hole++){
        const c=Array(g.length).fill(-1);
        function visit(i,used){
            if(i===g.length){
                if(valid(g,c,hole))seen.add(c.join(","));
                return;
            }
            if(i===hole){visit(i+1,used);return;}
            for(let colour=0;colour<=Math.min(4,used);colour++){
                if(g[i].some(j=>j<i&&c[j]===colour))continue;
                c[i]=colour;
                visit(i+1,Math.max(used,colour+1));
            }
        }
        visit(0,0);
    }
    return seen;
}
function classify(g,rad){
    const distance=g.map((row,h)=>rad===1?row:[...new Set(row.flatMap(v=>[v,...g[v]]))].filter(v=>v!==h));
    const pending=states(g), total=pending.size;
    let components=0, dead=0, smallest=Infinity, badExample;
    while(pending.size){
        components++;
        const key=pending.values().next().value;
        const queue=[key.split(",").map(Number)];
        pending.delete(key);
        let fixed=false;
        for(let q=0;q<queue.length;q++){
            const current=queue[q];
            const h=current.indexOf(-1);
            for(const p of palette){
                const c=[...current];c[h]=p;
                if(valid(g,c,-1))fixed=true;
                for(const next of distance[h]){
                    const candidate=[...c];candidate[next]=-1;
                    if(!valid(g,candidate,next))continue;
                    const normalized=canon(candidate);
                    if(pending.delete(normalized.join(",")))queue.push(normalized);
                }
            }
        }
        if(!fixed){
            dead++;
            smallest=Math.min(smallest,queue.length);
            badExample??=queue[0];
        }
    }
    return {total,components,dead,smallest,badExample};
}
const radius=Number(process.argv[2]??1);
const maxOrder=Number(process.argv[3]??8);
for(let n=6;n<=maxOrder;n++){
    let checked=0, failed=0, example, allStates=0;
    enumerate(n,n,adj=>{
        const graph=Array.from(adj,bits);
        const outcome=classify(graph,radius);
        checked++;
        allStates+=outcome.total;
        if(outcome.dead){failed++;example??={graph,...outcome};}
    });
    console.log(JSON.stringify({n,radius,checked,failed,allStates,example}));
}
