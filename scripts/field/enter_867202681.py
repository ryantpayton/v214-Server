# id 867202681 (Abrup Basin : Windsleep Forest Junction), field 867202681
sm.lockInGameUI(True, False)
sm.forcedFlip(True)
sm.spawnNpc(9400590, -1000, 120)
sm.showNpcSpecialActionByTemplateId(9400590, "summon", 0)
sm.spawnNpc(9400597, -1150, 120)
sm.showNpcSpecialActionByTemplateId(9400597, "summon", 0)
sm.forcedMove(False, 600)
sm.moveNpcByTemplateId(9400590, False, 600, 100)
sm.moveNpcByTemplateId(9400597, False, 600, 100)
sm.sendDelay(500)
sm.sendDelay(3500)
sm.speechBalloon(False, 0, 0, "You'd best apologize as soon as we get back to Skuas.", 3000, 1, 0, 0, 0, 4, 9400590, 4878499)
sm.sendDelay(3500)
sm.speechBalloon(False, 0, 0, "Wha... for what?", 3000, 1, 0, 0, 0, 4, 9400597, 4878499)
sm.sendDelay(3500)
sm.speechBalloon(False, 0, 0, "Oh come on, don't play dumb.", 3000, 1, 0, 0, 0, 4, 9400590, 4878499)
sm.spawnNpc(9400666, 400, 120)
sm.showNpcSpecialActionByTemplateId(9400666, "summon", 0)
sm.showNpcSpecialActionByTemplateId(9400666, "jumpattack", 0)
sm.sendDelay(4000)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(9400590) # Slaka
sm.sendNext("#face1#Wh... what?! Fembris? How did the Fembris get here?!")
sm.setParam(57)
sm.sendSay("#bFembris?!")
sm.setParam(37)
sm.setInnerOverrideSpeakerTemplateID(9400597) # Gurnardson
sm.sendSay("#face0#F-Fembris?!")
sm.setParam(57)
sm.sendSay("#bGet back!")
sm.forcedMove(False, 400)
sm.sendDelay(1000)
sm.lockInGameUI(False, True)
sm.startQuest(64123)
sm.warp(867202700)
