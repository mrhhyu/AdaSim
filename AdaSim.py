'''
Created on Apr 13, 2021
This is the official implementation of AdaSim applicable to BOTH directed and undirected graphs published in CIKM 2021 
@note: For directed graphs, similarity can be computed based on in-links or out-links
@author: masoud
'''
import numpy as np
import networkx as nx
import math
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize

def compute_AdaSim (graph='', decay_factor=0, iterations=0, alpha_val=1.0,link_type='',GT_path=''):

    if link_type not in {'in-link', 'out-link','none'}:
        print('Link-type must be in-link, out-link, or none ...')
        return        
    print('AdaSim Matrix form Computation is started for: {}\n'.format(graph))   
    #============================================================================================
        # reading graph and computing 'weights' matrix
    #============================================================================================    
    G = nx.read_edgelist(graph, create_using=nx.DiGraph(), nodetype = int)
    nodes = sorted(G.nodes())       # sorted list of all nodes
    adj = nx.adjacency_matrix(G,nodelist=nodes, weight=None)      # V*V adjacency matrix

    print('================================================================================================================================') 
    if link_type == 'in-link':            
        degrees = adj.sum(axis=0).T   # V*1 matrix (a column vector of size V)        
        weights = csr_matrix(1/np.log(degrees+math.e))  # keep weights of nodes; V*1 matrix;
        weight_matrix = csr_matrix(adj.multiply(weights)) # V*V matrix; column i have the weight of i's in-neighbors        
        #============================================================================================
            # similarity computation
        #============================================================================================        
        print('Iteration 1 ....\n')
        adamic_scores = csr_matrix(weight_matrix.T * adj)
        adamic_scores.setdiag(0) ## corresponding to the ∧ opertaor in Equation (12)
        adamic_scores = adamic_scores/np.max(adamic_scores)  # min-max normalization
        result_matrix = csr_matrix(decay_factor*alpha_val*adamic_scores)    
         
        ''' @NOTE: Set diagonal values to one for writing results; since they are NOT used in computing similarity scores, we can skip this line '''        
        result_matrix.setdiag(1) ## set diagonal values to one; it is just for writing results since they are NOT used in computing similarity scores
            
        weight_matrix = normalize(weight_matrix, norm='l1', axis=0) # column normalized weight_matrix    
        for itr in range (2, iterations+1):                            
            print("Iteration "+str(itr)+' .... \n')
            result_matrix.setdiag(0) ## diagonal values are set back to zero; corresponding to the ∧ opertaor in Equation (15)
            result_matrix =  decay_factor * (alpha_val* adamic_scores + (1-alpha_val) * (weight_matrix.T * result_matrix * weight_matrix)) 
            result_matrix.setdiag(1) ## setting back diagonal values to one for writing results, we can skip this line
            
        print('AdaSim Matrix form Computation is done ...')                    
        return result_matrix           

    else: ## applied to both out-link for directed graphs or undirecetd graphs
        degrees = adj.sum(axis=1).T   # 1*V matrix (a row vector of size V)        
        weights = csr_matrix(1/np.log(degrees+math.e))  # keep weights of nodes; 1*V matrix;
        weight_matrix = csr_matrix(adj.multiply(weights)) # V*V matrix; row i have the weight of i's out-links

        #============================================================================================
            # similarity computation
        #============================================================================================        
        print('Iteration 1 ....\n')
        adamic_scores = weight_matrix * adj.T
        adamic_scores.setdiag(0)
        adamic_scores = adamic_scores/np.max(adamic_scores)  # min-max normalization
        result_matrix = decay_factor*alpha_val*adamic_scores
        
        ''' @NOTE: Set diagonal values to one for writing results; since they are NOT used in computing similarity scores, we can skip this line '''                
        result_matrix.setdiag(1)
    
        weight_matrix = normalize(weight_matrix, norm='l1', axis=1) # row normalized weight_matrix    
        for itr in range (2, iterations+1):                            
            print("Iteration "+str(itr)+' .... \n')
            result_matrix.setdiag(0) ## diagonal values are set back to zero; corresponding to the ∧ opertaor in Equation (15)
            result_matrix =  decay_factor * (alpha_val* adamic_scores + (1-alpha_val) * (weight_matrix * result_matrix * weight_matrix.T)) #+ iden_matrix
            result_matrix.setdiag(1) ## setting back diagonal values to one for writing results, we can skip this line

        print('AdaSim Matrix form Computation is done ...')
        return result_matrix
            
