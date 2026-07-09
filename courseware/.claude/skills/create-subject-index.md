---
name: create-subject-index
description: 生成或更新学科目录首页（章节网格+考试链接+侧边栏导航+Hero Banner）
---

# 创建/更新学科目录首页

## 适用场景

用户说"创建新学科"、"更新物理首页"、"添加学科目录"时触发。

## 信息收集

- **学科中文名**：例如 "初中物理"
- **学科英文 slug**：例如 `physics`
- **学科 Emoji**：例如 "⚛️"
- **学科主题色**：例如 `#2563eb`（物理蓝）、`#059669`（化学绿）、`#7c3aed`（数学紫）
- **教材信息**：年级范围、册数、章节数
- **章节列表**：每章 `{编号, 中文标题, 英文文件名 slug, 节数摘要, 所属年级/学期, 特色标签}`
- **可用考试年份**：例如 2017-2027

## 文件路径

```
{subject}/index.html
```

示例：`physics/index.html`、`chemistry/index.html`

## HTML 模板

### 页面骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{学科中文名} · {教材版本}课件</title>
<link rel="stylesheet" href="../assets/css/common.css">
<style>
/* 学科特定的 hero、ch-card、ch-grid 样式 */
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <!-- 完整章节列表 -->
  </aside>
  <main class="main">
    <!-- Hero + 章节网格 + 考试链接 -->
  </main>
</div>
</body>
</html>
```

### Sidebar 结构

```html
<aside class="sidebar">
  <h3>{学科 Emoji} {学科名称}</h3>
  <ul class="chapter-list">
    <li><a href="ch01_sound.html"><span class="ch-num">1</span>声</a></li>
    <li><a href="ch02_light.html"><span class="ch-num">2</span>光</a></li>
    <li><a href="ch03_motion_force.html"><span class="ch-num">3</span>运动和力</a></li>
    <!-- ... 列出所有章节 ... -->
  </ul>
  <div style="padding:16px 0;margin-top:8px;border-top:1px solid var(--border);">
    <a href="../index.html" class="back-home">🏠 返回首页</a>
  </div>
</aside>
```

### Main 内容区

```html
<main class="main">
  <!-- Hero Banner -->
  <div class="phy-hero">
    <h1>{学科 Emoji} {学科名称}</h1>
    <p>{描述} · {教材版本} · 共{N}章</p>
  </div>

  <!-- 考试汇编链接（如有考试） -->
  <div style="margin-bottom:28px;">
    <a href="exam_collection.html" style="display:inline-block;padding:12px 24px;background:var(--warning);color:#fff;border-radius:10px;text-decoration:none;font-weight:600;">
      📝 中考真题汇编（2017-2027）
    </a>
  </div>

  <!-- 章节网格 — 按年级/学期分组 -->
  <h2 style="margin-bottom:16px;">八年级第一学期</h2>
  <div class="ch-grid">
    <a href="ch01_sound.html" class="ch-card">
      <div class="grade">八年级上</div>
      <h3>第一章 声</h3>
      <div class="sections">1.1 声波的产生和传播 · 1.2 声音的特征</div>
      <div class="sub-count">2节 · 含声波动画</div>
    </a>
    <a href="ch02_light.html" class="ch-card">
      <div class="grade">八年级上</div>
      <h3>第二章 光</h3>
      <div class="sections">1.1 光的反射 · 1.2 光的折射 · 1.3 透镜成像 · 1.4 光的色散</div>
      <div class="sub-count">4节 · 含透镜模拟</div>
    </a>
    <!-- ... 更多章节卡片 ... -->
  </div>

  <h2 style="margin:32px 0 16px;">八年级第二学期</h2>
  <div class="ch-grid">
    <!-- ... -->
  </div>

  <!-- 考试年份网格 -->
  <h2 style="margin:32px 0 16px;">📝 中考真题（按年份）</h2>
  <div style="display:grid; grid-template-columns:repeat(5,1fr); gap:12px; margin-bottom:24px;">
    <a href="exam_2027.html" style="text-align:center;padding:12px;background:#fff;border-radius:8px;text-decoration:none;color:var(--text);box-shadow:var(--shadow);">2027年</a>
    <a href="exam_2026.html" style="...">2026年</a>
    <!-- ... 每年一个链接 ... -->
  </div>
</main>
```

### 必需的 CSS（在 `<style>` 中）

```css
/* Hero — 使用学科主题色 */
.phy-hero {background:linear-gradient(135deg,#2563eb,#7c3aed);color:#fff;border-radius:20px;padding:40px 24px;margin-bottom:28px;}
.phy-hero h1 {font-size:1.8rem;margin-bottom:8px;}
.phy-hero p {opacity:.9;}

/* 化学用 .chem-hero */
.chem-hero {background:linear-gradient(135deg,#059669,#10b981);color:#fff;border-radius:20px;padding:40px 24px;margin-bottom:28px;}

/* 章节网格 */
.ch-grid {display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px;margin-bottom:32px;}

/* 章节卡片 */
.ch-card {
  background:#fff;border-radius:14px;padding:20px;text-decoration:none;
  box-shadow:0 2px 8px rgba(0,0,0,.06);border-left:4px solid {学科主题色};
  transition:transform .2s,box-shadow .2s;display:block;color:var(--text);
}
.ch-card:hover {transform:translateY(-2px);box-shadow:0 6px 20px rgba(0,0,0,.1);}
.ch-card .grade {font-size:.75rem;color:{学科主题色};font-weight:600;margin-bottom:4px;}
.ch-card h3 {font-size:1.05rem;margin-bottom:6px;}
.ch-card .sections {font-size:.8rem;color:var(--text-secondary);line-height:1.5;}

/* 物理/数学用 .sub-count */
.ch-card .sub-count {
  display:inline-block;margin-top:8px;font-size:.75rem;
  padding:3px 8px;background:{学科-light色};color:{学科主题色};border-radius:10px;
}

/* 化学用 .badge */
.ch-card .badge {
  display:inline-block;margin-top:8px;font-size:.75rem;
  padding:3px 8px;background:{学科-light色};color:{学科主题色};border-radius:10px;
}
```

## 关键约束规则

### 学科主题色对照

| 学科 | 主题色 | CSS 变量 | Hero 类名 | 卡片标签类 |
|---|---|---|---|---|
| 物理 | `#2563eb` | `--physics` | `.phy-hero` | `.sub-count` |
| 化学 | `#059669` | `--chemistry` | `.chem-hero` | `.badge` |
| 数学 | `#7c3aed` | 自定义 | `.math-hero` | `.sub-count` |
| 语文 | `#dc2626` | 自定义 | `.chinese-hero` | `.sub-count` |

### 卡片结构

- `.ch-card` 必须是 `<a>` 元素（可点击的整体卡片），不是 `<div>`
- 物理/数学使用 `.sub-count` 标签
- 化学使用 `.badge` 标签
- `border-left` 颜色必须与学科主题色一致

### 考试年份网格

- 使用 `grid-template-columns:repeat(5,1fr)`（5 列）
- 响应式下自动折行

### 路径

- CSS/JS：`../assets/css/common.css`（从学科子目录往上一级）
- 返回首页：`../index.html`

## 级联更新

创建/更新学科首页后，**必须**更新：

1. **根 `index.html`**：
   - 在正确的区域（初中阶段/高中阶段/竞赛专区）添加 `.subject-card`
   - 包含：icon、标题、描述、meta 标签、章节预览
   - `border-top` 颜色匹配学科主题

2. **`exam_bank.html`**（如有考试）：
   - 添加该学科的考试入口卡片

## 常见陷阱

- ❌ 化学首页使用 `.sub-count` 而非 `.badge` → 风格不一致
- ❌ 忘记更新 sidebar 中的章节列表
- ❌ `.ch-card` 使用 `<div>` 而非 `<a>` → 不可点击
- ❌ 考试年份网格使用错误的列数（应为 5 列）
- ❌ 根 `index.html` 放错区域（初中内容放到了高中区域）
- ❌ Hero 颜色与学科不匹配（化学用蓝色、物理用绿色）