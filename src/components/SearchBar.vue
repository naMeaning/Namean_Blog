<template>
  <section class="search-bar">
    <label class="search-bar__label" for="search-input">搜索文章或项目</label>
    <input
      id="search-input"
      v-model="query"
      class="search-bar__input"
      type="search"
      placeholder="输入标题、标签或摘要"
      autocomplete="off"
    />
    <p v-if="status === 'loading'" class="search-bar__hint">加载索引中…</p>
    <p v-else-if="query && results.length === 0" class="search-bar__hint">没有找到匹配内容</p>
    <ul v-if="results.length" class="search-bar__results">
      <li v-for="result in results" :key="result.item.id" class="search-bar__result">
        <a :href="result.item.url" class="search-bar__link">
          <span class="search-bar__title">{{ result.item.title }}</span>
          <span class="search-bar__meta">{{ result.item.type }}</span>
        </a>
        <p class="search-bar__summary">{{ result.item.summary }}</p>
        <div class="search-bar__tags">
          <span v-for="tag in result.item.tags" :key="tag" class="search-bar__tag">{{ tag }}</span>
        </div>
      </li>
    </ul>
  </section>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { getSearchIndex, type SearchIndexEntry } from "../lib/api";
import { searchIndex, type SearchResult } from "../lib/search";

const query = ref("");
const status = ref<"idle" | "loading">("loading");
const index = ref<SearchIndexEntry[]>([]);

const results = computed<SearchResult[]>(() =>
  searchIndex(query.value, index.value, 6),
);

onMounted(async () => {
  index.value = await getSearchIndex();
  status.value = "idle";
});
</script>

<style scoped>
.search-bar {
  display: grid;
  gap: 0.75rem;
  max-width: 720px;
}

.search-bar__label {
  font-weight: 600;
}

.search-bar__input {
  border: 1px solid #d5d5d5;
  border-radius: 8px;
  padding: 0.6rem 0.8rem;
  font-size: 1rem;
}

.search-bar__hint {
  color: #666;
  margin: 0;
}

.search-bar__results {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 1rem;
}

.search-bar__result {
  border: 1px solid #ececec;
  border-radius: 12px;
  padding: 0.75rem 1rem;
  background: #fff;
}

.search-bar__link {
  display: flex;
  justify-content: space-between;
  gap: 0.5rem;
  text-decoration: none;
  color: inherit;
}

.search-bar__title {
  font-weight: 600;
}

.search-bar__meta {
  font-size: 0.85rem;
  text-transform: uppercase;
  color: #999;
}

.search-bar__summary {
  margin: 0.5rem 0 0.75rem;
  color: #444;
}

.search-bar__tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.search-bar__tag {
  background: #f2f2f2;
  border-radius: 999px;
  padding: 0.2rem 0.6rem;
  font-size: 0.8rem;
}
</style>
