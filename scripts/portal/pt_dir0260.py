# id 1 (dir0260), field 867200260
sm.createQuestWithQRValue(64014, "scene1=1;scene2=1;scene4=1;mapIdx=0")
sm.createQuestWithQRValue(64014, "scene1=1;scene2=1;scene4=2;mapIdx=0")
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.moveCamera(True, 5000, 0, 0)
sm.spawnNpc(9400675, -445, 125)
sm.showNpcSpecialActionByTemplateId(9400675, "summon", 0)
sm.sendDelay(500)
sm.zoomCamera(1000, 2000, 2000, -200, 90)
sm.sendDelay(500)
sm.showNpcSpecialActionByTemplateId(9400675, "regen", 0)
sm.sendDelay(800)
sm.forcedFlip(True)
sm.showNpcSpecialActionByTemplateId(9400675, "skill1", 0)
sm.sendDelay(2000)
sm.playExclSoundWithDownBGM("Mob.img/9402244/skill1", 100)
sm.sendDelay(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.showFieldEffect("monsterPark/stageEff/clear", 0)
sm.playSound("Party1/Clear", 100)
sm.warp(867200281)
