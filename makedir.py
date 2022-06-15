import os


def makedir(data):
    try:
        os.mkdir(f'./database')
    except:
        pass
    try:
        os.mkdir(f'./database/{data}')
    except:
        pass
    try:
        os.mkdir(f'./database/{data}/S')
    except:
        pass
    try:
        os.mkdir(f'./database/{data}/We')
    except:
        pass
    try:
        os.mkdir(f'./database/{data}/ElementsParameters')
    except:
        pass
    for i in range(5):
        try:
            os.mkdir(f'./database/{data}/ElementsParameters/Element{i + 1}')
        except:
            pass
