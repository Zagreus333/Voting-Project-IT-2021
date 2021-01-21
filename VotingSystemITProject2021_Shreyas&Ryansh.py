tutorgroup = input("Enter name of tutor group:")
tutorgroup_list = ["7A", "7B", "7C", "7D", "7E", "7F", "8A", "8B", "8C", "8D", "8E", "8F", "9A", "9B", "9C", "9D", "9E", "9F", "10A", "10B", "10C", "10D", "10E", "10F", "11A", "11B", "11C", "11D", "11E", "11F"]
while tutorgroup_list == []:
    try:
        tutorgroup_list.remove(tutorgroup)
    except:
        print("This tutor group cannot be voted for")

try :
    num_of_students = int(input("Enter number of students between 28-35:"))
except:
    print("This is not a number")

if num_of_students >= 28 and num_of_students<= 35:
    print(tutorgroup, "has", num_of_students, "students")
else:
    print("This number of students is not allowed")
    num_of_students = int(input("Enter number of students between 28-35:"))


abstentions = 0
num_of_candidates = int(input("Enter number of candidates 1-4:"))

candidates = ["A", "B", "C", "D"]
if num_of_candidates == 3:
    candidates.remove("D")
    candidate1 = input("Enter candidate 1:")
    candidate2 = input("Enter candidate 2:")
    candidate3 = input("Enter candidate 3:")
elif num_of_candidates == 2:
    candidates.remove("D", "C")
    candidate1 = input("Enter candidate 1:")
    candidate2 = input("Enter candidate 2:")
elif num_of_candidates == 1:
    candidates.remove("D", "C", "B")
    candidate1 = input("Enter candidate 1:")
elif num_of_candidates == 4:
    candidate1 = input("Enter candidate 1:")
    candidate2 = input("Enter candidate 2:")
    candidate3 = input("Enter candidate 3:")
    candidate4 = input("Enter candidate 4:")
    print("You have entered the maximum number of candidates")
else:
   print("The number of candidates has been set to 4, which is the maximum limit")
   candidate1 = input("Enter candidate 1:")
   candidate2 = input("Enter candidate 2:")
   candidate3 = input("Enter candidate 3:")
   candidate4 = input("Enter candidate 4:")


can1_votes = 0
can2_votes = 0
can3_votes = 0
can4_votes = 0

voter_id = []
for i in range(0, num_of_students+1, 1):
    voter_id.append(i)


print("Voting has now begun")

for x in range(0, num_of_students, 1):
    v = int(input("Enter your voter ID:"))
    if v in voter_id:
       print("You are eligible to vote")
       vote = input("Enter the name of candidate you wish to vote for, or abstain:")
       voter_id.remove(v)
       if vote == candidate1:
           can1_votes += 1
           print("Your vote has been casted")
       if vote == candidate2:
           can2_votes += 1
           print("Your vote has been casted")
       if vote == candidate3:
           can3_votes += 1
           print("Your vote has been casted")
       if vote == candidate4:
           can4_votes += 1
           print("Your vote has been casted")
       if vote == "Abstain":
           abstentions += 1
           print("You have abstained")

    else:
        print("You have either already voted or have entered an invalid ID")

if voter_id == []:
    print("Voting has ended")
    print("Now showing results for", tutorgroup)
    if can1_votes > can2_votes and can1_votes > can3_votes and can1_votes > can4_votes:
      percent = (can1_votes/ num_of_students)* 100
      print(candidate1,"has won", "with", percent, "% votes")
      if can2_votes > can1_votes and can2_votes > can3_votes and can2_votes > can4_votes:
         percent = (can2_votes/ num_of_students)* 100
         print(candidate2,"has won", "with", percent, "% votes")
      if can3_votes > can1_votes and can3_votes > can2_votes and can3_votes > can4_votes:
         percent = (can3_votes/ num_of_students)* 100
         print(candidate3,"has won", "with", percent, "% votes")
      if can4_votes > can1_votes and can4_votes > can2_votes and can3_votes > can3_votes:
         percent = (can4_votes/ num_of_students)* 100
         print(candidate4,"has won", "with", percent, "% votes")


elif can1_votes == can2_votes == can3_votes:
      percent = (can1_votes/num_of_students)*100
      print(candidate1, ",", candidate2, "and", candidate3, "have tied with", percent, "% votes")
elif can1_votes == can2_votes == can4_votes:
      percent = (can1_votes/num_of_students)*100
      print(candidate1, ",", candidate2, "and", candidate4, "have tied with", percent, "% votes")
elif can1_votes == can3_votes == can4_votes:
      percent = (can1_votes/num_of_students)*100
      print(candidate1, ",", candidate3, "and", candidate4, "have tied with", percent, "% votes")
elif can2_votes == can3_votes == can4_votes:
      percent = (can2_votes / num_of_students) * 100
      print(candidate2, ",", candidate3, "and", candidate4, "have tied with", percent, "% votes")
elif can1_votes == can2_votes == can3_votes == can4_votes:
      percent = (can1_votes/num_of_students) * 100
      print("All Candidates have tied with", percent, "% votes")
elif can1_votes == can2_votes:
      percent = (can1_votes/num_of_students)* 100
      print(candidate1, "and", candidate2, "have tied with both having", percent, "% votes")
elif can2_votes == can3_votes:
      percent = (can2_votes/num_of_students)* 100
      print(candidate2, "and", candidate3, "have tied with both having", percent, "% votes")
elif can1_votes == can3_votes:
      percent = (can1_votes/num_of_students)* 100
      print(candidate1, "and", candidate3, "have tied with both having", percent, "% votes")
elif can1_votes == can4_votes:
      percent = (can1_votes/num_of_students)* 100
      print(candidate1, "and", candidate4, "have tied with both having", percent, "% votes")
elif can2_votes == can4_votes:
      percent = (can2_votes/num_of_students)* 100
      print(candidate2, "and", candidate4, "have tied with both having", percent, "% votes")
elif can3_votes == can4_votes:
      percent = (can3_votes/num_of_students)* 100
      print(candidate3, "and", candidate4, "have tied with both having", percent, "% votes")




if abstentions == 0:
   print("There have been no abstentions")
else:
   print("The number of people who have abstained are", abstentions)
