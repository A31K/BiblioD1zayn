from pathlib import Path
import json, textwrap, zipfile, os, html
root=Path('/mnt/data/bibliodesign_ready')
(root/'images').mkdir(exist_ok=True)

designs=[
    {
        'id':'eco-reading','title':'Эко-библиотека','tagline':'Тёплое пространство с растениями и природными материалами','category':['small','family','quiet'],'audience':'семьи, взрослые читатели, школьники','space':'малые и средние библиотеки','palette':'белый, шалфейный, бежевый, светлое дерево','materials':'дерево, пробка, текстиль, живые растения, матовые поверхности','zones':'зона чтения, зелёный уголок, место для тихой работы, открытые стеллажи','description':'Эко-оформление создаёт спокойную атмосферу и визуально разгружает пространство. Такой интерьер помогает читателю расслабиться, задержаться в библиотеке дольше и воспринимать её не только как место выдачи книг, но и как комфортную общественную среду. Мягкие зелёные акценты, натуральные фактуры и рассеянный свет делают зал дружелюбным и современным.','tips':['использовать светлые стеллажи и низкие перегородки','добавить растения в устойчивых кашпо','выделить тихую зону мягкими креслами','избегать слишком тёмной мебели'],
        'image':'eco-reading.svg'
    },
    {
        'id':'scandi-library','title':'Скандинавская библиотека','tagline':'Свет, простота и удобная навигация','category':['small','quiet','adult'],'audience':'взрослые читатели, студенты, посетители районных библиотек','space':'малые помещения и читальные залы','palette':'белый, молочный, светло-серый, мятный, натуральное дерево','materials':'дерево, хлопок, матовое стекло, простая металлическая фурнитура','zones':'абонемент, читальный стол, мягкая зона, витрина новинок','description':'Скандинавский стиль подходит библиотекам, которым важно выглядеть современно, но не перегруженно. Основу составляют светлые стены, простая мебель, понятная расстановка и тёплый локальный свет. Интерьер легко поддерживать в порядке, а посетителю удобно ориентироваться без лишних визуальных помех.','tips':['делать акцент на освещении','оставлять широкие проходы','использовать нейтральные цвета','поддерживать открытую систему навигации'],
        'image':'scandi-library.svg'
    },
    {
        'id':'minimal-study','title':'Минималистичная библиотека','tagline':'Чистое пространство для сосредоточенного чтения и учёбы','category':['quiet','adult','large'],'audience':'студенты, исследователи, взрослые читатели','space':'читальные залы, учебные пространства, библиотеки при учреждениях','palette':'белый, графитовый, светло-зелёный, серо-бежевый','materials':'ламинированные панели, металл, акустические панели, стекло','zones':'индивидуальные рабочие места, стеллажи, зона выдачи, тихие кабины','description':'Минимализм помогает создать среду, где ничто не отвлекает от работы с информацией. В таком оформлении важны строгая геометрия, удобные столы, достаточное количество розеток, качественное освещение и акустический комфорт. Стиль особенно подходит библиотекам с образовательной функцией.','tips':['не перегружать стены декором','продумать розетки и освещение','использовать акустические панели','выделить зону индивидуальной работы'],
        'image':'minimal-study.svg'
    },
    {
        'id':'loft-media','title':'Лофт-медиатека','tagline':'Свободная городская среда для встреч, лекций и медиа','category':['youth','events','large'],'audience':'молодёжь, творческие группы, участники мероприятий','space':'большие залы, медиатеки, молодёжные библиотеки','palette':'белый, бетонный серый, тёмный металл, зелёные акценты','materials':'металл, фанера, бетонные фактуры, трековое освещение','zones':'лекторий, медиазона, коворкинг, выставочная стена, стеллажи','description':'Лофт делает библиотеку более открытой и современной. Он хорошо работает там, где библиотека выполняет функции культурного центра: проводит лекции, встречи, мастер-классы и кинопоказы. Грубые фактуры уравновешиваются мягкой мебелью, зелёными деталями и понятной навигацией.','tips':['сочетать грубые фактуры с мягкими креслами','использовать мобильную мебель','добавить место для проекторов и экранов','оставить свободную центральную площадку'],
        'image':'loft-media.svg'
    },
    {
        'id':'classic-soft','title':'Современная классика','tagline':'Уважение к традиции без тяжёлого музейного эффекта','category':['adult','quiet','large'],'audience':'взрослые читатели, исследователи, гости центральных библиотек','space':'исторические здания, центральные библиотеки, большие читальные залы','palette':'белый, кремовый, оливковый, тёмное дерево, латунь','materials':'дерево, ткань, декоративные молдинги, настольные лампы','zones':'читальный зал, фонд открытого доступа, выставочные витрины, зона консультации','description':'Современная классика подходит библиотекам, где важно сохранить образ серьёзного культурного учреждения, но сделать его более лёгким и удобным. Интерьер строится на симметрии, качественной мебели, спокойной палитре и выразительном освещении.','tips':['не использовать слишком тяжёлые шторы','добавить современные рабочие места','сохранить визуальную торжественность','разместить витрины для редких изданий'],
        'image':'classic-soft.svg'
    },
    {
        'id':'kids-library','title':'Детская библиотека-игра','tagline':'Безопасная яркая среда для чтения, игры и первых открытий','category':['kids','family','events'],'audience':'дети, родители, педагоги','space':'детские библиотеки, семейные залы, школьные библиотеки','palette':'белый, мятный, жёлтый, мягкий оранжевый, светлое дерево','materials':'моющиеся покрытия, мягкие модули, ковролиновые зоны, фанера','zones':'зона сказок, игровая площадка, низкие стеллажи, место для чтения с родителями','description':'Детская библиотека должна быть понятной, безопасной и эмоционально привлекательной. Низкая мебель, округлые формы, цветовое зонирование и игровые элементы помогают ребёнку самостоятельно выбирать книги и чувствовать себя уверенно.','tips':['использовать мебель по росту детей','делать углы безопасными','выделять зоны цветом','добавить место для чтения на полу'],
        'image':'kids-library.svg'
    },
    {
        'id':'teen-hub','title':'Молодёжный хаб','tagline':'Библиотека как место общения, проектов и самовыражения','category':['youth','events','large'],'audience':'подростки, студенты, молодёжные клубы','space':'молодёжные библиотеки и открытые общественные зоны','palette':'белый, светло-зелёный, графитовый, акцентный лайм','materials':'модульная мебель, маркерные панели, пуфы, металл, пластик','zones':'коворкинг, зона встреч, медиастол, книжные острова, сцена для событий','description':'Молодёжный хаб объединяет библиотеку, коворкинг и пространство для мероприятий. Его задача — не только хранить книги, но и давать место для общения, работы над проектами, клубов и презентаций. Мебель должна быть мобильной, а интерьер — легко изменяемым.','tips':['использовать передвижные столы','оставить стену для объявлений и идей','добавить зарядные станции','предусмотреть разные сценарии света'],
        'image':'teen-hub.svg'
    },
    {
        'id':'silent-room','title':'Тихий читальный зал','tagline':'Максимум спокойствия, акустики и личного пространства','category':['quiet','adult','small'],'audience':'читатели, которым нужна концентрация','space':'читальные залы, отдельные комнаты, учебные пространства','palette':'белый, серо-зелёный, песочный, древесный','materials':'акустические панели, мягкий текстиль, дерево, матовые покрытия','zones':'индивидуальные столы, закрытые кабины, полки справочной литературы, зона отдыха','description':'Тихий зал решает задачу сосредоточенной работы. В нём особенно важны правильная акустика, удобная посадка, равномерный свет и ощущение защищённости. Цветовая гамма должна быть спокойной, без ярких раздражающих акцентов.','tips':['не ставить шумные зоны рядом','использовать мягкие покрытия','продумать индивидуальные светильники','сделать понятные правила поведения'],
        'image':'silent-room.svg'
    },
    {
        'id':'family-library','title':'Семейная библиотека','tagline':'Общее пространство для родителей, детей и совместного досуга','category':['family','kids','events'],'audience':'семьи с детьми, родители, группы выходного дня','space':'районные библиотеки, семейные центры, детско-взрослые залы','palette':'белый, фисташковый, бежевый, светло-жёлтый','materials':'дерево, мягкая мебель, моющиеся ткани, ковровые покрытия','zones':'детский уголок, зона семейного чтения, мастерская, выставка новинок','description':'Семейный формат делает библиотеку местом совместного досуга. Важно разделить активные и спокойные зоны, чтобы дети могли играть, а взрослые — читать или общаться. Интерьер должен быть тёплым, безопасным и легко обслуживаемым.','tips':['разделить шумную и тихую части','поставить диваны для совместного чтения','использовать моющиеся материалы','сделать зону мастер-классов'],
        'image':'family-library.svg'
    },
    {
        'id':'digital-library','title':'Цифровая медиабиблиотека','tagline':'Книги, технологии и медиа в одном пространстве','category':['youth','adult','large'],'audience':'студенты, исследователи, пользователи цифровых ресурсов','space':'медиатеки, университетские библиотеки, современные читальные залы','palette':'белый, холодный зелёный, светло-серый, чёрный акцент','materials':'стекло, металл, ламинированные панели, акустика, LED-освещение','zones':'компьютерные места, медиазал, зона сканирования, рабочие столы, полки','description':'Цифровая медиабиблиотека показывает, что библиотека работает не только с печатными книгами, но и с электронными ресурсами. Здесь важны эргономика рабочих мест, доступ к электричеству, понятная навигация и сочетание экранных зон с традиционным чтением.','tips':['предусмотреть розетки и кабель-каналы','разделить экранные и тихие зоны','добавить инструкции для пользователей','использовать регулируемое освещение'],
        'image':'digital-library.svg'
    },
    {
        'id':'inclusive-library','title':'Инклюзивная библиотека','tagline':'Доступная среда для разных возрастов и возможностей','category':['family','adult','quiet'],'audience':'все посетители, включая людей с ограниченной мобильностью','space':'публичные библиотеки, муниципальные учреждения, центры обслуживания','palette':'белый, мягкий зелёный, контрастный тёмно-серый, тёплый бежевый','materials':'нескользкие покрытия, контрастная навигация, удобные поручни, тактильные элементы','zones':'широкие проходы, доступная стойка, тихая зона, места ожидания, понятная навигация','description':'Инклюзивный дизайн делает библиотеку удобной для максимально широкого круга посетителей. Это не отдельный стиль, а подход: достаточная ширина проходов, ясные указатели, разные варианты посадки, отсутствие визуального шума и доступность основных функций.','tips':['делать проходы свободными','использовать контрастные указатели','ставить мебель разной высоты','избегать скользких покрытий'],
        'image':'inclusive-library.svg'
    },
    {
        'id':'art-library','title':'Арт-библиотека','tagline':'Пространство книг, выставок и визуальной культуры','category':['events','youth','large'],'audience':'творческие посетители, художники, школьники, студенты','space':'культурные центры, библиотеки с выставочной деятельностью','palette':'белый, шалфейный, терракотовый, светлое дерево, графит','materials':'галерейные стены, рейки, мобильные модули, направленный свет','zones':'выставочная линия, читальный остров, мастерская, стеллажи, зона лекций','description':'Арт-библиотека сочетает функции чтения, выставки и творческой мастерской. Белые стены работают как фон для экспозиций, а зелёные акценты делают пространство мягче. Такой вариант подходит библиотекам, которые хотят регулярно проводить события и менять оформление.','tips':['оставить стены для выставок','использовать мобильные панели','продумать направленный свет','сделать место для мастер-классов'],
        'image':'art-library.svg'
    }
]

# SVG generator
palettes = {
    'eco-reading':('#f7fbf7','#cfe5d3','#8fb99a','#e9d9bd','#4d6b57'),
    'scandi-library':('#fbfbf8','#dceee2','#9dc9a7','#e8dfcf','#52645a'),
    'minimal-study':('#ffffff','#d7e7dc','#a9cdb3','#eceff0','#303a35'),
    'loft-media':('#f9fbf8','#cfe6d5','#6d8f78','#d3d3cf','#303331'),
    'classic-soft':('#fffdf7','#dfeadd','#8aa37a','#dcc7a2','#5a4231'),
    'kids-library':('#fffefa','#d8f1df','#f5d66b','#f0a86e','#6e815f'),
    'teen-hub':('#ffffff','#cdf0d8','#9bd66f','#e9e9e9','#2e3331'),
    'silent-room':('#fbfbf7','#d6e4d8','#b5c3a1','#eadfca','#4b5a50'),
    'family-library':('#fffefa','#dff1da','#f3e7b2','#ead7bd','#59725f'),
    'digital-library':('#ffffff','#cfeee8','#a5d1ca','#e6eaee','#2c3438'),
    'inclusive-library':('#fffefa','#d7ead8','#7fa58a','#e9deca','#333d36'),
    'art-library':('#fffdf8','#d6ebdd','#c98d67','#ecdcc5','#3a3f39'),
}

def svg_for(d):
    bg, green, accent, wood, dark = palettes[d['id']]
    title = html.escape(d['title'])
    # Use stylized interior illustration
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 560" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0" stop-color="{bg}"/>
      <stop offset="1" stop-color="{green}"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#2d4938" flood-opacity="0.14"/>
    </filter>
  </defs>
  <rect width="900" height="560" rx="38" fill="url(#g)"/>
  <rect x="64" y="56" width="772" height="420" rx="28" fill="#ffffff" opacity="0.92" filter="url(#shadow)"/>
  <rect x="104" y="96" width="170" height="300" rx="18" fill="{wood}"/>
  <rect x="123" y="123" width="132" height="18" rx="8" fill="{dark}" opacity="0.72"/>
  <rect x="123" y="160" width="132" height="16" rx="8" fill="{accent}" opacity="0.86"/>
  <rect x="123" y="195" width="132" height="16" rx="8" fill="{dark}" opacity="0.36"/>
  <rect x="123" y="230" width="132" height="16" rx="8" fill="{accent}" opacity="0.7"/>
  <rect x="123" y="265" width="132" height="16" rx="8" fill="{dark}" opacity="0.5"/>
  <rect x="123" y="300" width="132" height="16" rx="8" fill="{accent}" opacity="0.75"/>
  <rect x="310" y="119" width="250" height="168" rx="22" fill="{green}" opacity="0.75"/>
  <rect x="342" y="151" width="185" height="18" rx="9" fill="#ffffff" opacity="0.72"/>
  <rect x="342" y="190" width="118" height="18" rx="9" fill="#ffffff" opacity="0.58"/>
  <circle cx="620" cy="158" r="48" fill="{accent}" opacity="0.72"/>
  <rect x="606" y="200" width="30" height="114" rx="15" fill="{dark}" opacity="0.36"/>
  <ellipse cx="620" cy="320" rx="68" ry="15" fill="{dark}" opacity="0.08"/>
  <rect x="326" y="336" width="282" height="34" rx="17" fill="{dark}" opacity="0.22"/>
  <rect x="362" y="372" width="44" height="52" rx="12" fill="{dark}" opacity="0.38"/>
  <rect x="530" y="372" width="44" height="52" rx="12" fill="{dark}" opacity="0.38"/>
  <rect x="658" y="270" width="108" height="76" rx="22" fill="{accent}" opacity="0.80"/>
  <rect x="684" y="242" width="56" height="56" rx="28" fill="{green}" opacity="0.88"/>
  <path d="M704 270c-38-36-8-79 32-93 8 37 1 74-32 93z" fill="{dark}" opacity="0.28"/>
  <path d="M725 266c35-42 82-21 88 22-40 10-72 4-88-22z" fill="{dark}" opacity="0.22"/>
  <text x="104" y="508" font-family="Arial, sans-serif" font-size="31" font-weight="700" fill="{dark}">{title}</text>
</svg>'''

for d in designs:
    (root/'images'/d['image']).write_text(svg_for(d), encoding='utf-8')

# CSS
css = r'''
:root{
  --bg:#fbfdfb;
  --surface:#ffffff;
  --surface-soft:#f2f8f3;
  --green:#7fb48b;
  --green-dark:#315f45;
  --green-soft:#dcefe1;
  --mint:#eef8f1;
  --text:#1f2e27;
  --muted:#61736a;
  --line:#dbe8df;
  --shadow:0 18px 45px rgba(35,75,52,.12);
  --radius:26px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Arial, Helvetica, sans-serif;background:var(--bg);color:var(--text);line-height:1.55}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.wrapper{width:min(1160px, calc(100% - 40px));margin:0 auto}
.topbar{position:sticky;top:0;z-index:50;background:rgba(251,253,251,.88);backdrop-filter:blur(16px);border-bottom:1px solid rgba(219,232,223,.75)}
.nav{height:76px;display:flex;align-items:center;justify-content:space-between;gap:18px}
.logo{display:flex;align-items:center;gap:12px;font-weight:800;font-size:22px;color:var(--green-dark)}
.logo-mark{width:42px;height:42px;border-radius:14px;background:linear-gradient(135deg,var(--green-soft),#fff);border:1px solid var(--line);display:grid;place-items:center;box-shadow:0 8px 20px rgba(49,95,69,.12)}
.logo-mark svg{width:25px;height:25px}
.menu{display:flex;gap:8px;align-items:center;flex-wrap:wrap;justify-content:flex-end}
.menu a{padding:10px 14px;border-radius:999px;color:#385046;font-weight:600;font-size:14px}
.menu a:hover,.menu a.active{background:var(--green-soft);color:var(--green-dark)}
.mobile-toggle{display:none;border:1px solid var(--line);background:#fff;border-radius:14px;padding:10px 12px;color:var(--green-dark);font-weight:700}
.hero{padding:74px 0 56px;position:relative;overflow:hidden}
.hero:before{content:"";position:absolute;inset:-180px -80px auto auto;width:480px;height:480px;background:radial-gradient(circle,var(--green-soft),transparent 65%);z-index:-1}
.hero-grid{display:grid;grid-template-columns:1.05fr .95fr;gap:38px;align-items:center}
.eyebrow{display:inline-flex;align-items:center;gap:8px;padding:8px 14px;border:1px solid var(--line);background:#fff;border-radius:999px;color:var(--green-dark);font-weight:700;font-size:14px}
h1{font-size:clamp(42px,7vw,78px);line-height:.98;margin:20px 0 20px;letter-spacing:-.04em;color:#1b2f25}
.lead{font-size:20px;color:var(--muted);max-width:720px;margin:0 0 28px}
.hero-actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:28px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;border:none;border-radius:16px;padding:14px 20px;font-weight:800;cursor:pointer;transition:.18s;background:var(--green-dark);color:#fff;box-shadow:0 12px 28px rgba(49,95,69,.22)}
.btn:hover{transform:translateY(-2px)}
.btn.secondary{background:#fff;color:var(--green-dark);border:1px solid var(--line);box-shadow:none}
.hero-card{background:#fff;border:1px solid var(--line);border-radius:34px;padding:18px;box-shadow:var(--shadow)}
.hero-card img{border-radius:24px;aspect-ratio:1.28/1;object-fit:cover;background:var(--mint)}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:14px}
.stat{background:var(--surface-soft);border:1px solid var(--line);border-radius:20px;padding:16px;text-align:center}
.stat strong{display:block;font-size:25px;color:var(--green-dark)}
.section{padding:54px 0}
.section-head{display:flex;justify-content:space-between;gap:20px;align-items:flex-end;margin-bottom:26px}
.section h2{font-size:clamp(30px,4vw,46px);line-height:1.06;margin:0;color:#1b2f25;letter-spacing:-.03em}
.section p.section-text{color:var(--muted);font-size:18px;max-width:720px;margin:12px 0 0}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;box-shadow:0 8px 26px rgba(49,95,69,.08);display:flex;flex-direction:column;min-height:100%}
.card-image{aspect-ratio:1.42/1;background:var(--mint);overflow:hidden}
.card-content{padding:20px;display:flex;flex-direction:column;gap:12px;flex:1}
.card h3{margin:0;font-size:22px;color:#1b2f25}
.card p{margin:0;color:var(--muted)}
.tags{display:flex;gap:7px;flex-wrap:wrap}
.tag{font-size:12px;font-weight:700;background:var(--mint);border:1px solid var(--line);color:var(--green-dark);border-radius:999px;padding:6px 10px}
.card-actions{margin-top:auto;display:flex;gap:10px;flex-wrap:wrap}
.filters{display:grid;grid-template-columns:1fr auto;gap:14px;margin-bottom:22px;align-items:center}
.search{width:100%;border:1px solid var(--line);background:#fff;border-radius:18px;padding:15px 18px;font-size:16px;outline:none;color:var(--text)}
.search:focus{border-color:var(--green);box-shadow:0 0 0 4px rgba(127,180,139,.14)}
.filter-buttons{display:flex;gap:8px;flex-wrap:wrap;justify-content:flex-end}
.filter-btn{border:1px solid var(--line);background:#fff;color:var(--green-dark);font-weight:800;border-radius:999px;padding:11px 14px;cursor:pointer}
.filter-btn.active,.filter-btn:hover{background:var(--green-dark);color:#fff;border-color:var(--green-dark)}
.page-title{padding:50px 0 24px;background:linear-gradient(180deg,#fff,transparent)}
.page-title h1{font-size:clamp(38px,5vw,62px);margin-bottom:16px}
.breadcrumb{color:var(--muted);font-weight:700;margin-bottom:12px}
.detail-grid{display:grid;grid-template-columns:.92fr 1.08fr;gap:28px;align-items:start}
.detail-panel{background:#fff;border:1px solid var(--line);border-radius:30px;padding:26px;box-shadow:var(--shadow)}
.detail-panel h2,.detail-panel h3{margin-top:0;color:#1b2f25}
.detail-panel ul{padding-left:20px;margin-bottom:0;color:var(--muted)}
.detail-image{border-radius:30px;border:1px solid var(--line);box-shadow:var(--shadow);background:#fff;padding:14px;position:sticky;top:96px}
.detail-image img{border-radius:22px}
.info-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:18px}
.info-box{background:var(--surface-soft);border:1px solid var(--line);border-radius:18px;padding:14px}
.info-box b{display:block;color:var(--green-dark);margin-bottom:4px}
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.step{background:#fff;border:1px solid var(--line);border-radius:24px;padding:22px;box-shadow:0 8px 22px rgba(49,95,69,.07)}
.step-num{width:38px;height:38px;border-radius:14px;background:var(--green-soft);color:var(--green-dark);font-weight:900;display:grid;place-items:center;margin-bottom:14px}
.form-card{background:#fff;border:1px solid var(--line);border-radius:30px;padding:26px;box-shadow:var(--shadow)}
.form-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.form-field{display:flex;flex-direction:column;gap:8px}
.form-field.full{grid-column:1/-1}
label{font-weight:800;color:#29483a}
input,textarea,select{border:1px solid var(--line);border-radius:16px;padding:14px 15px;font-size:16px;font-family:inherit;outline:none;background:#fff;color:var(--text)}
textarea{min-height:130px;resize:vertical}
input:focus,textarea:focus,select:focus{border-color:var(--green);box-shadow:0 0 0 4px rgba(127,180,139,.14)}
.note{font-size:14px;color:var(--muted);background:var(--surface-soft);border:1px solid var(--line);padding:14px 16px;border-radius:18px}
.gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.gallery a{display:block;background:#fff;border:1px solid var(--line);border-radius:24px;padding:10px;box-shadow:0 8px 22px rgba(49,95,69,.08)}
.gallery img{border-radius:18px}
.empty{background:#fff;border:1px dashed var(--green);border-radius:24px;padding:28px;text-align:center;color:var(--muted);grid-column:1/-1}
.footer{margin-top:60px;background:#f1f8f3;border-top:1px solid var(--line);padding:34px 0;color:var(--muted)}
.footer-grid{display:flex;justify-content:space-between;gap:20px;align-items:center;flex-wrap:wrap}
.footer a{font-weight:800;color:var(--green-dark)}
.toast{position:fixed;right:20px;bottom:20px;background:var(--green-dark);color:#fff;padding:14px 18px;border-radius:16px;box-shadow:var(--shadow);opacity:0;transform:translateY(10px);transition:.2s;z-index:100}
.toast.show{opacity:1;transform:translateY(0)}
@media(max-width:960px){.hero-grid,.detail-grid{grid-template-columns:1fr}.cards,.gallery{grid-template-columns:repeat(2,1fr)}.steps{grid-template-columns:repeat(2,1fr)}.filters{grid-template-columns:1fr}.filter-buttons{justify-content:flex-start}.detail-image{position:static}.menu{display:none;position:absolute;top:76px;left:20px;right:20px;background:#fff;border:1px solid var(--line);border-radius:22px;padding:12px;box-shadow:var(--shadow);align-items:stretch}.menu.open{display:flex;flex-direction:column}.menu a{border-radius:14px}.mobile-toggle{display:block}}
@media(max-width:640px){.wrapper{width:min(100% - 28px,1160px)}.hero{padding-top:46px}.cards,.gallery,.steps,.form-grid,.info-grid{grid-template-columns:1fr}.stats{grid-template-columns:1fr}.hero-actions{flex-direction:column}.btn{width:100%}.section-head{align-items:flex-start;flex-direction:column}.nav{height:70px}.menu{top:70px}h1{font-size:42px}}
'''
(root/'css'/'styles.css').write_text(css, encoding='utf-8')

# data.js
js_data = 'const DESIGN_DATA = ' + json.dumps(designs, ensure_ascii=False, indent=2) + ';\n'
(root/'js'/'data.js').write_text(js_data, encoding='utf-8')

# app.js
app_js = r'''
const categoryLabels = {
  all:'Все', small:'Маленькое помещение', large:'Большая библиотека', quiet:'Тихое чтение', events:'Мероприятия', family:'Семейная', youth:'Молодёжь', adult:'Взрослые', kids:'Детская'
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
  const tags=(item.category||[]).slice(0,3).map(t=>`<span class="tag">${categoryLabels[t]||t}</span>`).join('');
  return `<article class="card" data-categories="${(item.category||[]).join(' ')}" data-title="${item.title.toLowerCase()}" data-text="${(item.description+' '+item.tagline+' '+item.palette).toLowerCase()}">
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
  root.innerHTML=`<div class="page-title"><div class="wrapper"><div class="breadcrumb"><a href="designs.html">Каталог дизайнов</a> / ${item.title}</div><h1>${item.title}</h1><p class="lead">${item.tagline}</p></div></div>
  <section class="section"><div class="wrapper detail-grid">
    <div class="detail-image"><img src="${imagePath(item)}" alt="${item.title}"></div>
    <div class="detail-panel">
      <div class="tags">${(item.category||[]).map(t=>`<span class="tag">${categoryLabels[t]||t}</span>`).join('')}</div>
      <h2>Описание решения</h2>
      <p>${item.description}</p>
      <div class="info-grid">
        <div class="info-box"><b>Для кого подходит</b>${item.audience}</div>
        <div class="info-box"><b>Тип помещения</b>${item.space}</div>
        <div class="info-box"><b>Палитра</b>${item.palette}</div>
        <div class="info-box"><b>Материалы</b>${item.materials}</div>
      </div>
      <h3 style="margin-top:28px">Основные зоны</h3>
      <p>${item.zones}</p>
      <h3 style="margin-top:28px">Рекомендации по оформлению</h3>
      <ul>${(item.tips||[]).map(t=>`<li>${t}</li>`).join('')}</ul>
      <div class="hero-actions"><a class="btn" href="constructor.html">Подобрать похожий стиль</a><a class="btn secondary" href="designs.html">Вернуться в каталог</a></div>
    </div>
  </div></section>`;
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
      image:'eco-reading.svg',
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
  initMenu(); setActiveNav(); renderFeatured(); renderCatalog(); renderGallery(); renderDetail(); renderConstructor(); initAddForm(); initClearCustom();
});
'''
(root/'js'/'app.js').write_text(app_js, encoding='utf-8')

# Common pieces
def nav(active):
    return f'''<header class="topbar">
  <div class="wrapper nav">
    <a class="logo" href="index.html" aria-label="БиблиоДизайн">
      <span class="logo-mark"><svg viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M5 5.8c0-1 .8-1.8 1.8-1.8H19v14.2H6.8A1.8 1.8 0 0 1 5 16.4V5.8Z" stroke="#315f45" stroke-width="1.8"/><path d="M8 7.5h8M8 10.5h6M8 13.5h7" stroke="#7fb48b" stroke-width="1.8" stroke-linecap="round"/></svg></span>
      <span>БиблиоДизайн</span>
    </a>
    <button class="mobile-toggle" type="button">Меню</button>
    <nav class="menu" aria-label="Главное меню">
      <a data-nav="home" href="index.html">Главная</a>
      <a data-nav="designs" href="designs.html">Дизайны</a>
      <a data-nav="constructor" href="constructor.html">Подбор стиля</a>
      <a data-nav="gallery" href="gallery.html">Галерея</a>
      <a data-nav="add" href="add.html">Добавить свой</a>
      <a data-nav="guide" href="guide.html">Советы</a>
    </nav>
  </div>
</header>'''

def footer():
    return '''<footer class="footer"><div class="wrapper footer-grid"><div><b>БиблиоДизайн</b><br>Подбор идей для оформления библиотек и читальных пространств.</div><div><a href="designs.html">Каталог</a> · <a href="constructor.html">Подбор</a> · <a href="add.html">Добавить дизайн</a></div></div></footer><div class="toast"></div>'''

def scripts():
    return '<script src="js/data.js"></script><script src="js/app.js"></script>'

def head(title, desc):
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title><meta name="description" content="{desc}"><link rel="stylesheet" href="css/styles.css"></head>'''

# pages
index_html = head('БиблиоДизайн — идеи оформления библиотек','Сайт для подбора дизайна и оформления библиотечного пространства.') + '''
<body data-page="home">''' + nav('home') + '''
<main>
  <section class="hero">
    <div class="wrapper hero-grid">
      <div>
        <span class="eyebrow">Подбор оформления библиотек</span>
        <h1>БиблиоДизайн</h1>
        <p class="lead">Сайт помогает выбрать стиль оформления библиотеки: от тихого читального зала до семейной зоны, молодёжного хаба или современной медиатеки.</p>
        <p class="lead">Здесь можно посмотреть готовые варианты, изучить их описание, подобрать подходящий стиль под помещение и добавить собственную идею.</p>
        <div class="hero-actions">
          <a class="btn" href="designs.html">Смотреть дизайны</a>
          <a class="btn secondary" href="constructor.html">Подобрать стиль</a>
        </div>
      </div>
      <div class="hero-card">
        <img src="images/eco-reading.svg" alt="Интерьер современной библиотеки">
        <div class="stats">
          <div class="stat"><strong>12+</strong>готовых стилей</div>
          <div class="stat"><strong>6</strong>разделов сайта</div>
          <div class="stat"><strong>∞</strong>свои идеи</div>
        </div>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="wrapper">
      <div class="section-head"><div><h2>Что можно сделать на сайте</h2><p class="section-text">Главная страница не перегружена: все функции вынесены в отдельные вкладки, чтобы посетителю было удобно выбирать нужное.</p></div></div>
      <div class="steps">
        <div class="step"><div class="step-num">1</div><h3>Посмотреть дизайны</h3><p>Откройте каталог и сравните разные варианты оформления библиотек.</p></div>
        <div class="step"><div class="step-num">2</div><h3>Изучить описание</h3><p>У каждого дизайна есть аудитория, палитра, зоны, материалы и рекомендации.</p></div>
        <div class="step"><div class="step-num">3</div><h3>Подобрать стиль</h3><p>Ответьте на несколько вопросов и получите подходящие варианты.</p></div>
        <div class="step"><div class="step-num">4</div><h3>Добавить свой</h3><p>Сохраните собственную идею дизайна прямо в браузере.</p></div>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="wrapper">
      <div class="section-head"><div><h2>Популярные варианты</h2><p class="section-text">Несколько примеров из каталога. Полный список находится во вкладке «Дизайны».</p></div><a class="btn secondary" href="designs.html">Весь каталог</a></div>
      <div class="cards" id="featuredGrid"></div>
    </div>
  </section>
</main>''' + footer() + scripts() + '</body></html>'
(root/'index.html').write_text(index_html, encoding='utf-8')

designs_html = head('Дизайны библиотек — БиблиоДизайн','Каталог дизайнов и оформлений библиотек с описаниями.') + '''
<body data-page="designs">''' + nav('designs') + '''
<main>
  <section class="page-title"><div class="wrapper"><div class="breadcrumb">БиблиоДизайн / Каталог</div><h1>Дизайны библиотек</h1><p class="lead">Выберите вариант оформления, который подходит под размер помещения, аудиторию и задачи библиотеки.</p></div></section>
  <section class="section"><div class="wrapper">
    <div class="filters">
      <input class="search" id="searchInput" type="search" placeholder="Поиск: эко, детская, тихая зона, медиатека...">
      <div class="filter-buttons">
        <button class="filter-btn active" data-filter="all">Все</button>
        <button class="filter-btn" data-filter="small">Маленькие</button>
        <button class="filter-btn" data-filter="large">Большие</button>
        <button class="filter-btn" data-filter="quiet">Тихие</button>
        <button class="filter-btn" data-filter="events">Мероприятия</button>
        <button class="filter-btn" data-filter="family">Семейные</button>
        <button class="filter-btn" data-filter="youth">Молодёжь</button>
      </div>
    </div>
    <div class="cards" id="designGrid"></div>
    <div class="empty" id="emptyCatalog" style="display:none">По вашему запросу ничего не найдено. Попробуйте другой фильтр или добавьте свой дизайн.</div>
  </div></section>
</main>''' + footer() + scripts() + '</body></html>'
(root/'designs.html').write_text(designs_html, encoding='utf-8')

detail_html = head('Описание дизайна — БиблиоДизайн','Подробное описание выбранного дизайна библиотеки.') + '''
<body data-page="designs">''' + nav('designs') + '<main id="detailRoot"></main>' + footer() + scripts() + '</body></html>'
(root/'design.html').write_text(detail_html, encoding='utf-8')

constructor_html = head('Подбор стиля — БиблиоДизайн','Подбор подходящего оформления библиотеки по параметрам.') + '''
<body data-page="constructor">''' + nav('constructor') + '''
<main>
  <section class="page-title"><div class="wrapper"><div class="breadcrumb">БиблиоДизайн / Подбор стиля</div><h1>Подобрать оформление</h1><p class="lead">Ответьте на три вопроса, и сайт покажет варианты дизайна, которые лучше подходят под вашу задачу.</p></div></section>
  <section class="section"><div class="wrapper detail-grid">
    <form class="form-card" id="pickForm">
      <div class="form-grid">
        <div class="form-field"><label for="space">Размер помещения</label><select id="space" name="space"><option value="small">Небольшое помещение</option><option value="large">Большой зал</option></select></div>
        <div class="form-field"><label for="audience">Основная аудитория</label><select id="audience" name="audience"><option value="adult">Взрослые</option><option value="kids">Дети</option><option value="family">Семьи</option><option value="youth">Молодёжь</option></select></div>
        <div class="form-field full"><label for="task">Главная задача пространства</label><select id="task" name="task"><option value="quiet">Тихое чтение и учёба</option><option value="events">Мероприятия и встречи</option><option value="family">Семейный досуг</option><option value="youth">Проекты и общение</option></select></div>
      </div>
      <div class="hero-actions"><button class="btn" type="submit">Показать варианты</button><a class="btn secondary" href="designs.html">Открыть весь каталог</a></div>
    </form>
    <div><div class="note">Результаты появятся ниже после подбора. Это не строгий расчёт, а удобная подсказка для выбора направления оформления.</div></div>
  </div></section>
  <section class="section"><div class="wrapper"><div class="section-head"><div><h2>Подходящие варианты</h2><p class="section-text">Карточки появятся после заполнения формы.</p></div></div><div class="cards" id="pickResult"><div class="empty">Выберите параметры и нажмите «Показать варианты».</div></div></div></section>
</main>''' + footer() + scripts() + '</body></html>'
(root/'constructor.html').write_text(constructor_html, encoding='utf-8')

gallery_html = head('Галерея — БиблиоДизайн','Галерея визуальных идей оформления библиотек.') + '''
<body data-page="gallery">''' + nav('gallery') + '''
<main>
  <section class="page-title"><div class="wrapper"><div class="breadcrumb">БиблиоДизайн / Галерея</div><h1>Галерея идей</h1><p class="lead">Быстрый просмотр визуальных вариантов. Нажмите на изображение, чтобы открыть подробное описание дизайна.</p></div></section>
  <section class="section"><div class="wrapper"><div class="gallery" id="galleryGrid"></div></div></section>
</main>''' + footer() + scripts() + '</body></html>'
(root/'gallery.html').write_text(gallery_html, encoding='utf-8')

add_html = head('Добавить свой дизайн — БиблиоДизайн','Форма добавления собственного варианта дизайна библиотеки.') + '''
<body data-page="add">''' + nav('add') + '''
<main>
  <section class="page-title"><div class="wrapper"><div class="breadcrumb">БиблиоДизайн / Добавить свой</div><h1>Добавить свой дизайн</h1><p class="lead">Заполните карточку своего варианта оформления. Она сохранится в вашем браузере и появится в каталоге и галерее.</p></div></section>
  <section class="section"><div class="wrapper detail-grid">
    <form class="form-card" id="addDesignForm">
      <div class="form-grid">
        <div class="form-field"><label>Название</label><input name="title" required placeholder="Например: Уютная библиотека у окна"></div>
        <div class="form-field"><label>Короткое описание</label><input name="tagline" placeholder="Главная идея дизайна"></div>
        <div class="form-field"><label>Размер</label><select name="space"><option value="small">Маленькое помещение</option><option value="large">Большая библиотека</option></select></div>
        <div class="form-field"><label>Аудитория</label><select name="audience"><option value="adult">Взрослые</option><option value="kids">Дети</option><option value="family">Семьи</option><option value="youth">Молодёжь</option></select></div>
        <div class="form-field"><label>Задача</label><select name="task"><option value="quiet">Тихое чтение</option><option value="events">Мероприятия</option><option value="family">Семейный досуг</option><option value="youth">Общение и проекты</option></select></div>
        <div class="form-field"><label>Картинка</label><input id="imageFile" type="file" accept="image/*"></div>
        <div class="form-field"><label>Для кого подходит</label><input name="audienceText" placeholder="Например: школьники и родители"></div>
        <div class="form-field"><label>Тип помещения</label><input name="spaceText" placeholder="Например: небольшой зал 40 м²"></div>
        <div class="form-field"><label>Палитра</label><input name="palette" placeholder="Белый, шалфейный, дерево"></div>
        <div class="form-field"><label>Материалы</label><input name="materials" placeholder="Дерево, текстиль, металл"></div>
        <div class="form-field full"><label>Основные зоны</label><input name="zones" placeholder="Читальная зона, стеллажи, место для встреч"></div>
        <div class="form-field full"><label>Подробное описание</label><textarea name="description" required placeholder="Опишите, как выглядит пространство и какую задачу решает дизайн"></textarea></div>
        <div class="form-field full"><label>Рекомендации, каждая с новой строки</label><textarea name="tips" placeholder="Добавить мягкое освещение&#10;Использовать низкие стеллажи&#10;Оставить свободные проходы"></textarea></div>
      </div>
      <div class="hero-actions"><button class="btn" type="submit">Сохранить дизайн</button><button class="btn secondary" type="button" id="clearCustom">Очистить мои добавленные</button></div>
    </form>
    <div class="detail-panel"><h2>Предпросмотр картинки</h2><p>Если картинка не выбрана, сайт использует стандартную иллюстрацию. Добавленные данные сохраняются только в вашем браузере.</p><img id="imagePreview" alt="Предпросмотр" style="display:none;border-radius:20px;margin-top:16px"></div>
  </div></section>
</main>''' + footer() + scripts() + '</body></html>'
(root/'add.html').write_text(add_html, encoding='utf-8')

guide_html = head('Советы по оформлению — БиблиоДизайн','Практические советы по оформлению библиотечного пространства.') + '''
<body data-page="guide">''' + nav('guide') + '''
<main>
  <section class="page-title"><div class="wrapper"><div class="breadcrumb">БиблиоДизайн / Советы</div><h1>Советы по оформлению</h1><p class="lead">Короткие рекомендации, которые помогут сделать библиотеку удобной, понятной и визуально спокойной.</p></div></section>
  <section class="section"><div class="wrapper">
    <div class="cards">
      <article class="card"><div class="card-content"><span class="tag">Планировка</span><h3>Разделяйте зоны</h3><p>Тихое чтение, мероприятия, детская активность и работа за компьютером не должны мешать друг другу. Используйте стеллажи, цвет, ковры и свет для мягкого зонирования.</p></div></article>
      <article class="card"><div class="card-content"><span class="tag">Цвет</span><h3>Оставляйте светлую основу</h3><p>Белые и светлые стены визуально расширяют помещение. Зелёные акценты можно добавлять через мебель, растения, навигацию и декоративные элементы.</p></div></article>
      <article class="card"><div class="card-content"><span class="tag">Комфорт</span><h3>Думайте о разных посетителях</h3><p>Нужны разные посадочные места: столы для работы, кресла для отдыха, низкая мебель для детей, места ожидания и свободные проходы.</p></div></article>
      <article class="card"><div class="card-content"><span class="tag">Свет</span><h3>Сочетайте общий и локальный свет</h3><p>Одного потолочного света часто недостаточно. Настольные лампы, бра и подсветка зон делают чтение удобнее и создают уют.</p></div></article>
      <article class="card"><div class="card-content"><span class="tag">Навигация</span><h3>Помогайте ориентироваться</h3><p>Посетитель должен быстро понять, где абонемент, читальный зал, детская зона, мероприятия и новые книги. Навигация должна быть контрастной и простой.</p></div></article>
      <article class="card"><div class="card-content"><span class="tag">Гибкость</span><h3>Используйте мобильную мебель</h3><p>Передвижные столы, пуфы и лёгкие стеллажи позволяют быстро менять сценарий: лекция, клуб, выставка, мастер-класс или обычный день чтения.</p></div></article>
    </div>
  </div></section>
</main>''' + footer() + scripts() + '</body></html>'
(root/'guide.html').write_text(guide_html, encoding='utf-8')

readme = '''БиблиоДизайн — готовый статический сайт\n\nКак открыть:\n1. Распакуйте архив.\n2. Откройте файл index.html в браузере.\n\nСтраницы:\n- index.html — главная страница с названием и назначением сайта.\n- designs.html — каталог дизайнов библиотек с фильтрами и поиском.\n- design.html — отдельная страница подробного описания выбранного дизайна.\n- constructor.html — подбор стиля по параметрам.\n- gallery.html — галерея изображений.\n- add.html — добавление своего дизайна с сохранением в браузере.\n- guide.html — практические советы по оформлению.\n\nВажно:\nФорма «Добавить свой дизайн» работает через localStorage. Это значит, что добавленные варианты сохраняются в том браузере, где пользователь их добавил. Для публикации сайта на хостинге файлы можно загрузить как обычный статический сайт.\n'''
(root/'README.txt').write_text(readme, encoding='utf-8')

# zip
zip_path=Path('/mnt/data/БиблиоДизайн_готовый_многостраничный_сайт.zip')
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for p in root.rglob('*'):
        if p.is_file() and p.name != 'generate_site.py':
            z.write(p, p.relative_to(root))
print(zip_path)
