# StopLoss class

class StopLoss:
	# global positiontype
	# global currentprice, sltp, sltppercent, dynamicsltp
	
	# sltptriggeredcheck, dynsltptriggeredcheck = false

	def __init__(self, positiontype, currentprice, sltp, sltppercent, dynamicsltp, prevdynsltp, sltptriggeredcheck, dynsltptriggeredcheck):
		# global positiontype
		# global currentprice, sltp, sltppercent, dynamicsltp
		self.positiontype = str(positiontype).lower()
		self.currentprice = float(currentprice)
		self.sltp = float(sltp)
		self.sltppercent = float(sltppercent)
		self.dynamicsltp = float(dynamicsltp)
		self.prevdynsltp = float(prevdynsltp)
		self.sltptriggeredcheck = sltptriggeredcheck # False
		self.dynsltptriggeredcheck = dynsltptriggeredcheck # False
		
	def GetSLTP(positiontype, currentprice, sltppercent):
		# global positiontype
		# global currentprice, sltp, sltppercent, dynamicsltp
		if str(positiontype).lower() == "buy" :
			sltp = float(currentprice - ((sltppercent / 100.0) * currentprice))
		else:
			sltp = float(currentprice + ((sltppercent / 100.0) * currentprice))
		return sltp
		
	def GetSLTPPercent(positiontype, currentprice, sltp):
		# global positiontype
		# global currentprice, sltp, sltppercent, dynamicsltp
		if str(positiontype).lower() == "buy" :
			sltppercent = float(100.0 - ((sltp / currentprice) * 100.0))
		else:
			sltppercent = float(((sltp / currentprice) * 100.0) - 100.0)
		return sltppercent
		
	def GetDynamicSLTP(positiontype, currentprice, sltppercent, prevdynsltp):
		# global positiontype
		# global currentprice, sltp, sltppercent, dynamicsltp
		# if str(positiontype).lower() == "buy" :
		# 	dynamicsltp = float(currentprice - ((sltppercent / 100.0) * currentprice))
		# 	if sltp > dynamicsltp :
		# 		dynamicsltp = sltp
		# else:
		# 	dynamicsltp = float(currentprice + ((sltppercent / 100.0) * currentprice))
		# 	if sltp < dynamicsltp :
		# 		dynamicsltp = sltp
		# prevdynsltp = dynamicsltp
		if str(positiontype).lower() == "buy":
			dynamicsltp = float(currentprice - ((sltppercent / 100.0) * currentprice))
			if prevdynsltp > dynamicsltp:
				dynamicsltp = prevdynsltp
		else:
			dynamicsltp = float(currentprice + ((sltppercent / 100.0) * currentprice))
			if prevdynsltp < dynamicsltp:
				dynamicsltp = prevdynsltp
		# prevdynsltp = dynamicsltp
		return dynamicsltp
		
	def IsSLTPTriggered(positiontype, currentprice, sltp):
		# global positiontype
		# global currentprice, sltp
		sltptriggeredcheck = False
		if str(positiontype).lower() == "buy" :
			if currentprice <= sltp :
				sltptriggeredcheck = True
		else:
			if currentprice >= sltp :
				sltptriggeredcheck = True
		return sltptriggeredcheck
		
	def IsDynamicSLTPTriggered(positiontype, currentprice, dynamicsltp):
		# global positiontype
		# global currentprice, dynamicsltp
		dynsltptriggeredcheck = False
		if str(positiontype).lower() == "buy" :
			if currentprice <= dynamicsltp :
				dynsltptriggeredcheck = True
		else:
			if currentprice >= dynamicsltp :
				dynsltptriggeredcheck = True
		return dynsltptriggeredcheck
