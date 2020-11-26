import networkx as nx
from node2vec import Node2Vec
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.manifold import TSNE
import community as community_louvain


def deal_emb(graph):
    G = nx.Graph()
    for link in graph['links']:
        source = int(link['source'])
        target = int(link['target'])
        G.add_edge(source, target)
    node2vec = Node2Vec(G, dimensions=64, walk_length=30,
                        num_walks=200, workers=4)
    model = node2vec.fit(window=10, min_count=1, batch_words=4)
    vectors = model.wv.vectors
    anomaly_nodes = anomaly_detectors(vectors)
    projection_nodes = projection(vectors)
    community_nodes = community(G)
    return vectors, anomaly_nodes.tolist(), projection_nodes.tolist(), community_nodes


def anomaly_detectors(X):
    clf = IsolationForest(random_state=0).fit(X)
    anomaly_nodes = np.where(clf.predict(X) == -1)[0]
    return anomaly_nodes


def projection(X, method='tsne'):
    if method == 'tsne':
        X_embedded = TSNE(n_components=2).fit_transform(X)
    return X_embedded


def community(G):
    community_nodes = community_louvain.best_partition(G)
    group_num = max(list(community_nodes.values()))+1
    communities = []
    for i in range(group_num):
        communities.append([])
    for node in community_nodes.keys():
        group = community_nodes[node]
        communities[group].append(node)
    return communities
