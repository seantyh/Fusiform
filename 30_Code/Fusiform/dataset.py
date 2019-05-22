import torch
from torch.utils.data import Dataset
import numpy as np

def collate_fn(data):
    src, targ = zip(*data)
    
    src_lens = [x.shape[0] for x in src]    
    padded_src = torch.zeros(len(src), max(src_lens), src[0].shape[1])
    for i, src_x in enumerate(src):
        end = src_lens[i]
        padded_src[i, :end, :] = src_x
    targ_batch = torch.stack(targ, dim=0).float()

    return padded_src, targ_batch

class AffectiveDataset(Dataset):
    def __init__(self, ec_space, afflex_data):
        self.data = []
        self.ec = ec_space
        self.rs = np.random.RandomState(32434)
        for idx, row in afflex_data.iterrows():
            lemma = idx
            emotion = row[:5]
            polarity = row[5:]
            if emotion.sum() == 0:
                continue
            self.data.append({
                "lemma": lemma, 
                "emotion": emotion, 
                "polarity": polarity
            })            
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        item = self.data[idx]
        lemma = item["lemma"]
        emotion = item["emotion"]
        polarity = item["polarity"]
        
        ec_tensor = transform(lemma, self.ec)
        emo_tensor = torch.LongTensor(emotion)
        return ec_tensor, emo_tensor
    
def transform(lemma, ec):
    rs = np.random.RandomState(32434)
    ec_vec = []
    for ch in lemma:
        ec_x = ec.get_ec_coeffs(ch)
        if ec_x is None:
            ec_x = rs.randn(ec.get_ec_dim())
        ec_vec.append(ec_x)
    ec_tensor = torch.FloatTensor(ec_vec)
    return ec_tensor
