---
name: create-exam
description: 生成中考/高考真题试卷页面（单年份或多年份汇编，含年份Tab切换、题目来源标签）
---

# 创建真题试卷页面

## 适用场景

用户说"创建2027年真题"、"添加考试卷"、"生成真题汇编"时触发。

## 两种模式

- **模式 A：单年份试卷** — `exam_YYYY.html`，独立页面
- **模式 B：多年份汇编** — `exam_collection.html`，所有年份聚合

## 信息收集

- 学科、年份、考试名称（例如 "2027年上海中考物理"）
- 满分、考试时间
- 题目分组（例如 选择题12分、填空题24分、作图题6分、综合题28分）
- 每题内容：题目、选项、答案、解析、所属章节标签

## 文件路径

- 单年份：`{subject}/exam_{YYYY}.html`（例如 `physics/exam_2027.html`）
- 汇编：`{subject}/exam_collection.html`

## 单年份试卷模板

### 页面骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{YYYY}年{考试名称} - {学科}</title>
<link rel="stylesheet" href="../assets/css/common.css">
<style>
.year-tab{display:inline-block;padding:6px 16px;margin:4px;border-radius:8px;background:var(--bg);color:var(--text-secondary);text-decoration:none;font-size:.85rem;transition:var(--transition);border:1px solid var(--border);}
.year-tab:hover,.year-tab.active{background:var(--primary);color:#fff;border-color:var(--primary);}
.q-source{font-size:.78rem;color:var(--warning);margin-bottom:4px;font-weight:600;}
.q-tags{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:8px;}
.q-tags span{font-size:.7rem;padding:2px 8px;background:var(--primary-light);color:var(--primary);border-radius:10px;}
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <!-- 年份导航 -->
  </aside>
  <main class="main">
    <!-- 年份 tab + 题目 -->
  </main>
</div>
<script src="../assets/js/common.js"></script>
</body>
</html>
```

### Sidebar 结构

```html
<aside class="sidebar">
  <h3>📋 中考汇编</h3>
  <ul class="chapter-list">
    <li><a href="#s2027">2027年</a></li>
    <li><a href="#s2026">2026年</a></li>
    <li><a href="#s2025">2025年</a></li>
    <li><a href="#s2024">2024年</a></li>
    <!-- 每个年份链接到对应的 #sYYYY 锚点 -->
    <li style="margin-top:20px;"><a href="index.html">← {学科}目录</a></li>
  </ul>
  <div style="padding:16px 0;margin-top:8px;border-top:1px solid var(--border);">
    <a href="../index.html" class="back-home">🏠 返回首页</a>
  </div>
</aside>
```

### 年份 Tab

```html
<div style="margin-bottom:20px;">
  <a href="#s2027" class="year-tab">2027年</a>
  <a href="#s2026" class="year-tab">2026年</a>
  <a href="#s2025" class="year-tab">2025年</a>
  <!-- 所有年份 tab -->
</div>
```

### 年份区域

```html
<h2 id="s2027">2027年{考试名称}</h2>
<p style="color:var(--text-secondary);margin-bottom:16px;">满分{XX}分 · 考试时间{XX}分钟 · {其他信息}</p>

<h3>一、选择题（共{XX}分，{N}题×{X}分）</h3>

<!-- 选择题（有 q-source + q-tags） -->
<div class="exercise">
  <div class="q-source">📋 2027年真题 第1题</div>
  <div class="q-tags"><span>{知识点标签}</span><span>第{X}章</span></div>
  <div class="question"><span class="q-num">1</span>{题目文字}</div>
  <div class="options">
    <label><input type="radio" name="q27a1" value="A">A. {选项}</label>
    <label><input type="radio" name="q27a1" value="B">B. {选项}</label>
    <label><input type="radio" name="q27a1" value="C">C. {选项}</label>
    <label><input type="radio" name="q27a1" value="D">D. {选项}</label>
  </div>
  <button class="answer-btn" onclick="showAnswer(2701)">查看答案</button>
  <div class="answer" id="answer-2701" data-correct="B">✅ B。{解析}</div>
</div>

<h3>二、填空题（共{XX}分）</h3>

<!-- 填空题（无 .options，无 data-correct） -->
<div class="exercise">
  <div class="q-source">📋 2027年真题 第7题</div>
  <div class="q-tags"><span>{知识点标签}</span></div>
  <div class="question"><span class="q-num">7</span>{题目，含____填空}</div>
  <button class="answer-btn" onclick="showAnswer(2707)">查看答案</button>
  <div class="answer" id="answer-2707">✅ {答案}。{解析}</div>
</div>

<!-- 年份之间用 <hr> 分隔 -->
<hr style="margin:32px 0;border-color:var(--border);">
```

## 关键约束规则

### `showAnswer` ID 编号公式（最重要）

**考试页 MUST 使用 `year * 100 + questionNumber` 公式：**

- 2027 年第 1 题 → `showAnswer(2701)`，`id="answer-2701"`
- 2027 年第 15 题 → `showAnswer(2715)`，`id="answer-2715"`
- 2024 年第 1 题 → `showAnswer(2401)`，`id="answer-2401"`

### Radio `name` 格式

**考试页 MUST 使用 `q{YY}a{N}` 格式：**

- 2027 年第 1 题 → `name="q27a1"`
- 2027 年第 5 题 → `name="q27a5"`
- 2024 年第 3 题 → `name="q24a3"`

这个格式确保不同年份之间不会发生 radio 选择冲突。

### 题型区分

| 题型 | `.options` | `data-correct` | `showAnswer` 参数 |
|---|---|---|---|
| 选择题 | 有 | 有（大写字母） | `YYNN` |
| 填空题 | 无 | **无** | `YYNN` |
| 作图题 | 无 | **无** | `YYNN` |
| 综合题 | 无 | **无** | `YYNN` |

### `.q-source` 和 `.q-tags`

- `.q-source`：题目来源标签，格式 `📋 YYYY年真题 第N题`
- `.q-tags`：知识点标签，每个 `<span>` 是一个标签
- 这两个元素只在考试页使用，不在章节练习题页使用

## 多年份汇编模板

`exam_collection.html` 与单年份试卷结构相同，区别是：

1. 包含多个年份区域（每个 `<h2 id="sYYYY">`）
2. Sidebar 列出所有年份的锚点链接
3. 年份 tab 同样列出所有年份
4. 年份之间用 `<hr>` 分隔

## 级联更新

创建单年份试卷后，**必须**更新：

1. **`{subject}/index.html`**：在底部考试年份网格中添加链接
2. **`{subject}/exam_collection.html`**（如果存在）：添加新年份区域 + sidebar 链接 + 年份 tab

## 常见陷阱

- ❌ 忘记 `year * 100` 公式，使用简单序号 → 不同年份 ID 冲突
- ❌ radio `name` 不使用 `q{YY}a{N}` 格式 → 不同年份选项互相干扰
- ❌ 填空题的 `.answer` 添加了 `data-correct` → 无意义（common.js 找不到 radio 会跳过判断）
- ❌ 更新 `exam_collection.html` 时忘记同步更新 sidebar 和年份 tab
- ❌ Sidebar 链接全部指向同一个 `#sYYYY` → 复制粘贴 bug
- ❌ 忘记在 `{subject}/index.html` 添加新年份的考试链接