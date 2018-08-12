from tkinter import *
from AutocompleteEntry import AutocompleteEntry
from Geolocator import Geolocator


GL = Geolocator()
par = GL.get_pers_addr_reg()
acr = GL.get_addr_coord_reg()

list_names = list(par.keys())
list_addr = list(par.values())
y_list = [pd["Y"] for pd in acr["AddressData"]["AddressPoint"]]
x_list = [pd["X"] for pd in acr["AddressData"]["AddressPoint"]]

def search_name_1(event):
	name = e11.get()
	RoadName, RoadNumber = GL.get_addr_from_name(name)
	y,x = GL.get_coord_from_addr(RoadName,RoadNumber)
	
	e21.delete(0,END)
	e31.delete(0,END)
	e41.delete(0,END)
	
	if RoadName is None:
		e21.insert(10,"None")
	else:
		e21.insert(10,RoadName+" "+RoadNumber)
		e21.selection(None)
	if y is None:
		e31.insert(10,"None")
		e41.insert(10,"None")
	else:
		e31.insert(10, y)
		e41.insert(10, x)
	calc_distance()
def search_name_2(event):
	name = e12.get()
	RoadName, RoadNumber = GL.get_addr_from_name(name)
	y,x = GL.get_coord_from_addr(RoadName,RoadNumber)
	
	e22.delete(0,END)
	e32.delete(0,END)
	e42.delete(0,END)
	
	if RoadName is None:
		e22.insert(10,"None")
	else:
		e22.insert(10,RoadName+" "+RoadNumber)
		e22.selection(None)
	if y is None:
		e32.insert(10,"None")
		e42.insert(10,"None")
	else:
		e32.insert(10, y)
		e42.insert(10, x)
	calc_distance()
def search_addr_1(event):
	addr = e21.get()
	if len(addr.split(" "))>1:
		RoadName = addr.split(" ")[0]
		RoadNumber = addr.split(" ")[1]
		name = GL.get_name_from_addr(RoadName, RoadNumber)
		y,x = GL.get_coord_from_addr(RoadName,RoadNumber)
	else:
		name = None
		y = None
	e11.delete(0,END)
	e31.delete(0,END)
	e41.delete(0,END)
	
	if name is None:
		e11.insert(10,"None")
	else:
		e11.insert(10,name)
		e11.selection(None)
	if y is None:
		e31.insert(10,"None")
		e41.insert(10,"None")
	else:
		e31.insert(10, y)
		e41.insert(10, x)
	calc_distance()
def search_addr_2(event):
	addr = e22.get()
	if len(addr.split(" "))>1:
		RoadName = addr.split(" ")[0]
		RoadNumber = addr.split(" ")[1]
		name = GL.get_name_from_addr(RoadName, RoadNumber)
		y,x = GL.get_coord_from_addr(RoadName,RoadNumber)
	else:
		name = None
		y = None
	e12.delete(0,END)
	e32.delete(0,END)
	e42.delete(0,END)
	
	if name is None:
		e12.insert(10,"None")
	else:
		e12.insert(10,name)
		e12.selection(None)
	if y is None:
		e32.insert(10,"None")
		e42.insert(10,"None")
	else:
		e32.insert(10, y)
		e42.insert(10, x)
	calc_distance()
def search_coord_1(event):
	y = e31.get()
	x = e41.get()
	RoadName, RoadNumber = GL.get_addr_from_coord(y,x)
	if RoadName is None:
		name = None
	else:
		name = GL.get_name_from_addr(RoadName,RoadNumber)
	
	e11.delete(0,END)
	e21.delete(0,END)
	
	if RoadName is None:
		e21.insert(10,"None")
	else:
		e21.insert(10,RoadName+" "+RoadNumber)
		e21.selection(None)
	if name is None:
		e11.insert(10,"None")
	else:
		e11.insert(10, name)
		e11.selection(None)
	calc_distance()
def search_coord_2(event):
	y = e32.get()
	x = e42.get()
	RoadName, RoadNumber = GL.get_addr_from_coord(y,x)
	if RoadName is None:
		name = None
	else:
		name = GL.get_name_from_addr(RoadName,RoadNumber)
	
	e12.delete(0,END)
	e22.delete(0,END)
	
	if RoadName is None:
		e22.insert(10,"None")
	else:
		e22.insert(10,RoadName+" "+RoadNumber)
		e22.selection(None)
	if name is None:
		e12.insert(10,"None")
	else:
		e12.insert(10, name)
		e12.selection(None)
	calc_distance()

def calc_distance():
	ya = e31.get()
	xa = e41.get()
	yb = e32.get()
	xb = e42.get()
	if ya =="None" or yb =="None" or ya =="" or yb =="":
		labelText.set("Distance: Choose two positions")
	else:
		dist = GL.calc_euclidean_distance(ya,xa,yb,xb)
		labelText.set("Distance: "+"{0:.2f}".format(dist))


top = Tk()
top.title("Main")

top.minsize(width=500, height=250)

Label(top, text="Name").grid(row=0)
Label(top, text="Address").grid(row=1)
Label(top, text="Coordinates").grid(row=2)

Label(top, text="Name").grid(row=0, column=3)
Label(top, text="Address").grid(row=1, column=3)
Label(top, text="Coordinates").grid(row=2, column=3)



e11 = AutocompleteEntry(list_names, top)
e21 = AutocompleteEntry(list_addr, top)
e31 = Entry(top)
e41 = Entry(top)

e12 = AutocompleteEntry(list_names, top)
e22 = AutocompleteEntry(list_addr, top)
e32 = Entry(top)
e42 = Entry(top)

e11.bind("<Return>", search_name_1)
e21.bind("<Return>", search_addr_1)
e31.bind("<Return>", search_coord_1)
e41.bind("<Return>", search_coord_1)
e12.bind("<Return>", search_name_2)
e22.bind("<Return>", search_addr_2)
e32.bind("<Return>", search_coord_2)
e42.bind("<Return>", search_coord_2)

e11.grid(row=0, column=1)
e21.grid(row=1, column=1)
e31.grid(row=2, column=1)
e41.grid(row=3, column=1)

e12.grid(row=0, column=4)
e22.grid(row=1, column=4)
e32.grid(row=2, column=4)
e42.grid(row=3, column=4)

labelText = StringVar()
labelText.set("Distance: Choose two positions")
dist_label = Label(top, textvariable=labelText).grid(row=4, column=2)


top.mainloop()