JS and Node.js
**************

最具C的格式，scheme一切皆对象的形式。再加异步编程的模型，可以随意的用event来进行function call. 
每一个函数的执行都可以callback. 应该是每一个对象都有一个callback. 并且还有prototype机制，暂且当做反射来用吧。

#. 最好用的IDE  online/offfline
#. framework

快速入门：https://www.nodebeginner.org/index-zh-cn.html

当前最流行的前沿技术，都有哪些各有什么特点
------------------------------------------

#. single page application


Java script buffer,stream的概念不错，特别接近真实的数据结构。

http://v3.bootcss.com/ 用来生成UI的布局。
`facebook 前端UI开发框架：React <https://facebook.github.io/react/>`_ 
`Angular.js 介绍及实践教程 <https://www.ibm.com/developerworks/cn/web/1406_rentt_angularjs/index.html>`_ 主要GUI的控件与数据的绑定。

HTML5 下一代的HTML的规范，会有不少新特性。

如果对性能有更高的要求的可以用 https://infernojs.org/benchmarks

用nodejs来开发，就充分利用了html的灵活性来设计界面，同时nodejs又可以像传统编程来实现逻辑部分。

来实现各种 html的template 并且就像类一样，简版的react: https://github.com/mikeal/rza

Vue.js
======

#. cdn url 

#. v-bind:PROPERTY  -> :Property
   v-on:Click       -> @EVENT


   v-if
   v-for

.. code-block:: javascript

   <script src="https://unpkg.com/vue"<script>
   <div id="app">
       {{ name }}
   </div>

   New Vue ({
      el: "#app",
      data: {
        name : "max"
      }
   })

   Vue.Component



#. npm install -g vue-cli

webpack 相当于打包编译工具。
并且可优化代码。

React
======

利用用类对来对应网页，并且函数就是render()函数。利用面向对象的方式来构造网页。

npm -g create-react-app

MEAN stack
===========

Mongo,Express,Augular, Nodejs.

ReactX rxjs 异步处理库，类似于ajax.


Angular 2 
=========

.. code-block:: bash
   
   npm install -g @angular/cli
   ng new <new project>

#. Single Page
#. Update DOM
#. Handles Routing(of visual Parts)
#. Very reactive user experiences

ng-app,ng-xxx to binding things.
.. image:: /content/Stage_1/JavascriptAndNodeJS.Angular2_cs.png

Javascript 的promise机制
========================

生成二次回调机制，只有上一个调用成功，然后利用生成调用代码，然后再传给回调。


css
===

随着HTML的发展，css也从原来静态的模式匹配，发展到变量等动态有sass，再到支持对象模板的less等。
同时网页动画，从最简单的css动画,到gl动画。有各种各样的库http://www.css88.com/archives/7389

node debug
==========

直接采用的remote debug模式，node + chrome:inspect的模式。


显示系统 
========

PPT 可以采用 nodeppt来做，
https://github.com/DracoBlue/markdown-papers
