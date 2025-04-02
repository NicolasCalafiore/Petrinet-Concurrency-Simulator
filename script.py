import places
import transitions

def Clean_Instruction(instructions: str)-> list[str]:
    instructions = instructions.split('\n')
    return instructions


def Read_Instructions()-> list[list[str]]:
    instructions = open("instructions.txt", "r").read()
    data_memory = open("datamemory.txt", "r").read()
    registers = open("registers.txt", "r").read()

    instructions = Clean_Instruction(instructions)
    data_memory = Clean_Instruction(data_memory)
    registers = Clean_Instruction(registers)

    return [instructions, data_memory, registers]

def PrintComponents(dam: places.DAM, inb:  places.INB, rgf:  places.RGF ,inm:  places.INM, aib:  places.AIB, reb:  places.REB,adb:  places.ADB, lib:  places.LIB):
    print("INM: ", end="")
    inm.print()
    print("INB: ", end="")
    inb.print()
    print("AIB: ", end="")
    aib.print()
    print("LIB: ", end="")
    lib.print()
    print("ADB: ", end="")
    adb.print()
    print("REB: ", end="")
    reb.print()
    print("RGF: ", end="")
    rgf.print()
    print("DAM: ", end="")
    dam.print()



















def Cycle(dam: places.DAM, inb:  places.INB, rgf:  places.RGF, inm:  places.INM, aib:  places.AIB, reb:  places.REB, adb:  places.ADB, lib:  places.LIB, tick: int):
    places.Debug.log.append("\n\n New Cycle")
    if inm.is_executable(1, tick):
        places.Debug.log.append("\n\n INM EXECUTING DECODE/READ")
        transitions.DECODE(inb, inm, rgf, tick)

    if inb.is_executable(1, tick):
        command = inb.peek()
        keywords = ["<AND", "<SUB", "<ADD", "<OR"]
        if command.split(",")[0] in keywords:
            transitions.ISSUE1(aib, inb, tick)
        else:
            transitions.ISSUE2(lib, inb, tick)

    if aib.is_executable(1, tick):
        transitions.ALU(reb, aib, tick)

    if lib.is_executable(1, tick):
        transitions.ADDR(adb, lib, tick)

    if adb.is_executable(1, tick) and dam.is_executable(1, tick):
        transitions.LOAD(reb, dam, adb, tick)

    if reb.is_executable(1, tick) and rgf.is_executable(1, tick):
        transitions.WRITE(rgf, reb, tick)



if __name__ == '__main__':

    # Create all places
    dam = places.DAM()
    inb = places.INB()
    rgf = places.RGF()
    inm = places.INM()
    aib = places.AIB()
    reb = places.REB()
    adb = places.ADB()
    lib = places.LIB()

    # Read Input
    all_instructions = Read_Instructions()

    registers = all_instructions[2]
    for registers in all_instructions[2]:
        token = places.TOKEN(registers)
        rgf.add(token, -2)
    data_memory = all_instructions[1]
    for data_mem in all_instructions[1]:
        token = places.TOKEN(data_mem)
        dam.add(token, -2)
    instructions = all_instructions[0]
    for instruct in all_instructions[0]:
        token = places.TOKEN(instruct)
        inm.add(token, -2)

    tick: int = 0

    while tick < 4:
        print(f'STEP {tick}:')
        PrintComponents(dam, inb, rgf, inm, aib, reb, adb, lib)

        Cycle(dam, inb, rgf, inm, aib, reb, adb, lib, tick)
        tick+=1
        print()


    print("\n\n\n ----- REPORT -----")
    for log in places.Debug.log:
        print(log)
