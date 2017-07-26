from . import links

def write_file_single(eps_num, file_name):
    with open(file_name, 'w') as f :
        res = links.single_eps(eps_num)
        f.write(res)

def write_file_range(start, end, file_name):
    res = links.range_eps(start, end)
    with open(file_name, 'w') as f :
        for n, i in res.items():
            f.write(''.join([str(n), ' ', i, '\n']))
