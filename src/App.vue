<template>
  <div class="app-shell">
    <header class="site-header">
      <div class="brand">
        <span class="brand-mark">N</span>
        <div>
          <h1>Namean Studio</h1>
          <p>作品集 · 博客</p>
        </div>
      </div>
      <nav class="site-nav">
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/posts">Posts</RouterLink>
        <RouterLink to="/projects">Projects</RouterLink>
        <RouterLink to="/tags">Tags</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/contact">Contact</RouterLink>
      </nav>
    </header>

    <main class="site-main">
      <RouterView />
    </main>

    <footer class="site-footer">
      <div>
        <strong>© 2026 Namean Studio</strong>
        <p>聚焦技术解决方案、产品体验与行业洞察。</p>
      </div>
      <div class="footer-links">
        <a href="mailto:hello@namean.studio">hello@namean.studio</a>
        <span>Shanghai · Remote</span>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>
