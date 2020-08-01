
from Person import *
# from Fellowship import Fellowship


		# Initializing People
Gandalf  =  Wizzard("Gandalf")
Aragorn  =  Human("Aragorn")
Gimli    =  Dwarf("Gimli")
Legolas  =  Elf("Legolas")
Boromir  =  Human("Boromir")
Frodo    =  Hobbit("Frodo")
Sam      =  Hobbit("Sam")
Meriadoc =  Hobbit("Meriadoc")
Peregrin =  Hobbit("Peregrin")

# 		// Initializing Fellowships
FellowshipOfTheRing =  Fellowship("of The Ring")
EvilFellowship      =  Fellowship("of Evil")

# # // 0.3pts -> Every person has a name
# #print(Gandalf.name().equals("Gandalf"));
# # print(Gandalf.toString().equals("Gandalf"))


# # 		// 0.3pts -> There is no members yet
# #println(FellowshipOfTheRing.toString().equals("Fellowship of The Ring"));
# #System.out.println(EvilFellowship.toString().equals("Fellowship of Evil"));
print(EvilFellowship.count() == 0)
print(FellowshipOfTheRing.count() == 0)
print(FellowshipOfTheRing.hasNoMembers()==True)
print(FellowshipOfTheRing.hasMembers()==False)

# # # 		// 0.3pts -> Members count from 1 (not 0)
print(FellowshipOfTheRing.member(1) == None)
print(FellowshipOfTheRing.lastMember() == None)
# # 
# # 		// 0.3pts -> There is two members (order matters)
FellowshipOfTheRing.signUp(Gandalf) # member 1
FellowshipOfTheRing.signUp(Aragorn) # member 2
print(FellowshipOfTheRing.count() == 2)
print(FellowshipOfTheRing.hasNoMembers() == False)
print(FellowshipOfTheRing.hasMembers() == True)
# # 
# # 		// 0.4pts -> Member is a intermediary class between Fellowship and Person




# print(isinstance(FellowshipOfTheRing.member(1),Member))
# print(isinstance(FellowshipOfTheRing.member(2),Member))

# # 		// 0.4pts -> Through Member we can access the people
# #print(FellowshipOfTheRing.member(1).person().name().equals("Gandalf"))
# #print(FellowshipOfTheRing.member(1).person().equals(Gandalf))
# #print(FellowshipOfTheRing.member(1).person().equals( Wizard("Gandalf")))
# #print(!FellowshipOfTheRing.member(1).person().equals(Aragorn))
# #print(FellowshipOfTheRing.member(2).person().equals(Aragorn))

# # 		// 0.4pts -> Out of Range should not throw an exception
# #print(FellowshipOfTheRing.member(-1) == null)
# #print(FellowshipOfTheRing.member(3) == null)

# # 		// 0.4pts -> The relationship is bidirectional
# print(Aragorn.fellowship() == FellowshipOfTheRing)
print(FellowshipOfTheRing.member(1).get_name())

#print(Aragorn.fellowship() != EvilFellowship)
#print(Aragorn.fellowship() == Gandalf.fellowship())
#print(Gimli.fellowship() == null)

#print(Aragorn.isMemberOfAFellowship() == true)
#print(Aragorn.isMemberOfTheFellowship(FellowshipOfTheRing) == true)
#print(Aragorn.isMemberOfTheFellowship(EvilFellowship) == false)
#print(Gimli.isMemberOfAFellowship() == false)
#print(Gimli.isMemberOfTheFellowship(FellowshipOfTheRing) == false)
#print(Gimli.isMemberOfTheFellowship(EvilFellowship) == false)

# 		// 0.5pts -> However, a person can be member of only one fellowship
# 		EvilFellowship.signUp(Aragorn) // Aragorn has not been included
#print(EvilFellowship.count() == 0)
#print(EvilFellowship.hasNoMembers() == true)
#print(Aragorn.fellowship() == FellowshipOfTheRing)
#print(Aragorn.isMemberOfTheFellowship(FellowshipOfTheRing) == true)
#print(Aragorn.isMemberOfTheFellowship(EvilFellowship) == false)

# 		// 0.5pts -> There is another way to join the fellowships
# 		Gimli.join(FellowshipOfTheRing)
# 		Gimli.join(EvilFellowship) // has no effect (already in a fellowship)
#print(FellowshipOfTheRing.count() == 3)
#print(FellowshipOfTheRing.member(3).person().equals(Gimli))

# 		// 0.5pts -> Even indirect way
# 		Legolas.join(Gimli.fellowship())
#print(FellowshipOfTheRing.count() == 4)
#print(FellowshipOfTheRing.lastMember().person().equals(Legolas))

# 		// 0.5pts -> More queries
#print(FellowshipOfTheRing.count("Human") == 1)
#print(FellowshipOfTheRing.count("Elf") == 1)
#print(FellowshipOfTheRing.count("Hobbit") == 0)
#print(FellowshipOfTheRing.has("Human") == true)
#print(FellowshipOfTheRing.has("Hobbit") == false)

# 		// 0.6pts -> Get the fellowship complete (adding various members at one time)
#print(FellowshipOfTheRing.count() == 4)
# 		FellowshipOfTheRing.signUp(Boromir, Frodo)
# 		FellowshipOfTheRing.signUp(Sam, Meriadoc, Peregrin)
#print(FellowshipOfTheRing.count() == 9)
#print(FellowshipOfTheRing.count("Hobbit") == 4)
		
# 		// 0.6pts -> Left the FellowshipOfTheRing
#print(FellowshipOfTheRing.count() == 9)
#print(FellowshipOfTheRing.count("Human") == 2)
#print(Boromir.fellowship() == FellowshipOfTheRing)
#print(FellowshipOfTheRing.member(5).person() == Boromir)
		
# 		FellowshipOfTheRing.cancel(Boromir)

#print(FellowshipOfTheRing.count() == 8)
#print(FellowshipOfTheRing.count("Human") == 1)
#print(Boromir.fellowship() == null)
#print(FellowshipOfTheRing.member(5).person() == Frodo)
		
# 		// 0.6pts -> Other way to unsubscribe
# 		Frodo.left() // leave current fellowship if any
#print(FellowshipOfTheRing.count() == 7)
#print(Frodo.fellowship() == null)

# 		Gandalf.die()
#print(FellowshipOfTheRing.count() == 6)
#print(Gandalf.fellowship() == null)
		
# 		// 0.6pts -> People can't join fellowships after die
#print(FellowshipOfTheRing.count() == 6)
# 		Gandalf.join(FellowshipOfTheRing)
#print(Gandalf.fellowship() == null)
#print(FellowshipOfTheRing.count() == 6)
		
# 		// 0.7pts -> Asking if people are sharing a fellowship
#print(Meriadoc.isFellowOf(Peregrin) == true)
#print(Meriadoc.isFellowOf(Gandalf) == false)
#print(Meriadoc.isFellowOf(Boromir) == false)
#print(Meriadoc.isFellowOf(Meriadoc) == true)
#print(Gandalf.isFellowOf(Gandalf) == true)
		
# 		// 0.7pts -> Should be reflexive
#print(Meriadoc.isFellowOf(Peregrin) == Peregrin.isFellowOf(Meriadoc))
#print(Meriadoc.isFellowOf(Boromir) == Boromir.isFellowOf(Meriadoc))
		
# 		// 0.7pts -> Yet another way to join a fellowship
#print(Boromir.fellowship() == null)
# 		Boromir.fellow(Meriadoc)
#print(Boromir.fellowship() == Meriadoc.fellowship())
#print(Meriadoc.isFellowOf(Boromir) == true)
# 		Boromir.left()
#print(Boromir.fellowship() == null)
# 		Meriadoc.fellow(Boromir)
#print(Boromir.fellowship() == Meriadoc.fellowship())
		
# 		// 0.7pts -> Dissolve the fellowship :(
# 		FellowshipOfTheRing.dissolve()
#print(FellowshipOfTheRing.count() == 0)
#print(FellowshipOfTheRing.hasNoMembers() == true)
#print(FellowshipOfTheRing.member(1) == null)
#print(FellowshipOfTheRing.lastMember() == null)
# 	}
# }
# x = input("Done ") 

# if __name__ == "__main__":

#   print('Terminal execution!')
#   main()