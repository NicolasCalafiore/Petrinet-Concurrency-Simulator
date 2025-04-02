import places

def DECODE(inb: places.INB, inm: places.INM, rgf: places.RGF, tick):
    inb.add(inm.transfer(),tick, rgf)

def ISSUE2(lib: places.LIB, inb: places.INB,tick):
    lib.add(inb.transfer(),tick)

def ISSUE1(aib: places.AIB, inb: places.INB,tick):
    aib.add(inb.transfer(),tick)

def ALU(reb: places.REB, aib: places.AIB,tick):
    reb.add(aib.transfer(), tick)

def ADDR(adb: places.ADB, lib: places.LIB,tick):
    adb.add(lib.transfer(),tick)

def LOAD(reb: places.REB, dam: places.DAM, adb: places.ADB,tick):
    reb.add(dam.transfer(),tick)
    reb.add(adb.transfer(),tick)

def WRITE(rgf: places.RGF, reb: places.REB,tick, target: int = 0):
    rgf.TARGET = target
    rgf.add(reb.transfer(),tick)

def READ(inb: places.INB, rgf: places.RGF,tick): ## How do i deal with this?
    inb.add(rgf.transfer(),tick)