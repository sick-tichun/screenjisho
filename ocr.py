import easyocr
reader = easyocr.Reader(['ja'], gpu=True)
from jamdict import Jamdict
jam = Jamdict()
import re
import subprocess



#trippyred = ['^、-〿぀-ゟ゠-ヿ＀-￯一-龯\r\n\b']

def read(path):
    try:
        text = reader.readtext(path, detail=0)[0]
        print('befrore re: ' + text)
        text = re.sub(r"[^、-〿぀-ゟ゠-ヿ＀-￯一-龯]", '', text)
        print('after re: '+ text)
        result = jam.lookup(text)
        print(result)
        for word in result.entries:
            print(word + '\n')
    except:
        return






#test = reader.readtext('piss.png', detail=0)
#print(test)
#print(re.sub(r"[^、-〿぀-ゟ゠-ヿ＀-￯一-龯]", '', test[0]))