"use strict";
const palette=[0,1,2,3,4];
const signatures=[];
const unique=a=>a.some(c=>a.indexOf(c)===a.lastIndexOf(c));
const pairs=n=>Array.from({length:n},(_,i)=>Array.from({length:n-i-1},(_,j)=>[i,i+j+1])).flat();
function generate(values,used){
    const i=values.length;
    if(i===8){signatures.push(values);return;}
    if(i>=4) generate([...values,-1],used);
    for(let c=0;c<=Math.min(4,used);c++){
        if(i>=4 && c===values[i-4]) continue;
        generate([...values,c],Math.max(used,c+1));
    }
}
generate([],0);
const accept=(s,i,c)=>s[i]!==c&&s[i+4]!==c;
function extendsStar(s){
    return unique(s.slice(0,4)) && palette.some(c=>[0,1,2,3].every(i=>accept(s,i,c)));
}
function extendsAdjacentCubics(s){
    return palette.some(c=>accept(s,0,c)&&accept(s,1,c)&&palette.some(d=>
        c!==d&&accept(s,2,d)&&accept(s,3,d)&&unique([s[0],s[1],d])&&unique([s[2],s[3],c])));
}
function caps(maxExtra,maxEdges){
    const out=[];
    for(let extra=0;extra<=maxExtra;extra++){
        const edges=pairs(4+extra);
        for(let mask=0;mask<1<<edges.length;mask++){
            const e=edges.filter((_,i)=>mask&(1<<i));
            if(extra===maxExtra&&e.length>maxEdges) continue;
            const adj=Array.from({length:4+extra},()=>[]);
            for(const [u,v] of e){adj[u].push(v);adj[v].push(u);}
            if(adj.some((row,i)=>i<4?row.length>1:row.length>4||row.length===0))continue;
            out.push({extra,e,adj});
        }
    }
    return out;
}
function supported(cap,s){
    function finish(c){
        if(c.length!==cap.adj.length) return palette.some(colour=>finish([...c,colour]));
        for(const [u,v] of cap.e){
            if(u<4&&!accept(s,u,c[v]))return false;
            if(v<4&&!accept(s,v,c[u]))return false;
            if(c[u]===c[v])return false;
        }
        return cap.adj.every((row,i)=>i<4||unique(row.map(j=>c[j])));
    }
    return finish(s.slice(0,4));
}
for(const [name,extend,maxExtra,maxEdges] of [["star",extendsStar,1,3],["adjacent cubics",extendsAdjacentCubics,2,4]]){
    const bad=signatures.filter(s=>!extend(s));
    const all=caps(maxExtra,maxEdges);
    const comparison=all.map(cap=>{
        const examples=bad.filter(s=>supported(cap,s));
        return {extra:cap.extra,edges:cap.e,failures:examples.length,first:examples[0]};
    }).sort((a,b)=>a.failures-b.failures);
    console.log(JSON.stringify({name,states:signatures.length,bad:bad.length,caps:all.length,best:comparison.slice(0,6)}));
}
