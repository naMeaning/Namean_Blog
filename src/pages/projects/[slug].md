---
title: Project Detail
---

<article class="detail">
  <header class="detail__header">
    <h1 id="detail-title">加载中…</h1>
    <p id="detail-meta" class="detail__meta"></p>
    <div id="detail-tags" class="detail__tags"></div>
  </header>
  <div id="detail-content" class="detail__content"></div>
</article>

<script type="module">
  import { getContentDetail } from "../../lib/api.ts";
  import { applyDetailSeo } from "../../lib/seo.ts";

  const slug = window.location.pathname.split("/").filter(Boolean).pop();
  const titleEl = document.getElementById("detail-title");
  const metaEl = document.getElementById("detail-meta");
  const tagsEl = document.getElementById("detail-tags");
  const contentEl = document.getElementById("detail-content");

  if (slug) {
    const detail = await getContentDetail("projects", slug);
    if (detail) {
      titleEl.textContent = detail.title;
      metaEl.textContent = detail.date;
      tagsEl.innerHTML = detail.tags
        .map(
          (tag) =>
            `<a class="tag" href="/tags/${encodeURIComponent(tag)}/">${tag}</a>`,
        )
        .join("");
      contentEl.innerHTML = detail.content_html;
      const description = detail.summary || `${detail.title} 的详细内容。`;
      applyDetailSeo({
        title: detail.title,
        description,
        url: `${window.location.origin}${detail.url}`,
        type: "article",
      });
    } else {
      titleEl.textContent = "未找到项目";
    }
  }
</script>

<style>
  .detail__meta {
    color: #777;
  }

  .detail__tags {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-top: 0.5rem;
  }

  .detail__content {
    margin-top: 1.5rem;
    line-height: 1.7;
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
