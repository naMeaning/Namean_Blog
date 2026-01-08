<template>
  <section class="section">
    <div class="hero">
      <div>
        <p class="hero-kicker">科技质感 · 品牌叙事 · 产品增长</p>
        <h2>构建让客户信任的数字体验</h2>
        <p class="hero-subtitle">
          我们聚焦于技术行业的品牌与产品内容，通过清晰的信息架构与高效的交互体验，帮助企业传递核心价值。
        </p>
        <div class="hero-actions">
          <RouterLink class="primary" to="/projects">查看作品集</RouterLink>
          <RouterLink class="ghost" to="/posts">阅读最新文章</RouterLink>
        </div>
      </div>
      <div class="hero-panel">
        <h3>服务方向</h3>
        <ul>
          <li>数字品牌与官网升级</li>
          <li>产品体验与信息架构</li>
          <li>内容策略与行业洞察</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="section">
    <h3 class="section-title">精选文章</h3>
    <div class="card-grid">
      <article v-for="post in posts" :key="post.slug" class="card">
        <p class="card-meta">{{ post.date }} · {{ post.readingTime }}</p>
        <h4>{{ post.title }}</h4>
        <p class="card-summary">{{ post.summary }}</p>
        <div class="card-tags">
          <span v-for="tag in post.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
        <RouterLink class="card-link" :to="`/posts/${post.slug}`">阅读全文 →</RouterLink>
      </article>
    </div>
  </section>

  <section class="section">
    <h3 class="section-title">最新项目</h3>
    <div class="card-grid">
      <article v-for="project in projects" :key="project.slug" class="card">
        <p class="card-meta">{{ project.date }} · {{ project.role }}</p>
        <h4>{{ project.title }}</h4>
        <p class="card-summary">{{ project.summary }}</p>
        <div class="card-tags">
          <span v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
        <RouterLink class="card-link" :to="`/projects/${project.slug}`">查看项目 →</RouterLink>
      </article>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from "vue-router";
import { posts, projects } from "../lib/contentStore";
</script>

<style scoped>
.hero {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 32px;
  align-items: center;
}

.hero-kicker {
  color: #5ed0ff;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-size: 12px;
}

.hero h2 {
  font-size: 36px;
  margin: 12px 0;
}

.hero-subtitle {
  color: #b2b9c7;
  line-height: 1.6;
}

.hero-actions {
  margin-top: 24px;
  display: flex;
  gap: 16px;
}

.hero-actions a {
  padding: 10px 18px;
  border-radius: 10px;
  font-size: 14px;
}

.primary {
  background: linear-gradient(135deg, #4b7bec, #17c0eb);
  color: #0b0f1a;
}

.ghost {
  border: 1px solid rgba(94, 208, 255, 0.4);
  color: #5ed0ff;
}

.hero-panel {
  background: rgba(19, 27, 44, 0.9);
  padding: 24px;
  border-radius: 18px;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.hero-panel h3 {
  margin-bottom: 12px;
}

.hero-panel ul {
  list-style: none;
  display: grid;
  gap: 10px;
  color: #b5bbc9;
}

.card-meta {
  font-size: 12px;
  color: #90a0b5;
  margin-bottom: 10px;
}

.card-summary {
  margin: 12px 0 16px;
  color: #b2b9c7;
}

.card-tags {
  margin-bottom: 16px;
}

.card-link {
  color: #5ed0ff;
  font-size: 14px;
}
</style>
