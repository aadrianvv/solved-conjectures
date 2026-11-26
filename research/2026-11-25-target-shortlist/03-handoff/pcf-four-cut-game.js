"use strict";
const fs=require("node:fs"),vm=require("node:vm");
const source=fs.readFileSync("C:/Users/USER/AppData/Local/Temp/pcf-four-port-caps.js","utf8");
const {signatures,caps,supported}=vm.runInNewContext(source.slice(0,source.indexOf("\nfor(const [name,extend"))
    +"\n({signatures,caps,supported});");
const bits=Array.from({length:32},(_,x)=>x.toString(2).replaceAll("0","").length);
function glue(a,b){
    const lists=[31,31,31,31,31];
    for(let i=0;i<4;i++){
        lists[b[i]]&=~(1<<a[i]);
        if(a[i+4]!==-1) lists[b[i]]&=~(1<<a[i+4]);
        if(b[i+4]!==-1) lists[b[i+4]]&=~(1<<a[i]);
    }
    if(lists.includes(0))return false;
    lists.sort((a,b)=>bits[a]-bits[b]);
    function visit(i,used){
        if(i===5)return true;
        for(let open=lists[i]&~used;open;open&=open-1)if(visit(i+1,used|(open&-open)))return true;
        return false;
    }
    return visit(0,0);
}
const seen=new Set();
const all=caps(2,9).flatMap(cap=>{
    const accepting=[];
    for(let i=0;i<signatures.length;i++)if(supported(cap,signatures[i]))accepting.push(i);
    const key=accepting.join(",");
    if(seen.has(key))return [];
    seen.add(key);
    return [{cap,accepting}];
});
const memberships=all.map(({accepting})=>new Set(accepting));
const reduced=all.filter(({accepting},i)=>!all.some(x=>x.accepting.length<accepting.length&&x.accepting.every(k=>memberships[i].has(k))));
console.log(JSON.stringify({caps:all.length,reduced:reduced.map(({cap,accepting})=>[cap.e,accepting.length])}));
const used=[...new Set(reduced.flatMap(x=>x.accepting))];
const incomp=Array.from({length:signatures.length},()=>new Uint8Array(signatures.length));
for(let i=0;i<used.length;i++)for(let j=i;j<used.length;j++){
    const a=used[i],b=used[j];
    incomp[a][b]=incomp[b][a]=+(!glue(signatures[a],signatures[b]));
}
console.log(JSON.stringify({stateCount:used.length,stage:"compatibility complete"}));

let alive=new Set(used);
for(;;){
    const previous=alive.size;
    alive=new Set([...alive].filter(a=>reduced.every(({accepting})=>accepting.some(b=>alive.has(b)&&incomp[a][b]))));
    if(alive.size===previous)break;
}
console.log(JSON.stringify({pruned:used.length-alive.size,capSizes:reduced.map(x=>x.accepting.filter(a=>alive.has(a)).length)}));
const clauses=reduced.map(x=>x.accepting.filter(a=>alive.has(a)));
let nodes=0;
function descend(assigned,remaining,opposite){
    if(++nodes>100000)throw new Error("Search budget exhausted");
    if(!remaining.length){
        return {left:assigned.map(i=>signatures[i]),right:[...new Set(opposite.map(x=>x[0]))].map(i=>signatures[i])};
    }
    const options=remaining.map(clause=>clause.filter(a=>opposite.every(row=>row.some(b=>incomp[a][b]))))
        .sort((a,b)=>a.length-b.length);
    for(const a of options[0]){
        const result=descend([...assigned,a],options.slice(1).filter(row=>!row.includes(a)),
            opposite.map(row=>row.filter(b=>incomp[a][b])));
        if(result)return result;
    }
    return null;
}
const obstruction=clauses.some(row=>!row.length)?null:descend([],clauses,clauses);
console.log(JSON.stringify({obstruction,nodes}));
