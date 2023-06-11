def element_at(my_list, idx):
    i = my_list[idx]
    x = None
    if idx < 0 or idx > len(my_list):
        return(x)
    else:
        return(i)
