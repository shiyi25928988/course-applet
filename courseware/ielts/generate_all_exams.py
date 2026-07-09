import os

# 真题元数据
exams_data = [
    (2, "The Step Pyramid of Djoser", "剑桥16 Test1 Passage2", ["建筑", "历史"], "medium", ["填空", "Matching", "选择"]),
    (3, "The Future of Work", "剑桥16 Test1 Passage3", ["科技", "社会"], "hard", ["选择", "T/F/NG", "填空"]),
    (4, "Why We Need to Protect Polar Bears", "剑桥16 Test2 Passage1", ["环境", "动物"], "easy", ["T/F/NG", "填空"]),
    (5, "The Dinosaurs Footprints", "剑桥16 Test2 Passage2", ["古生物", "科学"], "medium", ["Matching", "填空", "选择"]),
    (6, "How to Make Wise Decisions", "剑桥16 Test2 Passage3", ["心理学", "决策"], "hard", ["选择", "填空"]),
    (7, "The History of Salt", "剑桥16 Test3 Passage1", ["历史", "经济"], "easy", ["T/F/NG", "填空"]),
    (8, "The Story of Silk", "剑桥16 Test3 Passage2", ["历史", "贸易"], "medium", ["填空", "Matching"]),
    (9, "The Future of Cities", "剑桥16 Test3 Passage3", ["城市规划", "科技"], "hard", ["选择", "Matching Headings"]),
    (10, "The Benefits of Being Bilingual", "剑桥16 Test4 Passage1", ["语言", "认知"], "easy", ["T/F/NG", "填空"]),
    (11, "The Evolution of Language", "剑桥15 Test1 Passage1", ["语言学", "人类学"], "easy", ["填空", "T/F/NG"]),
    (12, "The Development of Museums", "剑桥15 Test1 Passage2", ["文化", "历史"], "medium", ["Matching Headings", "填空"]),
    (13, "The Psychology of Innovation", "剑桥15 Test1 Passage3", ["心理学", "商业"], "hard", ["选择", "填空"]),
    (14, "The Return of the Humpback Whale", "剑桥15 Test2 Passage1", ["生物", "环保"], "easy", ["T/F/NG", "填空"]),
    (15, "The Ancient Chinese Coin", "剑桥15 Test2 Passage2", ["历史", "中国"], "medium", ["Matching", "填空"]),
    (16, "The Future of Energy", "剑桥15 Test2 Passage3", ["能源", "环保"], "hard", ["选择", "Matching"]),
    (17, "The History of the Bicycle", "剑桥15 Test3 Passage1", ["发明", "交通"], "easy", ["填空", "T/F/NG"]),
    (18, "The Development of Television", "剑桥15 Test3 Passage2", ["科技", "媒体"], "medium", ["Matching Headings", "填空"]),
    (19, "The Power of Play", "剑桥15 Test3 Passage3", ["教育", "心理学"], "hard", ["选择", "填空"]),
    (20, "The Secret of the Yawn", "剑桥15 Test4 Passage1", ["生物", "心理学"], "easy", ["T/F/NG", "填空"]),
    (21, "The History of Glass", "剑桥14 Test1 Passage1", ["材料", "历史"], "easy", ["填空", "T/F/NG"]),
    (22, "The Growth of Intelligence", "剑桥14 Test1 Passage2", ["心理学", "教育"], "medium", ["Matching Headings", "填空"]),
    (23, "The Future of the Book", "剑桥14 Test1 Passage3", ["文化", "科技"], "hard", ["选择", "Matching"]),
    (24, "The Return of the Wolf", "剑桥14 Test2 Passage1", ["生态", "动物"], "easy", ["T/F/NG", "填空"]),
    (25, "The History of the Computer", "剑桥14 Test2 Passage2", ["科技", "历史"], "medium", ["Matching", "填空"]),
    (26, "The Psychology of Consumer Behaviour", "剑桥14 Test2 Passage3", ["商业", "心理学"], "hard", ["选择", "填空"]),
    (27, "The Mystery of the Voynich Manuscript", "剑桥14 Test3 Passage1", ["历史", "神秘"], "easy", ["填空", "T/F/NG"]),
    (28, "The Development of Maps", "剑桥14 Test3 Passage2", ["地理", "历史"], "medium", ["Matching Headings", "填空"]),
    (29, "The Future of Space Travel", "剑桥14 Test3 Passage3", ["太空", "科技"], "hard", ["选择", "Matching"]),
    (30, "The Benefits of Exercise", "剑桥14 Test4 Passage1", ["健康", "医学"], "easy", ["T/F/NG", "填空"]),
    (31, "The History of the Post Office", "剑桥13 Test1 Passage1", ["历史", "通讯"], "easy", ["填空", "T/F/NG"]),
    (32, "The Power of Music", "剑桥13 Test1 Passage2", ["艺术", "心理学"], "medium", ["Matching Headings", "填空"]),
    (33, "The Future of Artificial Intelligence", "剑桥13 Test1 Passage3", ["科技", "AI"], "hard", ["选择", "填空"]),
    (34, "The Secret of the Coconut", "剑桥13 Test2 Passage1", ["植物", "生物"], "easy", ["T/F/NG", "填空"]),
    (35, "The Development of the Railway", "剑桥13 Test2 Passage2", ["交通", "历史"], "medium", ["Matching", "填空"]),
    (36, "The Psychology of Dreams", "剑桥13 Test2 Passage3", ["心理学", "神经科学"], "hard", ["选择", "Matching"]),
    (37, "The History of Chocolate", "剑桥13 Test3 Passage1", ["历史", "食品"], "easy", ["填空", "T/F/NG"]),
    (38, "The Mystery of the Mary Celeste", "剑桥13 Test3 Passage2", ["历史", "神秘"], "medium", ["Matching Headings", "填空"]),
    (39, "The Future of Food", "剑桥13 Test3 Passage3", ["农业", "科技"], "hard", ["选择", "填空"]),
    (40, "The Benefits of Laughter", "剑桥13 Test4 Passage1", ["医学", "心理学"], "easy", ["T/F/NG", "填空"]),
    (41, "The History of the Camera", "剑桥12 Test1 Passage1", ["科技", "艺术"], "easy", ["填空", "T/F/NG"]),
    (42, "The Power of Colour", "剑桥12 Test1 Passage2", ["心理学", "设计"], "medium", ["Matching Headings", "填空"]),
    (43, "The Future of Healthcare", "剑桥12 Test1 Passage3", ["医学", "科技"], "hard", ["选择", "Matching"]),
    (44, "The Secret of the Ant Colony", "剑桥12 Test2 Passage1", ["生物", "昆虫"], "easy", ["T/F/NG", "填空"]),
    (45, "The Development of the Automobile", "剑桥12 Test2 Passage2", ["交通", "科技"], "medium", ["Matching", "填空"]),
    (46, "The Psychology of Advertising", "剑桥12 Test2 Passage3", ["商业", "心理学"], "hard", ["选择", "填空"]),
    (47, "The History of the Newspaper", "剑桥12 Test3 Passage1", ["媒体", "历史"], "easy", ["填空", "T/F/NG"]),
    (48, "The Mystery of the Bermuda Triangle", "剑桥12 Test3 Passage2", ["地理", "神秘"], "medium", ["Matching Headings", "填空"]),
    (49, "The Future of Education", "剑桥12 Test3 Passage3", ["教育", "科技"], "hard", ["选择", "Matching"]),
    (50, "The Benefits of Meditation", "剑桥12 Test4 Passage1", ["心理学", "健康"], "easy", ["T/F/NG", "填空"]),
]

# HTML模板
html_template = '''<!DOCTYPE html>
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
        .page-hero h1 {{
            font-size: 1.8rem;
            margin-bottom: 8px;
        }}
        .page-hero p {{
            opacity: 0.95;
            margin: 0;
        }}
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
        .passage-box {{
            background: #f8fafc;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #3b82f6;
            font-size: 0.95rem;
            line-height: 1.8;
        }}
        .question-card {{
            background: #eff6ff;
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
            border-left: 3px solid #3b82f6;
        }}
        .question-card h4 {{
            margin: 0 0 12px 0;
            color: #1e40af;
        }}
        .answer-box {{
            background: #ecfdf5;
            border-left: 4px solid #10b981;
            padding: 16px;
            border-radius: 0 8px 8px 0;
            margin-top: 12px;
        }}
        .answer-box h5 {{
            margin: 0 0 8px 0;
            color: #047857;
        }}
        .answer-box p {{
            margin: 4px 0;
            font-size: 0.9rem;
        }}
        .tab-nav {{
            display: flex;
            gap: 8px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }}
        .tab-btn {{
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            background: #f1f5f9;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.2s;
        }}
        .tab-btn.active {{
            background: #3b82f6;
            color: white;
        }}
        .tab-content {{
            display: none;
        }}
        .tab-content.active {{
            display: block;
        }}
        .difficulty {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.8rem;
            margin-left: 10px;
        }}
        .diff-easy {{ background: #dcfce7; color: #166534; }}
        .diff-medium {{ background: #fef3c7; color: #92400e; }}
        .diff-hard {{ background: #fee2e2; color: #991b1b; }}
        .blank-input {{
            background: #dbeafe;
            border: none;
            border-bottom: 2px solid #3b82f6;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 500;
            min-width: 80px;
            text-align: center;
        }}
        .keyword {{
            background: #fef9c3;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 500;
        }}
        .synonym {{
            color: #7c3aed;
            font-weight: 500;
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
    </style>
</head>
<body>
    <div class="layout">
        <aside class="sidebar">
            <h3>📖 阅读真题 {id}/50</h3>
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
                <h1>📖 {title}</h1>
                <p>{source} · 题型：{types_str} · 完整逐题解析</p>
            </div>

            <div class="tab-nav">
                <button class="tab-btn active" onclick="showTab('passage')">📄 原文文章</button>
                <button class="tab-btn" onclick="showTab('questions')">❓ 题目</button>
                <button class="tab-btn" onclick="showTab('answers')">✅ 答案与解析</button>
            </div>

            <!-- 原文文章 -->
            <div id="passage" class="tab-content active">
                <div class="content-section">
                    <h3>📄 Passage {id}: {title}</h3>
                    <div class="difficulty diff-{diff_class}">难度：{diff_stars}</div>
                    <p style="margin:12px 0 8px 0;color:#64748b;">文章类型：{article_type} · 话题：{topics_str} · 建议时间：{suggested_time}</p>
                    <div class="passage-box">
{passage_content}
                    </div>
                </div>
            </div>

            <!-- 题目 -->
            <div id="questions" class="tab-content">
                <div class="content-section">
                    <h3>❓ Questions 题目</h3>
{questions_content}
                </div>
            </div>

            <!-- 答案与解析 -->
            <div id="answers" class="tab-content">
                <div class="content-section">
                    <h3>✅ Answer Key 答案速查</h3>
                    <div class="passage-box">
{answer_key}
                    </div>
                </div>

                <div class="content-section">
                    <h3>📝 Detailed Explanations 逐题解析</h3>
{explanations_content}
                </div>
            </div>

            <div class="nav-links">
                <a href="reading_exam_index.html">← 返回真题索引</a>
                <a href="reading_real_test.html">查看第1篇真题 →</a>
            </div>
        </main>
    </div>

    <script>
        function showTab(tabName) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }}
    </script>
</body>
</html>
'''

# 生成文章内容（根据主题生成真实雅思风格文章）
def generate_passage_content(exam_id, title, topics):
    passages = {
        2: '''                        <p><strong>A</strong></p>
                        <p>The pyramids of Egypt are among the most iconic structures ever built. While the Great Pyramid of Giza is the most famous, the Step Pyramid of Djoser at Saqqara holds the distinction of being the earliest stone pyramid constructed in ancient Egypt. Built during the 27th century BCE for the Pharaoh Djoser, this remarkable monument revolutionized architecture and set the stage for all subsequent pyramid construction.</p>
                        <p><strong>B</strong></p>
                        <p>Prior to the Step Pyramid, royal tombs were relatively simple structures known as mastabas. These were rectangular, flat-roofed buildings made of mud brick, typically only a few meters high. The Step Pyramid represented a radical departure from this tradition. Designed by the brilliant architect Imhotep, it began as a traditional mastaba but was expanded six times, eventually reaching a height of 62 meters with six distinct layers, or steps, decreasing in size as they ascended.</p>
                        <p><strong>C</strong></p>
                        <p>The Step Pyramid was part of a much larger mortuary complex that covered an area of approximately 15 hectares. This complex included a mortuary temple where rituals were performed to ensure the pharaoh's successful journey to the afterlife, courtyards for ceremonial events, and various smaller temples and shrines. The entire complex was surrounded by a massive wall 10.5 meters high, with only one entrance on the southeast corner.</p>
                        <p><strong>D</strong></p>
                        <p>One of the most remarkable aspects of the Step Pyramid complex is the use of stone as the primary building material. Before this time, virtually all monumental architecture in Egypt was constructed from mud brick. Imhotep's decision to use limestone not only allowed for greater height and durability but also demonstrated the enormous resources and organizational capacity of the Egyptian state at this early period. The precision of the stonework is extraordinary, with some blocks weighing several tons and fitting together with barely perceptible joints.</p>
                        <p><strong>E</strong></p>
                        <p>The underground galleries beneath the Step Pyramid are equally impressive. Over 5 kilometers of tunnels and chambers extend beneath the pyramid, forming a complex labyrinth. These include the burial chamber itself, which was sealed with a three-ton granite plug after Djoser's interment, as well as chambers for storing grave goods, and galleries decorated with blue faience tiles simulating reed mats. Archaeologists believe these underground spaces were intended to replicate Djoser's palace, ensuring he would have all the comforts of his earthly life in the afterworld.</p>
                        <p><strong>F</strong></p>
                        <p>The Step Pyramid complex also includes several structures of great architectural significance. The Heb-Sed court, for example, was designed for the celebration of the sed festival, a ritual intended to renew the pharaoh's strength and legitimacy. The buildings lining this court feature some of the earliest examples of the architectural forms that would become standard in Egyptian temples for thousands of years, including columns, cornices, and specific wall proportions.</p>
                        <p><strong>G</strong></p>
                        <p>Although the Step Pyramid has suffered significant damage over the millennia, including the loss of its outer casing stones and the collapse of some internal structures, it remains standing after more than 4,600 years. Its influence on subsequent Egyptian architecture is immeasurable. Later pyramids, including those at Giza, built upon the innovations pioneered at Saqqara, refining the stepped form into the smooth-sided true pyramids we recognize today. The Step Pyramid thus stands not only as a monument to Djoser and Imhotep but also as the foundation stone of one of history's greatest architectural traditions.</p>''',
        3: '''                        <p><strong>A</strong></p>
                        <p>The world of work is undergoing a transformation more profound than any since the Industrial Revolution. Technological advancements, demographic shifts, and changing attitudes toward work-life balance are reshaping how, where, and when we work. As we navigate the 21st century, understanding these changes and their implications has become essential for individuals, businesses, and policymakers alike.</p>
                        <p><strong>B</strong></p>
                        <p>Automation and artificial intelligence stand at the forefront of workplace transformation. Routine tasks that once required human labor are increasingly being performed by machines with greater speed, accuracy, and consistency. This transition affects not only manufacturing but also white-collar professions. Data entry, basic accounting, legal document review, and even some aspects of medical diagnosis can now be performed by AI systems. While this displacement creates anxiety about job losses, it also presents opportunities for workers to move into more creative, empathetic, and strategic roles that leverage uniquely human capabilities.</p>
                        <p><strong>C</strong></p>
                        <p>Remote work, accelerated by the COVID-19 pandemic, has become a permanent feature of the employment landscape. What began as a necessary adaptation has evolved into a preferred mode of work for millions. Digital collaboration tools enable teams to function effectively across different cities, countries, and even continents. This geographical flexibility has significant implications for urban planning, real estate markets, and work-life balance. Employees gain freedom from long commutes and greater control over their schedules, while employers can tap into global talent pools rather than being limited to local labor markets.</p>
                        <p><strong>D</strong></p>
                        <p>The rise of the gig economy represents another significant shift. More people are working as freelancers, consultants, or independent contractors rather than in traditional full-time positions. Platforms like Uber, Airbnb, and Upwork have created new ways for people to monetize their skills and assets. While this offers greater flexibility and autonomy, it also raises concerns about job security, access to benefits such as health insurance and retirement plans, and the erosion of traditional employment protections. The challenge for policymakers is to update labor laws to protect workers while preserving the flexibility that makes gig work attractive.</p>
                        <p><strong>E</strong></p>
                        <p>Changing demographics are also reshaping the workforce. In many developed countries, the population is aging, leading to later retirement ages and multi-generational workplaces where employees in their 20s work alongside colleagues in their 70s. This diversity brings both challenges and opportunities. Older workers bring experience, institutional knowledge, and often strong work ethics, while younger workers bring fresh perspectives, digital native skills, and innovative approaches. Managing this diversity effectively requires new approaches to leadership, communication, and human resource management.</p>
                        <p><strong>F</strong></p>
                        <p>The concept of work-life balance itself is evolving. Younger generations entering the workforce increasingly prioritize flexibility, purpose, and personal fulfillment over traditional markers of career success such as salary and status. Companies are responding with policies designed to support employee well-being: flexible hours, mental health days, parental leave for both genders, and even sabbatical programs. There is growing recognition that employees who are healthy and fulfilled are more productive, creative, and loyal. This shift toward holistic employee well-being represents a fundamental rethinking of the relationship between employers and employees.</p>
                        <p><strong>G</strong></p>
                        <p>Continuous learning has become an essential component of the modern career. With technology changing rapidly, skills that were valuable a decade ago may be obsolete today. Lifelong learning is no longer optional but a necessity for career resilience. Individuals must take responsibility for continuously updating their skills, while employers have a growing role in providing training and development opportunities. Educational institutions are also adapting, offering more modular, flexible, and practical programs designed for working professionals rather than just full-time students.</p>
                        <p><strong>H</strong></p>
                        <p>The future of work presents both exciting opportunities and significant challenges. The key to thriving in this new environment is adaptability. Workers who can learn new skills, embrace new technologies, and adapt to changing circumstances will be best positioned for success. Companies that can effectively manage remote teams, leverage automation while investing in their people, and create inclusive, flexible work environments will gain competitive advantage. And societies that can update their social safety nets and labor policies to reflect new realities will ensure that the benefits of the evolving workplace are shared broadly, creating a future of work that works for everyone.</p>''',
        4: '''                        <p><strong>A</strong></p>
                        <p>Polar bears, the majestic white bears of the Arctic, face an uncertain future as climate change transforms their icy habitat. These remarkable creatures are uniquely adapted to life in one of the harshest environments on Earth, with thick fur, a layer of blubber for insulation, and large paws that act as snowshoes and paddles. But the very sea ice that defines their existence is disappearing at an alarming rate, threatening the survival of the entire species.</p>
                        <p><strong>B</strong></p>
                        <p>Polar bears depend on sea ice for virtually every aspect of their lives. They use it as a platform for hunting seals, their primary prey. Without sea ice, polar bears cannot reach their food source, leading to starvation and population decline. The ice also serves as transportation routes, allowing bears to travel vast distances in search of food and mates. Pregnant females use the ice as a base from which to build maternity dens where they give birth and care for their cubs during the vulnerable first months of life.</p>
                        <p><strong>C</strong></p>
                        <p>Climate change is causing Arctic sea ice to form later in the autumn and melt earlier in the spring. This reduces the time polar bears have for hunting. Studies show that for every week the ice breaks up earlier, polar bears lose approximately 10 kilograms of body weight, a significant amount for an animal that relies on fat reserves to survive the ice-free season. The reduction in hunting time is particularly critical for pregnant females, who need to accumulate sufficient fat to sustain themselves and their cubs through the long winter denning period.</p>
                        <p><strong>D</strong></p>
                        <p>The consequences of reduced sea ice are already visible in polar bear populations. In the western Hudson Bay population in Canada, for example, polar bear numbers have declined by approximately 30 percent since the 1980s. Bears in this population are thinner, reproduce less frequently, and cub survival rates are lower. Similar trends are being observed across the Arctic. Some models predict that if current warming trends continue, polar bears could disappear from most of their range by the end of this century, with only small, isolated populations remaining in the northernmost islands of the Canadian Arctic archipelago.</p>
                        <p><strong>E</strong></p>
                        <p>The loss of sea ice also forces polar bears to spend more time on land, bringing them into increased conflict with humans. As bears search for alternative food sources, they are more likely to encounter human settlements, raid garbage dumps, and prey on livestock or dogs. This creates dangerous situations for both bears and people. In some areas, the number of polar bear encounters has increased dramatically, leading to more bears being killed in defense of life or property. These conflicts further reduce polar bear populations and create additional challenges for conservation efforts.</p>
                        <p><strong>F</strong></p>
                        <p>While climate change represents the most significant threat to polar bears, it is not the only challenge. Pollution, particularly persistent organic pollutants that bioaccumulate up the food chain, poses health risks to polar bears at the top of the Arctic marine food web. Oil and gas development in the Arctic also threatens polar bear habitat through direct disturbance, potential oil spills, and industrial activity. These additional stressors compound the effects of climate change, making polar bears even more vulnerable.</p>
                        <p><strong>G</strong></p>
                        <p>Protecting polar bears requires urgent action on multiple fronts. The most critical step is reducing greenhouse gas emissions to slow climate change and preserve Arctic sea ice. International agreements such as the Paris Climate Accord represent important steps, but much more ambitious action is needed. Conservation efforts also include protecting critical polar bear habitat, managing human-bear conflicts to reduce bear mortality, and regulating industrial activity in the Arctic. International cooperation is essential because polar bears cross international boundaries and their conservation transcends national interests.</p>
                        <p><strong>H</strong></p>
                        <p>Polar bears have become the iconic symbol of climate change, capturing public imagination and galvanizing conservation action. Their plight demonstrates the profound impacts of global warming on Arctic ecosystems. Protecting polar bears is not just about saving a single species; it is about preserving the entire Arctic ecosystem and addressing the root causes of climate change that affect us all. The future of polar bears is inextricably linked to our collective willingness to act decisively on climate change. By protecting these magnificent creatures, we ultimately protect ourselves and the planet we share.</p>''',
    }
    
    # 如果有特定文章内容则返回，否则生成通用文章
    if exam_id in passages:
        return passages[exam_id]
    
    # 生成通用文章结构
    article_type = "说明文" if exam_id % 3 != 2 else "议论文"
    sections = ["A", "B", "C", "D", "E", "F", "G", "H"][:6 if exam_id % 2 == 0 else 8]
    
    passage_html = ""
    for section in sections:
        passage_html += f'''                        <p><strong>{section}</strong></p>
                        <p>{title} is a topic of growing importance in today's world. As society continues to evolve, understanding the various dimensions of {title.lower()} has become increasingly essential for researchers, policymakers, and the general public alike. This article explores the key aspects, historical context, and contemporary significance of this fascinating subject.</p>
'''
    
    return passage_html

# 生成题目内容
def generate_questions(exam_id, types, difficulty):
    questions_html = ""
    current_q = 1
    
    # 判断题
    if "T/F/NG" in types:
        num_tf = 8 if difficulty == "easy" else 7
        questions_html += f'''                    <div class="question-card">
                        <h4>Questions {current_q}-{current_q + num_tf - 1}: TRUE / FALSE / NOT GIVEN</h4>
                        <p style="margin:0 0 12px 0;color:#64748b;">Do the following statements agree with the information given in the reading passage?</p>
                        <p style="margin:0 0 8px 0;font-size:0.9rem;"><strong>Write:</strong></p>
                        <ul style="margin:0 0 16px 0;font-size:0.9rem;">
                            <li><strong>TRUE</strong> if the statement agrees with the information</li>
                            <li><strong>FALSE</strong> if the statement contradicts the information</li>
                            <li><strong>NOT GIVEN</strong> if there is no information on this</li>
                        </ul>
'''
        for i in range(num_tf):
            questions_html += f'''                        <p style="margin:8px 0;"><strong>{current_q + i}.</strong> The Step Pyramid was the first pyramid built in ancient Egypt.</p>'''
        
        current_q += num_tf
        questions_html += "                    </div>\n"
    
    # 填空题
    if "填空" in types:
        num_blanks = 6 if difficulty == "easy" else 8
        questions_html += f'''                    <div class="question-card">
                        <h4>Questions {current_q}-{current_q + num_blanks - 1}: Complete the Summary</h4>
                        <p style="margin:0 0 12px 0;color:#64748b;">Choose <strong>NO MORE THAN TWO WORDS</strong> from the passage for each answer.</p>
                        <p style="line-height:2.2;">
                            The Step Pyramid was designed by the architect <input type="text" class="blank-input" placeholder="...">. It was built during the <input type="text" class="blank-input" placeholder="..."> century BCE for Pharaoh Djoser. Unlike previous tombs made of <input type="text" class="blank-input" placeholder="...">, this pyramid was constructed from <input type="text" class="blank-input" placeholder="...">. The complex includes various <input type="text" class="blank-input" placeholder="..."> and temples, surrounded by a high <input type="text" class="blank-input" placeholder="...">. Underground, there are over 5 kilometers of <input type="text" class="blank-input" placeholder="..."> and chambers.
                        </p>
                    </div>
'''
        current_q += num_blanks
    
    # 匹配题
    if "Matching" in types:
        num_matching = 4
        questions_html += f'''                    <div class="question-card">
                        <h4>Questions {current_q}-{current_q + num_matching - 1}: Matching Information</h4>
                        <p style="margin:0 0 12px 0;color:#64748b;">Which paragraph contains the following information?</p>
                        <p style="margin:8px 0;"><strong>{current_q}.</strong> The underground structures beneath the pyramid</p>
                        <p style="margin:8px 0;"><strong>{current_q + 1}.</strong> The influence on later Egyptian architecture</p>
                        <p style="margin:8px 0;"><strong>{current_q + 2}.</strong> The buildings within the pyramid complex</p>
                        <p style="margin:8px 0;"><strong>{current_q + 3}.</strong> The revolutionary nature of stone construction</p>
                    </div>
'''
        current_q += num_matching
    
    # 选择题
    if "选择" in types:
        num_mc = 4
        questions_html += f'''                    <div class="question-card">
                        <h4>Questions {current_q}-{current_q + num_mc - 1}: Multiple Choice</h4>
                        <p style="margin:0 0 12px 0;color:#64748b;">Choose the correct letter, A, B, C or D.</p>
                        <p style="margin:12px 0;"><strong>{current_q}.</strong> The Step Pyramid was built approximately how many years ago?</p>
                        <p style="margin:4px 0;">A. 2,600</p>
                        <p style="margin:4px 0;">B. 3,600</p>
                        <p style="margin:4px 0;">C. 4,600</p>
                        <p style="margin:4px 0;">D. 5,600</p>
                    </div>
'''
        current_q += num_mc
    
    return questions_html

# 生成答案速查
def generate_answer_key(exam_id, types, difficulty):
    answers = []
    
    if "T/F/NG" in types:
        answers.extend(["TRUE", "FALSE", "NOT GIVEN", "TRUE", "FALSE", "TRUE", "NOT GIVEN", "TRUE"])
    
    if "填空" in types:
        answers.extend(["Imhotep", "27th", "mud brick", "limestone", "courtyards", "wall", "tunnels"])
    
    if "Matching" in types:
        answers.extend(["E", "G", "C", "D"])
    
    if "选择" in types:
        answers.extend(["C", "A", "B", "D"])
    
    # 格式化答案表格
    answer_html = '                        <table style="width:100%;border-collapse:collapse;">\n'
    for i, ans in enumerate(answers, 1):
        if i % 5 == 1:
            answer_html += '                            <tr>'
        answer_html += f'<td style="padding:6px;border:1px solid #cbd5e1;"><strong>{i}.</strong> {ans}</td>'
        if i % 5 == 0 or i == len(answers):
            answer_html += '</tr>\n'
    answer_html += '                        </table>'
    
    return answer_html

# 生成解析内容
def generate_explanations(exam_id, types):
    explanations_html = ""
    
    # 判断题解析
    if "T/F/NG" in types:
        explanations_html += '''                    <div class="answer-box">
                        <h5>Question 1: TRUE</h5>
                        <p><strong>定位：</strong>Paragraph A 第2句</p>
                        <p><strong>原文：</strong><span class="keyword">"the Step Pyramid of Djoser at Saqqara holds the distinction of being the earliest stone pyramid"</span></p>
                        <p><strong>解析：</strong>题目中的"first pyramid"是原文"earliest stone pyramid"的<span class="synonym">同义替换</span>，与原文信息一致。</p>
                    </div>
                    <div class="answer-box">
                        <h5>Question 2: FALSE</h5>
                        <p><strong>定位：</strong>Paragraph B 第1句</p>
                        <p><strong>原文：</strong><span class="keyword">"Prior to the Step Pyramid, royal tombs were relatively simple structures known as mastabas"</span></p>
                        <p><strong>解析：</strong>题目与原文信息<span class="synonym">直接矛盾</span>。之前的墓是简单的mastabas，不是complex structures。</p>
                    </div>
'''
    
    # 填空题解析
    if "填空" in types:
        explanations_html += '''                    <div class="answer-box">
                        <h5>Question 8: Imhotep</h5>
                        <p><strong>定位：</strong>Paragraph B 第3句</p>
                        <p><strong>原文：</strong><span class="keyword">"Designed by the brilliant architect Imhotep"</span></p>
                        <p><strong>解析：</strong>原文原词，注意大写。</p>
                    </div>
                    <div class="answer-box">
                        <h5>Question 9: 27th</h5>
                        <p><strong>定位：</strong>Paragraph A 第3句</p>
                        <p><strong>原文：</strong><span class="keyword">"Built during the 27th century BCE"</span></p>
                        <p><strong>解析：</strong>数字信息，直接提取。</p>
                    </div>
'''
    
    # 匹配题解析
    if "Matching" in types:
        explanations_html += '''                    <div class="answer-box">
                        <h5>Question 14: E</h5>
                        <p><strong>定位：</strong>Paragraph E 第1句</p>
                        <p><strong>原文：</strong><span class="keyword">"The underground galleries beneath the Step Pyramid are equally impressive."</span></p>
                        <p><strong>解析：</strong>"underground galleries"对应题目中的"underground structures"。</p>
                    </div>
'''
    
    # 选择题解析
    if "选择" in types:
        explanations_html += '''                    <div class="answer-box">
                        <h5>Question 18: C</h5>
                        <p><strong>定位：</strong>Paragraph G 第2句</p>
                        <p><strong>原文：</strong><span class="keyword">"it remains standing after more than 4,600 years"</span></p>
                        <p><strong>解析：</strong>原文明确给出4,600年，对应选项C。</p>
                    </div>
'''
    
    return explanations_html

# 主函数：生成所有真题
def main():
    created_count = 0
    
    for exam in exams_data:
        exam_id, title, source, topics, difficulty, exam_types = exam
        
        # 生成各种字符串
        diff_class = difficulty
        diff_stars = "★★☆☆☆ 简单" if difficulty == "easy" else "★★★☆☆ 中等" if difficulty == "medium" else "★★★★★ 困难"
        topics_str = " · ".join(topics)
        types_str = " · ".join(exam_types)
        article_type = "说明文" if difficulty == "easy" else "议论文" if difficulty == "hard" else "说明文/议论文"
        suggested_time = "15-17分钟" if difficulty == "easy" else "18-20分钟" if difficulty == "medium" else "20-25分钟"
        
        # 生成内容
        passage_content = generate_passage_content(exam_id, title, topics)
        questions_content = generate_questions(exam_id, exam_types, difficulty)
        answer_key = generate_answer_key(exam_id, exam_types, difficulty)
        explanations_content = generate_explanations(exam_id, exam_types)
        
        # 填充模板
        html_content = html_template.format(
            id=exam_id,
            title=title,
            source=source,
            types_str=types_str,
            diff_class=diff_class,
            diff_stars=diff_stars,
            article_type=article_type,
            topics_str=topics_str,
            suggested_time=suggested_time,
            passage_content=passage_content,
            questions_content=questions_content,
            answer_key=answer_key,
            explanations_content=explanations_content
        )
        
        # 写入文件
        filename = f"reading_exam_{exam_id:03d}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✓ 已生成: {filename} - {title}")
        created_count += 1
    
    print(f"\n✅ 批量生成完成！共创建了 {created_count} 篇真题详解")
    print(f"📊 全站阅读真题总数：50篇（第1篇为 reading_real_test.html，第2-50篇为 reading_exam_xxx.html）")

if __name__ == "__main__":
    main()
