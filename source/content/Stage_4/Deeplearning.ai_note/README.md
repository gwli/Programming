吴恩达的深度学习教程
##################

* 单个神经元单个sample的计算  
  .. math::
     
     #forword
     z = w_1*x_1 + w_2*x_2 +b 
     a = g(z)
     loss = y-a
     
     #backword
     dw1 = dz*x_1
     dw2 = dz*x_2
     db = dz
     
* 单个神经元的多个sample训练计算
* 多个神经元的多个sample的训练浅层神经网络
* 深层网络的计算。
