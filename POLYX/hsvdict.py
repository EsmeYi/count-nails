import numpy as np
import collections
 
#define HSV color range
#for example: {color: [min, max]}
#{'red': [array([160,  43,  46]), array([179, 255, 255])]}
 
def getColorList():
    dict = collections.defaultdict(list)
 
    # # black
    # lower_black = np.array([0, 0, 0])
    # upper_black = np.array([180, 255, 46])
    # color_list = []
    # color_list.append(lower_black)
    # color_list.append(upper_black)
    # dict['black'] = color_list
 
    # # gray
    # lower_gray = np.array([0, 0, 46])
    # upper_gray = np.array([180, 43, 220])
    # color_list = []
    # color_list.append(lower_gray)
    # color_list.append(upper_gray)
    # dict['gray']=color_list
 
    # # white
    # lower_white = np.array([0, 0, 221])
    # upper_white = np.array([180, 30, 255])
    # color_list = []
    # color_list.append(lower_white)
    # color_list.append(upper_white)
    # dict['white'] = color_list
 
    # # red
    # lower_red = np.array([156, 43, 46])
    # upper_red = np.array([180, 255, 255])
    # color_list = []
    # color_list.append(lower_red)
    # color_list.append(upper_red)
    # dict['red']=color_list
 
    # # red
    # lower_red = np.array([0, 43, 46])
    # upper_red = np.array([10, 255, 255])
    # color_list = []
    # color_list.append(lower_red)
    # color_list.append(upper_red)
    # dict['red2'] = color_list
 
    # # orange
    # lower_orange = np.array([11, 43, 46])
    # upper_orange = np.array([25, 255, 255])
    # color_list = []
    # color_list.append(lower_orange)
    # color_list.append(upper_orange)
    # dict['orange'] = color_list
 
    # yellow
    lower_yellow = np.array([12, 180, 60])
    upper_yellow = np.array([30, 255, 255])
    color_list = []
    color_list.append(lower_yellow)
    color_list.append(upper_yellow)
    dict['yellow'] = color_list
 
    # green
    lower_green = np.array([35, 100, 60])
    upper_green = np.array([77, 255, 255])
    color_list = []
    color_list.append(lower_green)
    color_list.append(upper_green)
    dict['green'] = color_list
 
    # # cyan-blue
    # lower_cyan = np.array([78, 43, 46])
    # upper_cyan = np.array([99, 255, 255])
    # color_list = []
    # color_list.append(lower_cyan)
    # color_list.append(upper_cyan)
    # dict['cyan'] = color_list
 
    # blue
    lower_blue = np.array([78, 43, 46])
    upper_blue = np.array([124, 255, 255])
    color_list = []
    color_list.append(lower_blue)
    color_list.append(upper_blue)
    dict['blue'] = color_list
 
    # purple
    lower_purple = np.array([125, 43, 46])
    upper_purple = np.array([180, 255, 255])
    color_list = []
    color_list.append(lower_purple)
    color_list.append(upper_purple)
    dict['purple'] = color_list
 
    return dict
 
 
if __name__ == '__main__':
    color_dict = getColorList()
    print(color_dict)
 
    num = len(color_dict)
    print('num=',num)
 
    for d in color_dict:
        print('key=',d)
        print('value=',color_dict[d][1])
