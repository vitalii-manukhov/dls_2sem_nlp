import numpy as np

arr_1 = [1, 2, 3, 4, 5]
arr_1_np = np.array(arr_1)
result = np.sum([arr_1_np, [0] + arr_1[:-1]], axis=0)
print(result)