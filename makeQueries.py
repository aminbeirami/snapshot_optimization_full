import numpy as np
# SNAPSHOT_NO = 10
def make_queries(n):
    Q = np.vstack([
        np.random.normal(4, 4, (n, 1)),
        np.random.normal(20, 4, (n, 1)),
        np.random.normal(40, 4, (n, 1)),
        np.random.normal(60, 4, (n, 1)),
        np.random.normal(80, 4, (n, 1)),
        np.random.normal(100, 4, (n, 1))
        # np.random.normal(120, 4, (n, 1)),
        # np.random.normal(140, 4, (n, 1)),
        # np.random.normal(160, 4, (n, 1)),
        # np.random.normal(180, 4, (n, 1)),
        # np.random.normal(200, 4, (n, 1)),
        # np.random.normal(220, 4, (n, 1)),
        # np.random.normal(240, 4, (n, 1)),
        # np.random.normal(260, 4, (n, 1)),
        # np.random.normal(280, 4, (n, 1)),
        # np.random.normal(300, 4, (n, 1)),
        # np.random.normal(320, 4, (n, 1)),
        # np.random.normal(340, 4, (n, 1)),
        # np.random.normal(360, 4, (n, 1)),
        # np.random.normal(280, 4, (n, 1)),
        # np.random.normal(400, 4, (n, 1)),
        # np.random.normal(420, 4, (n, 1)),
        # np.random.normal(440, 4, (n, 1)),
        # np.random.normal(460, 4, (n, 1)),
        # np.random.normal(480, 4, (n, 1)),
        # np.random.normal(500, 4, (n, 1)),
        # np.random.normal(520, 4, (n, 1)),
        # np.random.normal(540, 4, (n, 1)),
        # np.random.normal(560, 4, (n, 1)),
        # np.random.normal(580, 4, (n, 1)),
        # np.random.normal(600, 4, (n, 1)),
        # np.random.normal(620, 4, (n, 1)),
        # np.random.normal(640, 4, (n, 1)),
        # np.random.normal(660, 4, (n, 1)),
        # np.random.normal(680, 4, (n, 1)),
        # np.random.normal(700, 4, (n, 1)),
        # np.random.normal(720, 4, (n, 1)),
        # np.random.normal(740, 4, (n, 1)),
        # np.random.normal(760, 4, (n, 1)),
        # np.random.normal(780, 4, (n, 1)),
        # np.random.normal(800, 4, (n, 1)),
        # np.random.normal(820, 4, (n, 1)),
        # np.random.normal(840, 4, (n, 1)),
        # np.random.normal(860, 4, (n, 1)),
        # np.random.normal(880, 4, (n, 1)),
        # np.random.normal(900, 4, (n, 1)),
        # np.random.normal(1000, 4, (n, 1)),
        # np.random.normal(1020, 4, (n, 1)),
        # np.random.normal(1040, 4, (n, 1)),
        # np.random.normal(1060, 4, (n, 1)),
        # np.random.normal(1080, 4, (n, 1)),
        # np.random.normal(1100, 4, (n, 1)),
        # np.random.normal(1120, 4, (n, 1)),
        # np.random.normal(1140, 4, (n, 1)),
        # np.random.normal(1160, 4, (n, 1)),
        # np.random.normal(1180, 4, (n, 1)),
        # np.random.normal(1200, 4, (n, 1)),
        # np.random.normal(1220, 4, (n, 1)),
        # np.random.normal(1240, 4, (n, 1)),
        # np.random.normal(1260, 4, (n, 1)),
        # np.random.normal(1280, 4, (n, 1)),
        # np.random.normal(1300, 4, (n, 1)),
        # np.random.normal(1310, 4, (n, 1)),
        # np.random.normal(1320, 4, (n, 1)),
        # np.random.normal(1340, 4, (n, 1)),
        # np.random.normal(1360, 4, (n, 1)),
        # np.random.normal(1380, 4, (n, 1)),
        # np.random.normal(1400, 4, (n, 1)),
        # np.random.normal(1420, 4, (n, 1)),
        # np.random.normal(1440, 4, (n, 1)),
        # np.random.normal(1460, 4, (n, 1)),
        # np.random.normal(1480, 4, (n, 1)),
        # np.random.normal(1500, 4, (n, 1))
        ])
    a, b = np.min(Q), np.max(Q)
    Q = np.vstack([Q, np.random.uniform(a, b, (10, 1))])
    Q = Q - np.min(Q)
    return np.squeeze(Q)

def save_file_queries(Q):
    f = open("data/queries.txt","a+")
    for i in range(len(Q)):
        f.write(str(Q[i])+"\n")
    f.close()

# def save_snap_no():
# 	f = open("data/snap_no.txt","w+")
# 	f.write(str(SNAPSHOT_NO))
# 	f.close()

query_list = make_queries(165)
print len(query_list)
save_file_queries(query_list)
# save_snap_no()
