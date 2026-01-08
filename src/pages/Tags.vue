<template>
  <section class="section">
    <h2 class="section-title">标签聚合</h2>
    <div class="tag-list">
      <RouterLink v-for="tag in tags" :key="tag" :to="`/tags/${tag}`" class="tag">
        {{ tag }}
      </RouterLink>
    </div>
  </section>
</template>

<script setup>
import { RouterLink } from "vue-router";
import { tags } from "../lib/contentStore";
</script>

<style scoped>
.tag-list {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}
</style>
