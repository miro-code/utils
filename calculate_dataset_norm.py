import torchvision
from torchvision import transforms 
import numpy as np
import sys 

def main(dataset):

    ds = getattr(torchvision.datasets, dataset)
    if dataset == "CIFAR10":
        train_set = ds(root="data", train=True, download=True, transform=transforms.ToTensor())
        #print(vars(train_set))
        print(train_set.data.shape)
        print(train_set.data.mean(axis=(0,1,2))/255) #data in its raw form is in[0, 255] not [0,1] float
        print(train_set.data.std(axis=(0,1,2))/255)

    elif dataset == "CIFAR100":
        train_set = ds(root="data", train=True, download=True, transform=transforms.ToTensor())
        #print(vars(train_set))
        print(train_set.data.shape)
        print(np.mean(train_set.data, axis=(0,1,2))/255)
        print(np.std(train_set.data, axis=(0,1,2))/255)

    elif dataset == "MNIST":
        train_set = ds(root="data", train=True, download=True, transform=transforms.ToTensor())
        #print(vars(train_set))
        print(list(train_set.data.size()))
        print(train_set.data.float().mean()/255)
        print(train_set.data.float().std()/255)
    elif dataset == "FashionMNIST":
        train_set = ds(root="data", train=True, download=True, transform=transforms.ToTensor())
        #print(vars(train_set))
        print(list(train_set.data.size()))
        print(train_set.data.float().mean()/255)
        print(train_set.data.float().std()/255)
    
if(__name__ == "__main__"):
    #dataset = sys.argv[1]
    dataset = "FashionMNIST"
    main(dataset)