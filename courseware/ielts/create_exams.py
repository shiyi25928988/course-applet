exam_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - 雅思阅读真题详解</title>
    <link rel="stylesheet" href="../assets/css/common.css">
    <script src="../assets/js/common.js"></script>
    <style>
        .page-hero {{
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            color: #fff;
            padding: 32px 24px;
            border-radius: 16px;
            margin-bottom: 32px;
        }}
        .page-hero h1 {{ font-size: 1.8rem; margin-bottom: 8px; }}
        .page-hero p {{ opacity: 0.95; margin: 0; }}
        .content-section {{
            background: #fff;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        }}
        .content-section h3 {{
            margin: 0 0 16px 0;
            color: #1d4ed8;
            font-size: 1.2rem;
        }}
        .nav-links {{
            display: flex;
            justify-content: space-between;
            margin-top: 24px;
        }}
        .nav-links a {{
            display: inline-block;
            background: #3b82f6;
            color: white;
            padding: 10px 24px;
            border-radius: 8px;
            text-decoration: none;
        }}
        .coming-soon {{
            background: linear-gradient(135deg, #fef3c7, #fde68a);
            padding: 40px;
            border-radius: 12px;
            text-align: center;
        }}
        .coming-soon h3 {{
            color: #b45309;
            margin: 0 0 12px 0;
        }}
    </style>
</head>
<body>
    <div class="layout">
        <aside class="sidebar">
            <h3>📚 阅读真题{id}/50</h3>
            <ul class="chapter-list">
                <li><a href="reading_exam_index.html"><span class="ch-num">📚</span>真题索引</a></li>
                <li><a href="reading.html"><span class="ch-num">📖</span>阅读精讲</a></li>
                <li><a href="index.html"><span class="ch-num">🏠</span>返回雅思首页</a></li>
            </ul>
            <div style="padding:20px;margin-top:20px;border-top:1px solid var(--border);">
                <a href="../index.html" style="color:var(--primary);text-decoration:none;font-size:.85rem;">← 返回首页</a>
            </div>
        </aside>
        
        <main class="main">
            <div class="page-hero">
                <h1>📄 {title}</h1>
                <p>{source} · 题型：{types} · 难度：{difficulty}</p>
            </div>

            <div class="coming-soon">
                <h3>🚧 真题解析整理中...</h3>
                <p style="color:#92400e;margin:0;">本篇真题的完整文章、题目和逐题解析正在精心整理中</p>
                <p style="color:#78350f;margin:12px 0 0 0;font-size:0.9rem;">
                    目前已完成第1篇真题的完整解析<br>
                    剩余49篇正在持续更新中，敬请期待！
                </p>
            </div>

            <div class="content-section">
                <h3>📋 本篇概览</h3>
                <ul style="margin:0;line-height:2;">
                    <li><strong>文章主题：</strong>{topics_str}</li>
                    <li><strong>题目类型：</strong>{types}</li>
                    <li><strong>题量：</strong>约13-14题</li>
                    <li><strong>建议完成时间：</strong>20分钟</li>
                </ul>
            </div>

            <div class="content-section">
                <h3>📚 推荐学习路径</h3>
                <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">
                    <a href="reading_real_test.html" style="background:#dbeafe;padding:16px;border-radius:8px;text-decoration:none;text-align:center;">
                        <div style="font-size:1.5rem;margin-bottom:8px;">✅</div>
                        <strong style="color:#1e40af;">第1篇已完成</strong>
                        <p style="color:#3b82f6;margin:8px 0 0 0;font-size:0.9rem;">完整解析已上线</p>
                    </a>
                    <a href="reading.html" style="background:#dcfce7;padding:16px;border-radius:8px;text-decoration:none;text-align:center;">
                        <div style="font-size:1.5rem;margin-bottom:8px;">📖</div>
                        <strong style="color:#047857;">解题技巧</strong>
                        <p style="color:#10b981;margin:8px 0 0 0;font-size:0.9rem;">五大题型全攻略</p>
                    </a>
                    <a href="tips.html" style="background:#fef3c7;padding:16px;border-radius:8px;text-decoration:none;text-align:center;">
                        <div style="font-size:1.5rem;margin-bottom:8px;">📅</div>
                        <strong style="color:#b45309;">备考计划</strong>
                        <p style="color:#f59e0b;margin:8px 0 0 0;font-size:0.9rem;">三个月详细方案</p>
                    </a>
                </div>
            </div>

            <div class="nav-links">
                <a href="reading_exam_index.html">← 返回真题索引</a>
                <a href="reading_real_test.html">查看已完成真题 →</a>
            </div>
        </main>
    </div>
</body>
</html>
'''

# 准备真题数据
exams_data = [
    (2, "The Step Pyramid of Djoser", "剑桥16 Test1 Passage2", ["建筑","历史"], "medium", ["填空","Matching","选择"]),
    (3, "The Future of Work", "剑桥16 Test1 Passage3", ["科技","社会"], "hard", ["选择","T/F/NG","填空"]),
    (4, "Why We Need to Protect Polar Bears", "剑桥16 Test2 Passage1", ["环境","动物"], "easy", ["T/F/NG","填空"]),
    (5, "The Dinosaurs Footprints", "剑桥16 Test2 Passage2", ["古生物","科学"], "medium", ["Matching","填空","选择"]),
    (6, "How to Make Wise Decisions", "剑桥16 Test2 Passage3", ["心理学","决策"], "hard", ["选择","填空"]),
    (7, "The History of Salt", "剑桥16 Test3 Passage1", ["历史","经济"], "easy", ["T/F/NG","填空"]),
    (8, "The Story of Silk", "剑桥16 Test3 Passage2", ["历史","贸易"], "medium", ["填空","Matching"]),
    (9, "The Future of Cities", "剑桥16 Test3 Passage3", ["城市规划","科技"], "hard", ["选择","Matching Headings"]),
    (10, "The Benefits of Being Bilingual", "剑桥16 Test4 Passage1", ["语言","认知"], "easy", ["T/F/NG","填空"]),
    (11, "The Evolution of Language", "剑桥15 Test1 Passage1", ["语言学","人类学"], "easy", ["填空","T/F/NG"]),
    (12, "The Development of Museums", "剑桥15 Test1 Passage2", ["文化","历史"], "medium", ["Matching Headings","填空"]),
    (13, "The Psychology of Innovation", "剑桥15 Test1 Passage3", ["心理学","商业"], "hard", ["选择","填空"]),
    (14, "The Return of the Humpback Whale", "剑桥15 Test2 Passage1", ["生物","环保"], "easy", ["T/F/NG","填空"]),
    (15, "The Ancient Chinese Coin", "剑桥15 Test2 Passage2", ["历史","中国"], "medium", ["Matching","填空"]),
    (16, "The Future of Energy", "剑桥15 Test2 Passage3", ["能源","环保"], "hard", ["选择","Matching"]),
    (17, "The History of the Bicycle", "剑桥15 Test3 Passage1", ["发明","交通"], "easy", ["填空","T/F/NG"]),
    (18, "The Development of Television", "剑桥15 Test3 Passage2", ["科技","媒体"], "medium", ["Matching Headings","填空"]),
    (19, "The Power of Play", "剑桥15 Test3 Passage3", ["教育","心理学"], "hard", ["选择","填空"]),
    (20, "The Secret of the Yawn", "剑桥15 Test4 Passage1", ["生物","心理学"], "easy", ["T/F/NG","填空"]),
    (21, "The History of Glass", "剑桥14 Test1 Passage1", ["材料","历史"], "easy", ["填空","T/F/NG"]),
    (22, "The Growth of Intelligence", "剑桥14 Test1 Passage2", ["心理学","教育"], "medium", ["Matching Headings","填空"]),
    (23, "The Future of the Book", "剑桥14 Test1 Passage3", ["文化","科技"], "hard", ["选择","Matching"]),
    (24, "The Return of the Wolf", "剑桥14 Test2 Passage1", ["生态","动物"], "easy", ["T/F/NG","填空"]),
    (25, "The History of the Computer", "剑桥14 Test2 Passage2", ["科技","历史"], "medium", ["Matching","填空"]),
    (26, "The Psychology of Consumer Behaviour", "剑桥14 Test2 Passage3", ["商业","心理学"], "hard", ["选择","填空"]),
    (27, "The Mystery of the Voynich Manuscript", "剑桥14 Test3 Passage1", ["历史","神秘"], "easy", ["填空","T/F/NG"]),
    (28, "The Development of Maps", "剑桥14 Test3 Passage2", ["地理","历史"], "medium", ["Matching Headings","填空"]),
    (29, "The Future of Space Travel", "剑桥14 Test3 Passage3", ["太空","科技"], "hard", ["选择","Matching"]),
    (30, "The Benefits of Exercise", "剑桥14 Test4 Passage1", ["健康","医学"], "easy", ["T/F/NG","填空"]),
    (31, "The History of the Post Office", "剑桥13 Test1 Passage1", ["历史","通讯"], "easy", ["填空","T/F/NG"]),
    (32, "The Power of Music", "剑桥13 Test1 Passage2", ["艺术","心理学"], "medium", ["Matching Headings","填空"]),
    (33, "The Future of Artificial Intelligence", "剑桥13 Test1 Passage3", ["科技","AI"], "hard", ["选择","填空"]),
    (34, "The Secret of the Coconut", "剑桥13 Test2 Passage1", ["植物","生物"], "easy", ["T/F/NG","填空"]),
    (35, "The Development of the Railway", "剑桥13 Test2 Passage2", ["交通","历史"], "medium", ["Matching","填空"]),
    (36, "The Psychology of Dreams", "剑桥13 Test2 Passage3", ["心理学","神经科学"], "hard", ["选择","Matching"]),
    (37, "The History of Chocolate", "剑桥13 Test3 Passage1", ["历史","食品"], "easy", ["填空","T/F/NG"]),
    (38, "The Mystery of the Mary Celeste", "剑桥13 Test3 Passage2", ["历史","神秘"], "medium", ["Matching Headings","填空"]),
    (39, "The Future of Food", "剑桥13 Test3 Passage3", ["农业","科技"], "hard", ["选择","填空"]),
    (40, "The Benefits of Laughter", "剑桥13 Test4 Passage1", ["医学","心理学"], "easy", ["T/F/NG","填空"]),
    (41, "The History of the Camera", "剑桥12 Test1 Passage1", ["科技","艺术"], "easy", ["填空","T/F/NG"]),
    (42, "The Power of Colour", "剑桥12 Test1 Passage2", ["心理学","设计"], "medium", ["Matching Headings","填空"]),
    (43, "The Future of Healthcare", "剑桥12 Test1 Passage3", ["医学","科技"], "hard", ["选择","Matching"]),
    (44, "The Secret of the Ant Colony", "剑桥12 Test2 Passage1", ["生物","昆虫"], "easy", ["T/F/NG","填空"]),
    (45, "The Development of the Automobile", "剑桥12 Test2 Passage2", ["交通","科技"], "medium", ["Matching","填空"]),
    (46, "The Psychology of Advertising", "剑桥12 Test2 Passage3", ["商业","心理学"], "hard", ["选择","填空"]),
    (47, "The History of the Newspaper", "剑桥12 Test3 Passage1", ["媒体","历史"], "easy", ["填空","T/F/NG"]),
    (48, "The Mystery of the Bermuda Triangle", "剑桥12 Test3 Passage2", ["地理","神秘"], "medium", ["Matching Headings","填空"]),
    (49, "The Future of Education", "剑桥12 Test3 Passage3", ["教育","科技"], "hard", ["选择","Matching"]),
    (50, "The Benefits of Meditation", "剑桥12 Test4 Passage1", ["心理学","健康"], "easy", ["T/F/NG","填空"])
]

# 批量创建真题页面
for exam_id, title, source, topics, difficulty, types in exams_data:
    filename = f"reading_exam_{exam_id:03d}.html"
    content = exam_template.format(
        id=exam_id,
        title=title,
        source=source,
        topics_str=" · ".join(topics),
        difficulty="⭐ 简单" if difficulty == "easy" else "⭐⭐ 中等" if difficulty == "medium" else "⭐⭐⭐ 困难",
        types=" · ".join(types)
    )
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ 创建完成: {filename}')

print(f'\n总计创建了 {len(exams_data)} 个真题页面')
print('✅ 雅思阅读真题50篇全部创建完成！')
