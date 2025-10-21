const state = { level:'materie', materiaId:null, argomentoId:null, fileId:null, manage:false, data:null };
const COLORS = ['#3b82f6','#ef4444','#10b981','#f59e0b','#8b5cf6','#ec4899','#06b6d4','#84cc16'];

const $ = (s,e=document)=>e.querySelector(s);
const $$ = (s,e=document)=>[...e.querySelectorAll(s)];

const listContainer = $('#listContainer');
const editorView = $('#editorView');
const listsView = $('#listsView');
const pageTitle = $('#pageTitle');
const breadcrumbs = $('#breadcrumbs');
const fileMeta = $('#fileMeta');
const editor = $('#editor');
const modalWrap = $('#modalWrap');
const modalTitle = $('#modalTitle');
const modalName = $('#modalName');
const colorChoices = $('#colorChoices');
const btnCancel = $('#btnCancel');
const btnConfirm = $('#btnConfirm');
const fab = $('#fab');

let modalCtx = null;

// ------------------- API -------------------
async function loadData(){
  try {
    const res = await fetch('/api/data');
    state.data = await res.json();
  } catch(e){ state.data = {materie:[]}; }
}
async function saveData(){
  await fetch('/api/data',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(state.data)});
}

// ------------------- Utils -------------------
function uid(){ return Math.random().toString(36).slice(2,9); }
function now(){ return Date.now(); }
function escapeHtml(s=''){ return s.replace(/[&<>"']/g,m=>({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }
function flash(text){
  const t=document.createElement('div'); t.textContent=text; t.className='flash'; document.body.appendChild(t);
  setTimeout(()=>t.remove(),1200);
}

// ------------------- CRUD -------------------
function currentMateria(){ return state.data.materie.find(m=>m.id===state.materiaId); }
function currentArgomento(){ return currentMateria()?.argomenti?.find(a=>a.id===state.argomentoId); }
function getCurrentFile(){ return currentArgomento()?.files?.find(f=>f.id===state.fileId); }

function addMateria({nome,colore}){ 
  state.data.materie.push({id:uid(),nome,colore,createdAt:now(),argomenti:[]}); 
  saveData(); render(); 
}
function addArgomento({nome,colore}){
  const m=currentMateria(); if(!m) return; m.argomenti??=[]; m.argomenti.push({id:uid(),nome,colore,createdAt:now(),files:[]}); 
  saveData(); render();
}
function addFile({nome,colore}){
  const a=currentArgomento(); if(!a) return; a.files??=[]; a.files.push({id:uid(),nome,colore,createdAt:now(),contenuto:'',lastSaved:null});
  saveData(); render();
}
function updateObj(type,id,patch){
  let obj=null;
  if(type==='materia') obj=state.data.materie.find(x=>x.id===id);
  if(type==='argomento') obj=currentMateria()?.argomenti?.find(x=>x.id===id);
  if(type==='file') obj=currentArgomento()?.files?.find(x=>x.id===id);
  if(obj) Object.assign(obj,patch);
  saveData(); render();
}

// ------------------- Render -------------------
function render(){
  document.body.classList.toggle('manage',state.manage);
  renderBreadcrumbs();
  if(state.level==='editor'){
    listsView.style.display='none'; editorView.style.display='block';
    const f=getCurrentFile();
    pageTitle.textContent=f?.nome||'Editor';
    fileMeta.textContent = f?.lastSaved ? 'Ultimo salvataggio: '+new Date(f.lastSaved).toLocaleString():'Mai';
    editor.innerHTML = f?.contenuto||'';
    return;
  }
  editorView.style.display='none'; listsView.style.display='block';
  if(state.level==='materie') renderList(state.data.materie,'materia');
  else if(state.level==='argomenti') renderList(currentMateria()?.argomenti||[],'argomento');
  else if(state.level==='files') renderList(currentArgomento()?.files||[],'file');
}

function renderBreadcrumbs(){
  const parts = [`<a href="#" data-nav="materie">Materie</a>`];
  if(state.level!=='materie' && state.materiaId) parts.push(` › <a href="#" data-nav="argomenti">${escapeHtml(currentMateria()?.nome||'')}</a>`);
  if(state.level==='files' || state.level==='editor') parts.push(` › <a href="#" data-nav="files">${escapeHtml(currentArgomento()?.nome||'')}</a>`);
  if(state.level==='editor') parts.push(` › <span>${escapeHtml(getCurrentFile()?.nome||'')}</span>`);
  breadcrumbs.innerHTML = parts.join(' ');
  $$('a[data-nav]', breadcrumbs).forEach(a=>{
    a.onclick=e=>{ e.preventDefault(); const go=a.dataset.nav;
      if(go==='materie'){ state.level='materie'; state.materiaId=null; state.argomentoId=null; state.fileId=null; }
      if(go==='argomenti'){ state.level='argomenti'; state.argomentoId=null; state.fileId=null; }
      if(go==='files'){ state.level='files'; state.fileId=null; }
      render();
    }
  });
}

function renderList(arr,type){
  listContainer.innerHTML='';
  if(!arr.length){ listContainer.innerHTML='<div class="muted">Nessun elemento. Usa il + in basso.</div>'; return; }
  arr.forEach(obj=>{
    const el=document.createElement('div'); el.className='item clickable';
    el.innerHTML=`<div class="left"><span class="color-dot" style="background:${obj.colore||'#94a3b8'}"></span><div><div class="name">${escapeHtml(obj.nome)}</div></div></div>`;
    el.querySelector('.left').onclick=()=>{
      if(type==='materia'){ state.level='argomenti'; state.materiaId=obj.id; }
      if(type==='argomento'){ state.level='files'; state.argomentoId=obj.id; }
      if(type==='file'){ state.level='editor'; state.fileId=obj.id; }
      render();
    };
    listContainer.appendChild(el);
  });
}

// ------------------- Modal -------------------
function openModal(mode,type,target=null){
  modalCtx={mode,type,target};
  modalTitle.textContent=(mode==='create'?'Nuovo ':'Modifica ')+type;
  modalName.value=target?.nome||'';
  modalWrap.style.display='flex';
}
function closeModal(){ modalWrap.style.display='none'; }

btnCancel.onclick=closeModal;
btnConfirm.onclick=()=>{
  const nome=modalName.value.trim(); if(!nome){ alert('Inserisci un nome'); return; }
  if(modalCtx.mode==='create'){
    if(modalCtx.type==='materia') addMateria({nome,colore:'#3b82f6'});
    if(modalCtx.type==='argomento') addArgomento({nome,colore:'#10b981'});
    if(modalCtx.type==='file') addFile({nome,colore:'#f59e0b'});
  } else updateObj(modalCtx.type,modalCtx.target.id,{nome});
  closeModal();
};

// ------------------- Eventi UI -------------------
$('#btnManage').onclick=()=>{ state.manage=!state.manage; render(); };
fab.onclick=()=>{ openModal('create',state.level==='materie'?'materia':state.level==='argomenti'?'argomento':'file'); };

// Editor base
$('#tbBold').onclick=()=>document.execCommand('bold');
$('#tbUndo').onclick=()=>document.execCommand('undo');
$('#tbRedo').onclick=()=>document.execCommand('redo');
$('#tbColor').oninput=e=>document.execCommand('foreColor',false,e.target.value);
$('#tbSize').onchange=e=>document.execCommand('formatBlock',false,e.target.value);

// Salvataggio editor
$('#tbSave').onclick=()=>{
  const f=getCurrentFile(); if(!f) return;
  f.contenuto=editor.innerHTML; f.lastSaved=now();
  saveData(); fileMeta.textContent='Ultimo salvataggio: '+new Date(f.lastSaved).toLocaleString();
  flash('Salvato!');
};

// ------------------- Boot -------------------
window.addEventListener('DOMContentLoaded', async ()=>{
  await loadData();
  render();
});
