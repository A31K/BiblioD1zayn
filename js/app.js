
const categoryLabels = {
  all:'Все', small:'Маленькое помещение', large:'Большая библиотека', quiet:'Тихое чтение', events:'Мероприятия', family:'Семейная', youth:'Молодёжь', adult:'Взрослые', kids:'Детская', lowcost:'Недорогой'
};

function $(selector, parent=document){return parent.querySelector(selector)}
function $all(selector, parent=document){return [...parent.querySelectorAll(selector)]}

function getCustomDesigns(){
  try{return JSON.parse(localStorage.getItem('bibliodesign_custom') || '[]')}catch(e){return []}
}
function saveCustomDesign(item){
  const items = getCustomDesigns();
  items.unshift(item);
  localStorage.setItem('bibliodesign_custom', JSON.stringify(items));
}
function allDesigns(){return [...DESIGN_DATA, ...getCustomDesigns()]}
function imagePath(item){return item.customImage || `images/${item.image}`}
function tagText(tags){return (tags||[]).map(t=>categoryLabels[t]||t).join(' · ')}
function shortText(text, limit=170){return text.length>limit ? text.slice(0,limit).trim()+'…' : text}
function showToast(text){
  let toast = $('.toast');
  if(!toast){toast=document.createElement('div');toast.className='toast';document.body.appendChild(toast)}
  toast.textContent=text;toast.classList.add('show');
  setTimeout(()=>toast.classList.remove('show'), 2500);
}
function initMenu(){
  const btn=$('.mobile-toggle'); const menu=$('.menu');
  if(btn && menu){btn.addEventListener('click',()=>menu.classList.toggle('open'))}
}
function setActiveNav(){
  const page=document.body.dataset.page;
  $all('.menu a').forEach(a=>{ if(a.dataset.nav===page) a.classList.add('active') });
}
function renderDesignCard(item){
  const extraBudget = item.budget ? `<span class=\"tag tag-budget\">Бюджет: ${item.budget}</span>` : '';
  const tags=(item.category||[]).slice(0,3).map(t=>`<span class="tag">${categoryLabels[t]||t}</span>`).join('') + extraBudget;
  return `<article class="card" data-categories="${(item.category||[]).join(' ')}" data-title="${item.title.toLowerCase()}" data-text="${(item.description+' '+item.tagline+' '+item.palette+' '+(item.whyFit||'')+' '+(item.budget||'')).toLowerCase()}">
    <a class="card-image" href="design.html?id=${encodeURIComponent(item.id)}"><img src="${imagePath(item)}" alt="${item.title}"></a>
    <div class="card-content">
      <div class="tags">${tags}</div>
      <h3>${item.title}</h3>
      <p><b>${item.tagline}</b></p>
      <p>${shortText(item.description)}</p>
      <div class="card-actions"><a class="btn secondary" href="design.html?id=${encodeURIComponent(item.id)}">Подробнее</a></div>
    </div>
  </article>`
}
function renderCatalog(){
  const grid=$('#designGrid'); if(!grid) return;
  const designs=allDesigns();
  grid.innerHTML=designs.map(renderDesignCard).join('');
  const buttons=$all('.filter-btn');
  const search=$('#searchInput');
  let active='all';
  function apply(){
    const q=(search?.value||'').trim().toLowerCase();
    let visible=0;
    $all('.card', grid).forEach(card=>{
      const cats=(card.dataset.categories||'').split(' ');
      const matchCat=active==='all'||cats.includes(active);
      const matchText=!q || (card.dataset.title+' '+card.dataset.text).includes(q);
      const show=matchCat&&matchText;
      card.style.display=show?'flex':'none'; if(show) visible++;
    });
    const empty=$('#emptyCatalog'); if(empty) empty.style.display=visible?'none':'block';
  }
  buttons.forEach(btn=>btn.addEventListener('click',()=>{buttons.forEach(b=>b.classList.remove('active'));btn.classList.add('active');active=btn.dataset.filter;apply()}));
  if(search) search.addEventListener('input',apply);
  apply();
}
function renderFeatured(){
  const grid=$('#featuredGrid'); if(!grid) return;
  grid.innerHTML=DESIGN_DATA.slice(0,3).map(renderDesignCard).join('');
}
function renderGallery(){
  const grid=$('#galleryGrid'); if(!grid) return;
  grid.innerHTML=allDesigns().map(item=>`<a href="design.html?id=${encodeURIComponent(item.id)}" title="${item.title}"><img src="${imagePath(item)}" alt="${item.title}"></a>`).join('');
}
function renderDetail(){
  const root=$('#detailRoot'); if(!root) return;
  const id=new URLSearchParams(location.search).get('id') || DESIGN_DATA[0].id;
  const item=allDesigns().find(d=>d.id===id) || DESIGN_DATA[0];
  document.title = item.title + ' — БиблиоДизайн';
  const furniture = (item.furnitureList||['стеллажи','столы','стулья','светильники','декор']).map(t=>`<li>${t}</li>`).join('');
  const steps = (item.implementationSteps||['Измерить помещение и определить зоны.','Разместить стеллажи и рабочие места.','Подобрать цветовую основу и материалы.','Проверить удобство проходов и освещения.']).map((t,i)=>`<li><b>${i+1}.</b> ${t}</li>`).join('');
  const planImg = item.planImage || 'plans/plan-practical-library.svg';
  const drawingImg = item.drawingImage || 'plans/drawing-practical-library.svg';
  root.innerHTML=`<div class="page-title"><div class="wrapper"><div class="breadcrumb"><a href="designs.html">Каталог дизайнов</a> / ${item.title}</div><h1>${item.title}</h1><p class="lead">${item.tagline}</p></div></div>
  <section class="section"><div class="wrapper detail-grid">
    <div class="detail-image"><img src="${imagePath(item)}" alt="${item.title}"></div>
    <div class="detail-panel">
      <div class="tags">${(item.category||[]).map(t=>`<span class="tag">${categoryLabels[t]||t}</span>`).join('')}${item.budget?`<span class="tag tag-budget">Бюджет: ${item.budget}</span>`:''}</div>
      <h2>Описание решения</h2>
      <p>${item.description}</p>
      <div class="info-grid">
        <div class="info-box"><b>Для кого подходит</b>${item.audience}</div>
        <div class="info-box"><b>Тип помещения</b>${item.space}</div>
        <div class="info-box"><b>Палитра</b>${item.palette}</div>
        <div class="info-box"><b>Материалы</b>${item.materials}</div>
        <div class="info-box"><b>Уровень бюджета</b>${item.budget || 'не указан'}</div>
        <div class="info-box"><b>Почему этот вариант подойдёт</b>${item.whyFit || item.description}</div>
      </div>
    </div>
  </div></section>
  <section class="section"><div class="wrapper"><div class="section-head"><div><h2>План и чертёж</h2><p class="section-text">Схемы помогают понять примерную расстановку мебели и зон. Это наглядный ориентир, который можно адаптировать под размеры своего помещения.</p></div></div>
    <div class="scheme-grid">
      <article class="scheme-card"><h3>План помещения</h3><img src="${planImg}" alt="План помещения — ${item.title}"><p>${item.planDescription || ''}</p></article>
      <article class="scheme-card"><h3>Чертёж / развёртка стены</h3><img src="${drawingImg}" alt="Чертёж дизайна — ${item.title}"><p>Развёртка показывает, как можно расположить стеллажи, рабочую поверхность, посадочные места и свет. По ней человеку проще представить, какие элементы нужны для воплощения дизайна.</p></article>
    </div>
  </div></section>
  <section class="section"><div class="wrapper detail-grid">
    <div class="detail-panel"><h2>Почему используются эти цвета</h2><p>${item.colorReason || ''}</p><h3 style="margin-top:28px">Почему выбраны эти материалы</h3><p>${item.materialReason || ''}</p></div>
    <div class="detail-panel"><h2>Что понадобится</h2><ul>${furniture}</ul><h3 style="margin-top:28px">Что важно предусмотреть</h3><ul>${(item.tips||[]).map(t=>`<li>${t}</li>`).join('')}</ul></div>
  </div></section>
  <section class="section"><div class="wrapper"><div class="detail-panel"><h2>Пошаговый план воплощения</h2><ol class="steps-list">${steps}</ol><div class="hero-actions"><a class="btn" href="constructor.html">Подобрать похожий стиль</a><a class="btn secondary" href="designs.html">Вернуться в каталог</a></div></div></div></section>`;
}
function renderConstructor(){
  const form=$('#pickForm'); const result=$('#pickResult'); if(!form||!result) return;
  form.addEventListener('submit',(e)=>{
    e.preventDefault();
    const fd=new FormData(form);
    const answers=[fd.get('space'),fd.get('audience'),fd.get('task')].filter(Boolean);
    const scored=allDesigns().map(d=>{
      let score=0; const cats=d.category||[];
      answers.forEach(a=>{ if(cats.includes(a)) score+=3; if((d.description+d.title+d.tagline+d.audience+d.space).toLowerCase().includes(String(a))) score+=1; });
      return {d,score};
    }).sort((a,b)=>b.score-a.score).slice(0,3).map(x=>x.d);
    result.innerHTML = scored.length ? scored.map(renderDesignCard).join('') : '<div class="empty">Пока нет подходящих вариантов. Попробуйте изменить параметры.</div>';
    result.scrollIntoView({behavior:'smooth', block:'start'});
  });
}
function initAddForm(){
  const form=$('#addDesignForm'); if(!form) return;
  const preview=$('#imagePreview'); const file=$('#imageFile');
  let customImage='';
  if(file){
    file.addEventListener('change',()=>{
      const f=file.files && file.files[0]; if(!f) return;
      const reader=new FileReader();
      reader.onload=()=>{customImage=reader.result; if(preview){preview.src=customImage; preview.style.display='block';}};
      reader.readAsDataURL(f);
    });
  }
  form.addEventListener('submit',(e)=>{
    e.preventDefault();
    const fd=new FormData(form);
    const cats=[fd.get('space'),fd.get('audience'),fd.get('task')].filter(Boolean);
    const now=Date.now();
    const item={
      id:'custom-'+now,
      title:fd.get('title')||'Мой дизайн библиотеки',
      tagline:fd.get('tagline')||'Пользовательский вариант оформления',
      category:cats.length?cats:['small'],
      audience:fd.get('audienceText')||'посетители библиотеки',
      space:fd.get('spaceText')||'помещение библиотеки',
      palette:fd.get('palette')||'белый, зелёный, натуральные оттенки',
      materials:fd.get('materials')||'материалы не указаны',
      zones:fd.get('zones')||'зоны не указаны',
      description:fd.get('description')||'Описание не указано.',
      tips:(fd.get('tips')||'').split('\n').map(s=>s.trim()).filter(Boolean),
      image:'eco-reading.png',
      customImage:customImage || ''
    };
    saveCustomDesign(item);
    showToast('Дизайн добавлен и сохранён в этом браузере');
    setTimeout(()=>location.href='design.html?id='+encodeURIComponent(item.id),700);
  });
}
function initClearCustom(){
  const btn=$('#clearCustom'); if(!btn) return;
  btn.addEventListener('click',()=>{ if(confirm('Удалить все добавленные вами дизайны из этого браузера?')){localStorage.removeItem('bibliodesign_custom'); location.reload();} });
}

document.addEventListener('DOMContentLoaded',()=>{
  initMenu(); setActiveNav(); renderFeatured(); renderCatalog(); renderGallery(); renderDetail(); renderConstructor(); initAddForm(); initClearCustom(); initChat();
});


const chatRoomLabels={general:'Общее обсуждение',styles:'Стили и идеи',kids:'Детские библиотеки',tech:'Мебель и техника'};
function getChatData(){try{return JSON.parse(localStorage.getItem('bibliodesign_chat')||'{}')}catch(e){return {}}}
function saveChatData(data){localStorage.setItem('bibliodesign_chat', JSON.stringify(data))}
function defaultChatSeed(){
  return {
    general:[{author:'Мария',topic:'Навигация',message:'Подскажите, какие указатели лучше использовать в небольшой библиотеке, чтобы посетители быстрее ориентировались?',time:'сегодня, 10:15'}],
    styles:[{author:'Илья',topic:'Скандинавский стиль',message:'Хочу сделать светлый зал с мягкими зелёными акцентами. Какие материалы лучше подойдут для спокойного современного интерьера?',time:'сегодня, 11:00'}],
    kids:[{author:'Ольга',topic:'Детская зона',message:'Нужна идея для детского читального уголка: низкие стеллажи, мягкие модули и безопасная мебель. Что посоветуете?',time:'сегодня, 11:35'}],
    tech:[{author:'Денис',topic:'Медиатека',message:'Планируем цифровую зону с компьютерами и местами для зарядки. Как лучше разделить её с тихим читальным залом?',time:'сегодня, 12:10'}]
  };
}
function ensureChatSeed(){
  const data=getChatData();
  if(!Object.keys(data).length){saveChatData(defaultChatSeed()); return defaultChatSeed();}
  return data;
}
function renderChatMessages(room){
  const box=$('#chatMessages'); if(!box) return;
  const data=ensureChatSeed();
  const items=(data[room]||[]);
  if(!items.length){box.innerHTML='<div class="empty">В этой комнате пока нет сообщений. Начните обсуждение первым.</div>'; return;}
  box.innerHTML=items.map(item=>`<article class="chat-message"><div class="chat-meta"><span class="chat-author">${item.author}</span>${item.topic?`<span class="chat-topic">${item.topic}</span>`:''}<span>${item.time||''}</span></div><p class="chat-text">${item.message}</p></article>`).join('');
  box.scrollTop=box.scrollHeight;
}
function initChat(){
  const form=$('#chatForm'); const roomList=$('#roomList'); const clearBtn=$('#clearChat'); const title=$('#chatRoomTitle');
  if(!form||!roomList) return;
  let currentRoom='general';
  ensureChatSeed();
  const setRoom=(room)=>{
    currentRoom=room; if(title) title.textContent=chatRoomLabels[room]||room;
    $all('.room-btn', roomList).forEach(btn=>btn.classList.toggle('active', btn.dataset.room===room));
    renderChatMessages(room);
  };
  roomList.addEventListener('click',(e)=>{const btn=e.target.closest('.room-btn'); if(!btn) return; setRoom(btn.dataset.room);});
  form.addEventListener('submit',(e)=>{
    e.preventDefault();
    const fd=new FormData(form); const author=String(fd.get('author')||'Гость').trim(); const message=String(fd.get('message')||'').trim(); const topic=String(fd.get('topic')||'').trim();
    if(!message) return;
    const data=ensureChatSeed();
    if(!data[currentRoom]) data[currentRoom]=[];
    const now=new Date();
    data[currentRoom].push({author, topic, message, time: now.toLocaleString('ru-RU', {day:'2-digit', month:'2-digit', hour:'2-digit', minute:'2-digit'})});
    saveChatData(data); form.reset(); renderChatMessages(currentRoom); showToast('Сообщение добавлено');
  });
  if(clearBtn){clearBtn.addEventListener('click',()=>{if(confirm('Очистить сообщения в текущей комнате?')){const data=ensureChatSeed(); data[currentRoom]=[]; saveChatData(data); renderChatMessages(currentRoom);}})}
  setRoom('general');
}
