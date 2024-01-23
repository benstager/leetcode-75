def is_valid(image:list[list[int]], x:int, y:int, color, prev_color):
    # check if its a valid square, false if the current pixel is equal to the target color or if its already been colored
    if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] == color or image[x][y] != prev_color:
        return False
    return True

def flood_fill(image:list[list[int]], sr:int, sc:int, color):
    # use queue approach
    queue = []
    queue.append([sr,sc])
    prev_color = image[sr][sc]
    image[sr][sc] = color

    # check each 4 - directional square
    while queue:
        # pop each iteration, indicating which square you are currently on
        current_pix = queue.pop()
        x = current_pix[0]
        y = current_pix[1]

        if is_valid(image, x+1, y, color, prev_color):
            image[x+1][y] = color
            queue.append([x+1,y])

        if is_valid(image, x-1, y, color, prev_color):
            image[x-1][y] = color
            queue.append([x-1,y])
        
        if is_valid(image, x, y+1, color, prev_color):
            image[x][y+1] = color
            queue.append([x,y+1])
        
        if is_valid(image, x, y-1, color, prev_color):
            image[x][y-1] = color
            queue.append([x,y-1])
        
    return image

test_case =[
[1, 1, 1, 1, 1, 1, 1, 1], 
[1, 1, 1, 1, 1, 1, 0, 0], 
[1, 0, 0, 1, 1, 0, 1, 1], 
[1, 2, 2, 2, 2, 0, 1, 0], 
[1, 1, 1, 2, 2, 0, 1, 0], 
[1, 1, 1, 2, 2, 2, 2, 0], 
[1, 1, 1, 1, 1, 2, 1, 1], 
[1, 1, 1, 1, 1, 2, 2, 1], 
    ]
     
#print(flood_fill(test_case, 4, 4, 3))

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

print(flood_fill(image, sr, sc, color))