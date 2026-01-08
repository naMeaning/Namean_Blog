---
title: Tag Detail
---

<section>
  <h1 id="tag-title">Tag</h1>
  <p id="tag-summary"></p>
</section>

<section>
  <h2>相关文章</h2>
  <div id="tag-posts" class="card-grid"></div>
</section>

<section>
  <h2>相关项目</h2>
  <div id="tag-projects" class="card-grid"></div>
</section>

<script type="module">
  import { getContentByTag } from "../../lib/api.ts";
  import { applyDetailSeo } from "../../lib/seo.ts";

  const tag = decodeURIComponent(
    window.location.pathname.split("/").filter(Boolean).pop() || "",
  );

  const titleEl = document.getElementById("tag-title");
  const summaryEl = document.getElementById("tag-summary");
  const postsEl = document.getElementById("tag-posts");
  const projectsEl = document.getElementById("tag-projects");

  titleEl.textContent = `Tag: ${tag}`;

  const { posts, projects } = await getContentByTag(tag);
  summaryEl.textContent = `共 ${posts.length} 篇文章，${projects.length} 个项目。`;

  const renderCards = (items) =>
    items
      .map(
        (item) => `
          <article class="card">
            <div class="card__header">
              <h3><a href="${item.url}">${item.title}</a></h3>
              <span class="card__date">${item.date}</span>
            </div>
            <p class="card__summary">${item.summary}</p>
            <div class="card__tags">
              ${item.tags
                .map(
                  (tagName) =>
                    `<a class="tag" href="/tags/${encodeURIComponent(tagName)}/">${tagName}</a>`,
                )
                .join("")}
            </div>
          </article>
        `,
      )
      .join("");

  postsEl.innerHTML = posts.length ? renderCards(posts) : "<p>暂无文章。</p>";
  projectsEl.innerHTML = projects.length
    ? renderCards(projects)
    : "<p>暂无项目。</p>";

  const description = `共 ${posts.length} 篇文章，${projects.length} 个项目。`;
  applyDetailSeo({
    title: `Tag: ${tag}`,
    description,
    url: window.location.href,
    type: "website",
  });
</script>

<style>
  .card-grid {
    display: grid;
    gap: 1.25rem;
    margin-top: 1rem;
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

  .tag {
    background: #f3f3f3;
    border-radius: 999px;
    padding: 0.2rem 0.7rem;
    font-size: 0.85rem;
    text-decoration: none;
    color: inherit;
  }
</style>
