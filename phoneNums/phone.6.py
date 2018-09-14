import json

vlist = list()

fp1 = open('xa.findinfo.web.txt','r',encoding='utf8')
fp2 = open('xa.findinfo.join.txt','r',encoding='utf8')

webs = fp1.readlines()
joins = fp2.readlines()

fp1.close()
fp2.close()

wmap = dict()
for l in webs:
    vals = l.split()
    wmap[vals[0]] = vals

jmap = dict()
for l in joins:
    vals = l.split()
    jmap[vals[0]] = vals

wmj = list()
for w,v in wmap.items():
    if w not in jmap:
        wmj.append(v)

jmw = list()
for w,v in jmap.items():
    if w not in wmap:
        jmw.append(v)

fp = open('webonly.txt','w')
for w in wmj:
    fp.write('\t'.join(w) + '\n')

fp.close()

'''
fp = open('jonly.txt','w')
json.dump(jmw,fp)
fp.close()
'''
