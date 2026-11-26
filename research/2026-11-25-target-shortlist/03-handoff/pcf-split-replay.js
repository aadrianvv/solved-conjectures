"use strict";
const fs=require("node:fs"), vm=require("node:vm");
const checkPath="C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/check_03_conflict_free_colouring.js";
const checker=fs.readFileSync(checkPath,"utf8");
const {enumerate,bits,verifyColouring}=vm.runInNewContext(checker.slice(0,checker.indexOf("\ncheckExamples();"))
    +"\n({enumerate,bits,verifyColouring});",{process:{argv:[]}});
const scratch=fs.readFileSync("C:/Users/USER/AppData/Local/Temp/pcf-random-csp.js","utf8");
const searchSource=scratch.slice(scratch.indexOf("const bit="),scratch.indexOf("\nconst budget"))
    .replace("excluded|=bit[phi[u]];","excluded|=phi[u]>=3 ? 24 : bit[phi[u]];")
    .replace("const choices=domain & ((1<<Math.min(5,used+1))-1);",String.raw`let allowed=used;
        for(const group of [7,24]){
            const unused=group & ~used;
            allowed|=unused & -unused;
        }
        const choices=domain & allowed;`)
    .replace("Math.max(used,c+1)","used | bit[c]")
    .replace("if(result && !verifyColouring(g,phi,5)) throw new Error(\"Invalid certificate\");",
        "if(result && (!verifyColouring(g,phi,5) || g.some((row,i)=>phi[i]>=3 && row.some(j=>phi[j]>=3)))) throw new Error(\"Invalid certificate\");");
const {search}=vm.runInNewContext(searchSource+"\n({search});",{verifyColouring});
for(let n=5;n<=10;n++){
    let count=0, bad=0, highest=0;
    for(let d=1;d<=n;d++) enumerate(n,d,adjacency=>{
        const g=Array.from(adjacency,bits);
        const {result,nodes}=search(g,100000);
        highest=Math.max(nodes,highest);
        count++;
        if(result===null) throw new Error("Node limit reached");
        if(!result && ++bad===1) console.log(JSON.stringify({firstFailure:n,d,g,nodes}));
    });
    console.log(JSON.stringify({n,count,bad,highest}));
}
