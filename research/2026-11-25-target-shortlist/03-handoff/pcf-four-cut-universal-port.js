"use strict";
const palette=[0,1,2,3,4];
const perm=a=>a.length?a.flatMap((x,i)=>perm(a.filter((_,j)=>i!==j)).map(r=>[x,...r])):[[]];
const permutations=perm(palette);
const pairsets=a=>a.flatMap((x,i)=>a.slice(i+1).map(y=>[x,y]));
const patterns=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[0,1,2]];
const singleton=a=>a.some(c=>a.indexOf(c)===a.lastIndexOf(c));
let tested=0, failures=0, first;
for(const b of patterns){
    const pairs=b.map(c=>{
        const allowed=palette.filter(x=>x!==c);
        return [...allowed.map(x=>[x]),...pairsets(allowed)];
    });
    for(const s0 of pairs[0])for(const s1 of pairs[1])for(const s2 of pairs[2]){
        const s=[s0,s1,s2];
        const possible=permutations.some(pi=>{
            const incoming=b.map(c=>pi[c]);
            if(incoming.some((c,i)=>c===i+1)||!singleton([0,...incoming]))return false;
            return [1,2,3].some(owner=>!incoming.includes(owner)
                &&s.every((pair,i)=>singleton([...pair.map(c=>pi[c]),i+1,owner])));
        });
        tested++;
        if(!possible){failures++;first??=[b,s];}
    }
}
console.log(JSON.stringify({tested,failures,first}));
