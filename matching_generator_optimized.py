import itertools
matching = ""
n = 1
k = 0

def to_base_4(n):
    s = ""
    while n:
        s = str(n % 4) + s
        n //= 4
    return s

def naive_intra_consistency():
    if matching.count('3') != matching.count('1'):
        return False
    return True

def intra_consistency_outer():
    for iN in range(0, n):
        if matching[iN] == '0':
            if iN == 0:
                if matching[(iN + 1)] == '0':
                    # print("first node")
                    # print("first layer")
                    # print("right")
                    # print("unoccupied")
                    return False
                if matching[(n - 1)] == '0':
                    # print("first node")
                    # print("first layer")
                    # print("left")
                    # print("unoccupied")
                    return False
            elif iN == n-1:
                if matching[0] == '0':
                    # print("last node")
                    # print("first layer")
                    # print("right")
                    # print("unoccupied")
                    return False
                if matching[iN - 1] == '0':
                    # print("last node")
                    # print("first layer")
                    # print("left")
                    # print("unoccupied")
                    return False
            else:
                if matching[(iN + 1)] == '0':
                    # print("first layer")
                    # print("right")
                    # print("unoccupied")
                    return False
                if matching[(iN - 1)] == '0':
                    # print("first layer")
                    # print("left")
                    # print("unoccupied")
                    return False
        elif matching[iN] == '3':
            if iN == 0:
                if matching[n - 1] != '1':
                    # print("first node")
                    # print("first layer")
                    # print("left")
                    # print("inconsistent")
                    return False
            else:
                if matching[iN - 1] != '1':
                    # print("first layer")
                    # print("left")
                    # print("inconsistent")
                    return False

        elif matching[iN] == '1':
            if iN == n - 1:
                if matching[0] != '3':
                    # print("last node")
                    # print("first layer")
                    # print("right")
                    # print("inconsistent")
                    return False
            else:
                if matching[iN + 1] != '3':
                    # print("first layer")
                    # print("right")
                    # print("inconsistent")
                    return False
    return True

def intra_consistency_inner():
    for iN in range(0, 2*n):
        if matching[iN] == '0':
            if iN == 0:
                if matching[(iN + 1)] == '0':
                    # print("first node")
                    # print("first layer")
                    # print("right")
                    # print("unoccupied")
                    return False
                if matching[((2*n) - 1)] == '0':
                    # print("first node")
                    # print("first layer")
                    # print("left")
                    # print("unoccupied")
                    return False
            elif iN == (2*n)-1:
                if matching[0] == '0':
                    # print("last node")
                    # print("first layer")
                    # print("right")
                    # print("unoccupied")
                    return False
                if matching[iN - 1] == '0':
                    # print("last node")
                    # print("first layer")
                    # print("left")
                    # print("unoccupied")
                    return False
            else:
                if matching[(iN + 1)] == '0':
                    # print("first layer")
                    # print("right")
                    # print("unoccupied")
                    return False
                if matching[(iN - 1)] == '0':
                    # print("first layer")
                    # print("left")
                    # print("unoccupied")
                    return False
        elif matching[iN] == '3':
            if iN == 0:
                if matching[(2*n) - 1] != '1':
                    # print("first node")
                    # print("first layer")
                    # print("left")
                    # print("inconsistent")
                    return False
            else:
                if matching[iN - 1] != '1':
                    # print("first layer")
                    # print("left")
                    # print("inconsistent")
                    return False

        elif matching[iN] == '1':
            if iN == (2*n) - 1:
                if matching[0] != '3':
                    # print("last node")
                    # print("first layer")
                    # print("right")
                    # print("inconsistent")
                    return False
            else:
                if matching[iN + 1] != '3':
                    # print("first layer")
                    # print("right")
                    # print("inconsistent")
                    return False
    return True

def naive_inter_consistency():
    if matching.count('2') % 2 != 0:
        return False
    return True

def inter_consistency():
    for iK in range(1, k+2):
        for iN in range(0, 2*n):
            if matching[((2 * n) * (iK)) + iN] == '0':
                if iK % 2 == 1:
                    if iN % 2 == 1:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] == '0':
                                # print("inter")
                                # print("unoccupied")
                                return False

                    else:
                        if iK != 1:
                            if matching[(((2 * n) * (iK - 1)) + iN)] == '0':
                                # print("inter")
                                # print("unoccupied")
                                return False
                else:
                    if iN % 2 == 1:
                        if matching[(((2 * n) * (iK - 1)) + iN)] == '0':
                            # print("inter")
                            # print("unoccupied")
                            return False
                    else:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] == '0':
                                # print("inter")
                                # print("unoccupied")
                                return False
            elif matching[((2 * n) * (iK)) + iN] == '2':
                if iK % 2 == 1:
                    if iN % 2 == 1:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] != '2':
                                # print("inter")
                                # print("inconsistent")
                                return False
                        else:
                            if matching[((2 * n) * (iK + 1)) + int((iN - 1)/2)] != '2':
                                # print("inter")
                                # print("inconsistent")
                                return False

                    else:
                        if iK != 1:
                            if matching[(((2 * n) * (iK - 1)) + iN)] != '2':
                                # print("inter")
                                # print("inconsistent")
                                return False
                        else:
                            if matching[int(iN/2)] != '2':
                                # print("inter")
                                # print("inconsistent")
                                return False  

                else:
                    if iN % 2 == 1:
                        if matching[(((2 * n) * (iK - 1)) + iN)] != '2':
                            # print("inter")
                            # print("inconsistent")
                            return False
                    else:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] != '2':
                                # print("inter")
                                # print("inconsistent")
                                return False
                        else:
                            if matching[((2*n) + (iK + 1 )) + int(iN/2)] != '2':
                                # print("inter")
                                # print("inconsistent")
                                return False
            
    for iN in range(0, n):
        if matching[iN] == '0':
            if matching[(2*n) + (2*iN)] == '0':
                # print("first layer")
                # print("inter")
                # print("unoccupied")
                return False
        elif matching[iN] == '2':
            if matching[(2*n) + (2*iN)] != '2':
                # print("first layer")
                # print("inter")
                # print("inconsistent")
                return False
        if matching[((2*n)*(k+2)) + iN] == '0':
            if k%2 == 1:
                if matching[(((k + 2 - 1) * (2 * n)) + (2 * iN))] == '0':
                    # print("last layer")
                    # print("inter")
                    # print("onccupied")
                    return False
            else:
                if matching[(((k + 2 - 1) * (2 * n)) + (2 * iN) + 1)] == '0':
                    # print("last layer")
                    # print("inter")
                    # print("onccupied")
                    return False

        elif matching[((2 * n) * (k + 2)) + iN] == '2':
            if k%2 == 1:
                if matching[(((k + 2 - 1) * (2 * n)) + (2 * iN))] != '2':
                    # print("last layer")
                    # print("inter")
                    # print("inconsistenst")
                    return False
            else:
                if matching[(((k + 2 - 1) * (2 * n)) + ((2 * iN) + 1))] != '2':
                    # print("last layer")
                    # print("inter")
                    # print("inconsistenst")
                    return False
        
    return True

def guess_generator_outer():
    beg_chunk = 4 ** (n-2)
    end_chunk = 4 ** n
    guess_idx=0
    for i in range(beg_chunk, end_chunk):
        if guess_idx == 1000:
            break
        guess_chunk = to_base_4(i)
        guess_chunk = '{:>0{number}s}'.format(guess_chunk, number=n)
        global matching
        matching = guess_chunk
        if naive_intra_consistency() and intra_consistency_outer():
            guess_idx+=1
            yield guess_chunk

#The problem here is only first guesses are seen
#You have two options:
#1)Instead of using range as a generator, use a list
# of that range and shuffle it using random.shuffle
#2)Change the direction of your iteration (e.g. to -1)
def guess_generator_inner():
    beg_chunk = 4 ** ((2*n) - 2)
    end_chunk = 4 ** (2*n)
    guess_idx=0
    for i in range(beg_chunk, end_chunk,1):
        if guess_idx == 1000:
            break
        guess_chunk = to_base_4(i)
        guess_chunk = '{:>0{number}s}'.format(guess_chunk, number=2*n)
        global matching
        matching = guess_chunk
        if naive_intra_consistency() and intra_consistency_inner():
            print(guess_chunk)
            guess_idx+=1
            yield guess_chunk

def guess_generator_first():
    outer_it = guess_generator_outer()
    for guess in outer_it:
        yield guess + ''.zfill(n)

def concat_inner_chunks(valid_inner_chunks):
    for idx, g in enumerate(itertools.product(valid_inner_chunks, repeat=k+1)):
        if idx == 10000:
            break
        print(f'concat{g}')
        yield g
    
def product(valid_first_chunks, concated_inner_chunks, valid_outer_chunks):
    for g in itertools.product(valid_first_chunks,concated_inner_chunks,valid_outer_chunks):
        yield g

def guess_generator():
    valid_outer_chunks = guess_generator_outer()
    valid_inner_chunks = guess_generator_inner()
    valid_first_chunks = guess_generator_first()
    concated_inner_chunks = concat_inner_chunks(valid_inner_chunks)
    guesses = product(valid_first_chunks, concated_inner_chunks, valid_outer_chunks)
    for guess in guesses:
        print(f'guess{guess}')
        global matching
        matching = guess[0]
        for chunk in guess[1]:
            matching += chunk
        matching += guess[2]
        if naive_inter_consistency() and inter_consistency():
            #print(matching)
            size = matching.count('1') + (matching.count('2')/2)
            print("the size of the matching is: {}".format(size) )
            break
n = int(input("please enter the number of cycle nodes of m-barrel fullerene graph "))
k = int(input("please enter the number of layers of m-barrel fullerene graph "))
guess_generator()