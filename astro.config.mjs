import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://jakob-figur.io',
  output: 'static',
  server: {
    port: 8501,
    host: true
  }
});
