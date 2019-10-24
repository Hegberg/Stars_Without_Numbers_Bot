

import Colour

class PlanetType:
	def __init__(self, colour):
		self.colour = colour

class Desert(PlanetType):
	def __init__(self):
		super(Desert, self).__init__(Colour.desert)
		#PlanetType.__init__(self, Colour.desert)

class MoltenLava(PlanetType):
	def __init__(self):
		super(MoltenLava, self).__init__(Colour.moltenLava)
		#PlanetType.__init__(self, Colour.moltenLava)

class Forset(PlanetType):
	def __init__(self):
		super(Forset, self).__init__(Colour.forest)
		#PlanetType.__init__(self, Colour.forest)

class Ocean(PlanetType):
	def __init__(self):
		super(Ocean, self).__init__(Colour.ocean)
		#PlanetType.__init__(self, Colour.ocean)

class Tundra(PlanetType):
	def __init__(self):
		super(Tundra, self).__init__(Colour.tundra)
		#PlanetType.__init__(self, Colour.tundra)
		