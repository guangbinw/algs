from pyquery import PyQuery as pq
from lxml import etree
import urllib

nums = [
'134',
'135',
'136',
'137',
'138',
'139',
'147',
'150',
'151',
'152',
'157',
'158',
'159',
'178',
'182',
'183',
'184',
'187',
'188',
'198']

u = 'http://www.diaosiso.com/mobile_number/shanxi_/373.html'
doc = pq(url=u)

'''
<div class="container">
<ul>
<li class="m_num">1300290</li><li class="m_num">1300291</li></ul>
</div>
'''
#lis = doc('li .m_num')
lis = doc('li')

fp = open('xa.nums.web1','w')

for li in lis.items():
    v = li.text()
    vh = v[:3]
    if vh in nums:
        fp.write(v+'\n')

fp.close()
