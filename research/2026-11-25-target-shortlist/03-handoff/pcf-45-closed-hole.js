"use strict";
const fs=require("node:fs"),vm=require("node:vm");
const src=fs.readFileSync("C:/Users/USER/AppData/Local/Temp/pcf-random-csp.js","utf8");
const prefix=src.slice(0,src.indexOf("\nconst budget")).replace("return {result,nodes};","return {result,nodes,phi};");
const {newGraph,link,search}=vm.runInNewContext(prefix+"\n({newGraph,link,search});",{require,process:{argv:[]}});
const G=newGraph(45);
const idx=(branch,layer,i)=>5+20*branch+5*layer+i%5;
for(let i=0;i<5;i++){
    link(G,i,(i+1)%5);
    for(let r=0;r<2;r++){
        link(G,i,idx(r,0,i));
        link(G,idx(r,1,i),idx(r,2,i));
        for(let shift=0;shift<3;shift++){
            link(G,idx(r,0,i),idx(r,1,i+shift));
            link(G,idx(r,2,i),idx(r,3,i+shift));
        }
    }
    link(G,idx(0,3,i),idx(1,3,i));
}
const blocked=(v,deleted)=>deleted.includes(v);
function connected(deleted){
    const first=G.findIndex((_,i)=>!blocked(i,deleted));
    const touched=new Set([first]), queue=[first];
    for(let i=0;i<queue.length;i++)for(const v of G[queue[i]]){
        if(blocked(v,deleted)||touched.has(v))continue;
        touched.add(v);queue.push(v);
    }
    return touched.size===45-deleted.length;
}
let connectivityPairs=0;
for(let i=0;i<45;i++){
    if(G[i].length!==4||G[i].some(v=>G[v].some(w=>G[i].includes(w))))throw new Error("Graph not quartic and triangle-free");
    for(let j=i+1;j<45;j++){
        if(!connected([i,j]))throw new Error("Two-vertex cut");
        connectivityPairs++;
    }
}
const full=search(G,1000000);
console.log(JSON.stringify({connectivityPairs,full}));
