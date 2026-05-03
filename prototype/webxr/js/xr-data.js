/** Shared dataset + helpers for WebXR Extinction Archive prototype */

export const PORTAL_LABELS = {
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

export const XR_VERSION = "site-lang-unified-v2-20260503";
const DATA_BASE = "../../data/";

export async function loadDataset() {
  const [speciesRes, archivalRes] = await Promise.all([
    fetch(`${DATA_BASE}research_extinct_animals_list.json`),
    fetch(`${DATA_BASE}archival_media_research.json`)
  ]);
  if (!speciesRes.ok || !archivalRes.ok) throw new Error("Data fetch failed");
  const speciesData = await speciesRes.json();
  const archivalData = await archivalRes.json();
  return { species: speciesData.species, archival: archivalData.species, meta: speciesData.meta };
}

export function slugify(text) {
  return String(text).toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
}

export function buildArchivalMap(archivalRows) {
  const map = new Map();
  archivalRows.forEach(row => map.set(row.scientific_name, row));
  return map;
}

export function regionToAnchor(region = "") {
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

export function speciesToPoints(species) {
  return species.map((s, idx) => {
    const anchor = regionToAnchor(s.region || "");
    const jitterLat = (seededRand(idx + 1) - 0.5) * 10;
    const jitterLon = (seededRand(idx + 91) - 0.5) * 14;
    return {
      ...s,
      slug: slugify(s.scientific_name),
      lat: Math.max(-75, Math.min(75, anchor.lat + jitterLat)),
      lon: anchor.lon + jitterLon
    };
  });
}

/** Spherical coords aligned with common Three.js globe examples (Y up). */
export function latLonToPosition(latDeg, lonDeg, radius, target) {
  const phi = ((90 - latDeg) * Math.PI) / 180;
  const theta = ((lonDeg + 180) * Math.PI) / 180;
  target.x = -radius * Math.sin(phi) * Math.cos(theta);
  target.y = radius * Math.cos(phi);
  target.z = radius * Math.sin(phi) * Math.sin(theta);
  return target;
}

export function categoryColorHex(category = "") {
  const c = category.toLowerCase();
  if (c.includes("bird")) return 0xf6e7a3;
  if (c.includes("mammal")) return 0xf3c8c8;
  if (c.includes("reptile")) return 0xc8edbf;
  if (c.includes("amphib")) return 0xafe7e8;
  if (c.includes("fish")) return 0xb8d8ff;
  if (c.includes("invertebrate")) return 0xdfc9f7;
  if (c.includes("insect")) return 0xfde3b8;
  if (c.includes("megafauna")) return 0xffd4b1;
  return 0xd0def2;
}

export function getSpeciesLink(slug, { fragment, view } = {}) {
  const params = new URLSearchParams();
  params.set("slug", String(slug));
  if (view) params.set("view", String(view));
  params.set("v", XR_VERSION);
  let u = `./species.html?${params.toString()}`;
  if (fragment) u += `#${String(fragment).replace(/^#/, "")}`;
  return u;
}

export function englishValue(value = "") {
  let text = String(value || "").trim();
  if (!text) return "";
  const replacements = [
    ["暂无策展线索。", "No curated leads yet."],
    ["暂无外部档案入口。", "No external archive links yet."],
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
