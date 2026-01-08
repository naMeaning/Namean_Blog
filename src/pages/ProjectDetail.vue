<template>
  <section v-if="project" class="section detail">
    <p class="detail-meta">{{ project.date }} · {{ project.role }}</p>
    <h2>{{ project.title }}</h2>
    <p class="detail-summary">{{ project.summary }}</p>
    <div class="detail-tags">
      <span v-for="tag in project.tags" :key="tag" class="tag">{{ tag }}</span>
    </div>
    <article class="detail-body">
      {{ project.content }}
    </article>
  </section>
  <section v-else class="section">
    <h2>未找到该项目</h2>
    <RouterLink to="/projects">返回项目列表 →</RouterLink>
  </section>
</template>

<script setup>
import { computed } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { projects } from "../lib/contentStore";

const route = useRoute();

const project = computed(() => projects.find((item) => item.slug === route.params.slug));
</script>

<style scoped>
.detail {
  max-width: 860px;
}

.detail-meta {
  color: #8fa2bf;
  font-size: 12px;
  margin-bottom: 12px;
}

.detail-summary {
  margin: 16px 0;
  color: #b2b9c7;
}

.detail-body {
  margin-top: 24px;
  line-height: 1.8;
  color: #d7dbe4;
}

.detail-tags {
  margin-top: 12px;
}
</style>
