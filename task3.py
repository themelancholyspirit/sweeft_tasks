
class Bomberman:

    def __init__(self, r, c, n):
        self.r = r
        self.c = c
        self.n = n
        self._grid = self._construct_grid(self.r)

    def _construct_grid(self, r):
        grid = []
        
        for _ in range(r):
            row = list(input().strip())
            grid.append(row)
        
        return grid
    
    @staticmethod
    def set(x, y, grid):
        if 0 <= x < r and 0 <= y < c:
            grid[x][y] = '.'
    
    def run(self):
        if self.n == 1:
            return self._grid
        
        if self.n % 2 == 0:
            return ['O' * self.c for _ in range(self.r)]
        
        self.n //= 2

        for _ in range((self.n+1) % 2 + 1):
            new_grid = [['O'] * self.c for _ in range(self.r)]

            for x in range(self.r):
                for y in range(self.c):
                    if self._grid[x][y] == 'O':
                        for i, j in zip((0,0,0,1,-1), (0,-1,1,0,0)):
                            Bomberman.set(x+i, y+j, new_grid)
            
            self._grid = new_grid
        
        return [''.join(x) for x in self._grid]


r, c, n = list(map(int, input().split()))
    
bomber_man = Bomberman(r, c, n)
    
print(); print('\n'.join(row for row in bomber_man.run()))