#____1____Solution
#import re

def get_cats_info(path):
    employees = []
    try:
        with open(path, encoding='utf-8') as file:
            
            #____1____Solution
            #for row in file.readlines():
                #employees += [dict(zip(["id", "name", "age"], re.split('[,\n]', row)))]
            
            #____3____Solution
            #for row in file.read().split('\n'):
                #employees += [dict(zip(["id", "name", "age"], row.split(',')))]
            
            #____2____Solution
            key_lists = ["id", "name", "age"]
            for row in file.read().split('\n'):
                row = row.split(',')
                employees +=[{key_lists[i]:row[i] for i in range(min(len(key_lists),len(row)))}]
        return employees
    
    except FileNotFoundError:
        return None
    
    except ValueError:
        return None
    
    except IndexError:
        return None