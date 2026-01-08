import fs from "node:fs";
import path from "node:path";
import { defineConfig } from "vite";

const prerenderRoutesPath = path.resolve(__dirname, "public/prerender-routes.json");
const prerenderRoutes = fs.existsSync(prerenderRoutesPath)
  ? JSON.parse(fs.readFileSync(prerenderRoutesPath, "utf-8"))
  : [];

export default defineConfig({
  build: {
    outDir: "dist",
  },
  define: {
    __PRERENDER_ROUTES__: JSON.stringify(prerenderRoutes),
  },
});
