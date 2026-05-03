# Extinction Archive Website Intro Video Script  
# 《灭绝档案》网站介绍影片脚本

**Length / 时长：** 4:30–5:00  
**Format / 形式：** 一镜到底录屏 + 英文口播  
**Core logic / 核心逻辑：** What problem did we find? → How do we solve it? → How does the website work?  
**中文逻辑：** 发现了什么问题 → 我们如何解决 → 网页如何运作

---

## 0. Recording Setup · 录制准备

建议从 `prototype/index.html` 首页开始录屏。录制时不要频繁返回浏览器上一页，尽量通过页面内的按钮和链接自然进入下一层页面。

Recommended starting point:

`prototype/index.html`

如果录本地版本，可使用：

`http://localhost:4173/prototype/index.html`

### Suggested Route · 建议录制路径

1. 首页点阵地图 / Homepage dot map
2. 中英切换 / Language switch
3. 点击一个物种点位 / Select one memorial point
4. 打开物种档案 / Open species dossier
5. 进入物种全表 / Open species table
6. 展示筛选与搜索 / Show search and filters
7. **伦理界面为主**（可先快速带过重点案例作铺垫）/ Ethics-focused beat (optional brief hero dossiers)
8. 沉浸式 WebXR：星球 → 物种卡片（What-if / 可选声音）→ 点击 **`Digital dossier`** 进入长页滚动（Summary / People-related causes / schematic footprint）→ 可选迁徙 / Planet → card → full dossier scroll → optional migration
9. 结尾停在星球或回到首页 / End on planet or return to map

---

## 1. Opening: The Problem · 开场：我们发现了什么问题

**Time / 时间：0:00–0:45**

### Visual Direction · 画面

打开首页，不要马上点击。先让观众看到白底点阵世界地图、54 个闪烁点位和左侧介绍卡片。镜头停留 3–5 秒，让点位的“呼吸感”被看见。

然后鼠标慢慢移动到地图上，轻轻 hover 几个点位，但暂时不点击。

### 中文理解

这一段要说清楚：我们的项目不是单纯展示“灭绝动物图片”，而是回应一个更深的问题：灭绝带走的不只是物种的外观，也带走了它们曾经在地球上存在的时间、地点、节律和与人类活动之间的关系。

### English Voiceover

> Extinction is often remembered through a single image: an animal, a date, or a label that says “gone.”  
> But extinction removes more than a body. It removes a way of living in time, a place in the world, and a relationship between species, habitats, and human activity.  
> Our project, Extinction Archive, begins with this problem: how can a website help people remember lost species without flattening them into static images?

---

## 2. The Concept: A Memorial Archive · 概念：一个纪念型档案

**Time / 时间：0:45–1:20**

### Visual Direction · 画面

鼠标移动到左侧介绍卡片，展示项目标题和文字。随后切换一次右上角语言按钮：中文 → EN，或 EN → 中文，再切回来。这个动作要慢，显示网站是双语系统。

### 中文理解

这一段解释解决方案的核心：我们把网站设计成一个“AI 纪念空间”，不是传统数据库。它把地图、档案、感官叙事、伦理选择和沉浸式体验连接起来。

### English Voiceover

> We respond by designing the archive as a memorial system, not just a database.  
> The website combines a visual world map, species dossiers, bilingual navigation, ethical reflection, and an immersive planet interface.  
> Visitors can move between Chinese and English, because the project is meant to be readable, shareable, and accessible to different audiences.

---

## 3. Homepage: 54 Memorial Points · 首页：54 个纪念点

**Time / 时间：1:20–2:00**

### Visual Direction · 画面

展示地图中心区域。鼠标慢慢 hover 一个点位，让点位高亮并“移到前层”。点击后打开物种弹窗。停留弹窗 4–6 秒。

如果当前是英文界面，确保弹窗显示英文名和学名；如果当前是中文界面，确保弹窗显示中文名、英文名和学名。

### 中文理解

讲清楚首页如何工作：54 个点不是装饰，而是每个物种的入口。点位是代表性展示坐标，不是 GPS 采样点。交互细节包括呼吸、悬停、高亮和点击弹窗。

### English Voiceover

> The homepage uses a dotted world map as the first layer of interaction.  
> Each blinking point represents one extinct species and a representative place where it once lived.  
> These are not GPS survey points; they are visual coordinates based on historical range and extinction records.  
> When the cursor approaches a point, the marker breathes, comes forward, and opens a short species card.

---

## 4. Species Dossier: From Point to Story · 物种档案：从点位进入故事

**Time / 时间：2:00–2:40**

### Visual Direction · 画面

物种档案有 **两条常用入口**，录制时二选一或各剪一段即可（勿在同一成片里两条都冗长走完）：

**路径 A · 经典 2D：**在首页弹窗中点击 `Open species dossier / 打开物种档案`，进入浅色 **`prototype/species.html`**。自上而下缓慢滚动即可。

**路径 B · WebXR 数字档案（长页面 · 与你截图一致）：**由 **`prototype/webxr/species.html`** 进入，或由球星卡片底部点击 **`Digital dossier`** 跳入同一页。让观众先读到顶栏眉标 **`EXTINCTION ARCHIVE · DIGITAL DOSSIER`**（或中文模式下对应文案），然后是 **大标题 + 学名一行**，以及灭绝时间与地区概要。向下滚动时**依次定格**：

- **Summary / 摘要：**橙色小节标题下的段落框（交代叙事引导，非判决书）。  
- **People-related causes / 与人类活动相关的原因：**若干 **pill 标签**（来自档案「灭绝原因」字段的短切片）+ 下方解释文字（说明标签只是讨论切片、不是穷尽清单）。  
- **More vs less human footprint (look)：**注意 **`schematic`** 徽标——表明示意图库影像为 **概念看图**，非同一地点实测对比；展示宽幅景观图后，**轻轻拖动对比滑轨**（例如约 20–40% ↔ 65–80%），让观众看见图层明暗或遮罩变化即可，不必读完所有说明。  
- 其后 **Key information / Open archives / Curated / Research protocol** 等区块：**快速扫过**，证明长页仍拴在开放档案与协议上。

### 中文理解

这一段说明：**物种档案不是只给名字**，而是把摘要叙事、与人类相关的压力标签、「 footprint 看图」式的感性对照，以及关键字段、外链入口、核对协议串在同一条垂直阅读动线里。它与球星卡片里的 What-if、声音按钮形成互补——**卡片偏即时交互，长页偏展开阅读**；**schematic** 则反复提醒观众：感性看图不等于测量数据。

### English Voiceover

> From the map, visitors can enter a species dossier—but the archive offers two depths.  
> The classic page stays bright and readable; the WebXR digital dossier lands on a long scroll with an archival eyebrow, an orange-accent section rhythm, and modular blocks.  
> Summary frames the species as interpretation, not a verdict. People-related causes render driver phrases as compact tags, then explicitly warn they are discussion slices, not the whole story.  
> The footprint comparison pairs stock imagery under a **schematic** badge: drag the slider to feel “more disturbed versus less,” without pretending it is a controlled before-and-after survey.  
> Further sections keep key fields, portal links, and research protocols in view—so immersion never detaches from citation.

---
## 5. Species Table: Search and Verify · 物种全表：搜索与核对

**Time / 时间：2:40–3:15**

### Visual Direction · 画面

通过页面导航进入 `Species Table / 物种全表`。展示浅色表格页面。输入一个关键词，例如 `Mammoth` 或 `bird`，再使用类别或资料完整度筛选。

### 中文理解

这一段解释：全表页面是研究和核对层。它让观众知道网站背后有数据结构，而不是随意生成的视觉。

### English Voiceover

> The website also includes a full species table.  
> This page makes the archive easier to inspect: visitors can search by scientific name, English name, or Chinese name, and filter the dataset by category or data availability.  
> This layer supports verification. It shows that the visual interface is backed by structured records.

---

## 6. Ethics Interface (Primary) · 伦理界面（本节主打）：从观看到判断

**Time / 时间：3:15–4:25**（建议 **伦理段落占约 2/3 时长**，重点案例仅作一句铺垫）

### Visual Direction · 画面（伦理为主，重点案例点到为止）

**快速带过（约 20–30 秒）：** 如需铺垫，可进入 `Hero Dossiers / 重点案例`，猛犸象 / 袋狼 tab 各闪一下或只停在一个案例上，让观众瞥见 **Cited / Interpolated / Speculative** 这类分层标签即可——不必展开读每条文案。

**重点停留（约 50–60 秒）：** 进入 `Ethics Interface / 伦理思考`（经典原型若在 `hero.html` 同页则下滑；WebXR 则打开 `ethics.html`）。  
- 先定格两根滑块标签与中英文含义各 2–3 秒；  
- **缓慢拖动**「去灭绝投入」与「生态不确定性耐受」各至少 **2–3 个不同位置**，让观众看清反馈段落如何切换（高投入高风险 / 保护优先 / 平衡路径等）；  
- 最后镜头落在 **反思日志** 输入框，停留 **5–8 秒**，可假装输入一行字再删掉，强调「可带走的态度」而非填空考试。

### 中文理解

网页前半段让人「看见」灭绝档案；**本节主打伦理——要让观众感到自己被邀请进来「表态」，而不止于同情。** 若片头带过重点案例，只需让观众瞥一眼叙事如何把证据分层（已引用 / 推断 / 推测），随即把注意力拉回：**伦理界面才是节拍重心。** 两根滑块把「去灭绝投入」与「生态不确定性耐受」落成可拖动的取舍：资源更多流向「复活」叙事，还是优先守住仍在呼吸的生态；我们愿意为不确定性买到哪一档「负责任」。拖动时反馈段落替你校对立场；**反思日志**不要求标准答案，只留一句可以带回课堂与生活的态度。

### English Voiceover

> After the map and dossiers let visitors see extinction as structured memory, this beat invites judgment—not pity alone.  
> Optional hero dossiers may cue layered evidence—cited, interpolated, speculative—but we do not linger there; the archive is also an ethics prompt.  
> The ethics interface is the hinge: two sliders turn abstract debate into concrete trade-offs—whether budgets lean toward de-extinction technologies or toward protecting ecosystems that still exist, and how much ecological uncertainty we accept before calling a stance responsible.  
> Each drag updates the guidance text beneath, naming your posture—balanced, conservation-first, or high appetite for risk—and the reflection log holds space for a stance you can revisit, without prescribing one “correct” answer.

---

## 7. Immersive WebXR: The Dark Experience · 沉浸式 WebXR：唯一的深色体验

**Time / 时间：4:25–4:55**（若同时演示 **What-if 分叉 + 声音 + 迁徙**，可从本节或尾声合计借用 **约 15–20 秒**，整体仍尽量压在约 5 分钟内）

### Visual Direction · 画面

进入 `WebXR Depth / Planet Home / 星球首页`。先让观众感到视觉断层：前面页面偏浅色、偏档案；这里唯独进入**深色星球空间**，星球占据画面重心。

1. **空间交互：**缓慢拖动地球，演示缩放（滚轮）与区域预设按钮（若使用）；光点在球面上的分布要让观众读出「全球缺席」。
2. **点开物种：**点击一枚光点或图标标记，弹出右侧 **物种卡片**。顶部为俗名、学名、类别与灭绝概要（中英混排属正常）。卡片内除文字元数据外，注意露出 **播放声音 / Play related-species recording**（界面会标明 **原物种录音** 或 **近缘物种替代录音**，例如猛犸象卡片上可能出现近缘说明）。**录制时请打开系统音量或示意观众戴耳机**，点击播放 **2–4 秒**；可顺带点 **静音 / Mute** 表明可控。
3. **What-if 伦理分叉（本节务必拍到）：**在卡片**中部向下滚动**（若默认未完整露出），直到看见 **「WHAT IF …」/「若无人类影响」** 类教育式分叉模块：一则反事实提问 + **三条可选分支**（pill / 按钮）。用鼠标 **缓慢 hover 其中一条**（如图选中「Stacked multiple drivers / 多重驱动叠加」亦可），让选项描边或高亮停留 **2–3 秒**，再 **单击一次**，露出下方灰色 **讨论提示**（说明古 DNA、年代学往往显示多重压力叠加——**讨论入口，非标准答案**）。口播点明：这是星球卡片里的「微型伦理排练」，与后面整页的伦理滑块形成梯度。
4. **底部工具条：**镜头扫过 **Digital dossier**、**Image source**、**IUCN / GBIF / MorphoSource** 等 pill；随即 **单击 `Digital dossier`**，进入下一步（不要只在卡片上结束）。
5. **完整数字档案长页（务必与截图层级对应）：**新页面为 **`webxr/species.html`** 全屏纵向档案。自上而下缓慢滚动：**眉标 + 主标题 + 学名** → **Summary** 段落框 → **People-related causes** 与 pill 标签及解释文案 → **More vs less human footprint (look)**（带 **schematic** 徽标、宽幅示意图）→ **拖动对比滑轨** 一次展示图层变化。其后 **Key information、Open archives** 等快速掠过即可。
6. **若仍有余时：**回到星球或保留在长页结尾；可选演示 **网格 / 路径 / 散开 / 迁徙演示** 之一。

### 中文理解

这一段要讲 **四层递进**。**（1）深色与球体**——从「阅读档案」跨入「可巡游的记忆场」。**（2）听觉**——界面在权限与史料允许时让玩家听见叫声片段；近缘替代录音会被标注。**（3）What-if 分叉**——卡片内三分支是「微型伦理排练」。**（4）Digital dossier 长页**——与球星卡片形成纵深：同一物种在这里展开为 **Summary + 人类相关标签 + schematic footprint 看图**，用橙色小节标题与卡片分区让观众感到「仍在档案系统里」，只是把叙事拉长到可教学的尺度。

### English Voiceover

> The immersive WebXR planet is deliberately the only dark interface in the site: everything before it stays bright and archival, while this layer shifts toward spatial memory—you orbit a field of lights where absence has geography.  
> Drag and zoom the globe, select a marker, and open the species card. Beyond taxonomy and extinction summaries, look for the audio affordance: press play when recordings exist, or when the interface offers a clearly labeled related-species proxy—headphones help, and the label matters ethically.  
> Then scroll within the card to the **What-if** fork: a counterfactual prompt with three branches—each option is an educational scenario, not a single “correct” extinction story. Hover and click one branch so the discussion note appears: paleogenomics and chronologies often show stacked pressures, so the UI rehearses judgment before the full ethics sliders page.  
> Use the pill cluster, then open **Digital dossier** to leave the floating card for the full scroll: eyebrow branding, Summary, people-related tags with their caveat copy, and the footprint comparison labeled **schematic**—drag its slider once to show how the interface pairs sensory imagery with explicit uncertainty. Quick-scan the remaining blocks for portals and protocols. Optional globe toggles—routes, scatter, migration—can close the beat if time remains.

---## 8. Closing · 结尾

**Time / 时间：4:55–5:10**

### Visual Direction · 画面

可以停留在沉浸式星球，也可以回到首页点阵地图。结尾画面建议停在呼吸点位上，安静一点。

### 中文理解

最后总结项目价值：它不是单纯数据库，也不是只做漂亮视觉；它是一套把灭绝记忆、证据、交互和伦理反思串起来的纪念系统。

### English Voiceover

> Extinction Archive is not simply a database, and it is not only a visual prototype.  
> It is a memorial system that connects lost species, evidence, interaction, and ethical reflection.  
> By moving from problem, to archive, to decision, the website asks a simple question: how should we remember what has disappeared, and what can we still protect?

---

## Short Production Notes · 拍摄提示

- 录制时鼠标移动要慢，避免观众看不清点击位置。
- 每个页面停留至少 5 秒，尤其是首页点位、物种弹窗、伦理滑块和 WebXR 星球。
- **WebXR 若演示动物叫声：**提前确认音量、戴耳机或外放适中；界面会区分「原物种录音 / 近缘替代」——口播可顺带一句，避免观众误以为全部是目标物种直录。
- **WebXR 物种卡片内的 What-if：**务必向下滚动到分叉区再录；猛犸象等物种有三条分支可选，展示一次 hover + 单击即可，突出「讨论提示、非唯一答案」。
- **`Digital dossier` 长页：**点击 pill 进入 `webxr/species.html` 后务必向下滚过 **Summary → People-related causes → More vs less human footprint (schematic)**，并拖动 footprint 滑轨一次。
- 如果使用英文口播，页面可以先切到英文；如果老师也需要看中文，可在开头展示一次语言切换即可。
- 建议不要把所有物种都点一遍，只点 1–2 个代表性点位，否则视频会变成操作演示而不是项目叙事。
- 重点是让观众理解：**问题是灭绝记忆被扁平化；解决方法是建立 AI 纪念档案；网页通过地图、档案、全表与 WebXR 完成叙事骨架——其中伦理滑块页承担「从观看到判断」的主转折；WebXR 球星卡片里的 What-if 与 `Digital dossier` 长页（Summary / People-related causes / schematic footprint）则把同一物种从「即时交互」推到「可教学的展开阅读」。本节录制时请把伦理段落时长压在滑块与反思日志上；星球段落务必拍到 What-if、（可选）声音，并进入长页滚过 schematic 区块。**

