import xmltodict
import numpy

class Geolocator:
	'Class for Geolocation'
	
	def __init__(self, *args):
	
		if len(args)!=2:
			addr_coord_reg_file = r"Data\Osoitteet.xml"
			pers_addr_reg_file = r"Data\Henkilot.txt"
		else:
			addr_coord_reg_file = args[0]
			pers_addr_reg_file = args[1]
		
		with open(addr_coord_reg_file) as fd:
			self.addr_coord_reg = xmltodict.parse(fd.read())
		
		self.pers_addr_reg = {}
		f = open(pers_addr_reg_file, "r")
		for line in f:
			if "," in line:
				self.pers_addr_reg[line.split(",")[0]] = line.split(",")[1].rstrip("\n")
				
				
	## Return python dictionaries ##		
	def get_addr_coord_reg(self):
		return self.addr_coord_reg
		
	def get_pers_addr_reg(self):
		return self.pers_addr_reg
		
		
	## Return name, address or coordinates based on one of the other ##	
	def get_addr_from_name(self, name):
		if name in self.pers_addr_reg.keys():
			addr = self.pers_addr_reg[name]
			return addr.split(" ")[0], addr.split(" ")[1]
		else:
			return None, None
			
	def get_name_from_addr(self, RoadName, RoadNumber):
		return next((name for name, addr in self.pers_addr_reg.items() if addr == RoadName+" "+RoadNumber),None)
	
	def get_coord_from_addr(self, RoadName, RoadNumber):
		addr_found = False
		for i in range(len(self.addr_coord_reg["AddressData"]["AddressPoint"])):
			if self.addr_coord_reg["AddressData"]["AddressPoint"][i]["RoadName"] == RoadName and self.addr_coord_reg["AddressData"]["AddressPoint"][i]["RoadNumber"] == RoadNumber:
				y = self.addr_coord_reg["AddressData"]["AddressPoint"][i]["Y"]
				x = self.addr_coord_reg["AddressData"]["AddressPoint"][i]["X"]
				addr_found = True
		if addr_found:
			return y,x
		else:
			return None, None
	
	def get_addr_from_coord(self, y,x):
		pd = next((pd for pd in self.addr_coord_reg["AddressData"]["AddressPoint"] if pd["Y"]==y and pd["X"]==x),None)
		if pd is None:
			return None, None
		else:
			return pd["RoadName"], pd["RoadNumber"]
			
	## Calculate distance between two points ##
	def calc_euclidean_distance(self,ya,xa,yb,xb):
		ya = float(ya.replace(",","."))
		xa = float(xa.replace(",","."))
		yb = float(yb.replace(",","."))
		xb = float(xb.replace(",","."))
		
		a = numpy.array((ya, xa))
		b = numpy.array((yb, xb))
		return numpy.linalg.norm(a-b)