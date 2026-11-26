"use strict";
const fs=require("node:fs"), vm=require("node:vm");
const p="C:/Users/USER/AppData/Local/Temp/pcf-random-csp.js";
const script=fs.readFileSync(p,"utf8");
const prefix=script.slice(0,script.indexOf("\nconst budget"));
const {search, newGraph, link}=vm.runInNewContext(prefix.replace("return {result,nodes};","return {result,nodes,phi};")
    +"\n({search,newGraph,link});",{require,process:{argv:[]}});
const vertices=newGraph(14);
for(let points=1;points<=7;points++) for(let lines=1;lines<=7;lines++){
    let mask=points&lines, parity=0;
    while(mask){mask &= mask-1; parity ^=1;}
    if(parity) link(vertices,points-1,lines+6);
}
console.log(JSON.stringify({vertices,...search(vertices,10000000)}));
