import torch

import time

import numpy as np

print("Cuda Availability:",torch.cuda.is_available())



a = torch.tensor([[1.,2.],[3.,4.]])

b = torch.tensor([[5.,6.],[7.,8.]])


a1 = a.cuda()
b1 = b.cuda()

# a2 = a.to('cuda')

# b2 = b.to('cuda')


start_time = time.time()

c = torch.matmul(a1,b1)



print("Matrix Multiplication on GPU:",time.time()-start_time,"Seconds","device:",c.device)

c1 = c.to('cpu')

print("after Multiplication:",c1)
print("Transpose",np.transpose(c1))
