from pyquery import PyQuery as pq
from lxml import etree
import urllib,time

def find(mobile,file):
    u = 'http://www.ip138.com:8080/search.asp?mobile=' + mobile + '&action=mobile'
    
    while True:
        try:
            doc = pq(url=u,encoding='GBK')
            break
        except :
            print('Error:' + u)
            time.sleep(60)

    '''
        urllib.error.HTTPError

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

    result = list()
    for td in tds.items():
        v = td.text()
        tmp = ''
        for c in v:
            if c not in ' \t\r\n\s\xa0':
                tmp = tmp + c
        result.append(tmp)
    
    file.write(mobile + '\t' + '\t'.join(result) + '\n')
    file.flush()


nums = [
#'134','135','136','137',
#'138','139','147','150',
#'151','152','157','158',
#'159','178','182','183',
'184','187','188','198']

vlist = list()
for num in nums:
    vlist1 = [num + '{:04d}'.format(v) for v in range(10000)]
    vlist = vlist + vlist1

file = open('xa.findinfo.gene.txt','w')

for mobile in vlist:
    find(mobile,file)

file.close()
