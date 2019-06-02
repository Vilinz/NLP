# 机器翻译与自动问答

------

**学号：16340181**

**姓名：彭伟林**

------

## 调参历程

首先，在用作者给出来的参数对模型进行训练的时候，我发现训练的时候loss值和perplexity值下降的速度有点慢，所以我尝试着减少bitchsize的大小，我将其设为128；与此同时，在训练的后期，loss值和perplexity值下降得更加平缓了，而动态调整学习率是一个不错的选择，我先用128大小的bitch与0.001的学习率训练了30个Epoch，然后用lr=0.0005训练10个Epoch，再用lr=0.0001训练10个Epoch。但这样调参到最后效果不明显，我觉得是bitchsize设置的问题，然后我将bitchsize设置为256，学习率为0.001，Epoch为100，最后可以得到一个比较好的结果，Loss值下降到1.5左右，perplexity下降到4左右。

1. 在bitchsize=128，lr=0.001训练30个Epoch的时候，我画出了他们数据的图像，显然，调整之后的训练效果更加好了，但是在后面就很难下降了，原因是bitchsize设置得太小了。

   ![1557761846041](C:/Users/彭伟林/AppData/Roaming/Typora/typora-user-images/1557761846041.png)

   ![1557761867950](C:/Users/彭伟林/AppData/Roaming/Typora/typora-user-images/1557761867950.png)

   

2. 根据1的经验，我重新把batchsize设为256，并且我调小了学习率为0.001，然后增加训练的次数到100次，最后Loss值可以下降到1.5左右，而perplexity可以下降到4左右。

   ![1557909840761](C:/Users/彭伟林/AppData/Roaming/Typora/typora-user-images/1557909840761.png)

   

   ![1557909865705](C:/Users/彭伟林/AppData/Roaming/Typora/typora-user-images/1557909865705.png)

   ![1557909880967](C:/Users/彭伟林/AppData/Roaming/Typora/typora-user-images/1557909880967.png)