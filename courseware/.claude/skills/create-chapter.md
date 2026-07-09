---
name: create-chapter
description: 生成初中物理/化学/数学/语文的章节知识讲解页面（知识点卡片、动画、练习题）
---

# 创建章节知识讲解页面

## 适用场景

用户说"创建新章节"、"添加第X章"、"生成[主题]的课件"时触发。

## 信息收集

在生成页面前，确认以下信息：

- **学科**：物理/化学/数学/语文（确定目录和 CSS 类名）
- **章节编号和中文标题**：例如 "第一章 声"
- **教材版本和年级**：例如 "八年级上 沪教版"
- **小节列表**：每节包含 `{节号, 标题, 知识点列表}`
- **练习题数量**：默认 5-8 题
- **是否需要动画**：Canvas 还是 SVG

## 文件路径

```
{subject}/ch{NN}_{topic_en}.html
```

- `NN`：两位数字章节号（01, 02, ...）
- `topic_en`：小写英文关键词（sound, light, motion_force）
- 示例：`physics/ch01_sound.html`

## HTML 模板

### 页面骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{章节标题} - {学科全称}</title>
<link rel="stylesheet" href="../assets/css/common.css">
<style>
/* 页面特定样式：动画容器、canvas 尺寸等 */
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <!-- sidebar 内容 -->
  </aside>
  <main class="main">
    <!-- 主要内容 -->
  </main>
</div>
<script src="../assets/js/common.js"></script>
<script>
// 动画代码（IIFE + requestAnimationFrame）
</script>
</body>
</html>
```

### Sidebar 结构

```html
<aside class="sidebar">
  <h3>{学科 Emoji} {学科名称}</h3>
  <ul class="chapter-list">
    <!-- 当前章节（active + subsections） -->
    <li><a href="ch01_topic.html" class="active"><span class="ch-num">1</span>{标题}</a>
      <div class="subsections">
        <a href="#sec1-1" data-section="s1">1.1 {节标题}</a>
        <a href="#sec1-2" data-section="s2">1.2 {节标题}</a>
        <a href="#exercises" data-section="ex">练习题</a>
      </div>
    </li>
    <!-- 其他章节（纯链接，无 subsections） -->
    <li><a href="ch02_topic.html"><span class="ch-num">2</span>{标题}</a></li>
    <li><a href="ch03_topic.html"><span class="ch-num">3</span>{标题}</a></li>
    <!-- ... 列出该学科所有章节 ... -->
  </ul>
  <div style="padding:16px 0;margin-top:8px;border-top:1px solid var(--border);">
    <a href="index.html" class="back-subject">📂 {学科}目录</a>
    <a href="../index.html" class="back-home">🏠 返回首页</a>
  </div>
</aside>
```

### Main 内容区结构

```html
<main class="main">
  <!-- 页面标题 -->
  <div class="page-title">{章节标题}</div>

  <!-- 学习目标卡片 -->
  <div class="card">
    <div class="card-title"><span class="icon">🎯</span>学习目标</div>
    <ul style="padding-left:20px;color:var(--text-secondary);line-height:2;">
      <li>目标1</li>
      <li>目标2</li>
    </ul>
  </div>

  <!-- 小节标题（必须同时有 data-section 和 id） -->
  <h2 data-section="s1" id="sec1-1" style="margin:28px 0 16px;">1.1 {节标题}</h2>

  <!-- 知识点卡片（单个） -->
  <div class="kp">
    <h3>{知识点标题}</h3>
    <p>{知识点内容}</p>
    <span class="formula">{公式}</span>
  </div>

  <!-- 知识点网格（并排） -->
  <div class="keypoints-grid">
    <div class="kp"><h3>标题1</h3><p>内容1</p></div>
    <div class="kp"><h3>标题2</h3><p>内容2</p></div>
    <div class="kp"><h3>标题3</h3><p>内容3</p></div>
  </div>

  <!-- 动画容器（Canvas） -->
  <div class="anim-container">
    <h3 style="margin-bottom:16px;">{动画标题}</h3>
    <canvas id="myCanvas" style="width:100%;height:300px;"></canvas>
    <div class="anim-controls">
      <button onclick="startAnim()">▶ 播放</button>
      <button class="reset" onclick="resetAnim()">↺ 重置</button>
    </div>
  </div>

  <!-- 动画容器（SVG） -->
  <div class="anim-container">
    <h3 style="margin-bottom:16px;">{图示标题}</h3>
    <svg viewBox="0 0 680 280" style="width:100%;max-width:680px;">
      <!-- SVG 内容 -->
    </svg>
  </div>

  <!-- 练习题区域 -->
  <h2 id="exercises" style="margin:28px 0 16px;">📝 练习题</h2>

  <div class="exercise">
    <div class="question"><span class="q-num">1</span>{题目文字}</div>
    <div class="options">
      <label><input type="radio" name="q1" value="A">A. 选项A</label>
      <label><input type="radio" name="q1" value="B">B. 选项B</label>
      <label><input type="radio" name="q1" value="C">C. 选项C</label>
      <label><input type="radio" name="q1" value="D">D. 选项D</label>
    </div>
    <button class="answer-btn" onclick="showAnswer(1)">查看答案</button>
    <div class="answer" id="answer-1" data-correct="A">✅ A。{解析}</div>
  </div>
</main>
```

## 关键约束规则

### CSS 类名
- 物理/数学：使用 `.kp`（蓝色左边框）
- 化学：使用 `.kp.chemistry`（绿色左边框）
- `.kp` 内可嵌入 `<table>`、`<ul>`、`<span class="formula">`

### `data-section` 属性
- **每个** `<h2>` 必须有 `data-section="sN"` 属性
- **每个** sidebar 的 subsection `<a>` 必须有对应的 `data-section="sN"`
- 两者必须匹配，否则 IntersectionObserver 滚动高亮失效

### 练习题机制
- 单选：`showAnswer(N)` 调用 `common.js`
- `id="answer-N"` 和 `data-correct="X"`（X 为大写字母 A/B/C/D）
- 所有 radio 的 `name` 属性必须为 `qN`（与 `showAnswer(N)` 参数一致）
- 答案文本格式：`✅ 正确答案：X。解释文字。`

### 动画代码
- Canvas 动画：IIFE 包裹 + `requestAnimationFrame` 循环
- 交互式动画：将控制函数暴露到 `window` 上（如 `window.setObjectPos`）
- 简单图示：优先使用内联 SVG（无需 JS）

### 路径
- CSS：`../assets/css/common.css`（从学科子目录往上一级）
- JS：`../assets/js/common.js`（同上）
- 返回首页：`../index.html`

## 级联更新

创建章节页面后，**必须**更新以下文件：

1. **`{subject}/index.html`**：
   - Sidebar 的 `<ul class="chapter-list">` 中添加新章节链接
   - 对应年级的 `<div class="ch-grid">` 中添加 `<a class="ch-card">` 卡片
   - 卡片包含：`.grade`（年级）、`h3`（章节名）、`.sections`（节列表）、`.sub-count`（节数+特色）

2. **`{subject}/chNN_topic_exercises.html`**（如果存在）：
   - Sidebar 中的返回链接指向新章节

## 常见陷阱

- ❌ 忘记给 `<h2>` 添加 `data-section` 属性 → 滚动高亮失效
- ❌ `name="q1"` 但 `showAnswer(2)` → 答案检查不匹配
- ❌ 忘记 `data-correct` 属性 → 答案无法判断对错
- ❌ Sidebar 只列当前章节 → 导航不完整，用户无法切换章节
- ❌ 创建新章节后不更新 `index.html` → 学科首页看不到新章节入口
- ❌ 化学章节使用 `.kp` 而非 `.kp.chemistry` → 样式颜色不对
- ❌ 子目录页面（如 `math/algebra/`）CSS 路径写成 `../assets/` 而非 `../../assets/`