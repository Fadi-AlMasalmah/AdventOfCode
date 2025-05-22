# # It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.
# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
# For example, consider the following section of corrupted memory:
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).
# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?


# mul(214,225)
# define a state machine, with states:'start' 'm', 'u', 'l', '(', 'num1', ',' , 'num2'. Each letter will be processed by the state machine, and the state machine will transition to the next state if the letter is valid, otherwise it will reset to the start state. If it reaches the end of a valid mul instruction, it will multiply the two numbers and add the result to the total.

class StateMachine: 
    def __init__(self):
        self.state = 'start'
        self.result = 0
        self.num1 = 0
        self.num2 = 0

    def process(self, letter):
        match self.state:
            case 'start':
                self.num1 = 0
                self.num2 = 0
                if letter == 'm':
                    self.state = 'm'
                else:
                    self.state = 'start'
            case 'm':
                if letter == 'u':
                    self.state = 'u'
                else:
                    self.state = 'start'
            case 'u':
                if letter == 'l':
                    self.state = 'l'
                else:
                    self.state = 'start'
            case 'l':
                if letter == '(':
                    self.state = '('
                else:
                    self.state = 'start'
            case '(':
                if letter.isdigit():
                    self.state = 'num1'
                    self.num1 = int(letter)
                else:
                    self.state = 'start'
            case 'num1':
                if letter.isdigit():
                    self.num1 *= 10
                    self.num1 += int(letter)
                elif letter == ',':
                    self.state = ','
                else:
                    self.num1 = 0
                    self.state = 'start'
            case ',':
                if letter.isdigit():
                    self.state = 'num2'
                    self.num2 = int(letter)
                else:
                    self.state = 'start'
            case 'num2':
                if letter.isdigit():
                    self.num2 *= 10
                    self.num2 += int(letter)
                elif letter == ')': 
                    self.result += self.num1 * self.num2
                    self.state = 'start'
                else:
                    self.num2 = 0
                    self.num1 = 0
                    self.state = 'start'

state_machine = StateMachine()
with open("input_3.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = list(line)
        for letter in data:
            state_machine.process(letter)
print(f"Result: {state_machine.result}")


######### Q2 #########
# The second part of the problem is to add do() and don't() instructions.

class EnablingStateMachine():
    def __init__(self):
        self.state = 'start'
        self.enabled = True
    def process(self, letter):
        match self.state:
            case 'start':
                if letter == 'd':
                    self.state = 'd'
            case 'd':
                if letter == 'o':
                    self.state = 'o'
                else:
                    self.state = 'start'
            case 'o':
                if letter == '(':
                    self.state = 'do('
                elif letter == 'n':
                    self.state = 'don'
                else:
                    self.state = 'start'
            case 'do(':
                if letter == ')':
                    self.enabled = True
                    self.state = 'start'
                else:
                    self.state = 'start'
            case 'don':
                if letter == "'":
                    self.state = 'don-quote"'
                else:
                    self.state = 'start'
            case 'don-quote"':
                if letter == 't':
                    self.state = 'dont'
                else:
                    self.state = 'start'
            case 'dont':
                if letter == '(':
                    self.state = 'dont('
                else:
                    self.state = 'start'
            case 'dont(':
                if letter == ')':
                    self.enabled = False
                    self.state = 'start'
                else:
                    self.state = 'start'
enabling_state_machine = EnablingStateMachine()
state_machine = StateMachine()
with open("input_3.txt", "r", encoding="utf-8") as f:
    for line in f:
        data = list(line)
        for letter in data:
            enabling_state_machine.process(letter)
            if enabling_state_machine.enabled:
                state_machine.process(letter)
            else:
                state_machine.process('#')

print(f"Result: {state_machine.result}")


                
                       
