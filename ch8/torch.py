import torch 
tensor1 = torch.tensor([1,2,3]) 
tensor2 = torch.tensor([4,5,6]) 
dot = torch.dot(tensor1, tensor2) 
mul = tensor1 * tensor2 
print("Dot Product:", dot) 
print("Element-wise Multiplication:", mul)
