- using 1 conv with 32 filters of (3,3)/ 1 maxpool (2,2)/ 1 hidden layer 128 / 1 drpout 0.5 => accuracy: 0.0569
- 2 conv and 2 maxpool => accuracy: 0.9124, loss: 0.3088
- filter in conv (2,2) => accuracy: 0.0565, loss: 3.4987
- filter in conv (4,4) => loss: 3.5047 - accuracy: 0.0550
- 64 filters in conv => loss: 3.4945 - accuracy: 0.0555
- maxpool (3,3) => loss: 3.5050 - accuracy: 0.0563
- maxpool (4,4) => loss: 3.5025 - accuracy: 0.0557
- 2 hidden layers 128 => loss: 0.4549 - accuracy: 0.8793
- + hidden layers 256 => loss: 0.3896 - accuracy: 0.8974
- + hidden layers 512 => loss: 3.5008 - accuracy: 0.0524
- dropout 0.6 => loss: 3.4949 - accuracy: 0.0554
- dropout 0.3 => loss: 3.4953 - accuracy: 0.0557
- remove dropout => loss: 0.5797 - accuracy: 0.9244
- remove dropout + 2 conv and 2 maxpool => loss: 0.5905 - accuracy: 0.8758
- remove dropout + add hidden layers 256 => loss: 0.4468 - accuracy: 0.9351
- add hidden layers 256 + 2 conv and 2 maxpool => loss: 0.2804 - accuracy: 0.9329
- remove dropout + add hidden layers 256 + 2 conv and 2 maxpool => loss: 0.2938 - accuracy: 0.9403

* I tried different methods, I first did single changes to compare the impacts of each one of them on the result, and then chose the methods that gave me the best impacts.
* The steps that didn't work well are when I changed the size and number of the filters for the convolutional layer, when I changed the size of the pooling layer and when I changed the value for the dropout.
* The steps that worked well are when I added another convolutional and pooling layer, when I added another hidden layer, and when I removed the dropout. So I used those 3 changes in order to get the best accuracy (0.9403).
* I noticed that the main step to do in order to improve the accuracy is to add hidden, convolutional and pooling layers, as for the dropouts, it is better not to use them when we have a small number of layers.

