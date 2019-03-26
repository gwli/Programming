JS and Node.js
###############

最具C的格式，scheme一切皆对象的形式。再加异步编程的模型，可以随意的用event来进行function call. 
每一个函数的执行都可以callback. 应该是每一个对象都有一个callback. 并且还有prototype机制，暂且当做反射来用吧。

#. 最好用的IDE  online/offfline
#. framework

快速入门：https://www.nodebeginner.org/index-zh-cn.html,https://github.com/mbeaudru/modern-js-cheatsheet

由于nodejs 本身采用异步并行机制，里面就会出大量的event以及相关的trigger 可以用hack. 进行定制化。并且nodejs是应用框架与语言相互融合。
https://github.com/muicss/sentineljs 利用 @keyframes的动态rule来检测DOM中新加的结点。


关键是要理解浏览器的render机制。现在的机制你只管取数据，然后扔给浏览器的engine来进行rendering. 

如何hacking这个rendering过程呢。


数组
====

https://github.com/waterlink/Challenge-Build-Your-Own-Array-In-Js，一个JS Array的测试集。

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



PWA(Progressive Web Apps)
=========================

用来解决适配不同的终端以及不同网速的设计结构。
把原生应用与网络融合起来，即有原生应用的快速与灵活，又有联网的好处，就像各种新闻客户端一样。
并且已经有一些好用的框架。
例如 preactjs.com 在DOM封装了一层，同时体积非常小与快速。
https://preactjs.com/ 3kb atlternative to React.


快速原型建模打桩
================

API Mocker 接口管理系统 https://github.com/DXY-F2E/api-mocker，
Graphql 接口管理采用基于字典对象的型式，可以方便的进行扩展与演化。
http://graphql.cn/
https://github.com/atulmy/fullstack-graphql

module 开发结构
===============

清理临时文件的工具: https://github.com/tj/node-prune

Vue.js
======

浏览器的工作原理 对比原来的dom,找到最小编辑距离，然后修改，并进行重绘。
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

react 的常用的一些设计模式 https://github.com/kentcdodds/advanced-react-patterns
https://github.com/Heydon/inclusive-design-checklist

MEAN stack
===========

Mongo,Express,Augular, Nodejs.

ReactX rxjs 异步处理库，类似于ajax.

storybook 不错 UI galaxy demo. https://storybook.js.org/examples/
https://github.com/storybooks/storybook
开源好用图标库 
https://feathericons.com/

快速fix 避免半夜加班改，还是失败 所以deploy的代码最好也要用版本控制，关键是数据也可以回退：https://github.com/maxchehab/quickfix

数据的回退: https://github.com/Meituan-Dianping/MyFlash

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
主要也就是MessageQeqeue再加上一个执行代码。特别适合建立异步的模拟机。是不是也特别适合区块链的
合约系统的开发。 

对于半静态的event call,promise是一个不错的机制。 

同时比回调函数更进了一步。就像有点像gl之类的操作。

.. code-block:: python
   
   var promise = getAsyncPromise("fileA.txt");
   promise.then(function(result){}).catch(function(error){});


这些并不是执行顺序，这一点与一般的编程语言不同的点，代码的输写顺序
与执行顺序是不一致的。

css
===


随着HTML的发展，css也从原来静态的模式匹配，发展到变量等动态有sass，再到支持对象模板的less等。
同时网页动画，从最简单的css动画,到gl动画。有各种各样的库http://www.css88.com/archives/7389
轻量的渐变库，https://github.com/LiikeJS/Liike

直接利用scss来生成各种效果图，例如各种有机的效果图。https://github.com/picturepan2/devices.css

一种自定义的动态转场动化，可以基于地图位置的转场： https://github.com/codrops/AnimatedFrameSlideshow

https://github.com/Flaque/merchant.js 可以做无聊动画的框架类似于doodle.


正是由于 nodejs这种异步的机制，只要给出一个总量，以后异步计算增量就可以真实反映进步了。
https://github.com/sindresorhus/p-progress

如何快速描述一个掌握的技能，准备一个面试宝典，过一遍，就能完全理解。
例如 https://github.com/Pau1fitz/react-interview
React 就是在DOM上面又封装了一层，VirtualDOM,并且这个DOM,对象化的，并且其rendering过程都是显式可控的。


node debug
==========

直接采用的remote debug模式，node + chrome:inspect的模式。

在线调试器有 jsfiddle,codePen,以及各种动画的galxy等等可以用，https://www.zhihu.com/question/31731104

https://github.com/fhinkel/type-profile, 充分利用V8的特性，这样可以有效的提高troubleshoot的效率。

快速原型的方法
==============

https://github.com/renatorib/react-powerplug ,采用Render Props的设计模式。


DashBoard
=========

各种中DashBoard的框架。
https://jslancerteam.github.io/crystal-dashboard/#/
https://github.com/akveo/nebular

类型检查
========

https://github.com/sindresorhus/is， 可以进行类型检查，基于类型检测好处，就是量纲法可以有效的减少错误。
benchmark
=========

对于各种framework，到底采用哪一个，最实用的标准之一，那就是性能对比。
https://github.com/krausest/js-framework-benchmark,performance的对比。

显示系统 
========

PPT 可以采用 nodeppt来做，
https://github.com/DracoBlue/markdown-papers

写出可以nodejs + asciidoc 可以参考 https://github.com/liubin/promises-book/

一些非常有用的转换工具
======================

把代码转化成图片，主要是用于ppt 的显示。

https://github.com/mplewis/src2png


Test
====

javascript的自动化测试框架: https://github.com/jest-community/jest-runner-eslint

同时还有商业化的控件库http://www.grapecity.com.cn/developer/wijmojs#price


浏览器引擎
=========

.. figure:: https://www.html5rocks.com/zh/tutorials/internals/howbrowserswork/webkitflow.png
    
   webkit 
    
.. figure:: https://www.html5rocks.com/zh/tutorials/internals/howbrowserswork/image008.jpg
   
   Mozilla 的 Gecko 呈现引擎主流程
   

`浏览器的工作原理 <https://www.html5rocks.com/zh/tutorials/internals/howbrowserswork/>`_

渲染引擎会遍历渲染树，由用户界面后端层将每个节点绘制出来

按照合理的顺序合并图层然后显示到屏幕上。

浏览器刷新的频率大概是60次/秒， 也就是说刷新一次大概时间为16ms

如果浏览器对每一帧的渲染工作超过了这个时间， 页面的渲染就会出现卡顿的现象。

以上过程是渐进的，并不一定严格按照顺序执行的，为了更快将内容呈现在不屏幕中， 不会等到HTML全部解析完成之后才开始构建渲染树和layout，它会在不断接收和处理其他网络资源的同时，就开始部分内容的解析和渲染

渲染完成之后会触发 ready事件

什么情况下会引起 reflow repaint
当render tree （元素尺寸） 发生变化时则会重新layout 则会因此reflow. 

浏览器首先下载html、css、js。 接着解析生成dom tree、rule tree和rendering tree。 再通过layout后渲染页面.

浏览器的内核是多线程的，它们在内核控制下相互配合以保持同步，一个浏览器至少实现三个常驻线程：JavaScript引擎线程，GUI渲染线程，浏览器事件触发线程

.. figure:: https://pic4.zhimg.com/80/e8704374ae3d80ab1de47f2cb6899a1a_hd.jpg
   
   webkit 
   
如何动画
=======

动画的性能优化 https://www.w3cplus.com/animation/animation-performance.html

.. code-block:: html

   <div style="width:75%">
            <canvas id="canvas"></canvas>
   </div>
   <script>
            var color = Chart.helpers.color;
            var scatterChartData = {
                datasets: [{
                    label: 'My First dataset',
                    xAxisID: 'x-axis-1',
                    yAxisID: 'y-axis-1',
                    borderColor: window.chartColors.red,
                    backgroundColor: color(window.chartColors.red).alpha(0.2).rgbString(),
                    data: [{
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }]
                }, {
                    label: 'My Second dataset',
                    xAxisID: 'x-axis-1',
                    yAxisID: 'y-axis-2',
                    borderColor: window.chartColors.blue,
                    backgroundColor: color(window.chartColors.blue).alpha(0.2).rgbString(),
                    data: [{
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }, {
                        x: randomScalingFactor(),
                        y: randomScalingFactor(),
                    }]
                }]
            };

            window.onload = function() {
                var ctx = document.getElementById('canvas').getContext('2d');
                window.myScatter = Chart.Scatter(ctx, {
                    data: scatterChartData,
                    options: {
                        responsive: true,
                        hoverMode: 'nearest',
                        intersect: true,
                        title: {
                            display: true,
                            text: 'Chart.js Scatter Chart - Multi Axis'
                        },
                        scales: {
                            xAxes: [{
                                position: 'bottom',
                                gridLines: {
                                    zeroLineColor: 'rgba(0,0,0,1)'
                                }
                            }],
                            yAxes: [{
                                type: 'linear',
                                // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                                display: true,
                                position: 'left',
                                id: 'y-axis-1',
                            }, {
                                type: 'linear',
                                // only linear but allow scale type registration. This allows extensions to exist solely for log scale for instance
                                display: true,
                                position: 'right',
                                reverse: true,
                                id: 'y-axis-2',

                                // grid line settings
                                gridLines: {
                                    drawOnChartArea: false,
                                    // only want the grid lines for one axis to show up
                                },
                            }],
                        }
                    }
                });
            }
            ;

            document.getElementById('randomizeData').addEventListener('click', function() {
                scatterChartData.datasets.forEach(function(dataset) {
                    dataset.data = dataset.data.map(function() {
                        return {
                            x: randomScalingFactor(),
                            y: randomScalingFactor()
                        };
                    });
                });
                window.myScatter.update();
            });
    </script>
