import numpy as np

# Problem summary: how many reports are safe? a report is safe if:
## 1. it is monotonic (increasing or decreasing)
## 2. the difference between consecutive elements is between 1 and 3
# Solution idea: use diff to calculate the difference between consecutive elements and check the difference values.

######## Q1 #########
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

# Part 2 summary: a report is safe if it can be made safe by removing one element.
# Solution idea: 
# 1. check if the report is safe
# 2. almost monotonic: if the report has only one error in the monotonicity.
## in this case, try removing one of the two elements around this error and check if the report is safe. 
# 3. not-even almost monotonic: if the report has more than one error in the monotonicity. It can not be made safe.
# 4. not safe but monotonic: if the report is monotonic then check if the amplitude of the diffs is between 1 and 3.
## in this case, try removing one of the two elements around the amplitude-error.




with open('input_2.txt', 'r') as f:
    num_safe = 0
    for line in f:
        report = list(map(int, line.split()))
        
        # check if the report is already safe
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

        ###### not even almost monotonic #######
        if sum(increasing) < l_diffs-1 and sum(decreasing) < l_diffs-1:
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
                # print('report is almost safe after removing the first element') 
                continue
            else:
                report_2 = np.delete(report_np, fault_index+1)
                is_almost_safe = check_report_is_safe(report_2)
                if is_almost_safe:
                    num_safe += 1
                    # print('report is almost safe after removing the second element') 
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
                    # print('report is totally monotonic, and it is safe after removing the first element that caused the amplitude problem')
                    continue
                else:
                    report_2 = np.delete(report_np, fault_index+1)
                    is_almost_safe = check_report_is_safe(report_2)
                    if is_almost_safe:
                        # print('report is totally monotonic, it is almost safe after removing the second element that caused the amplitude problem')
                        num_safe += 1
                        continue

    print(f'Q2: The number of safe reports after dampening is: {num_safe}')