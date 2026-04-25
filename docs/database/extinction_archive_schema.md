# Extinction Archive / Umwelt Archive — Database Schema

**Purpose:** Define what data the archive and website need, beyond your curated CSV, so the **planetary map → coordinate → species archive** flow, **multisensory reconstruction**, **music layering**, and **cited / interpolated / speculative** transparency can be implemented consistently.

**Source list:** `extinct_animals_database统一高优先级数据库（87种）.csv` (columns map to §6).

---

## 1. What kind of data the database holds

| Domain | Why it exists (ideation + BDC) |
|--------|--------------------------------|
| **Taxon (species)** | Canonical record per extinct species: names, scores, narrative hooks, data-readiness. |
| **Geography** | Map pins, last-known / culturally salient sites, polygons for range (structured uncertainty). |
| **Sensory & temporal reconstruction** | Per-channel proxies (vision, hearing, smell, touch, taste-as-metaphor): *what* is shown and *how certain* it is. |
| **Music / sonification** | Stems, parameters, and mix rules tied to biology (rhythm, migration, calls)—for the “ecological harmony” layer. |
| **Media & 3D** | URLs, files, licenses, Sketchfab/GLB, audio, prompts—not only your “3D模型参考链接” field. |
| **Epistemic provenance** | Every user-facing claim tagged **cited · interpolated · speculative**; links to sources. |
| **Sources** | Bibliography rows reused across taxa and scenes. |
| **Experience (site/WebXR)** | Scene IDs, copy decks, reflection prompts, ethics-branch content per locale. |
| **i18n** | Chinese / English (and future locales) for UI strings and narrative, without duplicating taxon rows. |

Optional later: **user reflection logs** (anonymous), **analytics events**, **Indigenous / community context** as first-class narrative blocks with consent flags.

---

## 2. Conceptual ER (entities)

```
taxonomic_group ──< taxon >── geographic_site
                    │   │
                    │   ├──< media_asset
                    │   ├──< reconstruction_layer   (per sensory channel + epistemic tier)
                    │   ├──< sonification_profile    (optional: stem definitions)
                    │   └──< taxon_citation >── citation

experience_scene ── taxon (optional FK)
locale_string ── (key-based i18n, not shown as FK on every table in MVP)
```

---

## 3. Recommended relational schema (PostgreSQL-flavoured)

Types are indicative; adjust for SQLite / Supabase / PlanetScale as needed.

### 3.1 `taxonomic_group`

Curated labels aligned with your CSV **类别** (can be hierarchical later).

| Column | Type | Notes |
|--------|------|--------|
| `id` | `uuid` PK | |
| `slug` | `text` UNIQUE | e.g. `pleistocene_megafauna`, `mammals` |
| `label_en` | `text` | |
| `label_zh` | `text` | nullable |
| `sort_order` | `int` | display order on filters |

### 3.2 `taxon` (core species row — one per scientific name)

| Column | Type | Notes |
|--------|------|--------|
| `id` | `uuid` PK | stable id for URLs and APIs |
| `scientific_name` | `text` UNIQUE NOT NULL | binomial, canonical |
| `common_name_en` | `text` | |
| `common_name_zh` | `text` | |
| `taxonomic_group_id` | `uuid` FK → `taxonomic_group` | from CSV 类别 |
| `extinction_period_raw` | `text` | verbatim from CSV, e.g. `1936`, `~4,000年前` |
| `extinction_year_ce` | `int` NULL | parsed when possible; else NULL |
| `extinction_year_ce_upper` | `int` NULL | range upper bound if fuzzy |
| `distribution_summary` | `text` | CSV 主要分布 |
| `extinction_drivers_summary` | `text` | CSV 灭绝原因分析 |
| `internal_notes` | `text` | CSV 备注 |
| `sensory_potential_score` | `smallint` CHECK 0–10 | CSV 感官重建潜力评分 |
| `music_layering_potential_score` | `smallint` CHECK 0–10 | CSV 音乐层叠潜力评分 |
| `data_availability` | `text` CHECK | `high` \| `medium` \| `low` (normalize CSV) |
| `slug` | `text` UNIQUE | URL-safe, e.g. `thylacinus-cynocephalus` |
| `featured_rank` | `int` NULL | homepage / map emphasis |
| `flags` | `jsonb` | e.g. `{"indigenous_context_required": true, "chronobiology_mvp": true}` |
| `created_at` | `timestamptz` | |
| `updated_at` | `timestamptz` | |

### 3.3 `geographic_site`

Supports multiple sites per taxon (range centroid, last sighting, type locality).

| Column | Type | Notes |
|--------|------|--------|
| `id` | `uuid` PK | |
| `taxon_id` | `uuid` FK → `taxon` ON DELETE CASCADE | |
| `site_role` | `text` | e.g. `last_known`, `range_centroid`, `cultural_anchor`, `fossil_locality` |
| `label_en` / `label_zh` | `text` | short map tooltip |
| `latitude` | `double precision` NULL | WGS84 |
| `longitude` | `double precision` NULL | |
| `uncertainty_m` | `int` NULL | radius if point uncertain |
| `geojson` | `jsonb` NULL | Polygon/MultiPolygon for range |
| `epistemic_tier` | `text` NOT NULL | `cited` \| `interpolated` \| `speculative` |
| `source_note` | `text` | human-readable provenance |
| `citation_id` | `uuid` NULL FK → `citation` | |

### 3.4 `reconstruction_layer`

Maps ideation channels to **graded** content (what the 360° / AR layer shows).

| Column | Type | Notes |
|--------|------|--------|
| `id` | `uuid` PK | |
| `taxon_id` | `uuid` FK → `taxon` | |
| `channel` | `text` NOT NULL | `visual` \| `auditory` \| `olfactory` \| `haptic` \| `narrative` \| `chronobiology` |
| `epistemic_tier` | `text` NOT NULL | `cited` \| `interpolated` \| `speculative` |
| `title_en` / `title_zh` | `text` | |
| `description_en` / `description_zh` | `text` | what this layer represents |
| `data_proxy_summary` | `text` | e.g. “orbit diameter → crepuscular inference” |
| `default_intensity` | `numeric(3,2)` | 0–1 for “gentle sensory load” |
| `enabled_by_default` | `boolean` | defaults-off channels |
| `sort_order` | `int` | |

### 3.5 `sonification_profile` (optional but aligned with ideation)

| Column | Type | Notes |
|--------|------|--------|
| `id` | `uuid` PK | |
| `taxon_id` | `uuid` FK → `taxon` UNIQUE | one profile per taxon for MVP |
| `stem_definitions` | `jsonb` | e.g. `[{"id":"migration","maps_to":"isotope_segments","tier":"cited"}]` |
| `mix_notes` | `text` | designer notes for harmony/tension metaphor |
| `bpm_range` | `int4range` NULL | optional |

### 3.6 `media_asset`

| Column | Type | Notes |
|--------|------|--------|
| `id` | `uuid` PK | |
| `taxon_id` | `uuid` FK → `taxon` | |
| `kind` | `text` | `sketchfab` \| `gltf` \| `audio` \| `image` \| `video` \| `document` |
| `url` | `text` NOT NULL | |
| `title` | `text` | |
| `license` | `text` NULL | |
| `attribution` | `text` NULL | required for Sketchfab etc. |
| `epistemic_tier` | `text` | |
| `channel` | `text` NULL | links asset to sensory channel |
| `is_primary` | `boolean` DEFAULT false | hero model on archive page |

### 3.7 `citation` & `taxon_citation`

| `citation` column | Type | Notes |
|-------------------|------|--------|
| `id` | `uuid` PK | |
| `cite_key` | `text` UNIQUE | e.g. `Lynch2015` |
| `apa_or_short` | `text` | display string |
| `url` | `text` NULL | |
| `bibtex` | `text` NULL | optional |

`taxon_citation`: (`taxon_id`, `citation_id`, `context` text) PK (`taxon_id`, `citation_id`).

### 3.8 `experience_scene` (WebXR / narrative)

| Column | Type | Notes |
|--------|------|--------|
| `id` | `uuid` PK | |
| `scene_id` | `text` UNIQUE NOT NULL | matches storyboard, e.g. `Scene_Mammoth_Steppe` |
| `taxon_id` | `uuid` NULL FK | NULL for global ethics hub |
| `locale` | `text` | `en` \| `zh` |
| `title` | `text` | |
| `body_markdown` | `text` | narration |
| `reflection_prompt` | `text` | post-immersion |
| `ethics_branch_id` | `text` NULL | links to configured trade-off UI |

### 3.9 `locale_string` (UI i18n)

| Column | Type | Notes |
|--------|------|--------|
| `key` | `text` | e.g. `ui.epistemic.cited` |
| `locale` | `text` | `en` \| `zh` |
| `value` | `text` | |
| PK | (`key`, `locale`) | |

---

## 4. Indexes (minimum)

- `taxon(scientific_name)`, `taxon(slug)`, `taxon(taxonomic_group_id)`, `taxon(data_availability)`.
- `geographic_site(taxon_id)`, `geographic_site` GiST on `geojson` if using PostGIS.
- `media_asset(taxon_id)`, `reconstruction_layer(taxon_id)`.

---

## 5. Static-site / JSON bundle shape (MVP)

If the first ship is **JSON + map tiles** without a DB server, use one file per taxon or a single `archive.json`:

```json
{
  "taxa": [
    {
      "id": "uuid",
      "slug": "thylacinus-cynocephalus",
      "names": { "scientific": "Thylacinus cynocephalus", "en": "Thylacine", "zh": "袋狼" },
      "group_slug": "mammals",
      "extinction": { "raw": "1936", "year_ce": 1936 },
      "distribution": "澳大利亚/塔斯马尼亚",
      "scores": { "sensory": 10, "music_layering": 10, "data_availability": "high" },
      "sites": [
        {
          "role": "last_known",
          "lat": null,
          "lon": null,
          "epistemic_tier": "speculative",
          "label_zh": "塔斯马尼亚（待填入精确坐标）"
        }
      ],
      "layers": [
        {
          "channel": "auditory",
          "tier": "cited",
          "title_en": "Historical recordings",
          "intensity_default": 0.6,
          "enabled_default": true
        }
      ],
      "media": [
        { "kind": "sketchfab", "url": "...", "tier": "interpolated", "channel": "visual" }
      ],
      "citations": []
    }
  ]
}
```

The relational tables above are the **normalized target**; this JSON is the **denormalized export** for frontend.

---

## 6. CSV → schema column mapping

Your file: **统一高优先级数据库（87种）.csv**

| CSV header (Chinese) | Target |
|----------------------|--------|
| 类别 | `taxonomic_group.slug` or FK; seed table from distinct values |
| 中文/英文俗名 | Parse into `taxon.common_name_zh` + `taxon.common_name_en` (split on `/` or ` / `) |
| 学名 | `taxon.scientific_name` |
| 灭绝时期/年份 | `taxon.extinction_period_raw` (+ optional parser → `extinction_year_ce`) |
| 主要分布 | `taxon.distribution_summary` + inform `geographic_site` labels (coords manual pass) |
| 感官重建潜力评分 | `taxon.sensory_potential_score` |
| 音乐层叠潜力评分 | `taxon.music_layering_potential_score` |
| 数据可用性 | `taxon.data_availability` (`High`→`high`, etc.) |
| 3D模型参考链接 | `media_asset` row(s), `kind = sketchfab` or `document` |
| 灭绝原因分析 | `taxon.extinction_drivers_summary` |
| 备注（paleo-data / 项目相关性） | `taxon.internal_notes`; also use to seed `reconstruction_layer` or `flags` |

**Not in CSV today (add during curation):** WGS84 coordinates, `epistemic_tier` per claim, citation IDs, separate EN/ZH narrative bodies, sonification stem JSON.

---

## 7. API sketch (REST)

- `GET /api/taxa?group=&availability=&min_sensory=` — list + map markers.
- `GET /api/taxa/:slug` — full archive card + layers + media + sites.
- `GET /api/taxa/:slug/scenes?locale=` — experience copy.
- `GET /api/groups` — filter chips.

---

## 8. Next steps for your team

1. **Import script:** CSV → `taxon` + `taxonomic_group` + initial `media_asset` rows.  
2. **Geocoding pass:** one `geographic_site` per taxon minimum (tier `interpolated` until paper cites lat/lon).  
3. **Lock epistemic tiers** on each `reconstruction_layer` before public demo.  
4. When the list grows to **87**, same schema; only row count changes.

---

*Schema version: 2026-04 — aligned with Umwelt Archive ideation and biodigital chronobiology research report.*
