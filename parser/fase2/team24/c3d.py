
from datetime import date
from variables import tabla as ts
from variables import NombreDB 
from variables import cont 
import tablaDGA as TAS
import sql as sql 
import mathtrig as mt
from reportTable import *


pila = []
for i in range(100):
    pila.append(i)

def ejecutar():
	global cont
	global ts
	NombreDB = ts.nameDB
	
	sql.execute("DROP INDEX idx_bodega;")
	sql.execute("DROP INDEX x;")
	graphTable(ts)
ejecutar()