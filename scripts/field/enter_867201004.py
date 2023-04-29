# id 867201004 (Abrup Basin : Svarti Entrance), field 867201004
sm.lockInGameUI(True, False)
sm.completeQuestNoCheck(64047)
sm.sendDelay(500)
sm.spawnNpc(9400587, 700, 0)
sm.showNpcSpecialActionByTemplateId(9400587, "summon", 0)
sm.spawnNpc(9400581, 640, 0)
sm.showNpcSpecialActionByTemplateId(9400581, "summon", 0)
sm.spawnNpc(9400580, 570, 0)
sm.showNpcSpecialActionByTemplateId(9400580, "summon", 0)
sm.spawnNpc(9400582, 520, 0)
sm.showNpcSpecialActionByTemplateId(9400582, "summon", 0)
sm.startQuest(64164)
sm.spawnNpc(9400584, 440, -35)
sm.showNpcSpecialActionByTemplateId(9400584, "summon", 0)
sm.spawnNpc(9400583, 380, -35)
sm.showNpcSpecialActionByTemplateId(9400583, "summon", 0)
sm.spawnNpc(9400588, 325, -35)
sm.showNpcSpecialActionByTemplateId(9400588, "summon", 0)
sm.spawnNpc(9400593, 400, 0)
sm.showNpcSpecialActionByTemplateId(9400593, "summon", 0)
sm.spawnNpc(9400591, 355, 0)
sm.showNpcSpecialActionByTemplateId(9400591, "summon", 0)
sm.spawnNpc(9400592, 300, 0)
sm.showNpcSpecialActionByTemplateId(9400592, "summon", 0)
sm.spawnNpc(9400589, 230, 0)
sm.showNpcSpecialActionByTemplateId(9400589, "summon", 0)
sm.spawnNpc(9400619, 180, 0)
sm.showNpcSpecialActionByTemplateId(9400619, "summon", 0)
sm.spawnNpc(9400585, 130, 0)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.spawnNpc(9400585, 80, 0)
sm.showNpcSpecialActionByTemplateId(9400585, "summon", 0)
sm.sendDelay(3000)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/open", 128)
sm.sendDelay(500)
sm.spawnNpc(9400597, 858, -45)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendNext("#face0#You've been working hard, haven't you? I'm impressed with how quickly you gather. ")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face4#You'll keep your promise now, won't you? ")
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#Ah... yes, of course, of course. I did promise, didn't I? We'll have to find you an appropriate space... Wait while I check...")
sm.sendDelay(250)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/close", 128)
sm.sendDelay(500)
sm.sendDelay(3000)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendNext("#face1#How can anyone treat their neighbors in such a disgusting fashion? ")
sm.sendDelay(250)
sm.flipNpcByTemplateId(9400587, True)
sm.sendDelay(250)
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendNext("#face0#We've had few dealings with Svarti in the past, just trading essential goods. ")
sm.sendSay("#face0#They've always been suspicious of us, particularly if their livestock went missing. ")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face0#They don't seem interested in taking us in at all. ")
sm.setInnerOverrideSpeakerTemplateID(9400580) # Alika
sm.sendSay("#face0#For once in my life, I can feel my patience just... slipping away. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face0#What do you think, Peytour? ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#We're nearly out of time. The snowstorm is nearly upon us.")
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face1#Our only option now is to force our way in. ")
sm.sendSay("#face1#It would be a net good for the town anyway, once the monsters descend upon it. At least we know what we're up against. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face1#At this point, I would almost prefer letting them be attacked... ")
sm.setInnerOverrideSpeakerTemplateID(9400589) # Peytour
sm.sendSay("#face0#Chief... you cannot entertain such thoughts! ")
sm.setParam(57)
sm.sendSay("#bLet's at least hear what they have to say next... we may be getting ahead of ourselves. ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400581) # Butler
sm.sendSay("#face1#Hearing them out is what has us trapped out here in the first place! Had we forced our way in, we'd be safe and settled by now. ")
sm.setInnerOverrideSpeakerTemplateID(9400587) # Kan
sm.sendSay("#face1#...")
sm.sendDelay(3000)
sm.sendDelay(2000)
sm.playSound("Sound/PL_MONAD.img/EP1/ACT2/scream", 128)
sm.setInnerOverrideSpeakerTemplateID(9400599) # Harpooner
sm.sendNext("Ahhh! ")
sm.flipNpcByTemplateId(9400587, False)
sm.spawnNpc(9400597, 980, 0)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.spawnNpc(9400598, 1010, 0)
sm.showNpcSpecialActionByTemplateId(9400598, "summon", 0)
sm.spawnNpc(9400599, 1040, 0)
sm.showNpcSpecialActionByTemplateId(9400599, "summon", 0)
sm.spawnNpc(9400599, 1070, 0)
sm.showNpcSpecialActionByTemplateId(9400599, "summon", 0)
sm.sendDelay(300)
sm.moveNpcByTemplateId(9400597, True, 200, 200)
sm.moveNpcByTemplateId(9400598, True, 190, 200)
sm.moveNpcByTemplateId(9400599, True, 180, 200)
sm.moveNpcByTemplateId(9400599, True, 170, 200)
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendNext("#face0#Aghhh! ")
sm.setParam(57)
sm.sendSay("#bWhat was that? ")
sm.setParam(37)
sm.sendSay("#face0#Poison gas! ")
sm.setParam(57)
sm.sendSay("#bPoison gas? Oh, no... ")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400582) # Cayne
sm.sendSay("#face0#Could it be that toxic beast we faced on the snowfield? ")
sm.flipNpcByTemplateId(9400582, True)
sm.sendDelay(500)
sm.setParam(57)
sm.sendNext("#bToxic beast? ")
sm.setParam(37)
sm.sendSay("#face0#You know, the pink monster that was puffing out poison! ")
sm.setParam(57)
sm.sendSay("#bThen we need fire arrows! ")
sm.setParam(37)
sm.sendSay("#face0#Right! Gillie! Fire arrows! ")
sm.moveNpcByTemplateId(9400583, False, 230, 200)
sm.sendDelay(500)
sm.setInnerOverrideSpeakerTemplateID(9400583) # Gillie
sm.sendNext("#face0#Fire arrows ready!")
sm.flipNpcByTemplateId(9400582, False)
sm.sendDelay(250)
sm.moveNpcByTemplateId(9400582, False, 500, 200)
sm.forcedMove(False, 500)
sm.sendDelay(1000)
sm.blind(True, 255, 0, 0, 0, 500)
sm.sendDelay(500)
sm.lockInGameUI(False, True)
sm.startQuest(64048)
sm.createQuestWithQRValue(64048, "chk=0")
sm.warp(867201020)