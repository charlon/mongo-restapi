import { fileURLToPath, URL } from "url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  // MARK: start vite build config

  // vite creates a manifest and assets during the build process (local and prod)
  // django collectstatics will put assets in '/static/mongo_rest/assets'
  // django will put the manifest in '/static/manifest.json'
  // vite manifest prefaces all files with the path 'mongo_rest/assets/xxxx'
  build: {
    manifest: true,
    rollupOptions: {
      input: [
        // list all entry points
        "./mongo_rest_vue/main.js",
      ],
    },
    outDir: "./mongo_rest/static/", // relative path to django's static directory
    assetsDir: "mongo_rest/assets", // default ('assets')... this is the namespaced subdirectory of outDir that vite uses
    emptyOutDir: false, // set to false to ensure favicon is not overwritten
  },
  base: "/static/", // allows for proper css url path creation during the build process

  // MARK: standard vite/vue plugin and resolver config
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./mongo_rest_vue", import.meta.url)),
    },
  },
});
