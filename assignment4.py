'''
    This file contains the template for Assignment4.  For testing it, I will place it
    in a different directory, call the function <first_second_third_mst>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

'''
MST Second MST Third MST
modified by Krustal Algorithm
version = 3.6.5
'''
from collections import defaultdict


class edge:
    def __init__(self, u, v, w, vis):
        '''
        u,v:u is the start vertice and v is the end vertice
        w:w is the weight of edge (u,v)
        vis:vis is a boolean variable which represents visited or not
        '''
        self.u = u
        self.v = v
        self.w = w
        self.visited = vis


def get_edges_from_adjacent(G):
    edges = []
    for i in range(len(G)):
        for j in range(i + 1, len(G)):
            temp = edge(i, j, G[i][j], False)
            edges.append(temp)
    return edges


def get_soreted_edges(edges):
    edges.sort(key=lambda x: x.w)


def find(x, fa):
    if x != fa[x]:
        fa[x] = find(fa[x], fa)
    return fa[x]


def dfs(u, v, mst, visited, path, res, G):
    '''
    to find all the weight of edges in path u2v
    '''
    if u == v:
        res.extend(path[:])
        return
    visited[u] = True
    for val in mst[u]:
        if not visited[val]:
            visited[u]
            path.append(G[u][val])
            dfs(val, v, mst, visited, path, res, G)
            path.pop()
    visited[u] = False
    return res


def sec_w_path(path):
    path.sort(reverse=True)
    return path[1]


def kruskal(edges, n, fa, u2v, mst, max_u2v_dis, G):
    for i in range(n):
        fa[i] = i
        u2v[i].append(i)
    minnum = 0
    sec_min = float('inf')
    thi_min = float('inf')
    k = 0
    for i in range(len(edges)):
        if (k == n - 1):
            break
        x1 = find(edges[i].u, fa)
        x2 = find(edges[i].v, fa)
        if (x1 != x2):  # disconnect -> connect
            minnum += edges[i].w
            k += 1
            edges[i].visited = True
            mst[edges[i].u].append(edges[i].v)
            mst[edges[i].v].append(edges[i].u)
            fa[x1] = x2
            for p_vex in u2v[x1]:
                for q_vex in u2v[x2]:
                    max_u2v_dis[p_vex][q_vex] = max_u2v_dis[q_vex][p_vex] = edges[i].w
            for val in u2v[x1]:
                u2v[x2].append(val)
            for val in u2v[x2]:
                u2v[x1].append(val)
    for i in range(len(edges)):
        if not edges[i].visited:
            if ((edges[i].w + minnum - max_u2v_dis[edges[i].u][edges[i].v]) <= sec_min):
                thi_min = sec_min
                sec_min = (edges[i].w + minnum - max_u2v_dis[edges[i].u][edges[i].v])
            else:
                continue
    for i in range(len(edges)):
        if not edges[i].visited:
            visited = [False] * n
            res = dfs(edges[i].u, edges[i].v, mst, visited, [], [], G)
            thi_min = min(thi_min, edges[i].w - sec_w_path(res) + minnum)

    return [minnum, sec_min, thi_min]

def get_array(input_file_path):
    f = open(input_file_path)
    input = f.read().split("\n")
    n = int(input[0])
    a = list()
    for i in range(1, len(input)):
        tmp = input[i]
        tmp_a = tmp.split(",")
        aa = list()
        for j in range(len(tmp_a)):
            aa.append(int(tmp_a[j]))
        a.append(aa)
    return a, n

def write_result(rst, output_file_path):
    with open(output_file_path, "w") as file:
        for i in rst:
            file.write(str(i) + "\n")


def first_second_third_mst(input_file_path, output_file_path):
    G, n = get_array(input_file_path)
    edges = get_edges_from_adjacent(G)
    get_soreted_edges(edges)
    fa = [0] * n
    u2v = defaultdict(list)  # u2v[u]=[v,...]
    mst = defaultdict(list)
    max_u2v_dis = [[-float('inf')] * n] * n  # the max weight of edges in u2v path
    rst = kruskal(edges, n, fa, u2v, mst, max_u2v_dis, G)
    write_result(rst, output_file_path)
    pass

import time
start_time = time.time()
first_second_third_mst("input3.in", "input3.out")
end_time = time.time()
dtime = end_time - start_time
print("The algorithm run: %.8s s" % dtime)



