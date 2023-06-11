#Taking input from user wheter part of CWS of not
cws=(input("Are you part of CWS=")).lower()
if(cws=='yes'):
    attend=int(input("Please enter not of classed attended="))
    if(attend>=3):
        assignment=int(input("Please enter not of asignments subimeted="))
        if(assignment>=3):
            print("You are eligible for certificate")
        else:
            print("You are not eligible for Certificate because you have not submitted enough assignments")
    else:
        print("You are not eligible for certificate because you have attented less than 3 days")
else:
    print("Sorry,you are not eligible for certificate")
