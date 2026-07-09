---
name: create-exercises
description: 为指定章节生成专项练习题页面（选择题+填空题+计算题，含进度条和填空检查）
---

# 创建章节练习题页面

## 适用场景

用户说"为第X章创建练习题"、"添加练习"、"生成[主题]的测验"时触发。

## 信息收集

- **所属章节文件**：例如 `physics/ch01_sound.html`
- **题目总数**：默认 15 题
- **题型分布**：例如 10 选择 + 3 填空 + 2 计算
- **题目内容**：每题的题干、选项、答案、解析

## 文件路径

```
{subject}/ch{NN}_{topic}_exercises.html
```

- 与父章节页面同名，加 `_exercises` 后缀
- 示例：`physics/ch01_sound_exercises.html`

## HTML 模板

### 页面骨架

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{章节标题} - 专项练习</title>
<link rel="stylesheet" href="../assets/css/common.css">
<style>
.fill input{width:120px;padding:6px 10px;border:2px solid var(--border);border-radius:6px;font-size:.95rem;}
.fill input.correct{border-color:var(--success);background:#dcfce7;}
.fill input.wrong{border-color:var(--danger);background:#fef2f2;}
.progress-bar{background:var(--border);height:8px;border-radius:4px;margin-bottom:24px;overflow:hidden;}
.progress-bar .fill-bar{height:100%;background:linear-gradient(90deg,var(--primary),#7c3aed);border-radius:4px;transition:width .4s;}
</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <!-- 简化 sidebar -->
  </aside>
  <main class="main">
    <!-- 题目列表 -->
  </main>
</div>
<script src="../assets/js/common.js"></script>
<script>
// checkFill 和 checkFill2 函数
</script>
</body>
</html>
```

### Sidebar 结构（简化版）

```html
<aside class="sidebar">
  <h3>📝 专项练习</h3>
  <ul class="chapter-list">
    <li><a href="#q1">第1题</a></li>
    <li><a href="#q6">第6题</a></li>
    <li><a href="#q11">第11题</a></li>
    <li style="margin-top:20px;"><a href="ch01_sound.html">← 返回{章节}课件</a></li>
  </ul>
  <div style="padding:16px 0;margin-top:8px;border-top:1px solid var(--border);">
    <a href="../index.html" class="back-home">🏠 返回首页</a>
  </div>
</aside>
```

Sidebar 的快速跳转链接应该每 5 题一个锚点。

### Main 内容区

```html
<main class="main">
  <div class="page-title">{章节标题}专项练习</div>
  <p style="color:var(--text-secondary);margin-bottom:20px;">共{N}题 · 覆盖{知识点范围}</p>

  <!-- 进度条 -->
  <div class="progress-bar">
    <div class="fill-bar" id="progress" style="width:0%;"></div>
  </div>

  <!-- 选择题 -->
  <h3 style="margin:24px 0 16px;">一、选择题</h3>

  <div class="exercise" id="q1">
    <div class="question"><span class="q-num">1</span>{题目}</div>
    <div class="options">
      <label><input type="radio" name="q1" value="A">A. {选项}</label>
      <label><input type="radio" name="q1" value="B">B. {选项}</label>
      <label><input type="radio" name="q1" value="C">C. {选项}</label>
      <label><input type="radio" name="q1" value="D">D. {选项}</label>
    </div>
    <button class="answer-btn" onclick="showAnswer(1)">查看答案</button>
    <div class="answer" id="answer-1" data-correct="A">✅ A。{解析}</div>
  </div>

  <!-- 填空题（单空） -->
  <h3 style="margin:24px 0 16px;">二、填空题</h3>

  <div class="exercise" id="q11">
    <div class="question"><span class="q-num">11</span>【填空题】{题目，用____标记填空位置}</div>
    <div class="fill">
      <input type="text" id="fill11" placeholder="请填写答案">
      <button class="answer-btn" onclick="checkFill(11,'{正确答案}')">检查</button>
    </div>
    <div class="answer" id="answer-11">✅ {正确答案}。{解析}</div>
  </div>

  <!-- 填空题（双空） -->
  <div class="exercise" id="q12">
    <div class="question"><span class="q-num">12</span>【填空题】{题目，有两个____和____}</div>
    <div class="fill">
      <input type="text" id="fill12a" placeholder="第一空">
      <input type="text" id="fill12b" placeholder="第二空" style="margin-left:8px;">
      <button class="answer-btn" onclick="checkFill2(12,'{答案1}','{答案2}')">检查</button>
    </div>
    <div class="answer" id="answer-12">✅ {答案1}、{答案2}。{解析}</div>
  </div>

  <!-- 返回链接 -->
  <div style="margin-top:32px;text-align:center;">
    <a href="ch01_sound.html" style="color:var(--primary);">← 返回课件</a>
  </div>
</main>
```

### 必需的 JS 函数

```javascript
<script src="../assets/js/common.js"></script>
<script>
function checkFill(n,answer){
  const el=document.getElementById('fill'+n);
  if(!el)return;
  const ans=document.getElementById('answer-'+n);
  if(el.value.trim()===answer){
    el.classList.add('correct');el.classList.remove('wrong');
    ans.classList.add('show','correct');ans.classList.remove('wrong');
  }else{
    el.classList.add('wrong');el.classList.remove('correct');
    ans.classList.add('show','wrong');ans.classList.remove('correct');
  }
}

function checkFill2(n,a1,a2){
  const e1=document.getElementById('fill'+n+'a'),
        e2=document.getElementById('fill'+n+'b');
  const ans=document.getElementById('answer-'+n);
  if(!e1||!e2)return;
  if(e1.value.trim()===a1&&e2.value.trim()===a2){
    e1.classList.add('correct');e2.classList.add('correct');
    e1.classList.remove('wrong');e2.classList.remove('wrong');
    ans.classList.add('show','correct');ans.classList.remove('wrong');
  }else{
    e1.classList.add('wrong');e2.classList.add('wrong');
    e1.classList.remove('correct');e2.classList.remove('correct');
    ans.classList.add('show','wrong');ans.classList.remove('correct');
  }
}
</script>
```

## 关键约束规则

### 输入 ID 命名
- 单空：`fill{N}`（例如 `fill11`）
- 双空：`fill{N}a` 和 `fill{N}b`（例如 `fill12a`, `fill12b`）
- `checkFill(N, answer)` 参数 N 必须与输入 ID 匹配

### 题型区分
- 选择题：有 `.options` 区 + `data-correct` 属性 + `showAnswer(N)` 按钮
- 填空题：有 `.fill` 区 + 文本输入框 + `checkFill(N, answer)` 按钮
- 填空题的 `.answer` 区 **不需要** `data-correct` 属性（不使用 common.js 的判断逻辑）
- 计算题/简答题：只有 `.question` + `showAnswer(N)` 按钮（无选项，无 `data-correct`）

### 进度条
- CSS 必须包含 `.progress-bar` 和 `.fill-bar` 样式
- 进度条是装饰性的，不需要 JS 联动

### 必须的 CSS（在 `<style>` 中）
```css
.fill input{width:120px;padding:6px 10px;border:2px solid var(--border);border-radius:6px;font-size:.95rem;}
.fill input.correct{border-color:var(--success);background:#dcfce7;}
.fill input.wrong{border-color:var(--danger);background:#fef2f2;}
.progress-bar{background:var(--border);height:8px;border-radius:4px;margin-bottom:24px;overflow:hidden;}
.progress-bar .fill-bar{height:100%;background:linear-gradient(90deg,var(--primary),#7c3aed);border-radius:4px;transition:width .4s;}
```

## 级联更新

创建练习题页面后，**必须**更新：

1. **父章节页面** `{subject}/chNN_topic.html`：
   - 在练习题区域末尾或 sidebar 中添加链接：
   - `<a href="ch01_sound_exercises.html">📝 更多练习题 →</a>`

## 常见陷阱

- ❌ 填空输入 ID 与 `checkFill` 参数不匹配（`id="fill11"` 但 `checkFill(12, ...)`）
- ❌ `checkFill`/`checkFill2` 函数忘记内联定义 → 按钮无响应（这两个函数不在 common.js 中）
- ❌ 填空题的 `.answer` 添加了 `data-correct` → 无意义且可能混淆
- ❌ 双空题输入框忘记 `fillNa`/`fillNb` 的 `a`/`b` 后缀
- ❌ Sidebar 的 `#q1` 锚点链接遗漏了 exercise div 上的 `id="q1"`
- ❌ 忘记在父章节页面添加练习题链接 → 用户找不到这个页面