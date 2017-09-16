JS and Node.js
**************

#. 最好用的IDE  online/offfline
#. framework

当前最流行的前沿技术，都有哪些各有什么特点
------------------------------------------

#. single page application


Java script buffer,stream的概念不错，特别接近真实的数据结构。

http://v3.bootcss.com/ 用来生成UI的布局。
`facebook 前端UI开发框架：React <https://facebook.github.io/react/>`_ 
`Angular.js 介绍及实践教程 <https://www.ibm.com/developerworks/cn/web/1406_rentt_angularjs/index.html>`_ 主要GUI的控件与数据的绑定。

HTML5 下一代的HTML的规范，会有不少新特性。


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
