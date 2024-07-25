# import torch
# # 创建一个张量
# x = torch.tensor([1.0, 2.03555, 3.4])
# print(x)

# import torch  
# import numpy as np  
# np.set_printoptions(precision=2)  # 设置NumPy打印的浮点数精度为2位    
# x = torch.tensor([1.0, 2.0355, 3.4])  
# print(x.numpy())  # 注意：这里是通过转换为NumPy数组来应用设置的  
# # 或者，如果你只是想打印而不关心NumPy数组，可以直接对x使用字符串格式化  
# print(f"tensor([{','.join(f'{v:.2f}' for v in x.tolist())}])") 

# 使用空格作为分隔符  
words = ['hello', 'world', 'this', 'is', 'a', 'test']  
result = ' '.join(words)  
print(result)  # 输出: hello world this is a test   
# 使用逗号和空格作为分隔符  
numbers = ['1', '2', '3', '4', '5']  
result = ', '.join(numbers)  
print(result)  # 输出: 1, 2, 3, 4, 5  
# 使用换行符作为分隔符，用于创建多行字符串  
lines = ['第一行', '第二行', '第三行']  
result = '\n'.join(lines)  
print(result)  
# 输出:  
# 第一行  
# 第二行  
# 第三行