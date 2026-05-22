import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      boxShadow: {
        glow: '0 20px 60px rgba(13, 110, 253, 0.15)',
      },
      colors: {
        brand: {
          50: '#eef6ff',
          500: '#0d6efd',
          700: '#0b5ed7',
        },
      },
    },
  },
  plugins: [],
};

export default config;
