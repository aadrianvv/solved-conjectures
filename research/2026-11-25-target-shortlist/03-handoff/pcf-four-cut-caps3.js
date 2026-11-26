"use strict";
const fs=require("node:fs"),vm=require("node:vm");
const source=fs.readFileSync("C:/Users/USER/AppData/Local/Temp/pcf-four-port-caps.js","utf8");
const {caps,supported}=vm.runInNewContext(source.slice(0,source.indexOf("\nfor(const [name,extend"))
    +"\n({caps,supported});");
const left=[[0,0,1,1,-1,2,2,2],[0,1,0,2,2,2,1,-1]];
const right=[[0,1,0,2,1,2,2,1],[0,1,2,3,3,2,1,2],[0,1,0,2,2,2,1,-1]];
const range=n=>Array.from({length:n},(_,i)=>i);
const pairs=indices=>indices.flatMap((u,i)=>indices.slice(i+1).map(v=>[u,v]));
const subsets=edges=>range(1<<edges.length).map(mask=>edges.filter((_,i)=>mask&(1<<i)));
function* generate(extra){
    const outside=range(extra).map(u=>u+4);
    for(const direct of caps(0,9)){
        for(const inner of subsets(pairs(outside))){
            const available=range(4).filter(i=>!direct.adj[i].length);
            function* fill(at, edges){
                if(at===available.length){
                    const e=[...edges,...direct.e,...inner];
                    const adj=Array.from({length:4+extra},()=>[]);
                    for(const [u,v] of e){adj[u].push(v);adj[v].push(u);}
                    if(outside.some(v=>!adj[v].length||adj[v].length>4))return;
                    yield {extra,e,adj};
                    return;
                }
                yield* fill(at+1,edges);
                for(const v of outside)yield* fill(at+1,[...edges,[available[at],v]]);
            }
            yield* fill(0,[]);
        }
    }
}
for(const extra of [3,4]){
    let tested=0, excludeLeft=0, excludeRight=0, exampleL,exampleR;
    for(const cap of generate(extra)){
        tested++;
        if(left.every(s=>!supported(cap,s))){excludeLeft++;exampleL??=cap.e;}
        if(right.every(s=>!supported(cap,s))){excludeRight++;exampleR??=cap.e;}
    }
    console.log(JSON.stringify({extra,tested,excludeLeft,excludeRight,exampleL,exampleR}));
}
