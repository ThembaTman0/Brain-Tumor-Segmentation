import numpy as np

class PrincipalComponentAnalysis:
    def __init__(self,data):
        self.data=data
        self.mu = np.mean(self.data,axis=0)
        self.p, self.e = self.pca()
        
    #returns eigen values
    def pca(self):
        c=np.cov(self.data.T)
        eigen_values,eigen_vectors=np.linalg.eig(c)
        #sort from highest to lowest
        idx=np.argsort(eigen_values)[::-1]
        eigen_values=eigen_values[idx]
        eigen_vectors=eigen_vectors[:,idx]
        return eigen_vectors,eigen_values

    #projects data to new subspace    
    def projection(self,data):
        #projection
        x=data-self.mu
        return x@self.p

    def d_principal_components(self,data,d):
        w=self.projection(data)
        w=w[:,:d]
        return w

    def d_rank_approximation(self,data,d): 
        w=self.projection(data)
        w=w[:,:d]
        p=self.p[:,:d]
        x_hat=np.dot(w,p.T)+self.mu    
        return x_hat

    def variation(self,delta):
        e = self.e
        d=np.cumsum(e)/np.sum(e)

        idx=np.where(d>delta)

        return np.min(idx)

    def variance_contributions(self):
        e = self.e
        v=e/np.sum(e)
        return v
