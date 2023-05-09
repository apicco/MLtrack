from trajalign.traj import Traj

class Traj( Traj ):
	
	__slots__ = Traj.__slots__
    __slots__.append( '_m2' )
    __slots__.append( '_m3' )
    __slots__.append( '_m4' )
    __slots__.append( '_m5' )
    __slots__.append( '_u02' )
    __slots__.append( '_u20' )
    __slots__.append( '_u11' )
    __slots__.append( '_ecc' )
    __slots__.append( '_m2_err' )
    __slots__.append( '_m3_err' )
    __slots__.append( '_m4_err' )
    __slots__.append( '_m5_err' )
    __slots__.append( '_u02_err' )
    __slots__.append( '_u20_err' )
    __slots__.append( '_u11_err' )
	

	def __init__(self,**annotations):

		#Trajectory main attributes
        super().__init__( **annotations )
 
		self._m2 = array([],dtype='float64') # second moment of brightness (f is the first)
		self._m3 = array([],dtype='float64') # third moment of brightness 
		self._m4 = array([],dtype='float64') # fourth moment of brightness 
		self._m5 = array([],dtype='float64') # fifth moment of brightness 
		self._u02 = array([],dtype='float64') # second moment of brightness along y 
		self._u20 = array([],dtype='float64') #	second moment of brightness along x
		self._u11 = array([],dtype='float64') # covariance brightness 
		self._ecc = array([],dtype='float64') # trajectory eccentricity

		self._m2_err = array([],dtype='float64')
		self._m3_err = array([],dtype='float64')
		self._m4_err = array([],dtype='float64')
		self._m5_err = array([],dtype='float64')
		self._u02_err = array([],dtype='float64')
		self._u20_err = array([],dtype='float64')
		self._u11_err = array([],dtype='float64')


	#Getters
	def m2(self,*items):
		if (len(items)==0): return self._m2
		elif len(items) == 1 : return self._m2[ items ]
		else: 
			try:
				return(self._m2[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().m2 are out of bounds')

	def m3(self,*items):
		if (len(items)==0): return self._m3
		elif len(items) == 1 : return self._m3[ items ]
		else: 
			try:
				return(self._m3[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().m3 are out of bounds')

	def m4(self,*items):
		if (len(items)==0): return self._m4
		elif len(items) == 1 : return self._m4[ items ]
		else: 
			try:
				return(self._m4[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().m4 are out of bounds')

	def m5(self,*items):
		if (len(items)==0): return self._m5
		elif len(items) == 1 : return self._m5[ items ]
		else: 
			try:
				return(self._m5[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().m5 are out of bounds')

	def u02(self,*items):
		if (len(items)==0): return self._u02
		elif len(items) == 1 : return self._u02[ items ]
		else: 
			try:
				return(self._u02[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().u02 are out of bounds')

	def u20(self,*items):
		if (len(items)==0): return self._u20
		elif len(items) == 1 : return self._u20[ items ]
		else: 
			try:
				return(self._u20[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().u20 are out of bounds')

	def u11(self,*items):
		if (len(items)==0): return self._u11
		elif len(items) == 1 : return self._u11[ items ]
		else: 
			try:
				return(self._u11[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().u11 are out of bounds')

	def m2_err(self,*items):
		if (len(items)==0): return self._m2_err
		elif len(items) == 1 : return self._m2_err[ items ]
		else:
			try:
				return(self._m2_err[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().f_err are out of bounds')
	
	def m3_err(self,*items):
		if (len(items)==0): return self._m3_err
		elif len(items) == 1 : return self._m3_err[ items ]
		else: 
			try:
				return(self._m3_err[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().m3_err are out of bounds')

	def m4_err(self,*items):
		if (len(items)==0): return self._m4_err
		elif len(items) == 1 : return self._m4_err[ items ]
		else: 
			try:
				return(self._m4_err[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().m4_err are out of bounds')

	def m5_err(self,*items):
		if (len(items)==0): return self._m5_err
		elif len(items) == 1 : return self._m5_err[ items ]
		else: 
			try:
				return(self._m5_err[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().m5_err are out of bounds')

	def u02_err(self,*items):
		if (len(items)==0): return self._u02_err
		elif len(items) == 1 : return self._u02_err[ items ]
		else: 
			try:
				return(self._u02_err[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().u02_err are out of bounds')

	def u20_err(self,*items):
		if (len(items)==0): return self._u20_err
		elif len(items) == 1 : return self._u20_err[ items ]
		else: 
			try:
				return(self._u20_err[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().u20_err are out of bounds')

	def u11_err(self,*items):
		if (len(items)==0): return self._u11_err
		elif len(items) == 1 : return self._u11_err[ items ]
		else: 
			try:
				return(self._u11_err[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().u11_err are out of bounds')

	def ecc(self,*items):
		if (len(items)==0): return self._ecc
		elif len(items) == 1 : return self._ecc[ items ]
		else: 
			try:
				return(self._ecc[[item for item in items]])
			except IndexError:
				print('Indexes in Traj().ecc are out of bounds')
	
