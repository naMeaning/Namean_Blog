<template>
  <section class="section">
    <h2 class="section-title">标签：{{ tagName }}</h2>
    <div class="card-grid">
      <article v-for="item in results" :key="item.slug" class="card">
        <p class="card-meta">{{ item.date }} · {{ item.type }}</p>
        <h3>{{ item.title }}</h3>
        <p class="card-summary">{{ item.summary }}</p>
        <RouterLink class="card-link" :to="item.link">查看详情 →</RouterLink>
      </article>
    </div>
  </section>
</template>

<script setup>
import { computed } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { posts, projects } from "../lib/contentStore";

const route = useRoute();

const tagName = computed(() => route.params.tag);

const results = computed(() => {
  const name = tagName.value;
  const postResults = posts
    .filter((post) => post.tags.includes(name))
    .map((post) => ({ ...post, type: "文章", link: `/posts/${post.slug}` }));
  const projectResults = projects
    .filter((project) => project.tags.includes(name))
    .map((project) => ({ ...project, type: "项目", link: `/projects/${project.slug}` }));
  return [...postResults, ...projectResults];
});
</script>

<style scoped>
.card-meta {
  font-size: 12px;
  color: #90a0b5;
  margin-bottom: 10px;
}

.card-summary {
  margin: 12px 0 16px;
  color: #b2b9c7;
}

.card-link {
  color: #5ed0ff;
  font-size: 14px;
}
</style>
