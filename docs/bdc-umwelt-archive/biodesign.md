# Biodesign Project — Planning Document（2 人 · 2–3 周 · MVP）

**Working title:** Extinction Archive / Umwelt Archive（灭绝档案 · 感官—时间胶囊）  
**Competition lens:** Biodesign Challenge 2026 — Biodigital Excellence + Narrative / Context  
**Last updated:** 2026-04-04

### 已书面锁定（Open action 已关闭）

```text
Species = Mammoth
Group2 = Group1Slim
```

- **英雄物种：** 真猛犸 *Mammuthus primigenius*（方案 A · 单物种深做）  
- **模块基调：** Dossier + Mixer + **完整短 Ethics**（讲演内 Ethics ≈ **2 min**，含 B 分支卡 + C 证据门禁）

---

## 1. Executive summary（一页说清楚）

在 **2–3 周内**，两人团队交付一套 **浏览器优先** 的沉浸式体验：**真猛犸 *M. primigenius* 档案（Dossier）** → **节律混音台（Mixer）** → **分支式伦理收束（Ethics · Group1Slim）**。  
**主命题 A（Umwelt）** 为轴，**辅命题 B（人类对灭绝的社会记忆）** 仅在文案与结构上点睛，不单独开大系统。

**质量控制原则：** **猛犸单物种做深** + 全链路可点通；科学折叠绑定 **同位素年层 / 光周期与适应证据**（可引用综述）。所有生成内容遵循 **Cited / Modeled / Speculative** 三级标签。

---

## 2. Locked decisions（已选与默认）

| 来源 | 你的选择 | 本计划中的落点 |
|------|-----------|----------------|
| Step 1 | 主 **A** + 辅 **B** | 交互以 **感知—节律—环境** 为主；集体记忆只在叙事与 Ethics 文案中出现 |
| Step 2 | **Group1Slim（已确认）** | Dossier + Mixer + Ethics；Ethics = **分支卡 B + 证据门禁 C**（§6–§7）；讲演 **~2 min** |
| Step 3 | **B** | 对外话术：**from biology**（古生态、形态与声学 proxy、文献）是核心；**活体装置非必需** |
| Step 4 物种 | **Mammoth（已确认）** | **单英雄：真猛犸** *M. primigenius*；科学折叠以 **北极光周期 / 适应相关基因组 / 象牙同位素与年层迁徙** 为主（§4） |
| Step 4 感官 | **A 或 C** | **默认 A**（嗅觉不进技术实现，仅叙事描写）；若工时有余再加 **C**（材质样本/代币，无食品） |
| Step 5 AI | **B 主 + A 辅** | 主：**参数化 + control/条件**（图像以结构约束优先）；辅：**shader / procedural** 承底，减少「空 prompt 幻觉」 |
| Step 5 Living | **讲师推荐** | **本轮不做复杂活体信号。** 与 Step 3 **B** 一致：零活体或 **Stretch：一盆植物 + 环境光/土壤湿度只读**（见 §5） |
| Step 6 | **B 主 + C 辅** | 结尾：**分支卡片**；进入前 **简短「证据分级」互动**（C 辅） |
| Step 7 AR | **A + B** | **主路径：桌面 Web**；**移动 WebAR** 为 **同一 URL 的增强模式**（扫描 3D 打印物触发同一段 GLB/叙事） |
| Step 7 R / 同位素 | **A + C** | 同位素/迁徙：**仅在 Dossier「科学」折叠层**；另输出 **1–2 张 R ggplot 静帧**用于 Slide + 网页缩略 |
| Step 8 | **2–3 周** | **单 Sprint**，见 §9；不做四个月模型 |
| 分工 | **C（扁平 + 审计会）** | 两人交叉全栈 + **每周 2× 30min 证据审计** |

---

## 3. MVP scope（必须）vs Stretch（可选）

### Must ship（评审可演示闭环）

1. **Dossier（猛犸 · 单页 deep）**  
   - 地理锚点：**末次盛冰期至全新世早期**北半球苔原—草原走廊（具体坐标需 Cited）  
   - **360° / 全景占位** + 分层文案（Cited / Modeled / Speculative）  
   - **科学折叠区（必做）：** 象牙 **Sr/O 等同位素年层** 或公开个案（如阿拉斯加个体迁徙年层）→ **R ggplot 静帧（§2 已锁定 A+C）**；可选 **PER2/BMAL1 等适应相关**综述级表述（逐条标 Modeled/Cited）

2. **Mixer（Web Audio · 猛犸 tuned）**  
   - ≥3 层建议标签：**季节/光周期 pulse**（Cited/Modeled）、**苔原—草原声景 bed**（可对近缘象/环境录音做 Speculative 标注）、**人类压力或气候收缩层**（人类纪叙事，文献或历史记录依据）  
   - **「和谐 vs 冲突」**：用简单的 DSP 规则表达（例：某层增益过高 → 侧链压限 / 失谐）— **规则表写进 README / Slide**

3. **Ethics（短）**  
   - **2–3 张分支卡** → 决定 **30–60s 不同「终曲」混音状态 + 不同结尾字幕**（B）  
   - 进入 Ethics 前 **3 题「这篇是 Cited 还是 Speculative？」**（C 辅），错 1 题也可进，但会弹出 **「推测边界」** 提示

4. **Physical + AR（轻）**  
   - **一件** 3D 打印（头骨简化几何 / 轨迹图腾 / 「档案token」三选一）  
   - 手机 **WebAR**：扫描后出现 **同一物种的标注点或 loop 动画**（与桌面 Dossier 内容一致，不另做一套故事）

5. **BDC 五件套映射（课程内可交付的最小高质量集）**  
   - **讲演**：按故事板 **8 min 讲 + 2 min Demo** 预演  
   - **视觉**：高清 UI 录屏 + 3–5 张 still  
   - **实体**：上述打印物 + AR 录屏  
   - **短片**：**45–90 s** 预告式（Mixer + Ethics 转折 + 一级标签闪现）  
   - **Slide**：含 **Methods + Citations + Limitations** 3 页硬性保底

### Stretch（只做多余的几天才开）

- **嗅觉/味觉 C：** 非食物材质 **触感代币** + 文案卡片（与 Dossier 同步）  
- **第二物种：** Mixer 里 **多一个「幽灵层」**（仅音频 bed，无完整 Dossier）  
- **Living：** 一盆植物 + 廉价湿度/光传感器 → 网页角落 **「仍在场的读数」** 小部件（与 Step 3 B 不冲突：定位为 **对照隐喻**，非核心科学 claim）

---

## 4. Hero species — **已锁定：真猛犸** *Mammuthus primigenius*

**范围冻结：** 仅 **1 个英雄物种** 的 Dossier + AR；Stretch 若加 Mixer「幽灵层」须另开文档，不默认。

| 支柱 | 用途（2–3 周内可答辩） | 标签倾向 |
|------|------------------------|----------|
| **同位素 + 年层** | 公开文献/报道中单个个体的 **tusk 逐层化学与迁徙重建** → Dossier 折叠区 + **ggplot 静帧** | 多 **Cited**（数据处理可为 **Modeled**） |
| **光周期 / 季节** | 北极纬度 **极端昼夜** 与行为节律叙事；可引用基因组综述中 **.clock 相关** 讨论 | **Cited + Modeled** 分清 |
| **Umwelt 视觉 proxy** | 象类低视锐 / 社会性引用；生成场景 **参数化光照、雾、地景** | 画面细部 **Speculative** |
| **灭绝叙事** | 气候变化与人类猎压等 **学界共识级** 表述，避免单一归因断言 | **Cited**；复杂处 **Modeled** |

**AR / 实体：** 打印物优先 **抽象 tusk 剖面「年层柱」** 或 **简化颅骨剪影** — 扫描后唤起 **同位素曲线缩略 + 同一段 GLB 环境**，与 Dossier 同源。

**已否决路径（勿再占会议时间）：** 旅鸽 / 袋狼英雄物种方案。

---

## 5. Bio + Digital architecture（简化系统表）

| 层 | 输入（必须可引用或声明 Modeled） | 输出 | 工具（建议） |
|----|-----------------------------------|------|----------------|
| Bio | 1 本篇物种综述级论文 + 2–3 篇方法/生态支撑；博物馆/时间线来源 | Dossier 字段 JSON / Markdown | Zotero / 简易 bib |
| Digital viz | Dossier 字段 → **视野/光照 band**、粒子密度 | 场景参数（非裸 prompt） | Three.js / R3F；shader 承底 |
| Digital gen **B 主** | 草图 mask / 深度参考 / 调色板约束 | 环境纹理或局部 detail pass | 任选：**本地 SD workflow** 或 API（注意成本与合规） |
| Digital gen **A 辅** | 时间 of day、季节 | sky、雾、地面 procedural | shader |
| Audio | 文献/近缘种 + **明确 Speculative** 的叫声 | Mixer 多层 `AudioContext` | Web Audio；Ableton 预bounce 可选 |
| Ethics | 保护生物学 **2–3 个硬权衡**（资源/入侵种/原住民数据主权择一深入） | 分支状态 → Mixer master preset | React state / 轻量 JSON |

**Living（推荐结论）：**  
- **默认：不做。**  
- **若坚持「会呼吸的对照」：** Stretch 采用 **单盆植物 + 光/湿度只读**，UI 文案固定为 **「现存环境样本，仅代表在场，不代表目标物种栖息地复原」**，避免伪科学。

---

## 6. Narrative — 200 字级 + 10 min 结构

**200 字叙事核（可改人名与物种）：**  
当物种消失，不只是生命消失，也是 **一种在时间中生活的方式** 被抹去。Extinction Archive 从 **最后栖息地的一个坐标** 出发，用可审计的生物证据重建 **Umwelt 的草案**：怎样的光、怎样的节律、怎样的声景曾在这里叠加。你调节 layers，会听见 **和谐如何转为冲突**——那往往是人类纪的压强。最后在 **分支伦理** 前，你必须看清 **哪些是事实、哪些是推测**。我们提问：**当数字可以「唤回」感知，它会促进保护，还是会成为遗忘的借口？**

**10 min oral 分段（±30s）：**

| 段 | 时长 | 内容 |
|----|------|------|
| Hook | 0:45 | 集体记忆断裂 + Umwelt 主命题 |
| Demo Dossier | 3:30 | **猛犸** deep；同位素折叠区 + **标签系统**走一遍 |
| Demo Mixer | 3:00 | 三层含义 + **冲突规则** |
| Ethics | 2:00 | **C 辅 45s** + **B 主 75s** 分支与终曲 |
| Reflect | 1:00 | 迭代记录、局限、下一步 |

---

## 7. Ethics Console — B 主 + C 辅（实现清单）

**C 辅（入门门禁，≤45s）：**  
- 3 条陈述（猛犸语境举例，可替换为你的最终措辞）：  
  ①「这支 Mixer 里的猛犸叫声与真实录音一致」→ **Speculative**（无录音）  
  ②「单凭公开数据即可 100% 还原该猛犸个体每一天的精确 GPS 轨迹」→ **Speculative**（推断与平滑模型必有不确定性）  
  ③「复活猛犸在科学上已无争议」→ **Speculative**（明显错误，用作门槛题）  
- UI：**二选一按钮**；完事后放行

**B 主（分支卡）：**  
- 卡 1：资金倾向 — **就地保护 vs 复活技术**（抽象为两选项，配 1 句后果）  
- 卡 2：**引入物种 / 强化入侵种防控**（简化二元）  
- 卡 3：**数据与土地**：**非原住民团队使用传统生态知识的边界**（以 **问题+「我们项目的承诺」** 呈现，避免替代言说）

**输出：** 预设 **2–3 套 Mixer master**（滤波 + 一层 mute）+ **不同 ending caption**（80 字内）

---

## 8. AR 策略 A + B（实现约束）

- **B 桌面 Web：** 主开发与录屏环境  
- **A Mobile WebAR：** 同一仓库；**AR 仅增加** `?ar=1` 或独立入口页  
- **内容复用：** 同一 GLB、同一音频 stem、同一物种 ID；**禁止**维护两套叙事文案  
- **翻车预案：** AR 不可用时 → Slide 内嵌 QR **跳 Dossier 同一锚点**

---

## 9. Schedule — 2–3 周（两人 · 模型 C）

假设 **21 天**；若只有 **14 天**，合并「集成」与「抛光」并 **砍掉 Stretch**。

### Week 1 — Discovery + Vertical slice

| 天 | Person A（偏全栈/视觉） | Person B（偏音频/研究/文案） |
|----|-------------------------|------------------------------|
| 1 | 脚手架：R3F 或 Vite+Three；路由骨架 | **猛犸文献 Sprint**：Zotero + **≥3 篇核心**（同位素个案 1 + 综述/基因组 1 + 灭绝机制 1） |
| 2 | Dossier 静态 UI + 三标签组件 | **猛犸**文献 → Dossier JSON 字段；C/M/S 初分 |
| 3 | **苔原—草原场景**：procedural base + **首批 control 图** | Mixer stem 表：**季节 pulse / 风与环境 / 人类纪层**（各附依据类型） |
| 4 | Mixer Web Audio 原型（3 层推子） | Ethics 状态机 JSON |
| 5 | **垂直切片**：猛犸 Dossier → Mixer | **证据审计 #1**（30min） |
| 6–7 | shader polish；移动端布局 | **R ggplot 静帧 v1**（tusk / 同位素）；伦理文案 v1 |

### Week 2 — Integration + Ethics + Physical

| 天 | A | B |
|----|---|---|
| 8 | Ethics UI（C+B）；结尾字幕逻辑 | 叙事稿 10min；Q&A 预表 10 条 |
| 9 | GLB 导出；**WebAR 最小可扫** | 3D 打印 STL 定稿；装机拍摄脚本 |
| 10 | AR fallback；性能 | Slide：Methods / Citations / Limits |
| 11 | **全链路 rehearsal** | 短片分镜 + 录音 |
| 12–14 | 预告片剪辑；UI still | 第二轮子 **证据审计 #2**；limitations 页定稿 |

### Week 3（若存在）— Polish + 缓冲

- 音频母带轻量处理；动效；Accessibility（字幕、键盘）  
- 模拟答辩 2 次；**只修 P0 bug**  
- **可选 Stretch：** 触感代币 C / 植物读数

---

## 10. Definition of Done（质量门槛）

- [ ] 一条路径 **无说明者可完成**：打开 → Dossier → Mixer → Ethics → 终曲  
- [ ] 所有 **Cited** 有年份+作者+题目（或完整 URL + 访问日）  
- [ ] **Speculative** 出现处 **≥3 处显式 UI 提示**  
- [ ] **Mixer 规则** 1 页可在 Slide 展示（非黑箱）  
- [ ] 3D 打印 + AR **录屏备用**  
- [ ] **Methods + Citations + Limitations** 3 页齐  
- [ ] 仓库 **README**：如何运行、素材来源、已知取舍

---

## 11. Risk register（简版）

| 风险 | 缓解 |
|------|------|
| 生成影像「太真」引误导 | B 主 A 辅 + 标签 + 低保和 / 水印 optional |
| 同种文献读不完 | **硬限 5 篇**；其余进 Appendix |
| WebAR 机型分裂 | 桌面录屏为主；AR 为 bonus |
| 两人串任务失控 | **每日 15min standup** + 审计会固定时间 |
| 猛犸叙事过度还原 | 所有冰川场景与「听见象鸣」标 **Speculative**；依赖象类近缘处标 **Modeled** |

---

## 12. ~~Open action~~ → **已确认（归档）**

下列内容 **2026-04-04** 由团队书面确认，**已写回 §2、§4、§3、§9**，MVP 与叙事以 **猛犸 + Group1Slim** 为唯一主线。

```text
Species = Mammoth
Group2 = Group1Slim
```

**后续若变更范围：** 须重写 §4 与 Dossier 数据源表，并更新 Limitations 页 — 不推荐在 2–3 周内改物种。

---

*End of planning document.*
