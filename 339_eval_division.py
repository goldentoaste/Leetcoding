from collections import defaultdict
from typing import List, Set, Dict, Optional, Tuple
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        mem : Dict[str, Dict[str, float]] = defaultdict(dict)

        for (numer, denom), ratio in zip(equations, values):
            mem[numer][denom] = ratio
            mem[denom][numer] = 1/ratio
        out = [] # put query results here.

        for source, target in queries:
            if source == target and source in mem:
                out.append(1)
                continue
            
            queue : List[Tuple[str, float]] = [(source, 1)]
            found = False
            visited = set()
            while queue:
                temp = []
                for name, val in queue:
                    if name in visited or name not in mem:
                        continue
                    visited.add(name)

                    denoms = mem[name]
                    if target in denoms:
                        out.append(val * denoms[target])
                        found = True
                        break
                    else:
                        temp.extend([(a, b * val) for a, b in denoms.items()])
                queue = temp
                if found:
                    break
            else:
                out.append(-1)

        return out



if __name__ == "__main__":
    o = Solution()
    print(o.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))