def scaled_number(v,f_min,f_max, t_min, t_max):

    """conver the list of number to their scaled version in the given range this function takes v the value, f_min the
    minimum value, f_max the maximum value in the list, t_min the minimum number to star the scale and t_max the max scale number"""

    return round(t_min + (t_max - t_min) * ((v - f_min) / (f_max - f_min)), 2)