
def convolve3d(image, kernel):
     C = len(image)           # Number of channels (3 for RGB)
     H = len(image[0])        # Height
     W = len(image[0][0])     # Width
     kH = len(kernel[0])      # Kernel height
     kW = len(kernel[0][0])   # Kernel width

     out_H = H - kH + 1
     out_W = W - kW + 1

     output = [[0 for _ in range(out_W)] for _ in range(out_H)]

     for i in range(out_H):
         for j in range(out_W):
             val = 0
             for c in range(C):
                 for m in range(kH):
                     for n in range(kW):
                         val += image[c][i + m][j + n] * kernel[c][m][n]
             output[i][j] = val
     return output    



