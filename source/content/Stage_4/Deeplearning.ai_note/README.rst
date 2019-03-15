吴恩达的深度学习教程
##################

* 单个神经元单个sample的计算 

  .. math::
     
     #forword
     z = w_1*x_1 + w_2*x_2 +b 
     a = g(z)
     loss = yloga -(1-y)log(1-a)
     
     
     #backword
     dw1 = dz*x_1
     dw2 = dz*x_2
     db = dz
     
   * 从这里可以看dz,a 都是要存入下，反向计算的还是需要这些值的。
   
* 单个神经元的多个sample训练计算
  
  .. math::
     
     coss = 1/m(loss_1 + ... + loss_m)
     dw1  = 1/m*sum(dw_1m)
     dw2  = 1/m* sum(dw_2m)
     db = 1/m *sum(dzm)
     
 
* 多个神经元的多个sample的训练浅层神经网络

  * W的个数随神经输入nx*nh 神经元的个数。 
    
    .. math:: 
      
       W= [[w11,w12,w13,...]
        [w21,w22,w23...]] 
        
     
* 深层网络的计算。
   
    * 每一层的计算
