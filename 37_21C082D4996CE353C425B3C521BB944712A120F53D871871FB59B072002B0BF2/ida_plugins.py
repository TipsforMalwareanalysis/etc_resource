import idaapi
import idc

addr = 0x0040135D

fp = open('api.txt', 'w')

def setbp():
    addr = 0x0040135D
    idc.AddBpt(addr)

def go():
    idc.RunTo(addr)
    idc.GetDebuggerEvent(WFNE_SUSP, -1) 

def printEAX():
    eax = cpu.eax

    idaapi.jumpto(eax)
    fp.write(idc.GetFunctionName(eax))

print "start"

while True:
    go()
    printEAX()

fp.close()
print "done"