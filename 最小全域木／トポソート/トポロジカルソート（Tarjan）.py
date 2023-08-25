def TarjanTopo(V, edges):
  def dfs(v):
    if visited[v] == 1:
      return 
    elif visited[v] == 0:
      visited[v] = 1 # 処理待ちにする
      for to_v in outedge[v]: 
        dfs(to_v)
      # 再帰
      visited[v] = 2 # 処理済にする
      # 再帰が終わったら，帰りがけにソート済の先頭に追加 
      sorted_g.appendleft(v)
    
  # ノードをすでに見たかどうかを格納する配列 # 0:未訪問，1:処理待ち，2:処理済
  visited = [0] * V
  outedge = [[] for _ in range (V)]

  for e in edges:
    outedge[e[0]].append(e[1]) 
    
  sorted_g = deque()
  # 全てのノードをチェックする 
  
  for i in range(V): 
    dfs(i)
  
  return sorted_g
  
