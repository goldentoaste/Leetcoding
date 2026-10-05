from typing import List, Set, Dict, Optional, Tuple

T = List[
    bool
]


class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """

        out = []
        mem = set()  # track states seen already.


        if turnedOn == 0:
            return ["0:00"]


        def rebuildBinaryNumber(bits: List[bool]):
            out = 0

            for bit in bits:
                out = out << 1
                if bit: 
                    out += 1
            
            return out

        def formatTime( bitsUsed: T):
            hour = rebuildBinaryNumber(bitsUsed[:4])
            seconds = rebuildBinaryNumber(bitsUsed[4:])

            if hour > 11 or seconds > 59:
                return None

            return str(hour) + ":" + str(seconds).rjust(2, '0')

        def getDigits(bitsRemain: int, bitsUsed: T):
            ident = (bitsRemain, tuple(bitsUsed))
            if ident in mem:
                return
            
            if bitsRemain == 0:
                formattedTime = formatTime( bitsUsed )
                if formattedTime:
                    out.append(formattedTime)
                mem.add(ident)

            for idx, bit in enumerate( bitsUsed):
                if not bit:
                    # change states
                    bitsUsed[idx] = True
                    getDigits(bitsRemain - 1, bitsUsed)

                    # revert
                    bitsUsed[idx] = False

            mem.add(ident)
            

        getDigits(turnedOn, [False,False,False,False, False,False,False,False,False,False,])

        return out

if __name__ == "__main__":
    o = Solution()
    for x in o.readBinaryWatch(2):
        print(x)
