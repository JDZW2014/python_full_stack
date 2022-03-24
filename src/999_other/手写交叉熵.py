import torch
from torch.nn import functional as F
import numpy as np
import math
torch.nn.CrossEntropyLoss


def ce_loss(y_true: np.ndarray, y_pred: np.ndarray, label_num):
    y_pred = np.exp(y_pred)
    y_pred /= np.sum(y_pred, axis=1, keepdims=True)
    y_pred = np.log(y_pred)
    
    one_hot_m = np.identity(label_num)
    y_true = one_hot_m[y_true]
    
    loss = np.sum(y_true * y_pred) / len(y_true)
    return loss

def fc_loss(y_true: np.ndarray, y_pred: np.ndarray, label_num, eps=0.00001):
    pass


def main():
    y_true = np.array([0, 2, 1, 0])
    y_pred = np.array([[0.5, 0.2, 0.3], [0.1, 0.1, 0.8], [0.5, 0.5, 0.0], [0.0, 0.6, 0.4]])
    loss1 = ce_loss(y_true=y_true, y_pred=y_pred, label_num=3)
    
    loss2 = F.cross_entropy(torch.from_numpy(y_pred), torch.from_numpy(y_true))
    pass

main()