import numpy as np

class CharacterSpace:
    def __init__(self, cv_itos, cv_stoi, cv_vectors, n_components=100):
        self.n_components = n_components        
        self.cv_dist = self.build_index(cv_vectors, n_components)
        self.stoi = cv_stoi
        self.itos = cv_itos        

    def build_index(self, cv_vectors, k):
        cv_k = cv_vectors[:,:k]
        cv_kc = cv_k - cv_k.mean(1)[:, np.newaxis]
        cv_kcn = cv_kc / np.sqrt(np.diag(np.dot(cv_kc, cv_kc.transpose())))[:, np.newaxis]
        cv_dist = np.dot(cv_kcn, cv_kcn.transpose())
        return cv_dist
    
    def most_similar(self, char):
        cv_dist = self.cv_dist
        stoi = self.stoi
        itos = self.itos
        neighbors = np.argsort(-cv_dist[stoi[char], :])[:20]
        similars = [itos[ch_i] for ch_i  in neighbors]
        return similars

