# id 940202029 (null), field 940202029
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(True, 255, 0, 0, 0, 0)
sm.spawnNpc(3001372, 800, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.spawnNpc(3001372, 700, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.spawnNpc(3001372, 600, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.spawnNpc(3001372, 500, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.spawnNpc(3001309, 900, 30)
sm.showNpcSpecialActionByTemplateId(3001309, "summon", 0)
sm.spawnNpc(3001301, 1130, -40)
sm.showNpcSpecialActionByTemplateId(3001301, "summon", 0)
sm.spawnNpc(3001302, 1370, -40)
sm.showNpcSpecialActionByTemplateId(3001302, "summon", 0)
sm.spawnNpc(3001303, 1260, -40)
sm.showNpcSpecialActionByTemplateId(3001303, "summon", 0)
sm.spawnNpc(3001304, 1220, 65)
sm.showNpcSpecialActionByTemplateId(3001304, "summon", 0)
sm.spawnNpc(3001305, 1310, 65)
sm.showNpcSpecialActionByTemplateId(3001305, "summon", 0)
sm.spawnNpc(3001316, 1650, 34)
sm.showNpcSpecialActionByTemplateId(3001316, "summon", 0)
sm.spawnNpc(3001315, 1600, 50)
sm.showNpcSpecialActionByTemplateId(3001315, "summon", 0)
sm.spawnNpc(3001317, 1710, 50)
sm.showNpcSpecialActionByTemplateId(3001317, "summon", 0)
sm.spawnNpc(3001318, 1670, 65)
sm.showNpcSpecialActionByTemplateId(3001318, "summon", 0)
sm.spawnNpc(3001319, 1750, 65)
sm.showNpcSpecialActionByTemplateId(3001319, "summon", 0)
sm.zoomCamera(0, 2000, 0, 1500, 65)
sm.forcedFlip(True)
sm.setSpeakerType(3)
sm.setParam(37)
sm.setColor(1)
sm.setInnerOverrideSpeakerTemplateID(3001350) # Illium
sm.sendNext("#face0#What is going on?")
sm.sendSay("#face0#Why is everyone...")
sm.blind(True, 255, 0, 0, 0, 0)
sm.sendDelay(1200)
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1400)
sm.zoomCamera(500, 2000, 500, 1000, 65)
sm.sendDelay(1500)
sm.setInnerOverrideSpeakerTemplateID(3001301) # Agate
sm.sendNext("#face3#Darius? You!")
sm.setInnerOverrideSpeakerTemplateID(3001309) # Darius
sm.sendSay("#face0#It didn't have to come to this. \r\nYou could have handed over the Elder Crystal without a fight.")
sm.setInnerOverrideSpeakerTemplateID(3001302) # Professor Kalsat
sm.sendSay("#face0#Agate, it's too late. The sanctuary is lost.")
sm.setInnerOverrideSpeakerTemplateID(3001301) # Agate
sm.sendSay("#face3#I can't give up hope yet.")
sm.setInnerOverrideSpeakerTemplateID(3001309) # Darius
sm.sendSay("#face2#Don't pity your precious sanctuary. Pity yourselves, for soon you will meet your end.")
sm.zoomCamera(500, 2000, 500, 1820, 65)
sm.sendDelay(1500)
sm.spawnNpc(3001372, 1900, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.spawnNpc(3001372, 2000, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.spawnNpc(3001372, 2100, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.spawnNpc(3001372, 2200, -1)
sm.showNpcSpecialActionByTemplateId(3001372, "summon", 0)
sm.flipNpcByTemplateId(3001316, False)
sm.flipNpcByTemplateId(3001315, False)
sm.flipNpcByTemplateId(3001317, False)
sm.flipNpcByTemplateId(3001318, False)
sm.flipNpcByTemplateId(3001319, False)
sm.sendDelay(30)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81035949, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81035950, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81035951, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81035952, 0, 0)
sm.showEffect("Effect/OnUserEff.img/emotion/oh", 0, 0, -20, 0, 81035953, 0, 0)
sm.sendDelay(1000)
sm.setInnerOverrideSpeakerTemplateID(3001318) # Model Student
sm.sendNext("We're surrounded!!")
sm.setInnerOverrideSpeakerTemplateID(3001301) # Agate
sm.sendSay("#face3#Students, take shelter in the school! Now!")
sm.setInnerOverrideSpeakerTemplateID(3001350) # Illium
sm.sendSay("#face9#Let me help!")
sm.setInnerOverrideSpeakerTemplateID(3001301) # Agate
sm.sendSay("#face3#You can help by protecting your friends.")
sm.sendSay("#face3#Now go!")
sm.setInnerOverrideSpeakerTemplateID(3001350) # Illium
sm.sendSay("#face0#Okay!")
sm.lockInGameUI(False, True)
sm.warp(940202034)