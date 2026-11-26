"use strict";
const fs=require("node:fs"), vm=require("node:vm");
const program=fs.readFileSync("C:/Users/USER/AppData/Local/Temp/pcf-random-csp.js","utf8");
const {search,newGraph,link,unlink,random}=vm.runInNewContext(program.slice(0,program.indexOf("\nconst budget"))
    +"\n({search,newGraph,link,unlink,random});",{require,process:{argv:[]}});
const reference="C:/Users/USER/Desktop/slopdrop/solved-conjectures-latest/.claude/worktrees/repo-sync-prioritize-e9099d/research/2026-11-25-target-shortlist/check_03_conflict_free_colouring.js";
const source=fs.readFileSync(reference,"utf8");
const {enumerate,bits}=vm.runInNewContext(source.slice(0,source.indexOf("\ncheckExamples();"))+"\n({enumerate,bits});",{process:{argv:[]}});

const modules=[];
for(let n=6;n<=8;n++){
    enumerate(n,n,adj=>{
        const base=Array.from(adj,bits);
        const edges=base.flatMap((row,i)=>row.filter(j=>i<j).map(j=>[i,j]));
        for(let a=0;a<Math.min(4,edges.length);a++){
            for(let b=a+1;b<Math.min(a+5,edges.length);b++){
                const graph=[...base.map(row=>[...row]),[],[]];
                for(const [i,e] of [[0,edges[a]],[1,edges[b]]]){
                    const [u,v]=e;
                    unlink(graph,u,v);
                    link(graph,u,n+i);link(graph,v,n+i);
                }
                modules.push(graph);
            }
        }
    });
}
function assemble(input, twists){
    const offsets=[];
    const size=input.reduce((total,graph)=>{offsets.push(total);return total+graph.length;},0);
    const graph=newGraph(size);
    const ports=input.map((g,i)=>[offsets[i]+g.length-2,offsets[i]+g.length-1]);
    for(let i=0;i<input.length;i++){
        const g=input[i];
        for(let v=0;v<g.length;v++)for(const w of g[v])if(v<w)link(graph,offsets[i]+v,offsets[i]+w);
    }
    if(input.length===2){
        for(const u of ports[0])for(const v of ports[1])link(graph,u,v);
    }else{
        for(let i=0;i<input.length;i++){
            const j=(i+1)%input.length;
            link(graph,ports[i][0],ports[j][twists[i]]);
            link(graph,ports[i][1],ports[j][1^twists[i]]);
        }
    }
    if(graph.some((row,v)=>row.length!==4||new Set(row).size!==4||row.some(u=>u===v||!graph[u].includes(v))))throw new Error("Invalid degree");
    return graph;
}
let checked=0, maximum=0, timeouts=0;
function test(graph,context){
    const r=search(graph,30000);
    maximum=Math.max(maximum,r.nodes);
    if(r.result===false){
        console.log(JSON.stringify({counterexample:graph,context,nodes:r.nodes}));
        process.exit(2);
    }
    if(r.result===null)timeouts++;
    checked++;
}
for(let i=0;i<modules.length;i++){
    const mod=modules[i];
    const partner=modules[random(modules.length)];
    test(assemble([mod,partner],[]),{mode:"bond",i});
    for(const length of [3,4,5,7]){
        for(const twist of [0,1]){
            test(assemble(Array.from({length},()=>mod),[twist,...Array(length-1).fill(0)]),{mode:"identical",i,length,twist});
        }
    }
}
for(let i=0;i<900;i++){
    const length=3+random(13);
    const input=Array.from({length},()=>modules[random(modules.length)]);
    const twists=Array.from({length},()=>random(2));
    test(assemble(input,twists),{mode:"mixed",i,length,twists});
}
console.log(JSON.stringify({modules:modules.length,checked,maximum,timeouts}));
