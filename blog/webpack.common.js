const path = require('path');
'./static/js/index.js'
module.exports = {
  mode: 'development',
  entry: path.resolve(__dirname,'static','js','index.js'),
  devtool: 'inline-source-map',
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: [[
              '@babel/preset-env', {
                targets: {
                  esmodules: true
                }
              }],
              '@babel/preset-react']
          }
        }
      },
      {
        test: [/\.s[ac]ss$/i, /\.css$/i],
        use: [
          // Creates `style` nodes from JS strings
          'style-loader',
          // Translates CSS into CommonJS
          'css-loader',
          // Compiles Sass to CSS
          'sass-loader',
        ],
      }
    ]
  },
  plugins: [],
  resolve: {
    extensions: ['.js'],
  },
  output: {
    filename: 'app.js',
    path: path.resolve(__dirname,'static','js','build'),
  },
};