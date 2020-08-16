PICTURE_WIDTH = 25
PICTURE_HEIGHT = 6
SIZE = PICTURE_HEIGHT*PICTURE_WIDTH

with open("day_8_input.txt","r") as f:
    message = [int(i) for i in f.read().rstrip()]
    layers = [message[x:x+SIZE] for x in range(0,len(message),SIZE)]
    layer_with_min_0 = 0
    min_0 = layers[0].count(0)

    for index in range(0,len(layers)):
        nb_0 = layers[index].count(0)
        if nb_0 < min_0:
            layer_with_min_0 = index
            min_0 = nb_0

    print(layers[layer_with_min_0].count(1)*layers[layer_with_min_0].count(2))
