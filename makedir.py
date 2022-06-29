import os


def makedir(data):
    try:
        os.mkdir(f'./results')
    except:
        pass
    try:
        os.mkdir(f'./results/{data}')
    except:
        pass
    try:
        os.mkdir(f'./results/{data}/S')
    except:
        pass
    try:
        os.mkdir(f'./results/{data}/We')
    except:
        pass
    try:
        os.mkdir(f'./results/{data}/ElementsParameters')
    except:
        pass
    for i in range(5):
        try:
            os.mkdir(f'./results/{data}/ElementsParameters/Element{i + 1}')
        except:
            pass
