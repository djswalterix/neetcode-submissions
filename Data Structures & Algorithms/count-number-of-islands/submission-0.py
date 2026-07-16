class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        seen = set()
        count = 0

        def flood(r, c):
            # base cases: out of bounds, water, or already seen
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0" or (r, c) in seen:
                return
            seen.add((r, c))
            # walk the 4 neighbors
            flood(r+1,c)
            flood(r-1,c)
            flood(r,c-1)
            flood(r,c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in seen:
                    count+=1          # what happens when you find a new blob?
                    flood(r,c)

        return count