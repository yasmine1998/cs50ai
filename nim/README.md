* I tried different methods, I first did single changes to compare the impacts of each one of them on the result, and then chose the methods that gave me the best impacts.
* The steps that didn't work well are when I changed the size and number of the filters for the convolutional layer, when I changed the size of the pooling layer and when I changed the value for the dropout.
* The steps that worked well are when I added another convolutional and pooling layer, when I added another hidden layer, and when I removed the dropout. So I used those 3 changes in order to get the best accuracy (0.9403).
* I noticed that the main step to do in order to improve the accuracy is to add hidden, convolutional and pooling layers, as for the dropouts, it is better not to use them when we have a small number of layers.

