
#function solver formatter to time it
def solver_functionator(solver_fun_input):
#    formatted_solver_fun_list=[]
#    loop_counter = 1
    #adding gen_returns part to not nest f string
    if " " not in solver_fun_input:
        temp_1fun_string=solver_fun_input+'(*gen_returns)'
        fun_list=[]
        fun_list.append(temp_1fun_string)
    else:
        fun_list=solver_fun_input.split()
        for i in range(len(fun_list)):
            fun_list[i]=fun_list[i]+'(*gen_returns)'
    return fun_list

#finishing formatting solver functions to add them to text file
#    for element in fun_list:
#        formatted_solver_fun_list.append(f'''print('Time of function #{loop_counter}: ' + timeit.timeit('{element}', number=10000))''')
#        loop_counter += 1
#    return formatted_solver_fun_list


#Initial UI
def inputer():
    print('\nPlease type in what modules to import.')
    print('If there is more than one, type them with a comma and space.')
    print('Examples:\nrandom \nrandom, os\n')
    import_modules=input()
    print('\nPlease type in the problem generating function (with module. prefix)')
    print('Example:\ntwo_sum.generator()\n')
    problem_gen=input()
    print('\nPlease type in all the solution functions you would like to time.')
    print('These will be seperated with a space and no proceeding(), including module. prefix')
    print('If you type multiple functions they will be timed according to the order they are inputed here.')
    print('Example:\ntwo_sum.BIG_O\ntwo_sum.hashtable two_sum.BIG_O\n')
    solution_functions=input()
    print('\nPlease type in desired sample size, int only:')
    sample_size = input()
    sample_size = [i for i in sample_size if i.isdigit()]
    sample_size = ''.join(sample_size)
    return import_modules, problem_gen, solution_functions, sample_size


def de_functionator(gend_fx):
    part=gend_fx.partition('(')
    part=list(part)
    part[0]=part[0]+'()'
    return part[0]


def timed_data_analyzer(timed_list, fx_dictionary):
    timed_list.sort()

    print('\nSIMPLE: ORDERED BY SPEED')
    for i, element in enumerate(timed_list):
        print(f'{i + 1}. {fx_dictionary[element]} -- {element} seconds')

    print('\nCOMPARATIVE:')
    for i, element in enumerate(timed_list):
        if i==0:
            print(f'{fx_dictionary[element]} was best at {element} seconds')
        else:
            print(f'{fx_dictionary[element]} lagged behind by +{timed_list[i]-timed_list[0]} sec')
