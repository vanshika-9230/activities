'''Case: We have an admission counsellor who wants to deliver a bulk message.

To the corresponding students with similar context, the admission counsellor asked a team of developers in EN2004 to help them creating a mechanism to deliver the same with an application that has a form like structure wherein
The counsellor can update the asked fields and messages will be processed.'''


names=input("enter the names of  the students:").split(",")
Admission_id=input("enter the Admission_id's of the students:").split(",")
cap_rank=input("enter the caprank of the students:").split(",")
message='''Hi {},\n\n Congratulations...!  {} You got selected for next round of recruitment process \ submit 
your academic credential including primary and secondary certificates. Your admission ID is {} and 
will be eligible \ for the next round of interview with a CAP rank of {} If you submit all the documents
on time and process university might offer you a scholarship. \n\n'''
for i in range(len(names)):
  print(message.format(names[i],"!!!",Admission_id[i],cap_rank[I])