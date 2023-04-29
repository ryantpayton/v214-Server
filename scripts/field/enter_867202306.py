# id 867202306 (Abrup Basin : Skuas), field 867202306
sm.lockInGameUI(True, False)
sm.spawnNpc(9400590, 515, -48)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.spawnNpc(9400582, 430, 40)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.spawnNpc(9400580, 377, 50)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400600, 322, 56)
sm.showNpcSpecialActionByTemplateId(9400600, "summon", 0)
sm.spawnNpc(9400601, 217, 68)
sm.showNpcSpecialActionByTemplateId(9400601, "summon", 0)
sm.spawnNpc(9400586, 159, 70)
sm.showNpcSpecialActionByTemplateId(9400586, "summon", 0)
sm.spawnNpc(9400597, -243, 80)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.spawnNpc(9400598, -296, 80)
sm.showNpcSpecialActionByTemplateId(9400598, "summon", 0)
sm.spawnNpc(9400599, -342, 80)
sm.showNpcSpecialActionByTemplateId(9400599, "summon", 0)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendNext("Birna, I don't think you need to be so hard on him. He's got a lot on his mind as the chief of his town. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("And I'm the chief of my town! But you don't see me mewling and sniping like that! ")
sm.sendSay("I've done all that I can to teach them the importance of cooperation, and they still just bicker and complain about their own needs... ")
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("They're young, Birna. They don't have the years of experience that we do. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("I suppose... ")
sm.setInnerOverrideSpeakerTemplateID(9400586) # Sanaan
sm.sendSay("This conflict will teach them, Birna. They're already learning, and by the time we pull through this storm they might finally understand. And seeing them grow reminds me that we're still maturing, too. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Ugh, don't remind me. I've always hated it when you're right. ")
sm.spawnNpc(9400604, 700, -20)
sm.showNpcSpecialActionByTemplateId(9400604, "summon", 0)
sm.moveNpcByTemplateId(9400604, True, 250, 100)
sm.sendDelay(2000)
sm.setInnerOverrideSpeakerTemplateID(9400604) # Miner
sm.sendNext("Chief Birna! ")
sm.flipNpcByTemplateId(9400600, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400600, False, 180, 60)
sm.sendDelay(2000)
sm.flipNpcByTemplateId(9400582, False)
sm.flipNpcByTemplateId(9400580, False)
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendNext("What is it? ")
sm.setInnerOverrideSpeakerTemplateID(9400604) # Miner
sm.sendSay("We've finished testing the new ballista! It's a real corker! ")
sm.sendSay("We can build more, but we'd need more wood and more hands. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Well then. See if some of the guards would be willing to take a break from training to help you out. Same with the miners. ")
sm.setInnerOverrideSpeakerTemplateID(9400604) # Miner
sm.sendSay("Will do! ")
sm.flipNpcByTemplateId(9400604, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400604, False, 500, 100)
sm.sendDelay(2000)
sm.flipNpcByTemplateId(9400600, True)
sm.setParam(57)
sm.sendNext("#bBallista? ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Our bright little scholar here drew up the blueprints for some weapons we can use to defend the town. The ballista required the fewest resources, so we started with that. ")
sm.setParam(57)
sm.sendSay("#bWow! Alika, that's amazing. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face0#Ha ha, it's no big deal... I never thought that semester in Siege Weapon Drafting would pay off, but here we are. Oh, and the Skuas craftsmen made some great improvements, too! ")
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Smart AND humble... is there anything our dear Alika can't do? ")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face0#...I just said the craftsmen made improvements I hadn't considered, you know. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Ha! Glad to hear we have a few bright minds among our own people as well. ")
sm.spawnNpc(9400635, 950, 0)
sm.showNpcSpecialActionByTemplateId(9400635, "summon", 0)
sm.spawnNpc(9400636, 1000, 0)
sm.showNpcSpecialActionByTemplateId(9400636, "summon", 0)
sm.spawnNpc(9400637, 1050, 0)
sm.showNpcSpecialActionByTemplateId(9400637, "summon", 0)
sm.spawnNpc(9400638, 1100, 0)
sm.showNpcSpecialActionByTemplateId(9400638, "summon", 0)
sm.spawnNpc(9400639, 1150, 0)
sm.showNpcSpecialActionByTemplateId(9400639, "summon", 0)
sm.spawnNpc(9400640, 1200, 0)
sm.showNpcSpecialActionByTemplateId(9400640, "summon", 0)
sm.moveNpcByTemplateId(9400635, True, 200, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400636, True, 200, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400637, True, 200, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400638, True, 200, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400639, True, 200, 100)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400640, True, 200, 100)
sm.sendDelay(2500)
sm.flipNpcByTemplateId(9400600, False)
sm.sendDelay(1500)
sm.sendNext("Thank you for meeting with me. As you may already know, we're constructing weapons to give us a defensive advantage if the town is attacked. ")
sm.sendSay("We've completed one weapon and the plan is to construct more, but we lack the materials and the manpower. ")
sm.setInnerOverrideSpeakerTemplateID(9400603) # Guard
sm.sendSay("Leave the wood to us! ")
sm.setInnerOverrideSpeakerTemplateID(9400604) # Miner
sm.sendSay("Our ore reserves are fine, so we can focus on construction! ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Thank you, everyone. Look out for each other and make sure no one is put in harm's way with these tasks.")
sm.flipNpcByTemplateId(9400635, False)
sm.flipNpcByTemplateId(9400636, False)
sm.flipNpcByTemplateId(9400637, False)
sm.flipNpcByTemplateId(9400638, False)
sm.flipNpcByTemplateId(9400639, False)
sm.flipNpcByTemplateId(9400640, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400635, False, 400, 100)
sm.moveNpcByTemplateId(9400636, False, 400, 100)
sm.moveNpcByTemplateId(9400637, False, 400, 100)
sm.moveNpcByTemplateId(9400638, False, 400, 100)
sm.moveNpcByTemplateId(9400639, False, 400, 100)
sm.moveNpcByTemplateId(9400640, False, 400, 100)
sm.sendDelay(500)
sm.flipNpcByTemplateId(9400600, True)
sm.sendDelay(500)
sm.sendDelay(2500)
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "Everything is going so well...", 2000, 1, 0, 0, 0, 4, 9400597, 4878499)
sm.sendDelay(2500)
sm.speechBalloon(False, 0, 0, "Chief, is that envy I hear in your voice?", 2000, 1, 0, 0, 0, 4, 9400598, 4878499)
sm.sendDelay(2500)
sm.sendNext("That confrontation between Slaka and Chief Gurnardson seems to have put the chief in poor spirits. ")
sm.setParam(57)
sm.sendSay("#bYeah... I suppose I should talk to him. ")
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400600, True, 530, 100)
sm.sendDelay(1000)
sm.sendDelay(2000)
sm.sendNext("#bChief Gurnardson... ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face1#Hmm? Ah, yes! I hope you've spoken to that ruffian Slaka... He, uh, clearly started... ")
sm.setInnerOverrideSpeakerTemplateID(9400598) # Thorson
sm.sendSay("Chief Gurnardson is right! That jerk started it! ")
sm.sendSay("We were just standing here, minding our own business, and then Slaka asked why we weren't doing anything, and then he started calling the chief gasbag and greaseball and- ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#Yes, YES, we remember! That's enough... But yes! How DARE he act so rudely towards us. Why, he practically owes us his life! ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Why WEREN'T you doing anything? ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face1#Huh? No... You see... That's... ")
sm.setInnerOverrideSpeakerTemplateID(9400598) # Thorson
sm.sendSay("...There was nothing that we could do. ")
sm.setParam(57)
sm.sendSay("#bWhat do you mean? There's always something more that needs to be done. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#Look, we've done our fair share, alright? We pitched tents! We moved rocks to the wall! What else do you want from us?! ")
sm.setInnerOverrideSpeakerTemplateID(9400598) # Thorson
sm.sendSay("Yeah, though... I have been wondering if we'll be able to help when the monsters attack. ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("This isn't about fair shares or doubts. If you see something that needs doing, do it. The one thing we know for sure is that standing around like this does nothing.")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face1#... ")
sm.setParam(57)
sm.sendSay("#b... ")
sm.setParam(37)
sm.sendSay("#face0#...Teach us! ")
sm.setParam(57)
sm.sendSay("#bWhat? ")
sm.setParam(37)
sm.sendSay("#face0#You know, like how you taught the Kaptafel lumberjacks to, um, fight with their axes! ")
sm.sendSay("#face0#Teach us how to fight with our harpoons! ")
sm.setInnerOverrideSpeakerTemplateID(9400600) # Birna
sm.sendSay("Surely you are better with a harpoon than #h0#? You were practically born with one in your hand. ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#And I've used it to spear fish in the river, not beasts on the land! I don't know how to fight... ")
sm.setParam(57)
sm.sendSay("#bThen I will teach you. But you should know, I didn't teach the others to fight with their axes. I taught them how to use their experience as woodcutters to fight. ")
sm.sendSay("#bAttacks aren't just about slicing and cutting, so with a little advice and practice you should be able to fight using your harpoons. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400598) # Thorson
sm.sendSay("R-really? ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#Then let's not dally! Lead on!")
sm.lockInGameUI(False, True)
sm.createQuestWithQRValue(64119, "dir1=1")
sm.startQuest(64119)
sm.warp(867202403)