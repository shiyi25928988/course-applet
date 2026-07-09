---
name: create-special-topic
description: 生成学科专项突破/专题深度讲解页面（无侧边栏容器布局，含题目编号圆圈和答案展开）
---

# 创建专项突破/专题深度页面

## 适用场景

用户说"创建[主题]专题"、"电学专项突破"、"力学综合"、"添加专题深度页面"时触发。

## 信息收集

- **学科和专题名称**：例如 "初中物理电学专项突破"
- **专题英文 slug**：例如 `electricity`
- **题目数量**：通常 20-60 道精选题目
- **题目内容**：每题的标题、题目文字、答案、解析
- **是否需要侧边栏**：大多数专题页不需要（容器布局），少数需要

## 文件路径

```
{subject}/{topic}_special.html
```

示例：`physics/electricity_special.html`、`physics/mechanics_special.html`

## 两种布局

### 布局 A：容器布局（默认，多数专题页使用）

无侧边栏，全宽容器，适合纯题目列表。

### 布局 B：侧边栏布局（少用）

有侧边栏 + 主内容区，适合有子专题分类的页面。

## 布局 A 模板（容器布局）

### 页面骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{专题标题} - {学科}</title>
<link rel="stylesheet" href="../assets/css/common.css">
<script src="../assets/js/common.js"></script>
<style>
/* 专题特定样式 */
</style>
</head>
<body>
<div class="container">
  <!-- 返回链接 -->
  <div class="back-links">
    <a href="index.html">← {学科}</a>&nbsp;|&nbsp;
    <a href="../exam_bank.html">← 题库中心</a>
  </div>
  <!-- Hero -->
  <div class="hero">
    <h1>{Emoji} {专题标题}</h1>
    <p>{描述} · 共 {N} 道精选题目</p>
  </div>
  <!-- 题目列表 -->
  <!-- 占位提示 -->
</div>
</body>
</html>
```

### 必需的 CSS（在 `<style>` 中）

```css
.container {max-width:900px;margin:0 auto;padding:20px;}
.back-links {margin-bottom:20px;display:flex;gap:12px;flex-wrap:wrap;}
.back-links a {
  display:inline-flex;align-items:center;padding:10px 18px;
  background:linear-gradient(135deg,{学科色1},{学科色2});color:#fff!important;
  text-decoration:none;border-radius:8px;font-weight:500;font-size:0.9rem;
  box-shadow:0 2px 8px rgba(0,0,0,.2);transition:all .3s ease;
}
.back-links a:hover {transform:translateY(-2px);box-shadow:0 4px 12px rgba(0,0,0,.35);}
.back-links a::before {content:"←";margin-right:6px;font-weight:bold;}

.hero {
  background:linear-gradient(135deg,{学科色1},{学科色2});
  color:#fff;padding:24px;border-radius:12px;margin-bottom:24px;
}
.hero h1 {font-size:1.5rem;margin-bottom:8px;}
.hero p {font-size:.95rem;opacity:.9;}

.question {
  background:#fff;border-radius:10px;padding:20px;margin-bottom:20px;
  box-shadow:0 2px 8px rgba(0,0,0,.06);
}

.q-num {
  display:inline-block;background:{学科色1};color:#fff;
  width:32px;height:32px;border-radius:50%;text-align:center;
  line-height:32px;font-weight:700;margin-right:10px;
}
.q-title {
  display:inline-block;font-weight:600;color:#1e293b;font-size:1.05rem;
}
.q-content {
  margin-top:16px;line-height:1.8;color:#374151;
}

.answer-btn {
  margin-top:16px;padding:10px 20px;background:{学科色1};color:#fff;
  border:none;border-radius:6px;cursor:pointer;font-size:.95rem;
}
.answer-btn:hover {opacity:.9;}

.answer {
  display:none;margin-top:16px;padding:16px;
  background:{学科浅色};border-radius:8px;border-left:3px solid {学科色1};
}
.answer.show {display:block;}
.answer-value {font-weight:600;color:{学科深色};margin-bottom:8px;}
.answer-solution {color:#475569;line-height:1.7;}
.answer-solution strong {color:{学科色1};}
```

### 题目区块结构

```html
<div class="question">
  <span class="q-num">1</span>
  <span class="q-title">{题目小标题}</span>
  <div class="q-content">
    {题目正文，可包含公式、分步骤问题等}
  </div>
  <button class="answer-btn" onclick="showAnswer(1)">查看答案与解析</button>
  <div class="answer" id="answer-1">
    <div class="answer-value">答案：{答案内容}</div>
    <div class="answer-solution"><strong>解析：</strong><br>{详细解析}</div>
  </div>
</div>
```

### 占位提示

```html
<div style="text-align:center;padding:20px;color:#64748b;background:#fff;border-radius:10px">
  <strong>更多题目整理中... 完整 {N} 道{专题}题正在陆续添加</strong>
</div>
```

## 布局 B 模板（侧边栏布局）

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{专题标题} - {学科}</title>
<link rel="stylesheet" href="../assets/css/common.css">
<style>
/* 专题特定样式 */
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <h3>{专题 Emoji} {专题名称}</h3>
    <ul class="chapter-list">
      <li><a href="#sub1">子专题1</a></li>
      <li><a href="#sub2">子专题2</a></li>
      <li><a href="#sub3">子专题3</a></li>
      <li style="margin-top:20px;"><a href="index.html">← {学科}目录</a></li>
    </ul>
    <div style="padding:16px 0;margin-top:8px;border-top:1px solid var(--border);">
      <a href="../index.html" class="back-home">🏠 返回首页</a>
    </div>
  </aside>
  <main class="main">
    <div class="page-title">{专题标题}</div>
    <!-- 子专题内容区域 -->
    <h2 id="sub1">子专题1</h2>
    <!-- 题目列表 -->
    <h2 id="sub2">子专题2</h2>
    <!-- 题目列表 -->
  </main>
</div>
<script src="../assets/js/common.js"></script>
</body>
</html>
```

## 关键约束规则

### 答案机制
- 使用 `common.js` 的 `showAnswer(N)` 函数
- 答案 div 使用 `id="answer-N"` 匹配
- **不需要** `data-correct` 属性（专题页只展示答案，不判断对错）
- 答案 div 包含 `.answer-value`（答案）和 `.answer-solution`（解析）两个子元素

### 题目编号
- `.q-num` 是圆形编号徽章（`border-radius:50%`）
- 背景色使用学科主题色

### 学科颜色对照

| 学科 | 主色 | 浅色 | 深色 |
|---|---|---|---|
| 物理 | `#2563eb` | `#dbeafe` | `#1e40af` |
| 化学 | `#059669` | `#d1fae5` | `#065f46` |
| 数学 | `#7c3aed` | `#ede9fe` | `#5b21b6` |

### 路径
- CSS：`../assets/css/common.css`
- JS：`../assets/js/common.js`（**放在 `<head>` 中**，因为 `showAnswer` 在页面加载时就需要）
- 返回链接：`index.html`（学科目录）+ `../exam_bank.html`（题库中心）

## 级联更新

创建专题页面后，**必须**更新：

1. **`{subject}/index.html`**：在合适位置添加专题入口链接或卡片
2. 更新占位提示中的总题目数，使其与实际一致

## 常见陷阱

- ❌ 给 `.answer` 添加 `data-correct` 属性 → 无意义（没有 radio 供判断）
- ❌ 忘记在 `<head>` 中引入 `common.js` → `showAnswer` 未定义
- ❌ `.q-num` 使用默认样式而非圆形 → 与专题页风格不一致
- ❌ `showAnswer(N)` 参数与 `id="answer-N"` 不匹配
- ❌ 选择错误的布局（子专题分类多的内容应使用侧边栏布局）
- ❌ 忘记添加返回链接 → 用户无法导航离开