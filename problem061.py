'''
Created on May 6, 2010

@author: bmann
'''
import sys
import itertools

def is_cyclic(perm):
    #num = str(num)
    one   = perm[0]
    two   = perm[1]
    three = perm[2]
    four  = perm[3]
    five  = perm[4]
    six   = perm[5]
    
    if one[-2:] == two[:2] and two[-2:] == three[:2] and three[-2:] == four[:2] and four[-2:] == five[:2] and five[-2:] == six[:2] and six[-2:] == one[:2]:
        return True
    else:
        return False
        
def triangle(num):
    return num * (num + 1) / 2

def square(num):
    return num ** 2

def pentagonal(num):
    return num * (3 * num - 1) / 2

def hexagonal(num):
    return num * (2 * num - 1)

def heptagonal(num):
    return num * (5 * num - 3) / 2

def octagonal(num):
    return num * (3 * num - 2)

trilist = []
sqlist = []
pentlist = []
hexlist = []
heplist = []
octlist = []

master = [trilist, sqlist, pentlist, hexlist, heplist, octlist]

def is_figurate(num):
    if num in trilist or num in sqlist or num in pentlist or num in hexlist or num in heplist or num in octlist:
        return True
    else:
        return False
    
def find_next_candidates(current, perm):
    i = []
    end = current[-2:]
    for j in range(len(perm)):
        if end == perm[j][:2]:
            i.append(j)
    return i
 
def could_be_cyclic(perm):
    for i in range(len(perm)):
        head_match = False
        tail_match = False
        for j in range(len(perm)):
            if i != j:
                if perm[i][:2] == perm[j][-2:]:
                    head_match = True
                if perm[i][-2:] == perm[j][:2]:
                    tail_match = True
        if head_match == False or tail_match == False:
            return False
    return True
                
def cyclic_gen():
    i = 101010101010
    while i < 1000000000000:
        nst = str(i)
        if len(nst) < 12:
            nst = '0' * (12 - len(nst)) + nst
        cyclic = nst[:2] + nst[2:4] + nst[2:4] + nst[4:6] + nst[4:6] + nst[6:8] + nst[6:8] + nst[8:10] + nst[8:10] + nst[10:12] + nst[10:12] + nst[:2]
        if not is_figurate(cyclic[:4]):
            i += 1000000000
            continue
        if not is_figurate(cyclic[4:8]):
            i += 10000000
            continue
        if not is_figurate(cyclic[8:12]):
            i += 100000
            continue
        if not is_figurate(cyclic[12:16]):
            i += 1000
            continue
        if not is_figurate(cyclic[16:20]):
            i += 10
            continue
        yield cyclic
        i += 1    

def find_next(val):
    result = []
    tail = val[-2:]
    for i in range(len(master)):
        for j in range(len(master[i])):
            pass

def has_one_connection(perm):
    for i in range(len(perm)):
        head_match = False
        tail_match = False
        for j in range(len(perm)):
            if i != j:
                if perm[i][:2] == perm[j][-2:]:
                    return True
                if perm[i][-2:] == perm[j][:2]:
                    return True
    return False
        
def prune(list, others):
    for val in list:
        head = val[:2]
        tail = val[-2:]
        remove = True
        for other_list in others:
            heads = [i[:2] for i in other_list]
            tails = [i[-2:] for i in other_list]
            if head in tails or tail in heads:
                remove = False
                break
        if remove:
            list.remove(val)

if __name__ == '__main__':
    i = 1
    while len(str(triangle(i))) <= 4:
        num = triangle(i)
        if len(str(num)) == 4 and str(num)[2] != '0':
            trilist.append(str(num))
        i += 1
    i = 1
    while len(str(square(i))) <= 4:
        num = square(i)
        if len(str(num)) == 4 and str(num)[2] != '0':
            sqlist.append(str(num))
        i += 1
    i = 1
    while len(str(pentagonal(i))) <= 4:
        num = pentagonal(i)
        if len(str(num)) == 4 and str(num)[2] != '0':
            pentlist.append(str(num))
        i += 1
    i = 1
    while len(str(hexagonal(i))) <= 4:
        num = hexagonal(i)
        if len(str(num)) == 4 and str(num)[2] != '0':
            hexlist.append(str(num))
        i += 1
    i = 1
    while len(str(heptagonal(i))) <= 4:
        num = heptagonal(i)
        if len(str(num)) == 4 and str(num)[2] != '0':
            heplist.append(str(num))
        i += 1
    i = 1
    while len(str(octagonal(i))) <= 4:
        num = octagonal(i)
        if len(str(num)) == 4 and str(num)[2] != '0':
            octlist.append(str(num))
        i += 1
        
    print len(trilist)
    print len(sqlist)
    print len(pentlist)
    print len(hexlist)
    print len(heplist)
    print len(octlist)
    
    prune(trilist, [sqlist, pentlist, hexlist, heplist, octlist])
    prune(sqlist, [trilist, pentlist, hexlist, heplist, octlist])
    prune(pentlist, [trilist, sqlist, hexlist, heplist, octlist])
    prune(hexlist, [trilist, sqlist, pentlist, heplist, octlist])
    prune(heplist, [trilist, sqlist, pentlist, hexlist, octlist])
    prune(octlist, [trilist, sqlist, pentlist, hexlist, heplist])
    print ""
    print len(trilist)
    print len(sqlist)
    print len(pentlist)
    print len(hexlist)
    print len(heplist)
    print len(octlist)
    
    o = 0
    while o < len(octlist):
        h = 0
        while h < len(heplist):
            h2 = 0
            while h2 < len(hexlist):
                p = 0
                while p < len(pentlist):
                    if has_one_connection([str(octlist[o]), str(heplist[h]), str(hexlist[h2]), str(pentlist[p])]):
                        s = 0
                        while s < len(sqlist):
                            t = 0
                            while t < len(trilist):
                                l = [str(trilist[t]), str(sqlist[s]), str(pentlist[p]), str(hexlist[h2]), str(heplist[h]), str(octlist[o])]
                                print l
                                if could_be_cyclic(l):
                                    perms = itertools.permutations(l)
                                    for perm in perms:
                                        if is_cyclic(perm):
                                            print perm
                                            sys.exit(0)
                                t += 1
                            s += 1
                    p += 1
                h2 += 1
            h += 1
        o += 1
    
#    
#    print 'cyclic time'
#    gen = cyclic_gen()
#    while True:
#        a = gen.next()
#        print a
#        if is_cyclic(a):
#            print "found it: %s" % a



#    a = 1
#    while len(str(triangle(a))) <= 4:
#        tri = triangle(a)
#        if len(str(tri)) == 4:
#            b = 1
#            while len(str(square(b))) <= 4:
#                sq = square(b)
#                if len(str(sq)) == 4:
#                    c = 1
#                    while len(str(pentagonal(c))) <= 4:
#                        pent = pentagonal(c)
#                        if len(str(pent)) == 4:
#                            d = 1
#                            while len(str(hexagonal(d))) <= 4:
#                                hex = hexagonal(d)
#                                if len(str(hex)) == 4:
#                                    e = 1
#                                    while len(str(heptagonal(e))) <= 4:
#                                        hep = heptagonal(e)
#                                        if len(str(hep)) == 4:
#                                            f = 1
#                                            while len(str(octagonal(f))) <= 4:
#                                                oct = octagonal(f)
#                                                if len(str(oct)) == 4:
#                                                    l = [str(tri), str(sq), str(pent), str(hex), str(hep), str(oct)]
#                                                    print l
#                                                    if could_be_cyclic(l):
#                                                        perms = itertools.permutations(l)
#                                                        for perm in perms:
#                                                            if is_cyclic(perm):
#                                                                print perm
#                                                                sys.exit(0)
#                                                f += 1
#                                        e += 1
#                                d += 1
#                        c += 1
#                b += 1
#        a += 1



#    i = 100000000000000000000000
#    while i < 999999999999999999999999:
#        if is_cyclic(i):
#            print "cyclic!"
#        i += 1