import numpy as np

def check_report_is_safe(report: list) -> bool:
    report_np = np.array(report)
    diffs = np.diff(report_np) # Calculate the difference between consecutive elements
    if all(diffs > 0) or all(diffs < 0):
        if(all(abs(diffs) >= 1) and all(abs(diffs) <= 3)):
            return True
    return False

with open('input_2.txt', 'r') as f:
    num_safe = 0
    for line in f:
        report = list(map(int, line.split()))
        if check_report_is_safe(report):
            num_safe += 1

    print(f'Q1: The number of safe reports is: {num_safe}')

######## Q2 #########

# def check_report_is_monotonic(report: list) -> bool:
#     report_np = np.array(report)
#     diffs = np.diff(report_np) # Calculate the difference between consecutive elements
#     if all(diffs > 0) or all(diffs < 0):
#         if(all(abs(diffs) >= 1) and all(abs(diffs) <= 3)):
#             return True
#     return False


with open('input_2.txt', 'r') as f:
    num_safe = 0
    for line in f:
        report = list(map(int, line.split()))
        
        if check_report_is_safe(report):
            num_safe += 1
            continue

        report_np = np.array(report)
        diffs = np.diff(report_np)
        l = len(report_np)
        l_diffs = len(diffs)

        # create a list of 1s for non-zero diffs and 0s otherwise
        increasing = ((diffs > 0)).tolist()
        decreasing = ((diffs < 0)).tolist()

        ###### non even almost monotonic #######
        if sum(increasing) < l_diffs-1 and sum(decreasing) < l_diffs-1:
            # print('Report is not even almost monotonic')
            continue
        
        ######## almost monotonic #######
        fault_index = -1
        if sum(increasing) == l_diffs-1:
            fault_index = increasing.index(False)
        elif sum(decreasing) == l_diffs-1:
            fault_index = decreasing.index(False)
        
        if fault_index > -1:
            # try removing one of the elements that caused the report to be non-decreasing or non-increasing 
            report_1 = np.delete(report_np, fault_index)
            is_almost_safe = check_report_is_safe(report_1)
            if is_almost_safe:
                num_safe += 1
                # print('is almost safe after removing the first element') 
                continue
            else:
                report_2 = np.delete(report_np, fault_index+1)
                is_almost_safe = check_report_is_safe(report_2)
                if is_almost_safe:
                    num_safe += 1
                    # print('is almost safe after removing the second element') 
                    continue
        
        #### monotonic #######
        if sum(increasing) == l_diffs or sum(decreasing) == l_diffs:
            # test if almost all the abs diffs are all between 1 and 3
            is_amplitude = ((abs(diffs) >= 1)).tolist() and ((abs(diffs) <= 3)).tolist()
            if sum(is_amplitude) < l_diffs-1:
                # print('more than one amplitude is not between 1 and 3')
                continue
            if sum(is_amplitude) == l_diffs-1:
                fault_index = is_amplitude.index(False)
                # try removing one of the elements that caused the problem
                report_1 = np.delete(report_np, fault_index)
                is_almost_safe = check_report_is_safe(report_1)
                if is_almost_safe:
                    num_safe += 1
                    # print('although totally monotonic, it is almost safe after removing the first element')
                    continue
                else:
                    report_2 = np.delete(report_np, fault_index+1)
                    is_almost_safe = check_report_is_safe(report_2)
                    if is_almost_safe:
                        # print('although totally monotonic, it is almost safe after removing the first element')
                        num_safe += 1
                        continue

    print(f'Q2: Num safe reports: {num_safe}')

