zeromq
======
http://zeromq.org/
https://zh.wikipedia.org/wiki/%C3%98MQ
https://program-think.blogspot.com/2011/08/opensource-review-zeromq.html

网络通迅库，要比使用socket要方便很多，同时也提供各种异步的机制。不必在重复开发。
单播，组播都是现成模块。 相当于是socket的泛化，原来socket解析，要自己做包解析
要从字节流解析出来，现在zeromq直接是消息块为单位的。相当于已经帮你断句了。

这一类的通信库有很多，例如nanomsg.
http://www.infoq.com/cn/news/2014/08/zeromq-not-first-choice

http://www.aosabook.org/en/zeromq.html
