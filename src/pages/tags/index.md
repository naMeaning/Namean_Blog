---
title: Tags
---

<section>
  <h1>Tags</h1>
  <p>所有标签聚合。</p>
  <div id="tag-list" class="tag-grid"></div>
</section>

<script type="module">
  import { getTags } from "../../lib/api.ts";

  const listEl = document.getElementById("tag-list");
  const tags = await getTags();

  listEl.innerHTML = tags
    .map(
      (tag) => `
        <a class="tag-card" href="/tags/${encodeURIComponent(tag.name)}/">
          <span class="tag-card__name">${tag.name}</span>
          <span class="tag-card__count">${tag.count} 篇</span>
        </a>
      `,
    )
    .join("");
</script>

<style>
  .tag-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 1rem;
    margin-top: 1rem;
  }

  .tag-card {
    display: flex;
    justify-content: space-between;
    gap: 0.5rem;
    border: 1px solid #ececec;
    border-radius: 12px;
    padding: 0.75rem 1rem;
    text-decoration: none;
    color: inherit;
    background: #fff;
  }

  .tag-card__name {
    font-weight: 600;
  }

  .tag-card__count {
    color: #777;
  }
</style>
