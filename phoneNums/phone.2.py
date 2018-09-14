from pyquery import PyQuery as pq
from lxml import etree
import urllib

fp = open('xa.nums21.txt','r')
vlist1 = [v.strip() for v in fp.readlines()]
fp.close()


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

    mflag = False
    cflag = False
    iflag = False

    city = '西安市'
    isp = '移动'
    for td in tds.items():
        v = td.text()
        if mobile in v:
            mflag = True
        elif city in v:
            cflag = True
        elif isp in v:
            iflag = True
    
    if mflag == False or cflag == False or iflag == False:
        file.write(mobile + '\t' + str(mflag) + '\t' + str(cflag)+ '\t' + str(iflag) + '\n')
    else:
        file.write(mobile + '\t' + 'True' + '\n')

    file.flush()

file = open('xa.findall.txt','w')

for mobile in vlist1:
    find(mobile,file)

file.close()
