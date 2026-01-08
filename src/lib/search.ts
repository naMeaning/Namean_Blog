import type { SearchIndexEntry } from "./api";

export interface SearchResult {
  item: SearchIndexEntry;
  score: number;
}

function normalizeQuery(query: string): string[] {
  return query
    .toLowerCase()
    .split(/[\s\-_/]+/)
    .map((token) => token.trim())
    .filter(Boolean);
}

function scoreEntry(tokens: string[], entry: SearchIndexEntry): number {
  if (tokens.length === 0) {
    return 0;
  }
  const haystack = [
    entry.title,
    entry.summary,
    entry.tags.join(" "),
    entry.content,
  ]
    .join(" ")
    .toLowerCase();

  let score = 0;
  for (const token of tokens) {
    if (entry.title.toLowerCase().includes(token)) {
      score += 6;
    }
    if (entry.tags.some((tag) => tag.toLowerCase().includes(token))) {
      score += 4;
    }
    if (entry.summary.toLowerCase().includes(token)) {
      score += 2;
    }
    if (haystack.includes(token)) {
      score += 1;
    }
  }
  return score;
}

export function searchIndex(
  query: string,
  index: SearchIndexEntry[],
  limit = 8,
): SearchResult[] {
  const tokens = normalizeQuery(query);
  if (tokens.length === 0) {
    return [];
  }
  return index
    .map((entry) => ({
      item: entry,
      score: scoreEntry(tokens, entry),
    }))
    .filter((result) => result.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, limit);
}
