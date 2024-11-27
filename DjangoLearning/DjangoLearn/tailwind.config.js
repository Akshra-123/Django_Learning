module.exports = {
  content: [
    './templates//*.html',  // adjust this path based on your project structure
    './/templates//*.html',
    './static/js//*.js',    // if you have JavaScript files where you use Tailwind classes
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}