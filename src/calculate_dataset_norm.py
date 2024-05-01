import torchvision
from torchvision import transforms
import torch
import sys

# Get dataset name from command line arguments
dataset_name = sys.argv[1]

# Fetch the dataset class dynamically from torchvision.datasets
dataset_class = getattr(torchvision.datasets, dataset_name)

# Define a generic transformation, converting images to tensors
transform = transforms.ToTensor()

# Download and load the dataset
train_set = dataset_class(root="data", train=True, download=True, transform=transform)

# Determine whether the data is in PIL Image format or already a tensor
if hasattr(train_set, 'data'):
    # If data is already a tensor (e.g., CIFAR, MNIST)
    data_tensor = train_set.data
else:
    # Convert data to tensor manually if it is in PIL Image format
    # This loop will convert all images in the dataset to tensors and stack them into a single tensor
    data_tensor = torch.stack([transform(img) for img, _ in train_set])

# Check if the tensor is a floating point type and convert if not
if not torch.is_floating_point(data_tensor):
    data_tensor = data_tensor.float()

# Normalize the data tensor by 255 if it is in the range [0, 255]
if data_tensor.max() > 1:
    data_tensor /= 255.0

# Calculate and print size, mean, and std of the dataset
print("Data shape:", data_tensor.shape)
print("Mean of the data:", data_tensor.mean(dim=(0, 1, 2)).tolist())
print("Standard deviation of the data:", data_tensor.std(dim=(0, 1, 2)).tolist())