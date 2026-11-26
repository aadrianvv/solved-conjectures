"use strict";
const fs=require("node:fs"),vm=require("node:vm");
const program=fs.readFileSync("C:/Users/USER/AppData/Local/Temp/pcf-random-csp.js","utf8");
const prefix=program.slice(0,program.indexOf("\nconst budget"));
const {search,newGraph,link,permute}=vm.runInNewContext(prefix+"\n({search,newGraph,link,permute});",{require,process:{argv:[]}});
const modified=prefix
    .replace("return [31 & ~excluded, completed];","return [(v<g.length/2 ? 29 : 30) & ~excluded, completed];")
    .replace("const choices=domain & ((1<<Math.min(5,used+1))-1);",`const fresh=28 & ~used;
        const choices=domain & (3 | used | (fresh & -fresh));`)
    .replace("Math.max(used,c+1)","used | bit[c]")
    .replace("if(result && !verifyColouring(g,phi,5))","if(result && (!verifyColouring(g,phi,5)||phi.some((c,i)=>c===(i<g.length/2?1:0))))");
const {search:restricted}=vm.runInNewContext(modified+"\n({search});",{require,process:{argv:[]}});
function randomBipartite(m){
    const g=newGraph(2*m);
    for(let k=0;k<4;k++){
        for(;;){
            const permutation=permute(m);
            if(permutation.some((j,i)=>g[i].includes(m+j)))continue;
            for(let i=0;i<m;i++)link(g,i,m+permutation[i]);
            break;
        }
    }
    return g;
}
const toIndex=n=>31-Math.clz32(n);
const indices=mask=>{
    const result=[];
    while(mask){const half=mask&-mask;result.push(toIndex(half));mask^=half;}
    return result;
};
function enumerate(m, visit){
    const options=[];
    for(let mask=15;mask<1<<m;mask++)if(indices(mask).length===4)options.push(mask);
    const rows=[15],residual=Array(m).fill(4);
    for(const j of [0,1,2,3])residual[j]--;
    function recur(start){
        const remaining=m-rows.length;
        if(residual.some(x=>x>remaining))return;
        if(!remaining){
            const g=newGraph(2*m);
            rows.forEach((mask,i)=>indices(mask).forEach(j=>link(g,i,m+j)));
            visit(g);
            return;
        }
        for(let i=start;i<options.length;i++){
            const neighbours=indices(options[i]);
            if(neighbours.some(j=>residual[j]<1))continue;
            neighbours.forEach(j=>residual[j]--);
            rows.push(options[i]);recur(i);rows.pop();
            neighbours.forEach(j=>residual[j]++);
        }
    }
    recur(0);
}
for(const m of [4,5,6,7,8,9,12,18,30,50]){
    let checked=0, max=0,timeouts=0;
    function verify(g){
        let r=restricted(g,40000);
        if(r.result===null){
            console.log(JSON.stringify({retry:m,index:checked}));
            r=restricted(g,1000000);
        }
        checked++;max=Math.max(max,r.nodes);
        if(r.result===null)timeouts++;
        if(r.result===false){
            console.log(JSON.stringify({failed:g,ordinary:search(g,3000000),nodes:r.nodes}));
            process.exit(2);
        }
    }
    if(m<=7)enumerate(m,verify);
    else for(let i=0;i<300;i++)verify(randomBipartite(m));
    console.log(JSON.stringify({m,checked,max,timeouts,scope:m<=7?"labelled cover":"random"}));
}
