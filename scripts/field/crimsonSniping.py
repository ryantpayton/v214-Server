# id 301050100 (Hidden Street : Mini-game: Ghost Sniper), field 301050100
sm.createQuestWithQRValue(31359, "")
sm.lockInGameUI(True, False)
sm.hideUser(True)
sm.showFieldEffect("killing/first/start", 0)
sm.createQuestWithQRValue(31359, "mission=success")
sm.startQuest(31262)
sm.showFieldEffect("monsterPark/clear", 0)
sm.playSound("Party1/Clear", 100)
sm.createQuestWithQRValue(31359, "")
sm.hideUser(False)
sm.lockInGameUI(False, True)
sm.warp(301000000)