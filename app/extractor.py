import re
import logging
logger = logging.getLogger(__name__)

def reader(lines):
    """[simple fuction to parase the log format]
    
    Arguments:
        lines {[list]} -- [all lines from log]
    
    Returns:
      final_dict[dict] -- [parased log in a dict format]
    """
    if len(lines)!=0:
        r = re.compile(r'[^\W\d_]', re.U)
        r2 = re.compile(r'[^\W]', re.U)
        final_ls = []
        #lines = file.readlines()
        for line in lines:
            line = line.decode('utf_8') ##Since flask recive in bytes
            if ('ENTER' in line) or ('EXIT' in line):
                l = line.split(":")
                if len(l)==3:
                    result = {}
                    if 'ENTER' in l[0]:
                        result["operation"] = str('ENTRY')
                    else:
                        result["operation"] = str('EXIT')
                    result["filename"] = str(l[1].strip())
                    l2 = ' '.join(l[2].split())
                    result["line_number"] = int(l2.split(" ")[0])
                    if (((r.match(l2.split(" ")[1].strip()[0])) or (l2.split(" ")[1].strip()[0]=="_")) and  
                    (r2.match(l2.split(" ")[1].strip()[-1]) or (l2.split(" ")[1].strip()[-1]=="_"))):
                        result["name"] = l2.split(" ")[1].strip()
                    else:
                        result["name"] = "anonymous"
                    final_ls.append(result)
                else:
                    logger.error("Please check the Format of the Log,Given Format isnt supported")
        final_dct = {"result":final_ls}
    else:
        logger.error('Zero length list has been entered')
    return final_dct