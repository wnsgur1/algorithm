import sys
input = sys.stdin.readline  # 입출력 속도 최적화를 위해 sys.stdin.readline 사용

def _find(a):
    # 경로 압축 최적화: 재귀적으로 루트 노드 찾으면서
    # par[a] = _find(par[a])를 사용해서 각 노드를 직접 루트에 연결
    # 원래 코드에서는 return _find(par[a])라서 불필요한 재귀 호출이 생길 수 있었음
    if par[a] != a:
        par[a] = _find(par[a])  # 바로 루트에 연결해서 경로 압축
    return par[a]

def _union(a, b):
    # 집합 병합을 위해 _find 호출해서 각 노드의 루트를 찾음
    a = _find(a)
    b = _find(b)

    if a == b:
        return  # 같은 집합에 속하면 병합할 필요 없음

    # Union by Rank: 트리 깊이가 낮은 쪽을 깊이가 높은 쪽에 병합
    if rank[a] < rank[b]:
        par[a] = b  # rank[b]가 더 크니까 a의 부모를 b로 설정
    elif rank[a] > rank[b]:
        par[b] = a  # rank[a]가 더 크니까 b의 부모를 a로 설정
    else:
        par[b] = a  # rank[a]랑 rank[b]가 같으면 b를 a에 병합
        rank[a] += 1  # 같은 깊이 트리 병합 후 rank[a]를 1 증가
    # 원래 코드에서 마지막에 par[b] = a가 중복으로 있어서 비효율적이었음

if __name__ == "__main__":
    n, m = map(int, input().split())
    rank = [0 for _ in range(n + 1)]  # 트리 높이 기록하는 rank 배열
    par = [i for i in range(n + 1)]   # 각 노드의 부모를 자기 자신으로 초기화

    results = []
    for _ in range(m):
        x, a, b = map(int, input().split())

        if x == 0:
            # 0 a b: a와 b가 속한 집합을 병합
            _union(a, b)
        else:
            # 1 a b: a와 b가 같은 집합에 있는지 확인
            if _find(a) == _find(b):
                results.append("YES")
            else:
                results.append("NO")
    
    # 결과를 한 번에 출력해서 출력 속도 개선
    print("\n".join(results))
