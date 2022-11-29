#การใช้งาน split
hh,mm,ss = input().split(':')
hh = int(hh)
mm = int(mm)
ss = int(ss)
seconds = ss + 60*mm + 60*60*hh
print(seconds)