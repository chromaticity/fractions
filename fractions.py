def gcd(x, y):
	if x == 0:
		return y

	return gcd(y % x, x)


def decimaldigits(x):
	return 1 if x%1 == 0 else len(str(x-int(x)))-2

#Fraction class
class Fraction:
	def simplify(self):
		gcf = gcd(abs(self.numerator), abs(self.denominator))
		self.numerator /= gcf
		self.denominator /= gcf

		if self.numerator < 0 and self.denominator < 0:
			self.numerator *= -1
			self.denominator *= -1

	def __init__(self, numerator = 0, denominator = 1):
		multiplyfactor = 10 ** max(decimaldigits(numerator), decimaldigits(denominator))
		self.numerator = multiplyfactor * numerator
		self.denominator = multiplyfactor * denominator
		self.simplify()

	def __internalstring(self, mixed = False):
		if self.denominator == 1:
			return str(int(self.numerator))
		elif self.numerator == 0:
			return "0"
		else:
			if mixed:
				wholepart = self.numerator // self.denominator
				fractionalnumerator = self.numerator-wholepart*self.denominator
				fractionstring = str(int(fractionalnumerator))+"/"+str(int(self.denominator))
				if wholepart == 0:
					return fractionstring
				else:
					return str(int(wholepart))+" "+fractionstring
			else:
				return str(int(self.numerator))+"/"+str(int(self.denominator))
	
	def __str__(self):
		return self.__internalstring()

	def mixedstring(self):
		return self.__internalstring(True)

	def __add__(self, other):
		return Fraction(self.numerator*other.denominator+other.numerator*self.denominator, self.denominator*other.denominator)

	def __sub__(self, other):
		return self+(-other)

	def __mul__(self, other):
		return Fraction(self.numerator*other.numerator, self.denominator*other.denominator)

	def __truediv__(self, other):
		return self * other.recip()

	def __float__(self):
		return self.numerator / self.denominator

	def __neg__(self):
		return Fraction(self.numerator * -1, self.denominator)

	def recip(self):
		return Fraction(self.denominator, self.numerator)

frac = Fraction(225, 16)
frac2 = Fraction(8, 45)
frac3 = Fraction(2, 5)

print(frac*frac2*frac3)
u