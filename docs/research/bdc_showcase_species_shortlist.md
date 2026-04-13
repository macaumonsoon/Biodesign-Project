# BDC 主展示物种建议名单（对齐 ideation + `PROJECT_PLAN.md`）

**目标：** 在 Biodesign Challenge 评审维度（**Narrative · Context · Reflection**、**Biodigital Excellence**）下，用最少物种讲清三件事：**时间位（chronobiology / 迁徙节律）**、**感官与档案（Umwelt / 影像与声）**、**伦理与殖民性（de-extinction、原住民主权、市场开发）**。

---

## Tier P0 — 必啃（与 `PROJECT_PLAN.md` MVP 一致）

| 学名 | 通用英文名 | 为何是主展示 | 与 ideation 的扣点 |
|------|------------|--------------|-------------------|
| *Mammuthus primigenius* | Woolly mammoth | 计划中的 **polar / circadian genomics**、**aDNA**、**同位素象牙迁徙**（Kik 等） | **时间厚化**：年/季尺度移动 → 可 sonification；冻尸与基因组论文支撑 **Cited** 层 |
| *Thylacinus cynocephalus* | Thylacine (Tasmanian tiger) | 计划中的 **orbit → 昼夜活动**、**殖民语境**、**Palawa-led 伦理** | **档案影像 + 声音史**（NFSA 等）；**伦理分叉**（de-extinction / TIGRR 等）必须显式标注 |
| *Ectopistes migratorius* | Passenger pigeon | 研究报告与 ideation 中的 **社会同步**、**群体声学层叠**、**Martha endling** | **“同步性坍塌”** 叙事；**声学缺席**（xeno-canto 等可能为空）本身可作为 **缺席的感知** |

> 这三类在 `scripts/extinction_archive_db/generate_archival_media_research.py` 的 `SPECIAL` 中各有 **14–17 条**馆际 / 数据集 / 文献深链（见下）。

---

## Tier P1 — 强烈建议（展览轮换 / “缺席与殖民性”副线）

| 学名 | 通用英文名 | 为何值得深啃 | 与 ideation 的扣点 |
|------|------------|----------------|-------------------|
| *Raphus cucullatus* | Dodo | **岛屿灭绝符号**、**牛津标本**、**CT / 系统发育** 文献链成熟 | **AR / 博物馆语法**（团队 CSV 已标 “AR 经典”）；适合 **殖民贸易与引入物种** 的 Context |
| *Pinguinus impennis* | Great auk | **BHL + 史密森 “Once There Were Billions”** 等档案密度极高 | **北大西洋开发史**与 **标本狂热**；与旅鸽形成 **“消失的百亿只”** 互文 |

> 二者在 `SPECIAL` 中各有 **14+** 条深链（博物馆、BOW、BHL、SI 展览、PMC 等）。

---

## Tier P2 — 备选（若需第三条声音线或澳亚视角）

| 学名 | 通用英文名 | 用途 |
|------|------------|------|
| *Numenius tenuirostris* | Slender-billed curlew | **极罕见现存录音** → “声学灭绝”与 **细嘴杓鹬** 的 **Cited audio** 示范 |
| *Smilodon fatalis* | Saber-toothed cat | **拉布雷亚式沥青坑档案**（若做北美更新世副线）；与猛犸共享 **更新世声景** 但需控制范围避免发散 |

---

## 数据落点

- **深链矩阵（可导入 Excel / DB）：** `data/extinction_archive/archival_media_research.csv`  
  - 重新生成：`python3 scripts/extinction_archive_db/generate_archival_media_research.py`  
- **方法说明 + 旗舰摘要：** `docs/research/archival_media_by_species.md`  
- **脚本内 curated 列表：** `SPECIAL` in `scripts/extinction_archive_db/generate_archival_media_research.py`

---

## 策展原则（给评审看的一句话）

**P0 三物种** = *时间生物学（猛犸）* + *档案伦理与原住民语境（袋狼）* + *社会节律与声学缺席（旅鸽）*；**P1** 用 *渡渡鸟 / 大海雀* 把 **岛屿与海洋开发史** 接进同一套 **认识论 UI**。

---

*Aligned with Extinction Archive / Umwelt Archive ideation and `PROJECT_PLAN.md` (April 2026).*
