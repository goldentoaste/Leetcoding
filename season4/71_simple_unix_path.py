
from typing import List, Set, Dict, Optional
null = None



class Solution:
    def simplifyPath(self, path: str) -> str:
        items = [item for item in path.split('/') if item != ""]

        # assume valid
        acc = []
        for item in items:
            if item == '.':
                continue
            if item == '..':
                if acc: # ignore illegal to parent
                    acc.pop()
                continue
            acc.append(item)

        return f'/{"/".join(acc)}'

if __name__ == "__main__":
    o = Solution()
    print(o.simplifyPath("/home/user/Documents/../Pictures")) # "/home/user/Pictures"