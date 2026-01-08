export type ContentType = "posts" | "projects";

export interface ContentListItem {
  slug: string;
  title: string;
  date: string;
  summary: string;
  tags: string[];
  draft: boolean;
  url: string;
}

export interface ContentDetail extends ContentListItem {
  content_html: string;
}

export interface TagSummary {
  name: string;
  count: number;
}

export interface SearchIndexEntry {
  id: string;
  type: ContentType;
  slug: string;
  title: string;
  summary: string;
  tags: string[];
  content: string;
  url: string;
}

const dataCache = new Map<string, Promise<unknown>>();

async function fetchJson<T>(path: string): Promise<T> {
  const response = await fetch(path);
  if (!response.ok) {
    throw new Error(`Failed to load ${path}: ${response.status}`);
  }
  return (await response.json()) as T;
}

function readData<T>(fileName: string): Promise<T> {
  const path = `/data/${fileName}`;
  const cached = dataCache.get(path);
  if (cached) {
    return cached as Promise<T>;
  }
  const request = fetchJson<T>(path);
  dataCache.set(path, request);
  return request;
}

export function getPosts(): Promise<ContentListItem[]> {
  return readData<ContentListItem[]>("posts.json");
}

export function getProjects(): Promise<ContentListItem[]> {
  return readData<ContentListItem[]>("projects.json");
}

export function getTags(): Promise<TagSummary[]> {
  return readData<TagSummary[]>("tags.json");
}

export function getSearchIndex(): Promise<SearchIndexEntry[]> {
  return readData<SearchIndexEntry[]>("search_index.json");
}

export async function getContentDetail(
  type: ContentType,
  slug: string,
): Promise<ContentDetail | null> {
  const fileName = type === "posts" ? "posts_detail.json" : "projects_detail.json";
  const items = await readData<ContentDetail[]>(fileName);
  return items.find((item) => item.slug === slug) ?? null;
}

export async function getContentByTag(tag: string): Promise<{
  posts: ContentListItem[];
  projects: ContentListItem[];
}> {
  const [posts, projects] = await Promise.all([getPosts(), getProjects()]);
  return {
    posts: posts.filter((entry) => entry.tags.includes(tag)),
    projects: projects.filter((entry) => entry.tags.includes(tag)),
  };
}
