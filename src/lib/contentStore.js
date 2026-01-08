export const posts = [
  {
    title: "科技质感网站的设计逻辑",
    slug: "tech-aesthetic-guideline",
    date: "2026-01-05",
    summary: "从视觉层级、动效节奏到排版密度，拆解科技感网站的核心组成。",
    tags: ["设计", "体验", "品牌"],
    readingTime: "6 min",
    content:
      "这是一篇示例文章内容，用于展示正文排版与信息块结构。你可以在这里填充 Markdown 转换后的 HTML。"
  },
  {
    title: "行业观察：AI 产品落地路径",
    slug: "ai-product-insights",
    date: "2026-01-02",
    summary: "从交付链路、数据反馈到业务闭环，梳理 AI 产品落地路径。",
    tags: ["AI", "产品"],
    readingTime: "8 min",
    content:
      "这里展示第二篇文章详情内容，用于演示详情页的布局与标签信息。"
  }
];

export const projects = [
  {
    title: "全球化品牌官网升级",
    slug: "global-brand-site",
    date: "2025-12-18",
    summary: "为科技企业打造多语言官网，提升海外客户转化率。",
    tags: ["官网", "增长"],
    role: "产品策略 / 体验设计",
    content:
      "项目详细说明文本，用于展示项目背景、目标、解决方案与成果。"
  },
  {
    title: "企业级平台设计系统",
    slug: "enterprise-design-system",
    date: "2025-11-08",
    summary: "建立统一的组件体系与视觉规范，加速产品交付。",
    tags: ["设计系统", "协作"],
    role: "设计负责人",
    content:
      "项目详情内容，展示设计系统建设步骤与落地经验。"
  }
];

export const tags = Array.from(
  new Set([...posts.flatMap((post) => post.tags), ...projects.flatMap((project) => project.tags)])
);
