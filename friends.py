from collections import deque

class Friends:
    def __init__(self):
        self.parent = []
        self.restrictions = []

    def friend_requests(self, n, restrictions, requests):
        self.parent = list(range(n))
        self.restrictions = [set() for _ in range(n)]

        for restriction in restrictions:
            self.restrictions[restriction[0]].add(restriction[1])
            self.restrictions[restriction[1]].add(restriction[0])

        result = []
        for request in requests:
            if self.can_be_friends(request[0], request[1]):
                self.union(request[0], request[1])
                result.append("approved")
            else:
                result.append("denied")

        return result

    def can_be_friends(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return True

        queue = deque([root_x])
        visited = {root_x}

        while queue:
            current = queue.popleft()
            if root_y in self.restrictions[current]:
                return False

            for neighbor in range(len(self.parent)):
                if self.find(neighbor) == current and neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

        return True

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

if __name__ == "__main__":
    solution = Friends()

    # Example 1
    n1 = 3
    restrictions1 = [[0, 1]]
    requests1 = [[0, 2], [2, 1]]
    print(solution.friend_requests(n1, restrictions1, requests1))

    # Example 2
    n2 = 5
    restrictions2 = [[0, 1], [1, 2], [2, 3]]
    requests2 = [[0, 4], [1, 2], [3, 1], [3, 4]]
    print(solution.friend_requests(n2, restrictions2, requests2))
