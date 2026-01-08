# Namean_Blog

## 目录结构

```
src/
  pages/
    index.md
    about.md
    contact.md
    posts/
      index.md
      [slug].md
    projects/
      index.md
      [slug].md
    tags/
      index.md
      [tag].md
  layouts/
  components/
  assets/
content/
  posts/
    hello-world.md
  projects/
    portfolio-site.md
```

## 本地运行

> 由于当前仓库仅提供内容与目录结构示例，可使用简单静态服务器预览页面目录。

```bash
python -m http.server 8080 --directory src
```

## 构建

> 这里提供一个最小化的静态导出示例，将 `src` 与 `content` 拷贝到 `dist/`。

```bash
mkdir -p dist && cp -R src content dist
```
