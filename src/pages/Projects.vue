<template>
  <section class="section">
    <h2 class="section-title">项目作品集</h2>
    <SearchBar v-model="keyword" />
    <div class="card-grid">
      <article v-for="project in filteredProjects" :key="project.slug" class="card">
        <p class="card-meta">{{ project.date }} · {{ project.role }}</p>
        <h3>{{ project.title }}</h3>
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
import { computed, ref } from "vue";
import { RouterLink } from "vue-router";
import SearchBar from "../components/SearchBar.vue";
import { projects } from "../lib/contentStore";

const keyword = ref("");

const filteredProjects = computed(() => {
  const query = keyword.value.trim().toLowerCase();
  if (!query) {
    return projects;
  }
  return projects.filter((project) =>
    [project.title, project.summary, project.tags.join(" ")].join(" ").toLowerCase().includes(query)
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
