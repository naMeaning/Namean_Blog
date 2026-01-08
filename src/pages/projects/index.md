---
title: Projects
---

<section>
  <h1>Projects</h1>
  <p>项目展示列表。</p>
  <div id="project-list" class="card-grid"></div>
</section>

<script type="module">
  import { getProjects } from "../../lib/api.ts";

  const listEl = document.getElementById("project-list");
  const projects = await getProjects();

  listEl.innerHTML = projects
    .map(
      (project) => `
        <article class="card">
          <div class="card__header">
            <h2><a href="${project.url}">${project.title}</a></h2>
            <span class="card__date">${project.date}</span>
          </div>
          <p class="card__summary">${project.summary}</p>
          <div class="card__tags">
            ${project.tags
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

  .tag {
    background: #f3f3f3;
    border-radius: 999px;
    padding: 0.2rem 0.7rem;
    font-size: 0.85rem;
    text-decoration: none;
    color: inherit;
  }
</style>
