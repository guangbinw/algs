from pyquery import PyQuery as pq
from lxml import etree
import urllib

def find(mobile,file):
    u = 'http://www.ip138.com:8080/search.asp?mobile=' + mobile + '&action=mobile'
    doc = pq(url=u,encoding='GBK')

    '''
        <TR class=tdc bgcolor=#EFF1F3>
            <TD width="138" align="center" noswap>您查询的手机号码段</TD>
            <TD width=* align="center" class=tdc2>1982979 <a href="http://jx.ip138.com/1982979/" target="_blank">测吉凶(<font color="red">新</font>)</a></TD>
        </TR>
        <TR class=tdc bgcolor=#EFF1F3>
            <TD align="center">卡号归属地</td><!-- <td width="138" align="center">卡号归属地</TD> -->
    <TD class="tdc2" align="center">陕西&nbsp;西安市</TD>
        </TR>
    '''

    tds = doc('TD.tdc2')

    file.write(mobile + '\t')
    for td in tds.items():
        v = td.text()
        tmp = ''
        for c in v:
            if c not in ' \t\r\n\s\xa0':
                tmp = tmp + c
        file.write(tmp + '\t')

    file.write('\n')
    file.flush()

fp = open('xa.nums.mobileonly.txt','r')
vlist1 = [v.strip() for v in fp.readlines()]
fp.close()

file = open('xa.findinfo.mobileonly.txt','w')

for mobile in vlist1:
    find(mobile,file)

file.close()


fp = open('xa.nums.webonly.txt','r')
vlist1 = [v.strip() for v in fp.readlines()]
fp.close()

file = open('xa.findinfo.webonly.txt','w')

for mobile in vlist1:
    find(mobile,file)

file.close()

fp = open('xa.nums.both.txt','r')
vlist1 = [v.strip() for v in fp.readlines()]
fp.close()

file = open('xa.findinfo.both.txt','w')

for mobile in vlist1:
    find(mobile,file)

file.close()
