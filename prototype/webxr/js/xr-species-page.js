import {
  loadDataset,
  buildArchivalMap,
  slugify,
  PORTAL_LABELS
} from "./xr-data.js";

function parseQuery() {
  return Object.fromEntries(new URLSearchParams(window.location.search).entries());
}

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function renderPortalLinks(portalUrls = {}) {
  const keys = Object.keys(portalUrls);
  if (!keys.length) return "<p class=\"xr-muted\">No portal links.</p>";
  return `<div class="xr-portals">${keys
    .map(k => {
      const label = PORTAL_LABELS[k] || k;
      const url = String(portalUrls[k] || "#").replace(/"/g, "%22");
      return `<a href="${url}" target="_blank" rel="noopener noreferrer">${esc(label)}</a>`;
    })
    .join("")}</div>`;
}

export async function initSpeciesPage() {
  const mount = document.getElementById("xr-species-mount");
  const query = parseQuery();
  const slug = query.slug || "";

  const { species, archival } = await loadDataset();
  const archivalMap = buildArchivalMap(archival);
  const hit = species.find(s => slugify(s.scientific_name) === slug);

  if (!hit) {
    mount.innerHTML = `<p>未找到物种档案（slug: <code>${esc(slug || "(empty)")}</code>）</p>`;
    return;
  }

  const arch = archivalMap.get(hit.scientific_name);
  const curated = arch?.notable_archives_curated || [];

  const rows = [
    ["row_id", hit.row_id],
    ["list_source", hit.list_source],
    ["category", hit.category],
    ["common_name_zh", hit.common_name_zh],
    ["common_name_en", hit.common_name_en],
    ["common_name_raw", hit.common_name_raw],
    ["scientific_name", hit.scientific_name],
    ["extinction_summary", hit.extinction_summary],
    ["region", hit.region],
    ["sensory_reconstruction_score", hit.sensory_reconstruction_score],
    ["music_layering_score", hit.music_layering_score],
    ["data_availability", hit.data_availability],
    ["model_3d_ref", hit.model_3d_ref],
    ["extinction_drivers", hit.extinction_drivers],
    ["notes", hit.notes],
    ["pharm_human_hook", hit.pharm_human_hook],
    ["verification_note", hit.verification_note]
  ];

  mount.innerHTML = `
    <article class="xr-dossier">
      <p class="xr-eyebrow">Destination dossier · 数字档案</p>
      <h2>${esc(hit.common_name_zh || hit.common_name_en)} <span class="xr-sci">${esc(hit.scientific_name)}</span></h2>
      <p class="xr-lead">${esc(hit.common_name_en || "")} · ${esc(hit.extinction_summary || "")} · ${esc(hit.region || "")}</p>

      <section class="xr-block">
        <h3>Epistemic layers / 认知分层</h3>
        <p><span class="xr-tier cited">Cited</span> 文献与博物馆可核验来源</p>
        <p><span class="xr-tier interp">Interpolated</span> 由近缘类群与形态节律推断的感官代理</p>
        <p><span class="xr-tier spec">Speculative</span> 沉浸式 Umwelt 场景仍为设计假说，需随研究迭代</p>
      </section>

      <section class="xr-block">
        <h3>Full field record / 数据集全字段</h3>
        <dl class="xr-kv">
          ${rows
            .map(
              ([k, v]) => `
            <dt>${esc(k)}</dt>
            <dd>${esc(v)}</dd>`
            )
            .join("")}
        </dl>
      </section>

      <section class="xr-block">
        <h3>Archival portals / 开放档案入口</h3>
        ${renderPortalLinks(arch?.portal_urls)}
      </section>

      <section class="xr-block">
        <h3>Curated archive hints</h3>
        ${
          curated.length
            ? `<ul>${curated.map(c => {
                const u = String(c.url || "#").replace(/"/g, "%22");
                return `<li><strong>${esc(c.type)}</strong>: ${esc(c.label)} — <a href="${u}" target="_blank" rel="noopener">open</a></li>`;
              }).join("")}</ul>`
            : "<p class=\"xr-muted\">No curated hints.</p>"
        }
      </section>

      <section class="xr-block">
        <h3>Research protocol</h3>
        <ul>
          ${(arch?.research_protocol || ["No protocol notes"]).map(x => `<li>${esc(x)}</li>`).join("")}
        </ul>
      </section>
    </article>
  `;
}
