module.exports = {
  assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:5000'
  },
  baseUrl: './',
  indexPath:"index.html",
  publicPath:""
}