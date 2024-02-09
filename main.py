from random import randint

def diceRoll():
  return randint(1,6)

def getDefence(amount = 2,strongHold = False,leader = False,buff=0):
  nums = [diceRoll() for i in range(amount)]
  nums.sort(reverse=True)
  if strongHold:
    nums[0] += 1
  if leader:
    nums[0] += 1
  nums[0] += buff
  return nums

def getAttack(amount = 3,leader = False,buff=0):
  nums = [diceRoll() for i in range(amount)]
  nums.sort(reverse=True)
  if leader:
    nums[0] += 1
  nums[0] += buff
  return nums


# defenders = 5
# attackers = 4
# currentBattle = 1
# print("The battle starts with {0} defenders and {1} attackers!".format(defenders, attackers))
# while defenders > 0 and attackers > 0:
#   combatWidth = min(defenders,attackers,2)
#   Def = getDefence(min(2,defenders))
#   Att = getAttack(min(3,attackers))
#   print(Def,"\n{0}".format(Att))
#   for i in range(combatWidth):
#     if Def[i] >= Att[i]:
#       attackers -= 1
#     else:
#       defenders -= 1
#   print(f"After Battle {currentBattle}: {defenders} defenders, {attackers} attackers")
#   currentBattle += 1



findDefence = True
onStrongHold = True
attackerLeader = True
defenderLeader = False
defenceBuff = 0
attackBuff = 0
iterations = 1000

if not findDefence:
  Defenders =  3
  increment = 1
  minAttackers = int(Defenders*0.75)
  maxAttackers = max(int(Defenders*1.75),10)
  # maxAttackers = 10
  stats = {}
  
  for Attackers in range(minAttackers,maxAttackers+1,increment):
    attackWins = 0
    attackersKilled = 0
    for i in range(iterations):
      defenders = Defenders
      attackers = Attackers
      while defenders > 0 and attackers > 0:
        combatWidth = min(defenders,attackers,2)
        Def = getDefence(min(2,defenders),onStrongHold,defenderLeader,defenceBuff)
        Att = getAttack(min(3,attackers),attackerLeader,attackBuff)
        for i in range(combatWidth):
          if Def[i] >= Att[i]:
            attackers -= 1
            #print("hi")
          else:
            defenders -= 1
      if defenders == 0:
        attackersKilled += Attackers - attackers
        attackWins += 1
    #print(attackersKilled,attackWins)
    if attackWins != 0:
      stats[Attackers] = [100* attackWins/iterations,round(attackersKilled/attackWins,1)]
    else:
      stats[Attackers] = [100* attackWins/iterations,None]
  
  print("{} defenders\n----------------------".format(Defenders))
  
  for key,value in stats.items():
    print(f"{key} attackers: {value}")
    # print(stats)

else:
  Attackers = 20
  increment = 2
  stats = {}
  for Defenders in range(Attackers,max(10,int(Attackers*2))+1,increment):
    defenceWins = 0
    defendersKilled = 0
    for i in range(iterations):
      defenders = Defenders
      attackers = Attackers
      while defenders > 0 and attackers > 0:
        combatWidth = min(defenders,attackers,2)
        Def = getDefence(min(2,defenders),onStrongHold,defenderLeader,defenceBuff)
        Att = getAttack(min(3,attackers),attackerLeader,attackBuff)
        for i in range(combatWidth):
          if Def[i] >= Att[i]:
            attackers -= 1
          else:
            defenders -= 1
      if attackers == 0:
        defendersKilled += Defenders - defenders
        defenceWins += 1
    stats[Defenders] = [100* defenceWins/iterations,round(defendersKilled/iterations,1)]
  print("{} attackers\n----------------------".format(Attackers))

  for key,value in stats.items():
    print(f"{key} defenders: {value}")
