# toobuk_vued3
python을 공부하면서 간단한 모듈을 만들었습니다.  
https://github.com/ramoi/toobuk  
그러다 좀 욕심이 생겨서 화면도 만들었네요  
https://github.com/ramoi/vue-d3  

그래서 두 놈을 연동해보았습니다.  
아마도 실무에서는 쓰지 않을테지요  
웹크롤링을 하는 더 좋은 라이브러리가 있을테구요  
vue-d3는 기능이 미미합니다. 실무에서는 쓸 수 없어요  
다만 이제 시작하는 분들에게 도움이 된다면 좋을 것 같네요  

## 설치 
python을 설치했다는 가정하에 진행합니다. 아래 사이트를 참고해주세요  
https://wikidocs.net/8

	pip install django
	pip install toobuk


그리고 작업 디렉토리를 만드 후, 프로젝트를 생성합니다. 아래는 statist라는 프로젝트를 생성하는 것입니다.  

	django-admin startproject statist
	cd statist
	mkdir templates

만일 작업 디렉토리가 C:\project 라면 아래와 같이 생성되었을 겁니다. 그리고 C:\project 하위에 vue 라는 디렉토리를 듭니다.  
이제 vue 디렉토리가 vue 작업 디렉토리입니다.  
https://github.com/ramoi/vue-d3#%EC%84%A4%EC%B9%98 로 가셔서 해당 프로젝트를 설치합니다.  
정상적으로 설치하시면 webpack.config.js 파일이 생성될텐데요. 해당 파일을 아래와 같이 수정합니다.  

~~~
var path = require('path')

var vs = {
  entry: './src/mainChart.js',
  output: {
    path: path.resolve(__dirname, './static'),
    publicPath: '/static/',
    filename: 'build.js'
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'vue-style-loader',
          'css-loader'
        ],
      },      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]'
        }
      }
    ]
  },
  resolve: {
    alias: {
      'vue$': 'vue/dist/vue.esm.js'
    },
    extensions: ['*', '.js', '.vue', '.json']
  },
  devServer: {
    historyApiFallback: true,
    noInfo: true,
    overlay: true
  },
  performance: {
    hints: false
  },
  devtool: '#eval-source-map'
}

var ds = {}
for( var e in vs) {
  ds[e] = vs[e]
}

ds.entry = './src/main.js'
ds.output = {
    path: path.resolve(__dirname, '../../statist/templates/static'),
    publicPath: '/static/',
    filename: 'build.js'
}

module.exports = [
  vs, ds
]

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map'
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: '"production"'
      }
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false
      }
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true
    })
  ])
}
~~~

최종적인 모습은 아래 이미지와 같습니다.

![캡쳐화면](https://user-images.githubusercontent.com/31053133/52839092-3cd48100-3138-11e9-842d-d049c0125b4d.png)

vue 디렉토리로 이동해서 빌드해줍니다.

	cd vue\chart
	yarn run dev


django 디렉토리로 이동해서 서버를 실행시킵니다.

	cd statist
	python manage.py runserver

웹브라우저에서 접속합니다.
[http://localhost:8000/](#http://localhost:8000/)