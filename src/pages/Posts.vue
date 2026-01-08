<template>
  <section class="section">
    <h2 class="section-title">文章列表</h2>
    <SearchBar v-model="keyword" />
    <div class="card-grid">
      <article v-for="post in filteredPosts" :key="post.slug" class="card">
        <p class="card-meta">{{ post.date }} · {{ post.readingTime }}</p>
        <h3>{{ post.title }}</h3>
        <p class="card-summary">{{ post.summary }}</p>
        <div class="card-tags">
          <span v-for="tag in post.tags" :key="tag" class="tag">{{ tag }}</span>
        </div>
        <RouterLink class="card-link" :to="`/posts/${post.slug}`">阅读全文 →</RouterLink>
      </article>
    </div>
  </section>
</template>

<script setup>
import { computed, ref } from "vue";
import { RouterLink } from "vue-router";
import SearchBar from "../components/SearchBar.vue";
import { posts } from "../lib/contentStore";

const keyword = ref("");

const filteredPosts = computed(() => {
  const query = keyword.value.trim().toLowerCase();
  if (!query) {
    return posts;
  }
  return posts.filter((post) =>
    [post.title, post.summary, post.tags.join(" ")].join(" ").toLowerCase().includes(query)
  );
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

.card-tags {
  margin-bottom: 16px;
}

.card-link {
  color: #5ed0ff;
  font-size: 14px;
}
</style>
