import numpy as np
from sklearn.cluster import KMeans
max_snap = 10
cost_table_dyn = []

def timeit(f, *args):
    start = time()
    f(*args)
    duration = time() - start
    return duration

def make_queries(n):
    Q = np.vstack([
        np.random.normal(4, 4, (n, 1)),
        np.random.normal(20, 4, (n, 1)),
        np.random.normal(40, 4, (n, 1)),
        np.random.normal(60, 4, (n, 1)),
        np.random.normal(80, 4, (n, 1)),
        np.random.normal(100, 4, (n, 1))])
    a, b = np.min(Q), np.max(Q)
    Q = np.vstack([Q, np.random.uniform(a, b, (10, 1))])
    Q = Q - np.min(Q)
    return np.squeeze(Q)

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

def save_multiple_query_dyn(max_snapshot,query_size):
	f = open("data/multiQueryDyn.txt","a+")
	f.write(str(query_size)+","+str(cost_table_dyn[max_snapshot][query_size])+'\n')
	f.close()
def save_multiple_query_clustering(snapshot,cost):
    f = open("data/multiQueryCluster.txt","a+")
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
print 'started examining with dynamic programming method '
for i in range(10,200,10):
	queries = sorted(make_queries(i))
	query_size = len(queries)
	cost_table_dyn = np.zeros((max_snap+1,query_size+1))
	init_cost_tables(max_snap,query_size)
	dynamic_cost(queries,max_snap,query_size)
	save_multiple_query_dyn(max_snap,query_size)
	print ' Done!'
# -------------------------------------------------------------------------------
	query_for_clustering = make_2D(queries)
	print 'started examining different clusters ... '
	clusters_list,centroids = cluster(query_for_clustering,max_snap)
	clusters_data = get_cluster_data(query_for_clustering,clusters_list,max_snap)
	overall_cost = calculate_cost(clusters_data)
	save_multiple_query_clustering(query_size,overall_cost)
	print str(i) + " , "+ str(overall_cost)
print 'examination was successful!' 

