import http from 'node:http';
import {readFile} from 'node:fs/promises';
import {resolve, extname, sep} from 'node:path';
const root=resolve(process.argv[2] || '.');
http.createServer(async(req,res)=>{try{const p=resolve(root,'.'+decodeURIComponent(new URL(req.url,'http://localhost').pathname));if(p!==root&&!p.startsWith(root+sep))throw Error();const file=p===root?p+'/index.html':p;const data=await readFile(file);res.setHeader('Content-Type',({'.html':'text/html','.css':'text/css','.mjs':'text/javascript','.json':'application/json'})[extname(file)]||'application/octet-stream');res.end(data);}catch{res.writeHead(404);res.end('Not found');}}).listen(4182,'127.0.0.1',()=>console.log('http://127.0.0.1:4182'));
