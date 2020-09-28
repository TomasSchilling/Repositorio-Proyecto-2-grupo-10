

import numpy as np

g = 9.81 #kg*m/s^2


class Barra(object):

	"""Constructor para una barra"""
	def __init__(self, ni, nj, R, t, E, ρ, σy):
		super(Barra, self).__init__()
		self.ni = ni
		self.nj = nj
		self.R = R
		self.t = t
		self.E = E
		self.ρ = ρ
		self.σy = σy

	def obtener_conectividad(self):
		"""Implementar"""
		return 

	def calcular_area(self):
		"""Calcula el area de una barra circular"""
		return R**2*np.pi

	def calcular_largo(self, reticulado):

		return np.sqrt((ni[0]-nj[0])**2+(ni[1]-nj[1])**2)

	def calcular_peso(self, reticulado):

		return ρ* calcular_largo(Barra)*calcular_area