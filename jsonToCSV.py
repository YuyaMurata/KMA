import ijson
import codecs
import tracemalloc

path = "C:/Users/zz17390/Documents/NetBeansProjects/KomatsuAnalyze/json/"
kisy = "syaryo_obj_PC200_form.json"

f = codecs.open(path+kisy, encoding='utf8')

for prefix, event, value in ijson.parse(f, ):
        if '顧客' in prefix:
            print(prefix,value)