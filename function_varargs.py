def func(a,*numbers,**params):
    print('a is',a)
    #遍历元组中所有项目
    for single_item in numbers:
        print('single_item ',single_item)
    #遍历字典中所有项目
    for firs_part,second_part in params.items():
        print(firs_part, '=', second_part)


func(10,1,3,5,7,9,jack=135,john=133,mary=186)