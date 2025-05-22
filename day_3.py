

# Problem summary: perform the multiplication of two numbers in the format mul(num1,num2) and add the result to a total. ignore any corrupted instructions in the string. 
# solution idea: define a state machine, with states:'start' 'm', 'u', 'l', '(', 'num1', ',' , 'num2'. Each letter will be processed, and the state machine will transition to the next state if the letter is valid, otherwise it will reset to the start state. If it reaches the end of a valid mul instruction, it will multiply the two numbers and add the result to the total.

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
print(f"First part result: {state_machine.result}")


######### Q2 #########
# The second part of the problem is to add do() and don't() instructions.
# The solution idea: add a second state machine on parallel that will enable or disable the first state machine.

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
                state_machine.process('#') # this will ignore the instruction

print(f"Second part result: {state_machine.result}")


                
                       
