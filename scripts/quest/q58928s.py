# id 58928 ([Hieizan Temple] Sad Little Boy), field 811000014
sm.setSpeakerID(9130107) # Mysterious Boy
sm.setParam(4)
sm.setInnerOverrideSpeakerTemplateID(9130107) # Mysterious Boy
sm.sendNext("*Sniff*")
sm.setParam(16)
sm.sendSay("(A boy in a place like this? Quite suspicious. And crying at that. I should just... pretend I didn't see.)")
sm.setParam(4)
res = sm.sendAskYesNo("*Sniff* WAHHHH.... Wait, is that... Is somebody there? Please, help me! ")
sm.startQuest(parentID)
sm.startQuest(58979)
sm.setParam(16)
sm.sendNext("Ergh... What's wrong?")
sm.setParam(4)
sm.sendSay("I used to serve the alliance military. I took care of the horses. We were led here from the guard post and... I guess passed out in all the chaos.")
sm.setParam(16)
sm.sendSay("Where are the other alliance soldiers? ")
sm.setParam(4)
sm.sendSay("All the soldiers went... I don't know. They're strange now. I-I'm scared. I want to get out of here. Could you find my sack for me?")
sm.sendSay("It's the only thing I have to remember my father by. I'm pretty sure I dropped it somewhere close by but I can't see, it's too dark.")
sm.sendPrev("It's a bag with very pretty flower prints. Don't judge.")
