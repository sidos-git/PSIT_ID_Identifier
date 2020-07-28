import webbrowser
s='https://erp.psit.in/assets/img/Simages/'
print("Enter 5 digit user ID")
id=input()
p='.jpg'
s+=id
s+=p

webbrowser.open(s, new=2)
