
def solution(A, B):
    stream = []
    living = 0

    for fish, dir in zip(A, B):

        # fish going up
        if dir == 0:
            if not stream:
                living +=1
                continue
            else:
                # try to each as many fish as in the down stream stack as possible
                while stream and fish > stream[-1]:
                    stream.pop()

                if not stream:
                    # the fish going up ate all fish going down
                    living +=1 
        else:
            stream.append(fish)
    return living + len(stream)