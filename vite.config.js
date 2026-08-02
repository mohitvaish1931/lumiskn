import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        mediFacials: resolve(__dirname, 'treatments/medi-facials/index.html'),
        antiAgeing: resolve(__dirname, 'treatments/anti-ageing/index.html'),
        pigmentation: resolve(__dirname, 'treatments/pigmentation/index.html'),
        acneManagement: resolve(__dirname, 'treatments/acne-management/index.html'),
        laserHairReduction: resolve(__dirname, 'treatments/laser-hair-reduction/index.html'),
      },
    },
  },
});
