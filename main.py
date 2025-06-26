from convoulation import convolve3d
print("Initial Commit")
image = [
    [
    [1, 2, 3, 0],
    [0, 1, 2, 3],
    [1, 2, 1, 0],
    [0, 1, 2, 1]
    ]
]

kernel = [
    [
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
    ]
]

output = convolve3d(image, kernel)

print("Fetaure Map:")
for row in output:
    print(row)

