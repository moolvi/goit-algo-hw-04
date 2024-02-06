import re

def get_cats_info(path):
    employees = []
    try:
        with open(path, encoding='utf-8') as file:
            for row in file.readlines():
                employees += [dict(zip(["id", "name", "age"], re.split('[,\n]', row)))]
        return employees
    
    except FileNotFoundError:
        return None
    
    except ValueError:
        return None
    
    except IndexError:
        return None