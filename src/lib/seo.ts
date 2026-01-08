export interface SeoPayload {
  title: string;
  description: string;
  url?: string;
  type?: string;
}

function upsertMetaTag(attribute: "name" | "property", key: string): HTMLMetaElement {
  const selector = `meta[${attribute}="${key}"]`;
  const existing = document.head.querySelector(selector) as HTMLMetaElement | null;
  if (existing) {
    return existing;
  }
  const meta = document.createElement("meta");
  meta.setAttribute(attribute, key);
  document.head.appendChild(meta);
  return meta;
}

export function applyDetailSeo(payload: SeoPayload): void {
  const { title, description, url, type = "article" } = payload;
  document.title = title;
  upsertMetaTag("name", "description").setAttribute("content", description);
  upsertMetaTag("property", "og:title").setAttribute("content", title);
  upsertMetaTag("property", "og:description").setAttribute("content", description);
  upsertMetaTag("property", "og:type").setAttribute("content", type);
  if (url) {
    upsertMetaTag("property", "og:url").setAttribute("content", url);
  }
}
