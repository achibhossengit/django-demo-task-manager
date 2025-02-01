/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html ", // templates at the project level
    "./**/templates/**/*.html" // template inside app
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

