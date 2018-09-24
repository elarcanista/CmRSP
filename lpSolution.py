from pulp import *
import solution as sol

def add(graph, key1, key2, item):
    if key1 in graph:
        graph[key1][key2] = item
    else:
        graph[key1] = {key2 : item}

def solve(instance):
    pr = LpProblem("CmRSP",LpMinimize)
    n = instance.n
    m = instance.m
    Q = instance.q
    U_id = list(map(lambda x: x.id, instance.U))
    W_id = list(map(lambda x: x.id, instance.W))
    Vp_id = U_id + W_id
    V_id = Vp_id + [0, n+1]
    E_id = (V_id, V_id)
    A_id = (U_id, U_id + W_id)
    c = lambda i, j: instance.V[i].euclidDistance(instance.V[j])
    d = lambda i, j: instance.V[i].euclidDistance(instance.V[j])
    #variables
    y_var = LpVariable.dicts("y", E_id, 0, None, LpInteger)
    z_var = LpVariable.dicts("z", A_id, 0, 1, LpInteger)
    w_var = LpVariable.dicts("w", W_id, 0, 1, LpInteger)
    k_var = {}
    for i in E_id[0]:
        k_var[i] = {}
        for j in range(i,E_id[1][-1]):
            k_var[i][j] = LpVariable("k_"+str(i)+"_"+str(j), 0, 1, LpInteger)
    #objective function
    pr += lpSum([c(i,j) * (y_var[i][j] + y_var[j][i])
                 for i in E_id[0] for j in range(i,E_id[1][-1]+1)]) /Q + \
          lpSum([d(i,j) * z_var[i][j]
                 for i in A_id[0] for j in A_id[1]]) , \
          "Total Cost of Routing and assignment"
    #constraints
    pr += lpSum([y_var[0][j] for j in Vp_id]) == len(U_id)
    pr += lpSum([y_var[n+1][j] for j in Vp_id]) == m*Q
    pr += lpSum([y_var[j][0] for j in Vp_id]) == m*Q - len(U_id)
    pr += lpSum([y_var[j][n+1] for j in Vp_id]) == 0
    for i in E_id[0]:
        pr += y_var[i][i] == 0
    pr += y_var[0][n+1] == 0
    pr += y_var[n+1][0] == 0
    for j in U_id:
        pr += lpSum([y_var[i][j] + y_var[j][i] for i in V_id]) == 2*Q*z_var[j][j]
    for j in W_id:
        pr += lpSum([y_var[i][j] + y_var[j][i] for i in V_id]) == 2*Q*w_var[j]
    for j in Vp_id:
        pr += lpSum([y_var[i][j] - y_var[j][i] for i in V_id]) == \
              2*lpSum([z_var[i][j] for i in U_id])
    for i in U_id:
        pr += lpSum([z_var[i][j] for j in Vp_id]) == 1
    for i in E_id[0]:
        for j in range(i,E_id[1][-1]):
            pr += y_var[i][j] + y_var[j][i] == k_var[i][j] * Q
    #solve
    pr.writeLP("CmRSP.lp")
    pr.solve(pulp.PULP_CBC_CMD(maxSeconds=300, msg=1, fracGap=0))
    # for v in pr.variables():
    #     print(v.name, "=", v.varValue)
    print(value(pr.objective))
    print("Statu# s:", LpStatus[pr.status])
    w = set()
    for i in w_var:
        if value(w_var[i]) == 1:
            w.add(i)
    y = {}
    for i in y_var:
        for j in y_var[i]:
            if value(y_var[i][j]) != 0:
                add(y, instance.V[i], instance.V[j], value(y_var[i][j]))
                add(y, instance.V[j], instance.V[i], value(y_var[j][i]))
    # for i in y[instance.V[0]]:
    #     if y_var[i.id][n+1] == 0:
    #         add(y, i, instance.V[n+1], 0)
    # for i in y[instance.V[n+1]]:
    #     if y_var[i.id][0] == 0:
    #         add(y, i, instance.V[0], 0)
    z = {}
    for i in z_var:
        for j in z_var[i]:
            if value(z_var[i][j]) == 1.0:
                z[instance.V[i]] = instance.V[j]
    print(w,y,z)
    return sol.Solution(w,y,z,instance)
