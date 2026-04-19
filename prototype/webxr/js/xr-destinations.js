import { loadDataset, slugify, getSpeciesLink } from "./xr-data.js";

const FIELD_ORDER = [
  "row_id",
  "list_source",
  "category",
  "common_name_zh",
  "common_name_en",
  "common_name_raw",
  "scientific_name",
  "extinction_summary",
  "region",
  "sensory_reconstruction_score",
  "music_layering_score",
  "data_availability",
  "model_3d_ref",
  "extinction_drivers",
  "notes",
  "pharm_human_hook",
  "verification_note"
];

const LABELS = {
  row_id: "Row",
  list_source: "Source",
  category: "Category",
  common_name_zh: "中文名",
  common_name_en: "English",
  common_name_raw: "Raw name",
  scientific_name: "Scientific",
  extinction_summary: "Extinction",
  region: "Region",
  sensory_reconstruction_score: "Sensory",
  music_layering_score: "Music",
  data_availability: "Data",
  model_3d_ref: "3D ref",
  extinction_drivers: "Drivers",
  notes: "Notes",
  pharm_human_hook: "Pharm / human hook",
  verification_note: "Verification"
};

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

export async function initDestinations() {
  const metaEl = document.getElementById("xr-dest-meta");
  const thead = document.querySelector("#xr-dest-table thead tr");
  const tbody = document.getElementById("xr-dest-body");
  const search = document.getElementById("xr-d-search");
  const cat = document.getElementById("xr-d-cat");
  const av = document.getElementById("xr-d-avail");

  const { species, meta } = await loadDataset();

  if (metaEl && meta) {
    metaEl.textContent = `Dataset: ${meta.counts?.total_rows ?? species.length} taxa · ${meta.disclaimer || ""}`;
  }

  const categories = [...new Set(species.map(s => s.category))].sort();
  categories.forEach(c => {
    const opt = document.createElement("option");
    opt.value = c;
    opt.textContent = c;
    cat.appendChild(opt);
  });

  thead.innerHTML = `<th>Detail</th>${FIELD_ORDER.map(
    k => `<th title="${esc(LABELS[k] || k)}">${esc(LABELS[k] || k)}</th>`
  ).join("")}`;

  function render(rows) {
    tbody.innerHTML = rows
      .map(r => {
        const slug = slugify(r.scientific_name);
        const cells = FIELD_ORDER.map(k => {
          const v = r[k];
          const long = k === "notes" || k === "verification_note" || k === "extinction_drivers";
          return `<td class="${long ? "long" : ""}">${esc(v)}</td>`;
        }).join("");
        return `<tr><td><a href="${getSpeciesLink(slug)}">Open</a></td>${cells}</tr>`;
      })
      .join("");
  }

  function apply() {
    const q = search.value.trim().toLowerCase();
    const filtered = species.filter(s => {
      const matchQ =
        !q ||
        String(s.scientific_name).toLowerCase().includes(q) ||
        String(s.common_name_en || "").toLowerCase().includes(q) ||
        String(s.common_name_zh || "").includes(q);
      const matchCat = !cat.value || s.category === cat.value;
      const matchAv = !av.value || s.data_availability === av.value;
      return matchQ && matchCat && matchAv;
    });
    render(filtered);
    document.getElementById("xr-d-count").textContent = `${filtered.length} / ${species.length} destinations`;
  }

  [search, cat, av].forEach(el => el.addEventListener("input", apply));
  apply();
}
