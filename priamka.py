from PIL import Image

pic = Image.new('RGB', (300, 250), 'white')
pixels = pic.load()
A = (30, 200)
B = (200, 100)
print(pic.size[1], pic.size[0])
if A[0] < B[0]:

    k = (B[1] - A[1]) / (B[0] - A[0])
    q = A[1] - k * A[0]
    for x in range(A[0], B[0]):
        y = int(k * x + q)
        if 0 <= x <= (pic.size[0]) and 0 <= y <= (pic.size[1]):
            pixels[x, y] = (0, 0, 0)

elif A[0] == B[0]:
    if A[1] < B[1]:
        for y in range(A[1], B[1]):
            x = A[0]

            if 0 <= x <= (pic.size[0]) and 0 <= y <= (pic.size[1]):
                pixels[x, y] = (0, 0, 0)
    elif A[1] == B[1]:
        x = A[0]
        y = A[1]
        if 0 <= x <= (pic.size[0]) and 0 <= y <= (pic.size[1]):
            pixels[x, y] = (0, 0, 0)
    else:
        for y in range(B[1], A[1]):
            x = A[0]
            if 0 <= x <= (pic.size[0]) and 0 <= y <= (pic.size[1]):
                pixels[x, y] = (0, 0, 0)

else:
    k = (A[1] - B[1]) / (A[0] - B[0])
    q = B[1] - k * B[0]
    for x in range(B[0], A[0]):
        y = int(k * x + q)
        if 0 <= x < (pic.size[0]) and 0 <= y < (pic.size[1]):
            pixels[x, y] = (0, 0, 0)

pic.save('line.png')