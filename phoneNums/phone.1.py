fp1 = open('xa.nums.web1','r')
fp2 = open('xa.nums.mobile','r')

vlist1 = [v.strip() for v in fp1.readlines()]
vlist2 = [v.strip() for v in fp2.readlines()]

vdif12 = [v for v in vlist1 if v not in vlist2]
vdif21 = [v for v in vlist2 if v not in vlist1]
vdif = [v for v in vlist1 if v in vlist2]

fp1.close()
fp2.close()


fp = open('xa.nums.webonly.txt','w')
for li in vdif12:
    fp.write(li+'\n')

fp = open('xa.numsmobileonly.txt','w')
for li in vdif21:
    fp.write(li+'\n')

fp = open('xa.nums.both.txt','w')
for li in vdif:
    fp.write(li+'\n')

fp.close()
