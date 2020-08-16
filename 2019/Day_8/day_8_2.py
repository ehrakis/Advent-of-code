PICTURE_WIDTH = 25
PICTURE_HEIGHT = 6
SIZE = PICTURE_HEIGHT*PICTURE_WIDTH

with open("day_8_input.txt","r") as f:
    message = [int(i) for i in f.read().rstrip()]
    layers = [message[x:x+SIZE] for x in range(0,len(message),SIZE)]

    final_picture = [2 for _ in range(SIZE)]
    for layer in layers:
        for index in range(SIZE):
            if final_picture[index] == 2 and layer[index] != 2:
                final_picture[index] = layer[index]

    for index in range(SIZE):
        if final_picture[index] == 0:
            final_picture[index] = '█'
        else:
            final_picture[index] = ' '

    for i in range(PICTURE_HEIGHT):
        print("".join(map(str, final_picture[PICTURE_WIDTH*i:PICTURE_WIDTH*(i+1)])))
