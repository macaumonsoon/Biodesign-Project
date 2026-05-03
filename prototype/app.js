const HERO_CONTENT = {
  mammoth: {
    title: "Woolly Mammoth - Temporal Niche Dossier",
    summary: "Arctic photoperiod adaptation, cold sensation, and long-range acoustic hypotheses.",
    lines: [
      { tier: "cited", text: "Circadian-related genetic changes are reported in mammoth genomics literature." },
      { tier: "interp", text: "Infrasound communication is modeled from elephant relatives and body-scale priors." },
      { tier: "spec", text: "Immersive dawn-to-polar-night scene dynamics are design hypotheses." }
    ]
  },
  thylacine: {
    title: "Thylacine - Dusk Vision Dossier",
    summary: "Orbit-informed diel behavior reconstruction and colonial extinction context.",
    lines: [
      { tier: "cited", text: "Historical records and morphology support crepuscular/nocturnal behavior hypotheses." },
      { tier: "interp", text: "RGC-like motion/contrast POV is an inferred visual interface, not direct thylacine measurement." },
      { tier: "spec", text: "First-person Umwelt rendering remains speculative and explicitly labeled." }
    ]
  }
};

const PORTAL_LABELS = {
  iucn_red_list_search: "IUCN",
  gbif_species_search: "GBIF Species",
  gbif_occurrence_search: "GBIF Occurrence",
  morphosource_search: "MorphoSource",
  pbdb_taxon_api: "PBDB API",
  pbdb_classic_ui: "PBDB UI",
  bhl_literature_search: "BHL",
  eol_search: "EOL",
  smithsonian_3d_search: "Smithsonian 3D",
  sketchfab_search: "Sketchfab",
  wikipedia: "Wikipedia",
  xeno_canto_search: "Xeno-canto",
  macaulay_library_search: "Macaulay Library"
};

const LANG_KEY = "ea-lang";
const SPECIES_DETAIL_VERSION = "classic-species-english-values-v4-20260503";

const PAGE_COPY = {
  zh: {
    home: "首页",
    archive: "物种档案",
    hero: "重点案例",
    detail: "物种详情",
    archiveTitle: "物种档案浏览",
    archiveLead: "这里汇总本项目收录的灭绝物种，可按类别和资料完整度筛选，并进入单个物种档案查看来源与说明。",
    heroTitle: "重点案例",
    heroLead: "以猛犸象和袋狼为例，展示如何把科学资料、历史记录和沉浸式叙事结合起来。",
    speciesTitle: "物种详情",
    speciesLead: "查看物种基本信息、灭绝原因、资料来源和可继续核对的开放档案入口。",
    searchPlaceholder: "按俗名 / 学名搜索...",
    allCategories: "全部类别",
    allAvailability: "全部数据级别",
    showing: n => `显示 ${n} 个物种`,
    openDetail: "打开详情",
    imageSource: "图片来源",
    chineseName: "中文名",
    category: "类别",
    extinction: "灭绝时间",
    region: "区域",
    data: "资料完整度",
    sensory: "感官资料",
    music: "声音资料",
    drivers: "灭绝原因",
    notes: "补充说明",
    verification: "验证说明",
    exhibitBlocks: "展览说明",
    portals: "档案入口",
    curated: "策展线索",
    protocol: "研究协议",
    notFound: slug => `找不到物种 slug：${slug || "（空）"}`,
    ethics: "伦理思考",
    budget: "去灭绝研究投入优先级：",
    risk: "生态不确定性的接受程度：",
    reflection: "反思日志",
    save: "保存反思",
    load: "载入上次反思",
    reflectionPlaceholder: "当一个物种从地球上消失，我们应该如何记住它、解释它，并避免新的消失？",
    saved: "已保存到本地浏览器。",
    loaded: "已载入上次记录。",
    balanced: "平衡路径：既讨论技术可能性，也要清楚说明证据边界、生态风险和公众参与方式。",
    high: "高投入、高风险接受度：若推进去灭绝研究，必须明确技术安全、生态评估和原住民/当地社群的知情参与。",
    low: "保护优先路径：即使不尝试复活，灭绝物种仍需要被记录、解释，并转化为今天的保护行动。"
  },
  en: {
    home: "Home",
    archive: "Archive Cards",
    hero: "Hero Dossiers",
    detail: "Species Detail",
    archiveTitle: "Archive Browse (54 Species Card Layer)",
    archiveLead: "Current data source is local JSON; every species card now uses an independent real-image marker.",
    heroTitle: "Hero Dossiers (Depth Layer)",
    heroLead: "Immersive narrative prototypes for Mammoth and Thylacine",
    speciesTitle: "Single Species Detail",
    speciesLead: "Detail page with archival portals, curation metadata, and image sources.",
    searchPlaceholder: "Search by common/scientific name...",
    allCategories: "All Categories",
    allAvailability: "All Availability",
    showing: n => `Showing ${n} species`,
    openDetail: "Open detail",
    imageSource: "Image source",
    chineseName: "Chinese name",
    category: "Category",
    extinction: "Extinction",
    region: "Region",
    data: "Data",
    sensory: "Sensory score",
    music: "Music score",
    drivers: "Extinction drivers",
    notes: "Project notes",
    verification: "Verification",
    exhibitBlocks: "Exhibit Content Blocks",
    portals: "Archival Portals",
    curated: "Curated Archive Hints",
    protocol: "Research Protocol",
    notFound: slug => `Species not found for slug: ${slug || "(empty)"}`,
    ethics: "Ethics Fork",
    budget: "De-extinction budget priority: ",
    risk: "Risk tolerance for ecological uncertainty: ",
    reflection: "Reflection Log",
    save: "Save reflection",
    load: "Load last reflection",
    reflectionPlaceholder: "What does irreversible loss of biological memory mean to you?",
    saved: "Reflection saved locally.",
    loaded: "Last reflection loaded.",
    balanced: "Balanced strategy. Reflection prompt: where should uncertainty be communicated to the public?",
    high: "High de-extinction investment + high risk tolerance. What safeguards and sovereignty commitments are non-negotiable?",
    low: "Conservation-first strategy. What extinct memory work is still ethically required even without revival?"
  }
};

const ZH_NAME_OVERRIDES = {
  "Psittirostra psittacea": "夏威夷鹦嘴雀",
  "Melamprosops phaeosoma": "波奥吸蜜鸟",
  "Perameles papillon": "纳拉伯兔耳袋狸",
  "Perameles myosuros": "东南袋狸",
  "Perameles notina": "沙漠袋狸",
  "Chaeropus ecaudatus": "猪足袋狸",
  "Chaeropus yirratji": "北方猪足袋狸",
  "Zalophus japonicus": "日本海狮",
  "Dusicyon australis": "福克兰群岛狼",
  "Numenius tenuirostris": "细嘴杓鹬",
  "Camptorhynchus labradorius": "拉布拉多鸭",
  "Tachybaptus rufolavatus": "阿劳特拉䴙䴘",
  "Corvus hawaiiensis": "夏威夷乌鸦",
  "Conuropsis carolinensis": "卡罗莱纳长尾鹦鹉",
  "Campephilus imperialis": "帝王啄木鸟",
  "Vermivora bachmanii": "巴赫曼林莺",
  "Psephotellus pulcherrimus": "天堂鹦鹉",
  "Ninox albifacies": "笑鸮",
  "Tympanuchus cupido cupido": "荒原松鸡",
  "Chelonoidis abingdonii": "平塔岛象龟",
  "Cylindraspis indica": "留尼汪巨龟",
  "Cylindraspis triserrata": "圆顶毛里求斯巨龟",
  "Cylindraspis peltastes": "罗德里格斯巨龟",
  "Bolyeria multocarinata": "圆岛穴居蟒",
  "Hoplodactylus delcourti": "德尔库尔巨壁虎",
  "Incilius periglenes": "金蟾蜍",
  "Cynops wolterstorffi": "滇池蝾螈",
  "Litoria nyakalensis": "山雾蛙",
  "Psephurus gladius": "白鲟",
  "Sympterichthys unipennis": "光滑手鱼",
  "Glaucopsyche xerces": "泽西斯蓝蝶",
  "Conus lugubris": "暗锥螺",
  "Pieris wollastoni": "马德拉大白蝶",
  "Lipotes vexillifer": "白鱀豚",
  "Oophaga speciosa": "华丽箭毒蛙"
};

function hasChinese(text = "") {
  return /[\u3400-\u9fff]/.test(String(text));
}

function currentPrototypeLang() {
  return localStorage.getItem(LANG_KEY)
    || localStorage.getItem("prototype-lang")
    || localStorage.getItem("xr-lang")
    || localStorage.getItem("ethics-lang")
    || (document.documentElement.lang?.startsWith("en") ? "en" : "zh");
}

function setGlobalLanguage(lang) {
  const selected = lang === "en" ? "en" : "zh";
  localStorage.setItem(LANG_KEY, selected);
  localStorage.setItem("prototype-lang", selected);
  localStorage.setItem("xr-lang", selected);
  localStorage.setItem("ethics-lang", selected);
  document.documentElement.lang = selected === "zh" ? "zh-Hans" : "en";
  document.querySelectorAll("[data-lang], [data-xr-lang], [data-ethics-lang]").forEach((button) => {
    const value = button.dataset.lang || button.dataset.xrLang || button.dataset.ethicsLang;
    button.setAttribute("aria-pressed", String(value === selected));
  });
  window.dispatchEvent(new CustomEvent("ea:languagechange", { detail: { lang: selected } }));
}

function t(key, ...args) {
  const value = PAGE_COPY[currentPrototypeLang()]?.[key] ?? PAGE_COPY.en[key];
  return typeof value === "function" ? value(...args) : value;
}

function localizedCategoryText(category = "") {
  if (currentPrototypeLang() !== "zh") return category;
  const c = String(category).toLowerCase();
  if (c.includes("megafauna")) return "更新世巨型动物";
  if (c.includes("mammal")) return "哺乳动物";
  if (c.includes("bird")) return "鸟类";
  if (c.includes("reptile")) return "爬行动物";
  if (c.includes("amphib")) return "两栖动物";
  if (c.includes("fish")) return "鱼类";
  if (c.includes("invertebrate")) return "无脊椎动物";
  if (c.includes("insect")) return "昆虫";
  return category || "物种";
}

function localizedSpeciesName(row) {
  if (currentPrototypeLang() !== "zh") return row.common_name_en || row.scientific_name;
  if (ZH_NAME_OVERRIDES[row.scientific_name]) return ZH_NAME_OVERRIDES[row.scientific_name];
  if (hasChinese(row.common_name_zh)) return row.common_name_zh;
  return `${localizedCategoryText(row.category)}物种`;
}

function localizedRegionText(region = "") {
  if (currentPrototypeLang() === "zh") return region || "-";
  const replacements = [
    ["欧亚", "Eurasia"],
    ["欧洲", "Europe"],
    ["亚洲", "Asia"],
    ["北美", "North America"],
    ["南美", "South America"],
    ["美洲", "Americas"],
    ["非洲", "Africa"],
    ["澳大利亚/塔斯马尼亚", "Australia / Tasmania"],
    ["澳大利亚", "Australia"],
    ["塔斯马尼亚", "Tasmania"],
    ["新西兰", "New Zealand"],
    ["马达加斯加", "Madagascar"],
    ["毛里求斯", "Mauritius"],
    ["留尼汪", "Reunion"],
    ["加拉帕戈斯", "Galapagos"],
    ["夏威夷", "Hawaii"],
    ["加勒比", "Caribbean"],
    ["印度洋", "Indian Ocean"],
    ["太平洋", "Pacific"],
    ["大西洋", "Atlantic"],
    ["北极", "Arctic"],
    ["西伯利亚", "Siberia"],
    ["中国", "China"],
    ["日本海", "Sea of Japan"],
    ["日本", "Japan"],
    ["印度尼西亚", "Indonesia"],
    ["白令海", "Bering Sea"],
    ["佛得角海域", "Cape Verde marine region"]
  ];
  let text = region || "-";
  replacements.forEach(([zh, en]) => {
    text = text.replaceAll(zh, en);
  });
  text = text.replaceAll("、", ", ");
  if (/[\u3400-\u9fff]/.test(text)) return "See source range";
  return text;
}

function localizedDataText(value = "") {
  if (currentPrototypeLang() === "zh") return value || "-";
  let text = String(value || "").trim();
  if (!text) return "-";
  const replacements = [
    ["暂无", "Not available"],
    ["人类狩猎", "human hunting"],
    ["人类竞争", "human competition"],
    ["人类+气候", "human pressure + climate"],
    ["气候变暖", "climate warming"],
    ["气候变化", "climate change"],
    ["气候", "climate"],
    ["森林丧失", "forest loss"],
    ["猎物减少", "prey decline"],
    ["营养压力", "nutritional pressure"],
    ["疾病", "disease"],
    ["项目提及，最后一只录音存在", "mentioned in the project; last-known individual has recorded media"],
    ["装甲壳，触觉/视觉强", "armored shell, strong tactile and visual reconstruction potential"],
    ["触觉/视觉强", "strong tactile and visual reconstruction potential"],
    ["视觉/声音重建", "visual and sound reconstruction"],
    ["声音层叠潜力高", "high potential for layered sound design"],
    ["步态节奏适合低频音乐层", "gait rhythm suits a low-frequency music layer"],
    ["洞穴化石，冬眠节奏音乐", "cave fossils; hibernation rhythm for music design"],
    ["骨骼/迁徙路径数据", "skeletal and migration-route data"],
    ["牙齿化石推断饮食/声音", "tooth fossils inform diet and sound inference"],
    ["咬合力强，吼声模拟潜力极高", "strong bite force; very high potential for roar simulation"],
    ["毛发/皮肤化石，气味重建", "hair and skin fossils; scent reconstruction"],
    ["冻尸DNA丰富、耳结构/吼声/心率完美适合音乐层", "rich frozen DNA; ear structure, calls, and heart-rate cues suit the music layer"],
    ["确认", "confirmed"],
    ["可能灭绝", "possibly extinct"],
    ["灭绝", "extinct"],
    ["濒危", "endangered"],
    ["极危", "critically endangered"],
    ["美国东南", "southeastern United States"],
    ["美国", "United States"],
    ["北美", "North America"],
    ["南美", "South America"],
    ["美洲", "Americas"],
    ["欧洲", "Europe"],
    ["欧亚", "Eurasia"],
    ["亚洲", "Asia"],
    ["非洲", "Africa"],
    ["澳大利亚/塔斯马尼亚", "Australia / Tasmania"],
    ["澳大利亚", "Australia"],
    ["塔斯马尼亚", "Tasmania"],
    ["新西兰", "New Zealand"],
    ["中国长江", "Yangtze River, China"],
    ["中国", "China"],
    ["日本海", "Sea of Japan"],
    ["日本", "Japan"],
    ["白令海", "Bering Sea"],
    ["夏威夷", "Hawaii"],
    ["马达加斯加", "Madagascar"],
    ["毛里求斯", "Mauritius"],
    ["留尼汪", "Reunion"],
    ["加拉帕戈斯", "Galapagos"],
    ["佛得角海域", "Cape Verde marine region"],
    ["栖息地丧失", "habitat loss"],
    ["栖地破坏", "habitat destruction"],
    ["过度捕猎", "overhunting"],
    ["狩猎", "hunting"],
    ["入侵物种", "invasive species"],
    ["气候变化", "climate change"],
    ["污染", "pollution"],
    ["筑坝", "damming"],
    ["误捕", "bycatch"],
    ["人类活动", "human activity"],
    ["录音存在", "recordings exist"],
    ["无", "none"]
  ];
  replacements.forEach(([zh, en]) => {
    text = text.replaceAll(zh, en);
  });
  text = text.replace(/~?([\d,]+)年前/g, "~$1 years ago");
  text = text.replaceAll("、", ", ").replace(/\s*\+\s*/g, " + ");
  if (/[\u3400-\u9fff]/.test(text)) return "English translation pending; verify against source records.";
  return text;
}

function prototypeCopy(key, ...args) {
  const lang = currentPrototypeLang();
  const bundle = window.PROTOTYPE_COPY?.[lang] || window.PROTOTYPE_COPY?.zh;
  const value = bundle?.[key];
  return typeof value === "function" ? value(...args) : value;
}

async function loadImageManifest() {
  try {
    const res = await fetch("./webxr/assets/animal-image-manifest.json");
    if (!res.ok) return [];
    const data = await res.json();
    return Array.isArray(data.sources) ? data.sources : [];
  } catch {
    return [];
  }
}

async function loadMigrationManifest() {
  try {
    const res = await fetch("./webxr/assets/animal-migration-manifest.json");
    if (!res.ok) return [];
    const data = await res.json();
    return Array.isArray(data.sources) ? data.sources : [];
  } catch {
    return [];
  }
}

function imageSourceForSpecies(row, imageSources = []) {
  const slug = slugify(row.scientific_name || row.common_name_en || row.row_id);
  return imageSources.find(source => source.slug === slug) || null;
}

function attachMarkerImages(points, imageSources = []) {
  points.forEach(point => {
    const source = imageSourceForSpecies(point, imageSources);
    if (!source?.markerPath) return;
    const img = new Image();
    img.src = `./webxr/${source.markerPath.replace("./", "")}`;
    point.markerImage = img;
    point.imageSource = source;
  });
  return points;
}

async function loadData() {
  try {
    const [speciesRes, archivalRes] = await Promise.all([
      fetch("../data/research_extinct_animals_list.json"),
      fetch("../data/archival_media_research.json")
    ]);
    if (!speciesRes.ok || !archivalRes.ok) throw new Error("Data fetch failed");
    const speciesData = await speciesRes.json();
    const archivalData = await archivalRes.json();
    return { species: speciesData.species, archival: archivalData.species };
  } catch (e) {
    const mount = document.getElementById("archive-list");
    mount.innerHTML = `<div class="species-row">Data load failed. Start local server:<br><code>python3 -m http.server 4173</code><br>Then open <code>http://localhost:4173/prototype/</code></div>`;
    throw e;
  }
}

function heroTemplate(heroKey, imageSources = []) {
  const zhHero = {
    mammoth: {
      title: "猛犸象 - 时间生态位档案",
      summary: "北极光周期适应、冷感知，以及长距离低频声假设。",
      lines: [
        { tier: "cited", text: "猛犸基因组研究报告了与昼夜节律相关的遗传变化。" },
        { tier: "interp", text: "次声交流基于近缘象类与体型尺度进行推断建模。" },
        { tier: "spec", text: "从黎明到极夜的沉浸场景动态属于设计假设。" }
      ]
    },
    thylacine: {
      title: "袋狼 - 黄昏视觉档案",
      summary: "基于眼眶形态的昼夜行为重建，以及殖民灭绝语境。",
      lines: [
        { tier: "cited", text: "历史记录与形态学支持黄昏/夜行行为假设。" },
        { tier: "interp", text: "运动与对比度视觉界面是推断结果，并非直接测量。" },
        { tier: "spec", text: "第一人称 Umwelt 渲染仍为推测，并需明确标注。" }
      ]
    }
  };
  const h = currentPrototypeLang() === "zh" ? zhHero[heroKey] : HERO_CONTENT[heroKey];
  const speciesSlug = heroKey === "mammoth" ? "mammuthus-primigenius" : "thylacinus-cynocephalus";
  const source = imageSources.find(s => s.slug === speciesSlug);
  const tierLabel = {
    cited: currentPrototypeLang() === "zh" ? "已引用" : "cited",
    interp: currentPrototypeLang() === "zh" ? "推断" : "interp",
    spec: currentPrototypeLang() === "zh" ? "推测" : "spec"
  };
  return `
    <article class="hero-card">
      ${source ? `<img class="hero-photo" src="./webxr/${source.markerPath.replace("./", "")}" alt="${h.title}" />` : ""}
      <h3>${h.title}</h3>
      <p>${h.summary}</p>
      <ul>
        ${h.lines.map(l => `<li><span class="tag ${l.tier}">${tierLabel[l.tier] || l.tier}</span> ${l.text}</li>`).join("")}
      </ul>
    </article>`;
}

function slugify(text) {
  return text.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

function buildArchivalMap(archivalRows) {
  const map = new Map();
  archivalRows.forEach(row => map.set(row.scientific_name, row));
  return map;
}

function getSpeciesLink(r) {
  return `./species.html?slug=${encodeURIComponent(slugify(r.scientific_name))}&v=${SPECIES_DETAIL_VERSION}`;
}

function markerImg(source, alt, className = "species-thumb") {
  return source?.markerPath
    ? `<img class="${className}" src="./webxr/${source.markerPath.replace("./", "")}" alt="${alt}" loading="lazy" />`
    : `<div class="${className} thumb-fallback" aria-hidden="true">${String(alt || "?").slice(0, 1)}</div>`;
}

function renderArchive(rows, archivalMap, imageSources = []) {
  const list = document.getElementById("archive-list");
  const stats = document.getElementById("archive-stats");
  stats.textContent = t("showing", rows.length);
  list.innerHTML = rows.map(r => {
    const a = archivalMap.get(r.scientific_name);
    const source = imageSourceForSpecies(r, imageSources);
    const iucn = a?.portal_urls?.iucn_red_list_search || "#";
    const gbif = a?.portal_urls?.gbif_species_search || "#";
    return `
      <div class="species-row" id="${slugify(r.scientific_name)}">
        ${markerImg(source, r.common_name_en || r.scientific_name)}
        <strong>${localizedSpeciesName(r)}</strong>
        <span class="meta">(${r.scientific_name})</span><br>
        <span class="meta">${localizedCategoryText(r.category)} | ${t("extinction")}: ${r.extinction_summary}</span><br>
        <span class="meta">${r.extinction_drivers}</span><br>
        <a href="${getSpeciesLink(r)}">${t("openDetail")}</a>
        ${source?.sourceUrl ? `<a href="${source.sourceUrl}" target="_blank" rel="noopener noreferrer">${t("imageSource")}</a>` : ""}
        <a href="${iucn}" target="_blank" rel="noopener noreferrer">IUCN</a>
        <a href="${gbif}" target="_blank" rel="noopener noreferrer">GBIF</a>
      </div>`;
  }).join("");
}

function wireEthics() {
  const budget = document.getElementById("budget");
  const risk = document.getElementById("risk");
  const bv = document.getElementById("budget-value");
  const rv = document.getElementById("risk-value");
  const out = document.getElementById("ethics-output");

  const update = () => {
    bv.textContent = budget.value;
    rv.textContent = risk.value;
    const b = Number(budget.value);
    const r = Number(risk.value);
    if (b > 65 && r > 55) {
      out.textContent = t("high");
    } else if (b < 35 && r < 40) {
      out.textContent = t("low");
    } else {
      out.textContent = t("balanced");
    }
  };
  budget.addEventListener("input", update);
  risk.addEventListener("input", update);
  window.addEventListener("ea:languagechange", update);
  update();
}

function wireReflection() {
  const input = document.getElementById("reflection-input");
  const save = document.getElementById("save-reflection");
  const load = document.getElementById("load-reflection");
  const status = document.getElementById("reflection-status");
  const key = "umwelt_archive_reflection";

  save.addEventListener("click", () => {
    localStorage.setItem(key, input.value || "");
    status.textContent = t("saved");
  });
  load.addEventListener("click", () => {
    input.value = localStorage.getItem(key) || "";
    status.textContent = t("loaded");
  });
}

function wireHeroTabs(imageSources = []) {
  const heroMount = document.getElementById("hero-content");
  const render = (key) => {
    heroMount.innerHTML = heroTemplate(key, imageSources);
  };
  render("mammoth");
  document.querySelectorAll(".tab").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      render(btn.dataset.hero);
    });
  });
  window.addEventListener("ea:languagechange", () => {
    render(document.querySelector(".tab.active")?.dataset.hero || "mammoth");
  });
}

function fillCategoryFilter(species) {
  const select = document.getElementById("category-filter");
  const categories = [...new Set(species.map(s => s.category))];
  categories.sort().forEach(c => {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = c;
    select.appendChild(opt);
  });
}

function wireFilters(species, archivalMap, imageSources = []) {
  const search = document.getElementById("search");
  const cat = document.getElementById("category-filter");
  const av = document.getElementById("availability-filter");
  const apply = () => {
    const q = search.value.trim().toLowerCase();
    const filtered = species.filter(s => {
      const matchQ = !q ||
        s.scientific_name.toLowerCase().includes(q) ||
        (s.common_name_en || "").toLowerCase().includes(q) ||
        (s.common_name_zh || "").includes(q);
      const matchCat = !cat.value || s.category === cat.value;
      const matchAv = !av.value || s.data_availability === av.value;
      return matchQ && matchCat && matchAv;
    });
    renderArchive(filtered, archivalMap, imageSources);
  };
  [search, cat, av].forEach(el => el.addEventListener("input", apply));
  window.addEventListener("ea:languagechange", apply);
  apply();
}

function renderPortalLinks(portalUrls = {}) {
  const keys = Object.keys(portalUrls);
  if (!keys.length) return `<p>${currentPrototypeLang() === "zh" ? "暂无外部档案入口。" : "No portal links available."}</p>`;
  const zhLabels = {
    iucn_red_list_search: "红色名录",
    gbif_species_search: "物种数据库",
    gbif_occurrence_search: "分布记录",
    morphosource_search: "形态资料",
    pbdb_taxon_api: "古生物数据库",
    pbdb_classic_ui: "古生物资料",
    bhl_literature_search: "生物文献",
    eol_search: "生命百科",
    smithsonian_3d_search: "三维馆藏",
    sketchfab_search: "三维模型",
    wikipedia: "百科资料",
    xeno_canto_search: "鸟声资料",
    macaulay_library_search: "声音影像库"
  };
  return `<div class="portal-list">${keys.map(k => {
    const label = currentPrototypeLang() === "zh" ? (zhLabels[k] || "外部资料") : (PORTAL_LABELS[k] || k);
    const url = portalUrls[k];
    return `<a href="${url}" target="_blank" rel="noopener noreferrer">${label}</a>`;
  }).join("")}</div>`;
}

function parseQuery() {
  const p = new URLSearchParams(window.location.search);
  return Object.fromEntries(p.entries());
}

function renderSpeciesDetail(species, archivalMap, slug, imageSources = []) {
  const mount = document.getElementById("species-detail");
  const hit = species.find(s => slugify(s.scientific_name) === slug);
  if (!hit) {
    mount.innerHTML = `<p>${t("notFound", slug)}</p>`;
    return;
  }
  const arch = archivalMap.get(hit.scientific_name);
  const curated = arch?.notable_archives_curated || [];
  const source = imageSourceForSpecies(hit, imageSources);
  const isZh = currentPrototypeLang() === "zh";
  const exhibitBlocks = [
    { title: isZh ? "灭绝与原因" : "Extinction context", content: localizedDataText(hit.extinction_drivers || "-") },
    { title: isZh ? "背景说明" : "Context notes", content: localizedDataText(hit.notes || (isZh ? "暂无" : "—")) },
    { title: isZh ? "核实说明" : "Verification", content: localizedDataText(hit.verification_note || (isZh ? "建议对照红色名录与一手文献。" : "Validate via IUCN and primary sources.")) }
  ];
  const maybeChineseName = isZh ? `<p><strong>${t("chineseName")}:</strong> ${hit.common_name_zh || "-"}</p>` : "";
  mount.innerHTML = `
    <div class="species-detail-head">
      ${markerImg(source, hit.common_name_en || hit.scientific_name, "species-detail-photo")}
      <div>
        <h2>${localizedSpeciesName(hit)} <span class="meta">(${hit.scientific_name})</span></h2>
        ${maybeChineseName}
        <p><strong>${t("category")}:</strong> ${localizedCategoryText(hit.category)} | <strong>${t("extinction")}:</strong> ${localizedDataText(hit.extinction_summary)} | <strong>${t("region")}:</strong> ${localizedRegionText(hit.region)}</p>
        <p><strong>${t("drivers")}:</strong> ${localizedDataText(hit.extinction_drivers)}</p>
        <p><strong>${t("notes")}:</strong> ${localizedDataText(hit.notes || "-")}</p>
        <p><strong>${t("verification")}:</strong> ${localizedDataText(hit.verification_note || "-")}</p>
        ${source?.sourceUrl ? `<p><a href="${source.sourceUrl}" target="_blank" rel="noopener noreferrer">${t("imageSource")}</a></p>` : ""}
      </div>
    </div>

    <h3>${t("exhibitBlocks")}</h3>
    <div class="cards-grid">
      ${exhibitBlocks.map(b => `
        <div class="species-row">
          <strong>${b.title}</strong>
          <p class="meta">${b.content}</p>
        </div>
      `).join("")}
    </div>

    <h3>${t("portals")}</h3>
    ${renderPortalLinks(arch?.portal_urls)}

    <h3>${t("curated")}</h3>
    <ul>
      ${curated.length ? curated.map(c => `<li><strong>${c.type}</strong>: ${localizedDataText(c.label)} (<a href="${c.url}" target="_blank" rel="noopener noreferrer">${isZh ? "打开" : "open"}</a>)</li>`).join("") : `<li>${isZh ? "暂无策展线索。" : "No curated hints yet."}</li>`}
    </ul>

    <h3>${t("protocol")}</h3>
    <ul>
      ${(arch?.research_protocol || [isZh ? "暂无协议备注。" : "No protocol notes"]).map(x => `<li>${localizedDataText(x)}</li>`).join("")}
    </ul>
  `;
}

function regionToAnchor(region = "") {
  const r = region.toLowerCase();
  const has = (...tokens) => tokens.some(t => r.includes(t));
  if (has("北美", "north america", "canada", "united states", "alaska")) return { lat: 46, lon: -100 };
  if (has("南美", "south america", "brazil", "argentina", "chile")) return { lat: -15, lon: -60 };
  if (has("欧洲", "europe")) return { lat: 51, lon: 10 };
  if (has("亚洲", "asia", "西伯利亚", "china", "japan", "indonesia")) return { lat: 35, lon: 90 };
  if (has("澳大利亚", "tasmania", "australia")) return { lat: -25, lon: 134 };
  if (has("非洲", "africa")) return { lat: 5, lon: 20 };
  if (has("白令", "arctic", "北极")) return { lat: 66, lon: -170 };
  if (has("毛里求斯", "madagascar", "reunion", "加拉帕戈斯", "galapagos")) return { lat: -15, lon: 65 };
  return { lat: 10, lon: 0 };
}

function seededRand(seed) {
  const x = Math.sin(seed) * 10000;
  return x - Math.floor(x);
}

function migrationPointForSpecies(row, migrationSources = []) {
  const rowSlug = slugify(row.scientific_name || row.common_name_en || row.row_id);
  const match = migrationSources.find(source => source.slug === rowSlug || source.scientificName === row.scientific_name);
  const waypoint = match?.waypoints?.[Math.floor((match.waypoints?.length || 1) / 2)];
  if (!waypoint) return null;
  return { lat: waypoint.lat, lon: waypoint.lon };
}

function speciesToPoints(species, migrationSources = []) {
  return species.map((s, idx) => {
    const migrationPoint = migrationPointForSpecies(s, migrationSources);
    const anchor = regionToAnchor(s.region || "");
    const jitterLat = (seededRand(idx + 1) - 0.5) * 10;
    const jitterLon = (seededRand(idx + 91) - 0.5) * 14;
    return {
      ...s,
      slug: slugify(s.scientific_name),
      lat: migrationPoint ? migrationPoint.lat : Math.max(-75, Math.min(75, anchor.lat + jitterLat)),
      lon: migrationPoint ? migrationPoint.lon : anchor.lon + jitterLon
    };
  });
}

function categoryIcon(category = "") {
  const c = category.toLowerCase();
  if (c.includes("bird")) return "B";
  if (c.includes("mammal")) return "M";
  if (c.includes("reptile")) return "R";
  if (c.includes("amphib")) return "A";
  if (c.includes("fish")) return "F";
  if (c.includes("invertebrate")) return "I";
  if (c.includes("insect")) return "N";
  if (c.includes("megafauna")) return "G";
  return "S";
}

function categoryColor(category = "") {
  const c = category.toLowerCase();
  if (c.includes("bird")) return "#f6e7a3";
  if (c.includes("mammal")) return "#f3c8c8";
  if (c.includes("reptile")) return "#c8edbf";
  if (c.includes("amphib")) return "#afe7e8";
  if (c.includes("fish")) return "#b8d8ff";
  if (c.includes("invertebrate")) return "#dfc9f7";
  if (c.includes("insect")) return "#fde3b8";
  if (c.includes("megafauna")) return "#ffd4b1";
  return "#d0def2";
}

function projectPoint(latDeg, lonDeg, rotDeg, cx, cy, radius, zoom = 1) {
  const lat = (latDeg * Math.PI) / 180;
  const lon = ((lonDeg + rotDeg) * Math.PI) / 180;
  const x3 = Math.cos(lat) * Math.sin(lon);
  const y3 = Math.sin(lat);
  const z3 = Math.cos(lat) * Math.cos(lon);
  if (z3 <= 0) return null;
  return {
    x: cx + x3 * radius * zoom,
    y: cy - y3 * radius * zoom,
    z: z3
  };
}

function mapProject(lat, lon, bounds) {
  return {
    x: bounds.left + ((lon + 180) / 360) * bounds.width,
    y: bounds.top + ((90 - lat) / 180) * bounds.height
  };
}

function pointInPolygon(lon, lat, polygon) {
  let inside = false;
  for (let i = 0, j = polygon.length - 1; i < polygon.length; j = i++) {
    const xi = polygon[i][0];
    const yi = polygon[i][1];
    const xj = polygon[j][0];
    const yj = polygon[j][1];
    const intersects = ((yi > lat) !== (yj > lat)) && (lon < ((xj - xi) * (lat - yi)) / (yj - yi) + xi);
    if (intersects) inside = !inside;
  }
  return inside;
}

function drawDottedPolygon(ctx, bounds, polygon, color, dotStep = 3.2) {
  const lons = polygon.map(p => p[0]);
  const lats = polygon.map(p => p[1]);
  const minLon = Math.floor(Math.min(...lons));
  const maxLon = Math.ceil(Math.max(...lons));
  const minLat = Math.floor(Math.min(...lats));
  const maxLat = Math.ceil(Math.max(...lats));

  for (let lat = minLat; lat <= maxLat; lat += dotStep) {
    for (let lon = minLon; lon <= maxLon; lon += dotStep) {
      if (!pointInPolygon(lon, lat, polygon)) continue;
      const keep = seededRand(lon * 12.9898 + lat * 78.233) > 0.08;
      if (!keep) continue;
      const p = mapProject(lat, lon, bounds);
      ctx.beginPath();
      ctx.fillStyle = color;
      ctx.arc(p.x, p.y, 1.35, 0, Math.PI * 2);
      ctx.fill();
    }
  }
}

function drawDottedWorldMap(ctx, bounds) {
  const colors = {
    america: "rgba(108, 182, 191, 0.48)",
    europe: "rgba(157, 191, 107, 0.46)",
    asia: "rgba(222, 181, 91, 0.46)",
    africa: "rgba(216, 195, 106, 0.44)",
    oceania: "rgba(207, 156, 166, 0.42)"
  };
  const land = [
    {
      color: colors.america,
      polygon: [[-168, 62], [-150, 72], [-120, 74], [-88, 68], [-56, 52], [-67, 34], [-83, 20], [-104, 16], [-125, 28], [-150, 45]]
    },
    {
      color: colors.america,
      polygon: [[-74, 83], [-22, 79], [-18, 64], [-42, 58], [-65, 66]]
    },
    {
      color: colors.america,
      polygon: [[-111, 31], [-86, 23], [-78, 8], [-84, 7], [-100, 18]]
    },
    {
      color: colors.america,
      polygon: [[-80, 12], [-60, 6], [-36, -14], [-48, -55], [-67, -55], [-78, -22]]
    },
    {
      color: colors.europe,
      polygon: [[-11, 36], [0, 58], [25, 70], [48, 58], [40, 42], [18, 34]]
    },
    {
      color: colors.africa,
      polygon: [[-18, 34], [30, 36], [52, 12], [42, -34], [18, -36], [-8, -28], [-17, 5]]
    },
    {
      color: colors.asia,
      polygon: [[32, 36], [46, 58], [75, 70], [145, 70], [168, 56], [150, 38], [130, 28], [114, 12], [96, 6], [78, 8], [62, 24], [45, 26]]
    },
    {
      color: colors.asia,
      polygon: [[65, 31], [89, 30], [95, 8], [78, 6]]
    },
    {
      color: colors.asia,
      polygon: [[100, 22], [122, 22], [128, 3], [112, -8], [98, 8]]
    },
    {
      color: colors.asia,
      polygon: [[128, 43], [146, 46], [146, 32], [132, 31]]
    },
    {
      color: colors.asia,
      polygon: [[95, 4], [136, 7], [150, -8], [126, -13], [104, -6]]
    },
    {
      color: colors.oceania,
      polygon: [[112, -12], [154, -11], [153, -39], [132, -44], [114, -31]]
    },
    {
      color: colors.oceania,
      polygon: [[166, -34], [179, -39], [174, -47], [166, -45]]
    },
    {
      color: colors.africa,
      polygon: [[43, -13], [51, -17], [49, -26], [44, -25]]
    }
  ];

  land.forEach(piece => drawDottedPolygon(ctx, bounds, piece.polygon, piece.color));
}

function drawMemorialPoint(ctx, point) {
  const { x, y, r, pulse, isActive, isHover } = point;
  const activeBoost = isActive ? 1.9 : isHover ? 1.45 : 1;
  const ring = r + 1.4 * activeBoost;

  ctx.save();
  ctx.shadowColor = isActive
    ? `rgba(36, 97, 106, ${0.42 + pulse * 0.26})`
    : `rgba(28, 154, 177, ${0.26 + pulse * 0.2})`;
  ctx.shadowBlur = isActive ? 14 + pulse * 10 : 4 + pulse * 8;
  ctx.strokeStyle = isActive
    ? "rgba(36, 97, 106, 0.96)"
    : isHover
      ? "rgba(28, 130, 150, 0.9)"
      : `rgba(18, 137, 161, ${0.6 + pulse * 0.18})`;
  ctx.lineWidth = isActive || isHover ? 2.4 : 1.7;
  ctx.beginPath();
  ctx.arc(x, y, ring, 0, Math.PI * 2);
  ctx.stroke();
  ctx.fillStyle = isActive
    ? "rgba(36, 97, 106, 0.86)"
    : `rgba(32, 150, 174, ${0.48 + pulse * 0.16})`;
  ctx.beginPath();
  ctx.arc(x, y, r * activeBoost, 0, Math.PI * 2);
  ctx.fill();
  ctx.fillStyle = "rgba(255,255,255,0.94)";
  ctx.beginPath();
  ctx.arc(x, y, Math.max(1.05, r * 0.3), 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
}

function findNearestScreenPoint(points, x, y) {
  let best = null;
  let bestDistance = Infinity;
  for (const point of points) {
    const dx = x - point.x;
    const dy = y - point.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    if (distance <= point.hitRadius && distance < bestDistance) {
      best = point;
      bestDistance = distance;
    }
  }
  return best;
}

function drawLandBlob(ctx, lat, lon, width, height, rotationDeg, cx, cy, radius, zoom, color) {
  const p = projectPoint(lat, lon, rotationDeg, cx, cy, radius, zoom);
  if (!p) return;
  const perspective = 0.55 + p.z * 0.45;
  ctx.save();
  ctx.translate(p.x, p.y);
  ctx.rotate(((lon + rotationDeg) % 35) * Math.PI / 180);
  ctx.scale(perspective, perspective * (0.82 + p.z * 0.18));
  ctx.beginPath();
  ctx.ellipse(0, 0, width * zoom, height * zoom, 0, 0, Math.PI * 2);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.restore();
}

function drawEarthSurface(ctx, rotation, cx, cy, radius, zoom) {
  const land = "rgba(72, 122, 96, 0.68)";
  const dry = "rgba(126, 111, 86, 0.58)";
  const ice = "rgba(190, 225, 232, 0.7)";

  // Simplified continental masses for a more Earth-like read, not a GIS map.
  drawLandBlob(ctx, 48, -104, 66, 34, rotation, cx, cy, radius, zoom, land);
  drawLandBlob(ctx, 18, -86, 30, 18, rotation, cx, cy, radius, zoom, "rgba(72, 126, 74, 0.78)");
  drawLandBlob(ctx, -19, -60, 32, 62, rotation, cx, cy, radius, zoom, land);
  drawLandBlob(ctx, 7, 21, 42, 58, rotation, cx, cy, radius, zoom, dry);
  drawLandBlob(ctx, 51, 18, 32, 20, rotation, cx, cy, radius, zoom, "rgba(94, 142, 88, 0.82)");
  drawLandBlob(ctx, 47, 82, 86, 42, rotation, cx, cy, radius, zoom, land);
  drawLandBlob(ctx, 24, 78, 48, 28, rotation, cx, cy, radius, zoom, dry);
  drawLandBlob(ctx, -25, 134, 36, 22, rotation, cx, cy, radius, zoom, dry);
  drawLandBlob(ctx, 72, -42, 34, 14, rotation, cx, cy, radius, zoom, ice);
  drawLandBlob(ctx, -72, 20, 120, 16, rotation, cx, cy, radius, zoom, ice);
}

function drawCityLightCluster(ctx, lat, lon, count, spread, rotationDeg, cx, cy, radius, zoom) {
  for (let i = 0; i < count; i++) {
    const jitterLat = (seededRand((lat + i) * 8.91) - 0.5) * spread;
    const jitterLon = (seededRand((lon + i) * 13.37) - 0.5) * spread * 1.55;
    const p = projectPoint(lat + jitterLat, lon + jitterLon, rotationDeg, cx, cy, radius, zoom);
    if (!p) continue;
    const alpha = 0.18 + p.z * 0.72;
    const size = 0.65 + seededRand(i * 19.3 + lat) * 1.6;
    ctx.save();
    ctx.shadowColor = `rgba(255, 207, 120, ${alpha})`;
    ctx.shadowBlur = 5 + p.z * 8;
    ctx.fillStyle = `rgba(255, 218, 138, ${alpha})`;
    ctx.beginPath();
    ctx.arc(p.x, p.y, size, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

function drawCityLights(ctx, rotation, cx, cy, radius, zoom) {
  // Dense clusters approximate the "night Earth" reference image:
  // North America, Europe, Middle East / India, East Asia.
  drawCityLightCluster(ctx, 40, -96, 90, 18, rotation, cx, cy, radius, zoom);
  drawCityLightCluster(ctx, 43, -74, 46, 10, rotation, cx, cy, radius, zoom);
  drawCityLightCluster(ctx, 50, 8, 110, 16, rotation, cx, cy, radius, zoom);
  drawCityLightCluster(ctx, 31, 35, 38, 9, rotation, cx, cy, radius, zoom);
  drawCityLightCluster(ctx, 22, 78, 82, 18, rotation, cx, cy, radius, zoom);
  drawCityLightCluster(ctx, 35, 116, 86, 16, rotation, cx, cy, radius, zoom);
  drawCityLightCluster(ctx, 36, 138, 36, 7, rotation, cx, cy, radius, zoom);
}

function drawGlobe(ctx, canvas, state) {
  const w = canvas.clientWidth || window.innerWidth;
  const h = canvas.clientHeight || window.innerHeight;
  const now = state.blinkTime ?? performance.now();

  ctx.clearRect(0, 0, w, h);
  const bg = ctx.createLinearGradient(0, 0, w, h);
  bg.addColorStop(0, "#fffdf8");
  bg.addColorStop(0.58, "#f8faf6");
  bg.addColorStop(1, "#eef5f2");
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, w, h);

  const bounds = {
    left: w * 0.25,
    top: h * 0.18,
    width: w * 0.7,
    height: h * 0.62
  };

  ctx.save();
  ctx.globalCompositeOperation = "source-over";
  drawDottedWorldMap(ctx, bounds);
  ctx.restore();

  ctx.save();
  const mapTitle = prototypeCopy("mapTitle") || "EXTINCTION DOT MAP";
  const mapSubtitle = prototypeCopy("mapSubtitle") || "54 MEMORIAL POINTS · EXTINCT SPECIES";
  ctx.fillStyle = "rgba(36, 97, 106, 0.94)";
  ctx.font = `720 ${Math.max(23, Math.min(54, w * 0.04))}px -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif`;
  ctx.letterSpacing = currentPrototypeLang() === "zh" ? "0.12em" : "0.08em";
  ctx.textAlign = "center";
  ctx.fillText(mapTitle, bounds.left + bounds.width * 0.5, h * 0.105);
  ctx.fillStyle = "rgba(36, 97, 106, 0.78)";
  ctx.font = `700 ${Math.max(12, Math.min(22, w * 0.016))}px -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif`;
  ctx.fillText(mapSubtitle, bounds.left + bounds.width * 0.5, h * 0.15);
  ctx.restore();

  // latitude and longitude guides are intentionally removed for the flat dot-map style.

  // Blinking memorial points: all breathe; hovered/selected points are drawn last.
  state.screenPoints = [];
  const pointDraws = [];
  for (const item of state.points) {
    const p = mapProject(item.lat, item.lon, bounds);
    const pulse = 0.5 + 0.5 * Math.sin(now / 520 + item.lat * 0.37 + item.lon * 0.11);
    const r = 2.4 + pulse * 1.4;
    const isActive = item.slug === state.selectedSlug;
    const isHover = item.slug === state.hoverSlug;

    pointDraws.push({
      x: p.x,
      y: p.y,
      r,
      pulse,
      isActive,
      isHover,
      item,
      z: isActive ? 2 : isHover ? 1 : 0
    });
    state.screenPoints.push({ x: p.x, y: p.y, r, hitRadius: isActive || isHover ? 16 : 12, item });
  }
  pointDraws
    .sort((a, b) => a.z - b.z)
    .forEach(point => drawMemorialPoint(ctx, point));
}

function popupHtml(item, archivalMap) {
  const a = archivalMap.get(item.scientific_name);
  const iucn = a?.portal_urls?.iucn_red_list_search || "#";
  const isZh = currentPrototypeLang() === "zh";
  const title = isZh ? localizedSpeciesName(item) : (item.common_name_en || item.scientific_name);
  const secondaryName = isZh && item.common_name_en ? `<p>${item.common_name_en}</p>` : "";
  const region = localizedRegionText(item.region || "-");
  return `
    <h3>${title}</h3>
    ${secondaryName}
    <p>${item.scientific_name}</p>
    <p>${item.category} · ${item.extinction_summary}</p>
    <p>${region}</p>
    <a href="./species.html?slug=${encodeURIComponent(item.slug)}&v=${SPECIES_DETAIL_VERSION}">${prototypeCopy("open") || (currentPrototypeLang() === "zh" ? "打开物种档案" : "Open species dossier")}</a>
    <a href="${iucn}" target="_blank" rel="noopener noreferrer">IUCN</a>
  `;
}

function ensureLanguageSwitch() {
  const header = document.querySelector(".top");
  if (!header || header.querySelector(".page-lang-switch")) return;
  const switcher = document.createElement("div");
  switcher.className = "page-lang-switch";
  switcher.innerHTML = `
    <button type="button" data-lang="zh">中文</button>
    <button type="button" data-lang="en">EN</button>
  `;
  header.appendChild(switcher);
  switcher.querySelectorAll("[data-lang]").forEach(button => {
    button.addEventListener("click", () => setGlobalLanguage(button.dataset.lang));
  });
}

function updatePageChrome() {
  const page = document.body.dataset.page;
  document.documentElement.lang = currentPrototypeLang() === "zh" ? "zh-Hans" : "en";
  document.querySelectorAll("[data-lang]").forEach(button => {
    button.setAttribute("aria-pressed", String(button.dataset.lang === currentPrototypeLang()));
  });

  const title = document.querySelector(".top h1");
  const lead = document.querySelector(".top p");
  const nav = document.querySelectorAll(".main-nav a");
  if (page === "archive") {
    document.title = `${t("archive")} - Umwelt Archive`;
    if (title) title.textContent = t("archiveTitle");
    if (lead) lead.textContent = t("archiveLead");
    const search = document.getElementById("search");
    if (search) search.placeholder = t("searchPlaceholder");
    const cat = document.getElementById("category-filter")?.querySelector("option[value='']");
    const av = document.getElementById("availability-filter")?.querySelector("option[value='']");
    if (cat) cat.textContent = t("allCategories");
    if (av) av.textContent = t("allAvailability");
  }
  if (page === "hero") {
    document.title = `${t("hero")} - Umwelt Archive`;
    if (title) title.textContent = t("heroTitle");
    if (lead) lead.textContent = t("heroLead");
    document.querySelector(".ethics h2") && (document.querySelector(".ethics h2").textContent = t("ethics"));
    document.querySelector(".reflection h2") && (document.querySelector(".reflection h2").textContent = t("reflection"));
    const labels = document.querySelectorAll(".ethics label");
    if (labels[0]) labels[0].childNodes[0].textContent = t("budget");
    if (labels[1]) labels[1].childNodes[0].textContent = t("risk");
    const input = document.getElementById("reflection-input");
    if (input) input.placeholder = t("reflectionPlaceholder");
    document.getElementById("save-reflection") && (document.getElementById("save-reflection").textContent = t("save"));
    document.getElementById("load-reflection") && (document.getElementById("load-reflection").textContent = t("load"));
    const tabs = document.querySelectorAll(".hero-tabs .tab");
    if (tabs[0]) tabs[0].textContent = currentPrototypeLang() === "zh" ? "猛犸象" : "Woolly Mammoth";
    if (tabs[1]) tabs[1].textContent = currentPrototypeLang() === "zh" ? "袋狼" : "Thylacine";
    const legend = document.querySelectorAll(".tier-legend .tag");
    if (legend[0]) legend[0].textContent = currentPrototypeLang() === "zh" ? "已引用" : "Cited";
    if (legend[1]) legend[1].textContent = currentPrototypeLang() === "zh" ? "推断" : "Interpolated";
    if (legend[2]) legend[2].textContent = currentPrototypeLang() === "zh" ? "推测" : "Speculative";
  }
  if (page === "species") {
    document.title = `${t("detail")} - Umwelt Archive`;
    if (title) title.textContent = t("speciesTitle");
    if (lead) lead.textContent = t("speciesLead");
  }
  if (nav[0]) nav[0].textContent = t("home");
  if (nav[1]) nav[1].textContent = page === "archive" ? t("hero") : t("archive");
  if (nav[2]) nav[2].textContent = t("hero");
}

function setupLanguage() {
  ensureLanguageSwitch();
  setGlobalLanguage(currentPrototypeLang());
  updatePageChrome();
  window.addEventListener("ea:languagechange", updatePageChrome);
}

async function initHome() {
  const canvas = document.getElementById("globe-canvas");
  const popup = document.getElementById("point-popup");
  const countLine = document.getElementById("species-count-line");
  const toggle = document.getElementById("toggle-autorotate");
  if (!canvas || !popup || !countLine || !toggle) return;

  const [{ species, archival }, imageSources, migrationSources] = await Promise.all([
    loadData(),
    loadImageManifest(),
    loadMigrationManifest()
  ]);
  const archivalMap = buildArchivalMap(archival);
  const points = attachMarkerImages(speciesToPoints(species, migrationSources), imageSources);
  const updateChrome = () => {
    countLine.textContent =
      prototypeCopy("count", species.length) ||
      `This globe includes ${species.length} extinct species linked to human activity.`;
    toggle.textContent = state.autoRotate
      ? (prototypeCopy("pause") || "Pause Rotate")
      : (prototypeCopy("resume") || "Resume Rotate");
  };

  const ctx = canvas.getContext("2d");
  const state = {
    rotation: 0,
    zoom: 1,
    offsetX: 0,
    offsetY: 0,
    points,
    screenPoints: [],
    hoverSlug: null,
    selectedSlug: null,
    blinkTime: 0,
    autoRotate: true,
    dragging: false,
    dragStartX: 0,
    dragStartY: 0
  };
  updateChrome();
  window.addEventListener("prototype:languagechange", updateChrome);

  function resize() {
    canvas.width = window.innerWidth * window.devicePixelRatio;
    canvas.height = window.innerHeight * window.devicePixelRatio;
    ctx.setTransform(window.devicePixelRatio, 0, 0, window.devicePixelRatio, 0, 0);
  }
  resize();
  window.addEventListener("resize", resize);

  function frame() {
    if (state.autoRotate) state.blinkTime += 16.7;
    drawGlobe(ctx, canvas, state);
    requestAnimationFrame(frame);
  }
  frame();

  toggle.addEventListener("click", () => {
    state.autoRotate = !state.autoRotate;
    updateChrome();
  });

  canvas.addEventListener("mousemove", e => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const hit = findNearestScreenPoint(state.screenPoints, x, y);
    state.hoverSlug = hit?.item.slug || null;
    canvas.style.cursor = hit ? "pointer" : "default";
  });

  canvas.addEventListener("mouseleave", () => {
    state.hoverSlug = null;
    canvas.style.cursor = "default";
  });

  canvas.addEventListener("click", e => {
    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const hit = findNearestScreenPoint(state.screenPoints, x, y);
    if (!hit) {
      popup.classList.add("hidden");
      state.selectedSlug = null;
      state.hoverSlug = null;
      return;
    }
    state.selectedSlug = hit.item.slug;
    state.hoverSlug = hit.item.slug;
    popup.innerHTML = popupHtml(hit.item, archivalMap);
    popup.style.left = `${Math.min(window.innerWidth - 340, x + 18)}px`;
    popup.style.top = `${Math.min(window.innerHeight - 180, y + 18)}px`;
    popup.classList.remove("hidden");
  });
}

async function initHeroPage() {
  const imageSources = await loadImageManifest();
  wireHeroTabs(imageSources);
  wireEthics();
  wireReflection();
}

async function initArchivePage() {
  const [{ species, archival }, imageSources] = await Promise.all([loadData(), loadImageManifest()]);
  const archivalMap = buildArchivalMap(archival);
  fillCategoryFilter(species);
  wireFilters(species, archivalMap, imageSources);
}

async function initSpeciesPage() {
  const [{ species, archival }, imageSources] = await Promise.all([loadData(), loadImageManifest()]);
  const archivalMap = buildArchivalMap(archival);
  const query = parseQuery();
  const render = () => renderSpeciesDetail(species, archivalMap, query.slug || "", imageSources);
  render();
  window.addEventListener("ea:languagechange", render);
}

async function init() {
  setupLanguage();
  const page = document.body.dataset.page;
  if (page === "home") return initHome();
  if (page === "hero") return initHeroPage();
  if (page === "archive") return initArchivePage();
  if (page === "species") return initSpeciesPage();
}

init().catch(console.error);
