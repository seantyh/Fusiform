#pylint: disable=invalid-name
import torch
import torch.nn as nn
import torch.nn.functional as F
from .dataset import transform

class AffectiveEcModel(nn.Module):
    def __init__(self, feat_dim, hidden_dim, out_dim):
        super(AffectiveEcModel, self).__init__()
        self.rnn = nn.GRU(feat_dim, hidden_dim, batch_first=True)
        self.h2o = nn.Linear(hidden_dim, out_dim)

    def forward(self, X):
        ro, _ = self.rnn(X)
        ro = ro[:,-1,:]
        o = torch.sigmoid(self.h2o(ro))
        return o

class AffectiveEcPredictor:
    def __init__(self, model, ec_space):
        self.ec = ec_space
        self.model = model
    
    def predict(self, lemma):
        X = transform(lemma, self.ec).unsqueeze(0)
        ypred = self.model(X)
        return ypred.squeeze().detach().numpy()
    
    def predict_class(self, lemma):
        ypred = self.predict(lemma)
        classes = ["Happy", "Sad", "Fear", "Anger", "Surprise"]
        ret = []
        for pred_x, class_x in zip(ypred, classes):
            if pred_x > 0.5:
                ret.append(class_x)
        return ret