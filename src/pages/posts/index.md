---
title: Posts
---

<section>
  <h1>Posts</h1>
  <p>最新文章列表。</p>
  <div id="post-tags" class="tag-cloud"></div>
  <div id="post-list" class="card-grid"></div>
</section>

<script type="module">
  import { getPosts, getTags } from "../../lib/api.ts";

  const listEl = document.getElementById("post-list");
  const tagsEl = document.getElementById("post-tags");

  const [posts, tags] = await Promise.all([getPosts(), getTags()]);

  tagsEl.innerHTML = tags
    .map(
      (tag) =>
        `<a class="tag" href="/tags/${encodeURIComponent(tag.name)}/">${tag.name} (${tag.count})</a>`,
    )
    .join("");

  listEl.innerHTML = posts
    .map(
      (post) => `
        <article class="card">
          <div class="card__header">
            <h2><a href="${post.url}">${post.title}</a></h2>
            <span class="card__date">${post.date}</span>
          </div>
          <p class="card__summary">${post.summary}</p>
          <div class="card__tags">
            ${post.tags
              .map(
                (tag) =>
                  `<a class="tag" href="/tags/${encodeURIComponent(tag)}/">${tag}</a>`,
              )
              .join("")}
          </div>
        </article>
      `,
    )
    .join("");
</script>

<style>
  .card-grid {
    display: grid;
    gap: 1.25rem;
    margin-top: 1.5rem;
  }

  .card {
    border: 1px solid #e5e5e5;
    border-radius: 12px;
    padding: 1rem 1.25rem;
    background: #fff;
  }

  .card__header {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    align-items: baseline;
  }

  .card__date {
    font-size: 0.85rem;
    color: #999;
  }

  .card__summary {
    color: #444;
  }

  .card__tags {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .tag-cloud {
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
    margin-top: 1rem;
  }

  .tag {
    background: #f3f3f3;
    border-radius: 999px;
    padding: 0.2rem 0.7rem;
    font-size: 0.85rem;
    text-decoration: none;
    color: inherit;
  }
</style>
