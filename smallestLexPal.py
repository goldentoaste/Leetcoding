from typing import List, Set, Dict, Optional

null = None


def getKeyIdentifier(key: str) -> str:

    mem = [0] * 26

    for s in key:
        mem[ord(s) - 97] += 1

    center = ""
    out = []

    for i, l in enumerate(mem):
        if l % 2 != 0:
            center = chr(i + 97)
            l -= 1

        out.append(chr(i + 97) * (l // 2))

    return "".join(out) + center + "".join(reversed(out))


if __name__ == "__main__":
    print(getKeyIdentifier("zyxxxyz"))
