# id 867200405 (Abrup Basin : Kaptafel Ashes), field 867200405
sm.lockInGameUI(True, False)
sm.spawnNpc(9400581, -30, 365)
sm.showNpcSpecialActionByTemplateId(9400581, "summon", 0)
sm.spawnNpc(9400585, -135, 381)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.spawnNpc(9400585, -182, 387)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face0#Hey, you! ")
sm.setParam(57)
sm.sendSay("#b...? ")
sm.sendDelay(1000)
sm.flipNpcByTemplateId(9400585, True)
sm.flipNpcByTemplateId(9400585, True)
sm.sendDelay(500)
sm.moveNpcByTemplateId(9400585, True, 1000, 130)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400585, True, 1000, 130)
sm.sendDelay(3000)
sm.moveNpcByTemplateId(9400581, True, 100, 50)
sm.sendDelay(1000)
sm.setParam(37)
sm.sendNext("#face0#I let it slide earlier, but you're not from around here, are you? ")
sm.setParam(57)
sm.sendSay("#bYes, that's true. Why? ")
sm.setParam(37)
sm.sendSay("#face0#I am curious why someone as powerful as you would come out here. ")
sm.sendSay("#face0#I assume you aren't offended by my questioning. As leader of this dispatch and protector of this town, I have a right to know. ")
sm.setParam(57)
sm.sendSay("#bWell then... I came here because I received a letter asking for help. ")
sm.sendSay("#bSo since you brought it up, I have a right to be here. ")
sm.setParam(37)
sm.sendSay("#face0#Indeed... May I see the letter? ")
sm.setParam(57)
sm.sendSay("#b... ")
sm.sendDelay(500)
sm.sendDelay(4000)
sm.avatarOriented("Effect/OnUserEff.img/questEffect/PL_MONAD1/0")
sm.setParam(37)
sm.sendNext("#face0#This was not sent by a resident, you know. ")
sm.setParam(57)
sm.sendSay("#bIf that's all, I have matters to attend to. ")
sm.setParam(37)
sm.sendSay("#face0#Just a moment. A final question... Do you intend to stay here further? ")
sm.setParam(57)
sm.sendSay("#bYes. I was summoned by a call for help, and I won't be leaving until the sender is safe. ")
sm.setParam(37)
sm.sendSay("#face0#I see. ")
sm.sendDelay(500)
sm.forcedMove(False, 250)
sm.sendDelay(1500)
sm.flipNpcByTemplateId(9400581, False)
sm.sendDelay(500)
sm.showEffect("Effect/OnUserEff.img/emotion/angry", 0, 0, 0, 0, 16992557, 0, 0)
sm.sendDelay(1000)
sm.sendNext("#face1#I am not done speaking with you. ")
sm.sendDelay(500)
sm.forcedFlip(True)
sm.sendDelay(500)
sm.sendNext("#face0#If you intend to stay, then you will follow my orders for the duration of your stay. ")
sm.setParam(57)
sm.sendSay("#bThat won't be a problem... as long as your orders line up with my plans.")
sm.sendDelay(500)
sm.showEffect("Effect/OnUserEff.img/emotion/angry", 0, 0, 0, 0, 16992557, 0, 0)
sm.sendDelay(3000)
sm.completeQuestNoCheck(64023)
sm.startQuest(64024)
sm.spawnNpc(9400590, 2500, 380)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.spawnNpc(9400587, 450, 70)
sm.showNpcSpecialActionByTemplateId(9400587, "summon", 0)
sm.spawnNpc(9400596, 550, 70)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.spawnNpc(9400593, 1050, 130)
sm.showNpcSpecialActionByTemplateId(9400593, "summon", 0)
sm.spawnNpc(9400591, 1100, 130)
sm.showNpcSpecialActionByTemplateId(9400591, "summon", 0)
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendNext("#face1#Snow... snowstorm! ")
sm.sendDelay(1000)
sm.sendDelay(500)
sm.showEffect("Effect/OnUserEff.img/emotion/shade", 5000, 0, 0, 0, 17002146, 0, 0)
sm.flipNpcByTemplateId(9400596, False)
sm.sendDelay(500)
sm.flipNpcByTemplateId(9400591, False)
sm.moveNpcByTemplateId(9400590, True, 500, 300)
sm.sendNext("#face1#It's a snowstorm!! ")
sm.sendDelay(500)
sm.sendDelay(1000)
sm.spineScreen(True, True, False, 10000, "Map/Effect2.img/Blizzard/skeleton","normal2","")
sm.sendDelay(10000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.sendDelay(2000)
sm.forcedMove(True, 30)
sm.spawnNpc(9400580, 0, 300)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400582, 50, 300)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.spawnNpc(9400591, 100, 300)
sm.showNpcSpecialActionByTemplateId(9400591, "summon", 0)
sm.spawnNpc(9400618, 140, 250)
sm.showNpcSpecialActionByTemplateId(9400618, "summon", 0)
sm.spawnNpc(9400596, 180, 250)
sm.showNpcSpecialActionByTemplateId(9400596, "summon", 0)
sm.spawnNpc(9400587, -200, 300)
sm.showNpcSpecialActionByTemplateId(9400587, "summon", 0)
sm.spawnNpc(9400589, -270, 300)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.spawnNpc(9400590, -330, 300)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.spawnNpc(9400583, -380, 300)
sm.showNpcSpecialActionByTemplateId(9400583, "summon", 0)
sm.spawnNpc(9400585, -430, 300)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.spawnNpc(9400617, -480, 300)
sm.showNpcSpecialActionByTemplateId(9400617, "summon", 0)
sm.spawnNpc(9400585, -580, 300)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face1#What is all this ruckus about a simple snowstorm? ")
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#Simple? Ha! Spoken like someone ignorant of real snowstorms. ")
sm.setParam(57)
sm.sendSay("#bIt looks serious... How strong is it? ")
sm.setParam(37)
sm.sendSay("#face0#Strong? It's overpowering! This is looking to be the biggest snowstorm in recent memory! ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#Slaka! We don't need a panic now. ")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#It's still just a snowstorm. We must repair as many buildings and set up as many tents as possible before it reaches us. ")
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendSay("#face0#Great plan! Especially if you intend to freeze to death. ")
sm.sendSay("#face0#None of our buildings are in any shape to weather a storm like this. Look at those clouds. How long do you think we have until it hits? ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#It pains me to say this, but Slaka is right. We have a matter of hours before the storm hits. We cannot set up shelter in that time. ")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face4#Then... we must evacuate, yes? Pack up and take shelter in another town? ")
sm.setParam(57)
sm.sendSay("#bSounds like it. And if that's the plan, we don't really have time to debate. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#Chief Kan, you should say something. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#...We have no choice. Let us pack what we can and leave immediately. ")
sm.sendSay("#face0#We have good relations with the town just across the river. I'm sure they will take us in. ")
sm.setInnerOverrideSpeakerTemplateID(9400591) # Shulla
sm.sendSay("W-wait! We're coming back after the storm passes, right? We're not truly abandoning our town, are we? ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#Of course. ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#Shulla, I understand your fear, but I promise you this. As soon as the storm ends, I will return and restore our town to its original glory! ")
sm.sendSay("#face0#When our loved ones return, I want their homes to look just the way they remembered. ")
sm.setInnerOverrideSpeakerTemplateID(9400591) # Shulla
sm.sendSay("Oh, Peytour. Thank you... Thank you. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#We have little time, people. Grab what you can and meet back here as soon as possible.")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#Hero! ")
sm.setInnerOverrideSpeakerTemplateID(9400585) # Afinas Soldier
sm.sendSay("Yes, sir!")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#What is the status of our reinforcements? Did headquarters respond?")
sm.setInnerOverrideSpeakerTemplateID(9400585) # Afinas Soldier
sm.sendSay("No, sir. They told us to await their response, and then nothing since.")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#Understood. ")
sm.completeQuestNoCheck(64024)
sm.lockInGameUI(False, True)
sm.warp(867200400)
