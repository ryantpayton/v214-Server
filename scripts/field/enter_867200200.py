# id 867200200 (Abrup Basin : Steep Mountain Trail), field 867200200
sm.createQuestWithQRValue(64014, "scene1=0;mapIdx=0")
sm.lockInGameUI(True, False)
sm.removeAdditionalEffect()
sm.blind(False, 0, 0, 0, 0, 1000)
sm.sendDelay(1000)
sm.forcedMove(False, 50)
sm.sendDelay(300)
sm.forcedInput(6)
sm.sendDelay(1000)
sm.zoomCamera(1000, 1000, 3000, 740, -400)
sm.sendDelay(1000)
sm.setSpeakerType(3)
sm.setParam(57)
sm.setColor(1)
sm.sendNext("#b(How did that human trainwreck get all the way up there?)")
sm.sendDelay(1500)
sm.zoomCamera(1000, 1000, 3000, 2330, -400)
sm.sendDelay(2000)
sm.sendNext("#b(Aw, nuts... If he follows me down, he's getting eaten for sure.)")
sm.sendSay("#b(Better clear out the monsters along the way, for his sake.)")
sm.sendDelay(500)
sm.sendDelay(1000)
sm.moveCamera(True, 0, 0, 0)
sm.lockInGameUI(False, True)
sm.showFieldEffect("monsterPark/stageEff/stage", 0)
sm.showFieldEffect("monsterPark/stageEff/number/1", 0)
sm.showFieldEffect("monsterPark/clear", 0)
sm.playSound("Party1/Clear", 100)
