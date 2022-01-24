def MAIN():
    import timer_and_ui, timeit, os
    fx_dict={}
    time_list=[]

    #UI
    imports, genfx, solution_functions = timer_and_ui.inputer()
    solution_functions = timer_and_ui.solver_functionator(solution_functions)


    for i, v in enumerate(solution_functions):
        string = f'\nimport {imports}\ngen_returns={genfx}\n{v}'
        with open('temp.txt', 'w') as f:
            f.write(string)
        f.close()

        with open('temp.txt', 'r') as f:
            code=f.read()
            timed_code=timeit.timeit(code, number=30)
            fx_dict[timed_code] = timer_and_ui.de_functionator(v)
            time_list.append(timed_code)
        f.close()

        print(f'''
DETAILED:
#{i+1} function was timed with code:
    {string}

The average run time across 30 samples was: {timed_code} seconds
''')

    os.remove('temp.txt')

    if len(time_list)>1:
        timer_and_ui.timed_data_analyzer(time_list,fx_dict)

if __name__ == "__main__":
    MAIN()