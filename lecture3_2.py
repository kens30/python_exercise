import sys
args = sys.argv
tmpInt = int(args[1])

if (tmpInt % 2) == 0 :
    print('2の倍数です')
elif (tmpInt % 3) == 0 :
    print('3の倍数です')
elif (tmpInt % 5) == 0 :
    print('5の倍数です')