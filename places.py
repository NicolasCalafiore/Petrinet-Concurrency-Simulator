class Debug:
    log: list[str] = []

class TOKEN:
    def __init__(self, token_data:str):
        self.token_data = token_data
        self.arrival_tick = -1

class PLACE:
    def __init__(self):
        self.data = []
        self.max_tokens = 100

    def token_count(self)->int:
        return len(self.data)

    def print(self)->None:
        for memory in self.data:
            print(memory.token_data, end=",")
        print()

    def is_executable(self, cost, curr_tick)->bool:
        Debug.log.append(f'Is {self.__class__.__name__} executable?')
        if len(self.data) == 0:
            Debug.log.append(f'Empty {self.__class__.__name__}')
            return False
        else:
            Debug.log.append(f'Arrival Tick: {self.data[0].arrival_tick} vs Current Tick: {curr_tick}')
            Debug.log.append(str(self.data[0].arrival_tick < curr_tick))
        return len(self.data) >= cost and self.data[0].arrival_tick < curr_tick

    def transfer(self):
        Debug.log.append(f'Token {self.data[0].token_data} transferred from {self.__class__.__name__}')
        if len(self.data) == 0:
            print("!!!!!!!!!!!!     EMPTY COMMANDS!     !!!!!!!!!!!!")
            return "ERROR"
        temp = self.data[0]
        self.data.pop(0)
        return temp

    def peek(self):
        return self.data[0].token_data

    def add(self, token: TOKEN, tick):
        Debug.log.append(f'Token {token.token_data} added to {self.__class__.__name__}')
        token.arrival_tick = tick
        self.data.append(token)


class DAM(PLACE):
    TARGET: int = 0  # To be manipulated/accessed from script.py

    def __init__(self):
        super().__init__()
        self.MEM_LIST: list[None | TOKEN] = []
        self.MEM_LIST.append(None)
        self.MEM_LIST.append(None)
        self.MEM_LIST.append(None)
        self.MEM_LIST.append(None)
        self.MEM_LIST.append(None)
        self.MEM_LIST.append(None)
        self.MEM_LIST.append(None)
        self.MEM_LIST.append(None)


    def add(self, token: TOKEN, tick):
        Debug.log.append(f'Token {token.token_data} added to {self.__class__.__name__}')
        token.arrival_tick = tick
        self.MEM_LIST[self.TARGET] = token


    def peek(self):
        return self.MEM_LIST[self.TARGET].token_data



class RGF(PLACE):
    def __init__(self):
        super().__init__()
        self.MEM_LIST: list[None | TOKEN] = [None] * 8

    def add(self, token: TOKEN, tick):
        Debug.log.append(f'Token {token.token_data} added to {self.__class__.__name__}')
        token.arrival_tick = tick
        parts = token.token_data.strip("<>").split(",")
        reg_name = parts[0]
        index = int(reg_name.replace("R", ""))
        self.MEM_LIST[index] = token

    def peek(self):
        return self.MEM_LIST[0].token_data if self.MEM_LIST[0] is not None else "None"

    def get_register_value(self, reg_name: str) -> str:
        index = int(reg_name.replace("R", ""))
        token = self.MEM_LIST[index]
        if token is not None:
            parts = token.token_data.strip("<>").split(",")
            return parts[1]
        return None


class INM(PLACE):   # Holds all instructions
    def __init__(self):
        super().__init__()



class INB(PLACE):
    def __init__(self):
        super().__init__()

    def add(self, token: TOKEN, tick, rgf: 'RGF' = None):
        if rgf is not None:

            parts = token.token_data.strip("<>").split(",")
            if len(parts) == 4:
                opcode, dest, src1, src2 = parts

                val1 = rgf.get_register_value(src1)
                val2 = rgf.get_register_value(src2)

                token = TOKEN(f"<{opcode},{dest},{val1},{val2}>")
        token.arrival_tick = tick
        self.data.append(token)





class LIB(PLACE):
    def __init__(self):
        super().__init__()



class ADB(PLACE):
    def __init__(self):
        super().__init__()



class REB(PLACE):
    def __init__(self):
        super().__init__()

    def add(self, token: TOKEN, tick):
        command = token.token_data.split(",")
        output = "ERROR 1"
        if command[0] == "<ADD":
            output = f'<{command[1]}>, {command[2]} + {command[3]}'

        print("Output: ", output)

class AIB(PLACE):
    def __init__(self):
        super().__init__()
