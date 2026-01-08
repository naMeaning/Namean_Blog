<template>
  <section v-if="post" class="section detail">
    <p class="detail-meta">{{ post.date }} · {{ post.readingTime }}</p>
    <h2>{{ post.title }}</h2>
    <p class="detail-summary">{{ post.summary }}</p>
    <div class="detail-tags">
      <span v-for="tag in post.tags" :key="tag" class="tag">{{ tag }}</span>
    </div>
    <article class="detail-body">
      {{ post.content }}
    </article>
  </section>
  <section v-else class="section">
    <h2>未找到该文章</h2>
    <RouterLink to="/posts">返回文章列表 →</RouterLink>
  </section>
</template>

<script setup>
import { computed } from "vue";
import { RouterLink, useRoute } from "vue-router";
import { posts } from "../lib/contentStore";

const route = useRoute();

const post = computed(() => posts.find((item) => item.slug === route.params.slug));
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
