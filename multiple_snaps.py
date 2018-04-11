import numpy as np
from sklearn.cluster import KMeans

cost_table_dyn = []
max_snap = 100

def fetch_queries():
    queries = []
    with open('data/queries.txt') as f:
        for items in f:
            queries.append(float(items.translate(None,'\n')))
    f.close()
    return queries

def make_2D(queries):
	new_array = []
	for i in range(len(queries)):
		new_array.append([queries[i],0])
	return new_array

def calc_single_cost(Q):
    if Q == []:
        return 0
    else:
        cost = 0.0;
        snap_pos = np.median(Q)
        for i in range(len(Q)):
            cost += abs(Q[i] - snap_pos)
        return cost

def init_cost_tables(no_snap,size_queries):
    init_val = -1
    for j in range (no_snap+1):
        for i in range(size_queries+1):
            cost_table_dyn[j][i] = init_val

def calc_cost(Q,cut):
    if cut >0:
        Q = Q[-cut:]
        cost = calc_single_cost(Q)
        return cost
    else:
        return 0

def init_first_row(Q,size_queries):
    for i in range(1,size_queries+1):
        queries = Q[:i]
        cost_table_dyn[1][i] = calc_single_cost(queries)

def dynamic_cost(Q,no_snap,size_queries):
    init_first_row(Q,size_queries)
    for j in range(2,no_snap+1):
        for i in range(1,size_queries+1):
            min_value = np.inf
            for k in range(1,i+1):
                current_cost = cost_table_dyn[j-1][k]+calc_cost(Q[:i],(i-k))
                if current_cost < min_value:
                    min_value = current_cost
            cost_table_dyn[j][i] = min_value
            print str(j)+","+str(i)+" , "+str(min_value)

def elbow(queries,max_snapshot):
	cost = []
	for i in range(1,max_snapshot+1):
		kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
		y_kmeans = kmeans.fit_predict(queries)
		cost.append(kmeans.inertia_)
	return cost

def cluster(queries,n):
    kmeans = KMeans(n_clusters= n, init = 'k-means++',max_iter = 300, n_init = 10, random_state = 0)
    y_kmeans = kmeans.fit_predict(queries)
    return y_kmeans, kmeans.cluster_centers_

def get_cluster_data(queries,clusters,n):
    clusters_data = []
    for s in range(n):
        clusters_data.append([])
    for j in range(n):
        for i in range(len(queries)):
            if clusters[i] == j:
                clusters_data[j].append(queries[i][0])      
    return clusters_data

def save_multiple_snap(max_snapshot,query_size):
	f = open("data/multisnapDyn.txt","a+")
	for i in range(1,max_snapshot+1):
		f.write(str(i)+","+str(cost_table_dyn[i][query_size])+'\n')
	f.close()
def save_multiple_snap_clustering(snapshot,cost):
    f = open("data/multisnapCluster.txt","a+")
    f.write(str(snapshot)+","+str(cost)+"\n")
    f.close()

def calculate_cost(data):
    overall_cost = 0
    for i in range(len(data)):
        snapshot = np.median(data[i])
        cost = 0
        for j in range(len(data[i])):
            single_cost = abs(data[i][j]-snapshot)
            cost += single_cost
        overall_cost+=cost
    return overall_cost


queries = sorted(fetch_queries())
query_size = len(queries)
# -------------------------------------------------------------------------------
print 'started examining with dynamic programming method'
cost_table_dyn = np.zeros((max_snap+1,query_size+1))
init_cost_tables(max_snap,query_size)
dynamic_cost(queries,max_snap,query_size)
save_multiple_snap(max_snap,query_size)
print ' Done!'
# -------------------------------------------------------------------------------
query_for_clustering = make_2D(queries)
elbowing = elbow(query_for_clustering,max_snap)
print 'started examining different clusters ... '
for i in range(1,max_snap+1):
    clusters_list,centroids = cluster(query_for_clustering,i)
    clusters_data = get_cluster_data(query_for_clustering,clusters_list,i)
    overall_cost = calculate_cost(clusters_data)
    save_multiple_snap_clustering(i,overall_cost)
    print str(i) + " , "+ str(overall_cost)
print 'examination was successful!' 