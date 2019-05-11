#!/usr/bin/env python3

import random 
#import discord_webhook

#from discord_webhook import DiscordWebhook

class Province:
  def __init__(self, name, role, santablanca, unidad):
    self.name=name
    self.role=role
    self.santablanca=santablanca
    self.unidad=unidad
    self.neighbours=[]
    self.santablancabases=[]
    self.unidadbases=[]

class Objective:
  def __init__(self, name, regions_available, replay, stage):
    self.name=name
    self.regions_available=regions_available
    self.replay=replay
    self.stage=stage

def getRandomPercentage():
  percentage=random.randint(0,100)
  return percentage

def roll20():
  diceroll=random.randint(1,20)
  return diceroll

def getRandomFromList(item_list):
  result=random.choice(item_list)
  return result

def pickRandomFromList(item_list):
  count=0
  result=random.choice(item_list)
  for item in item_list:
    if item == result:
      item_list.pop(count)
    count+=1
  return result

def createMission(province, stage="Any"):
  # generate 1st region and mission
  objective=getRandomFromList(objectives)

  # remove a non replayable objective once picked
  if objective.replay == "False":
    count=0
    for item in objectives:
      if objective.name == item.name:
        objectives.pop(count)
      count+=1
  targets=["Unidad", "Santa Blanca"]

  # check a starting objective can only be picked first
  if stage != "First" and objective.stage == "First":
    while objective.stage == "First":
      objective=getRandomFromList(objectives)

  # check an ending objective can only be picked last
  if stage != "Last" and objective.stage == "Last":
    while objective.stage == "Last":
      objective=getRandomFromList(objectives)

  target=random.choice(targets)
  enemy=""
  target_base=""
  while enemy=="" and target_base == "":
    if target=="Unidad":
      if province.unidadbases !=[]:
        target_base=getRandomFromList(province.unidadbases)
        enemy=target
      elif province.unidadbases ==[]:
        target_base=getRandomFromList(province.santablancabases)
        enemy="Santa Blanca"

    if target=="Santa Blanca":
      if province.santablancabases !=[]:
        target_base=getRandomFromList(province.santablancabases)
        enemy=target
      elif province.santablancabases ==[]:
        target_base=getRandomFromList(province.unidadbases)
        enemy="Unidad"

  province=province.name
  objective=objective.name

  if "Convoy Raid" in objective or "Supply Raid" in objective or "Radio Defence" in objective:
    target_base=""
    enemy="Unidad/Santa Blanca"

  mission=province+"\n"+"("+enemy+") "+target_base+"\n"+objective+"\n"

  return mission
  # generate location for mission

# create all provinces with their respective neighbour regions
barvechos=Province("Barvechos", "Smuggling", "True", "False")
barvechos.neighbours=["Remanzo", "San Mateo", "Itacua", "Pucara", "Montuyoc", "Mojocoyo"]
barvechos.santablancabases=["Outpost at -15.9046:-65.2770", "Outpost at -16.0527:-65.6560", "Nidia Flores' Hacienda at -16.0613:-65.2286", "Barvechos Base at -16.2979:-65.7998", "Outpost at -16.4010:-65.3331"]
barvechos.unidadbases=[]

caimanes=Province("Caimanes","Smuggling", "True", "True" )
caimanes.neighbours=["Villa Verde", "La Cruz", "Ocoro"]
caimanes.santablancabases=["Caimanes Base at -17.0870:-59.5111", "Puerto Chico at -17.4332:-59.9147", "Outpost at -16.5258:-59.7029", "Riverine Checkpoint at -16.8887:-59.8687", "San Miguel Ruins at -17.1435:-59.3558", "Los Hombres Jaguares at -17.6992:-60.4047", "Buchon House at -17.8809:-59.9572", "Outpost at -17.8872:-60.4476", "Frontera at -18.3046:-59.6977"]
caimanes.unidadbases=["Combat Outpost at -17.5576:-60.0290"]

espiritu_santo=Province("Espiritu Santo","Influence", "True", "True")
espiritu_santo.neighbours=["Villa Verde", "Ocoro", "P.N. De Agua Verde", "Monte Puncu"]
espiritu_santo.santablancabases=["Outpost at -13.4493:-59.8263", "Alta Gracia Mine at -13.8579:-59.8367", "Experimental Farm at -13.9279:-60.6678 (Activate Gold Rush North)", "Outpost at -13.8147:-59.7741", "Buchone Chapel at -13.3885:-59.8769", "Espiritu Santo Base at -14.2258:-60.4062", "Pilgrim House at -14.3262:-60.5883", "Santa Muerte Sanctuary at -14.3140:-60.2679", "Pilgrim House at -14.3943:-59.8732", "Guari at -14.5689:-60.8857", "Guari Mine (Activate Gold Rush South) at -14.7254:-61.1261", "Los Humildes Pereginos at -14.6974:-60.1638", "Outpost at -14.9157:-60.6743", "Miski Secure Barn at -14.9417:-60.4722", "Outpost at -15.0616:-60.1876", "Bahia Floresta at -15.1089:-61.1704", "Buchon House at -15.5881:-61.306221"]
espiritu_santo.unidadbases=["Observation Post at -14.4879:-60.5534", "Observation Post at -14.9171:-60.3187"]

flor_de_oro=Province("Flor De Oro","Security", "True", "True")
flor_de_oro.neighbours=["La Cruz", "Libertad", "Malca"]
flor_de_oro.santablancabases=["Halcone House at -19.5860:-60.8542"]
flor_de_oro.unidadbases=["Train Freight Yard at -18.9769:-61.0279", "Combat Outpost at-19.1658:-60.7622", "Combat Outpost at -19.3973:-61.4335", "Combat Outpost at -19.5399:-61.3875", "M.O.B Jaguar at -19.7258:-61.3069", "Checkpoint at -19.7196:-60.6198", "Unidad Military Hospital at -20.1173:-61.3039", "Huma Chua Saw Mill at -20.009:-61.0725", "Observation Post at -20.2876:-60.9279", "Makeshift Runway at -20.4355:-61.1149", "Chorrilos Wood Storage at -20.5666:-60.9740", "F.O.B Serpiente at -20.7047:-60.7092", "Armadillo Hunting Lodge at -19.7604:-60.9505"]

inca_camina=Province("Inca Camina", "Smuggling", "True", "False")
inca_camina.neighbours=["Montuyoc", "Pucara", "Malca"]
inca_camina.santablancabases=["Outpost at -18.3782:-65.4316", "Inca Camina Base at -18.8244:-65.8488", "Inca Chaca at -18.9817:-66.3338", "Inca Camina Freight Yard at -19.3348:-65.6077", "Inca Ruins at -19.7177:-66.0793", "Nuevo Mondo (Activate La Cabra) at -20.7704:-66.2638", "Julpe Alto at -20.0327:-65.0955", "Gas Station Via B-Gas at -19.4551:-65.7370", "Nevado Llamiru Garage at -19.5616:-64.8941", "Sicario House at -19.7804:-64.2542"]
inca_camina.unidadbases=[]

itacua=Province("Itacua", "Security", "True", "True")
itacua.neighbours=["P.N. De Agua Verde", "Ocoro", "La Cruz", "Pucara", "Montuyoc", "Barvechos", "San Mateo"]
itacua.santablancabases=["Buena Vida at -16.5783:-62.9360", "Culta at -16.8427:-63.8123", "Yopil at -16.5876:-63.6337", "Outpost at -16.9820:-63.0898", "Sicario House at -17.4471:-63.8672", "Outpost at -17.7863:-63.7272", "La Casa Del Mexicano at -17.9384:-62.9972", "Itacua Base at -18.0587:-63.0224"]
itacua.unidadbases=["Observation Post at -17.5011:-64.3476", "F.O.B Armadillo at -17.2320:-62.5995"]

koani=Province("Koani", "Smuggling", "True", "True")
koani.neighbours=["Media Luna", "Remanzo", "Mojocoyo"]
koani.santablancabases=["Koani Air Base at -13.4093:-66.8731", "Koani Lithium Mine at -13.3871:-66.2418", "Truck Stop Mamani at -13.6394:-66.1433", "Truck Depot at -13.6723:-65.7238", "Santa Blanca Living District at -13.5149:-65.6601", "Huertes Mine at -13.4265:-65.5742", "Koani Railway Camp at -13.5467:-65.3957", "Makeshift Runway at -13.9494:-67.1305", "Outpost at -14.0440:-66.1611", "Locotal Mine at -14.1256:-66.0708", "Outpost at -14.1991:-65.9867", "Outpost at -14.2922:-66.6190", "Improvised Runway at -14.4084:-66.8874", "Outpost at -14.5843:-66.3809", "Train Cemetary at -14.7994:-66.9725", "El Buen Sal at -14.3152:-67.2641"]
koani.unidadbases=["Combat Outpost at -14.0201:-66.4676", "Combat Outpost at -14.1417:-65.7675"]

la_cruz=Province("La Cruz", "None", "True", "True")
la_cruz.neighbours=["Libertad", "Flor De Oro", "Malca", "Pucara", "Itacua", "Ocoro", "Caimanes"]
la_cruz.santablancabases=["Outpost at -19.0160:-62.0777", "Outpost at -18.5532:-61.5798", "Buchon House at -18.8285:-61.5322", "Makeshift Runway at -18.7510:-61.4100", "Santa Elena at -18.8326:-61.2646", "Outpost at -18.2215:-61.3355", "Outpost at -19.3545:-60.4568", "Outpost at -19.9750:-60.0452", "La Cruz Base at -18.8994:-59.6008"]
la_cruz.unidadbases=["Combat Outpost at -18.6185:-62.2939"] #removed because bug "F.O.B Vibora at -18.3184:-61.8807"

libertad=Province("Libertad", "Production", "True", "True")
libertad.neighbours=["Flor De Oro", "La Cruz"]
libertad.santablancabases=["Outpost at -19.7704:-59.8733", "Outpost at -21.0844:-59.6732"]
libertad.unidadbases=["Observation Post at -19.6004:-60.1480", "Forestry Site at -19.7670:-60.5152", "F.O.B OSO Hormiguero at -19.9627:-69.5835", "Viloma Gas Field at -20.1486:-60.4367", "Viloma Dos Oil Field at -20.1511:-60.2021", "Viloma Uno Oil Field at -20.1745:-60.0065", "Viloma Refinery at -20.2009:-59.8745", "Viloma at -20.2831:-59.8538", "Libertad Airport at -20.4104:-59.7259", "Viloma Cuatro Gas Field at -21.0073:-59.8257", "Combat Outpost at -20.8695:-59.9252"]

malca=Province("Malca", "Influence", "True", "True")
malca.neighbours=["Flor De Oro", "Pucara", "Inca Camina"]
malca.santablancabases=["Outpost at -19.7211:-63.7050", "Banado at -19.5943:-63.4107", "La Buena Muerte at -19.7512:-63.2402", "Holy Malca Base at -20.2008:-62.9102", "Uma Marca at -19.8787:-62.2842", "Uma Marca Mine at -20.0821:-62.1037", "Outpost at -20.7216:-61.8012", "Sicario House at -20.8358:-61.4405"]
malca.unidadbases=["Combat Outpost at -20.4258:-62.1464"]

media_luna=Province("Media Luna", "Security", "False", "True")
media_luna.neighbours=["Tabacal", "P.N. De Agua Verde", "San Mateo", "Remanzo", "Koani"]
media_luna.santablancabases=[]
media_luna.unidadbases=["Combat Outpost at -13.1606:-64.8185", "Checkpoint at -13.7862:-64.8963", "Combat Outpost at -13.5780:-64.5997", "Combat Outpost at -13.8744:-64.7063", "Shooting Range at -13.7710:-64.5424", "F.O.B Buitre at -13.4642:-64.1641", "Checkpoint at -13.8437:-64.2482", "M.O.B Condor at -14.2316:-64.2738", "Observation Post at -14.6724:-64.1607"]

mojocoyo=Province("Mojocoyo", "Security", "True", "True")
mojocoyo.neighbours=["Koani", "Remanzo", "Barvecos", "Montuyoc"]
mojocoyo.santablancabases=["Chacatal at -16.3945:-66.3850", "Sicario House at -16.4449:-66.1775", "Cocaine Hideout at -16.1433:-65.9715", "Outpost at -15.9195:-66.7552", "Cocaine Hideout at -15.8040:-66.4904", "Lieutenant House at -15.7563:-66.1692", "Cocaine Hideout at -15.7817:-65.6206", "Private Helipad at -15.5992:-65.4836", "Prison Camp at -15.3835:-66.1407", "Cocaine Hideout at -15.4128:-66.5337", "Makeshift Runway at -15.5185:-66.7080", "Capachunco at -15.2369:-66.2465", "Mojocoyo Base at -15.1087:-65.8853"]
mojocoyo.unidadbases=["Checkpoint at -15.1414:-66.1282"]

monte_puncu=Province("Monte Puncu", "None", "True", "False")
monte_puncu.neighbours=["Espiritu Santo", "P.N. De Agua Verde", "Tabacal"]
monte_puncu.santablancabases=["Experimental Farm 01 at -14.4834:-61.9416", "Secure Barn at -14.4194:-61.8816", "Outpost at -14.0092:-61.3377", "Chaca Barraca at -13.7347:-61.3759"]
monte_puncu.unidadbases=[]

montuyoc=Province("Montuyoc", "Security", "True", "False")
montuyoc.neighbours=["Inca Camina", "Mojocoyo", "Pucara", "Itacua", "Barvechos"]
montuyoc.santablancabases=["Choza Padre Mine at -17.4733:-67.0352", "Makeshift Runway at -17.0097:-66.0852", "Outpost at -16.5728:-65.9857", "Supply Depot at -17.2104:-65.7707", "Sicarios Boot Camp at -17.4075:-65.4886", "Montuyoc Training Base at -17.5932:-64.8947", "Checkpoint at -17.9589:-65.6220", "Choza Padre at -18.0881:-66.3717"]
montuyoc.unidadbases=[]

ocoro=Province("Ocoro", "Production", "True", "True")
ocoro.neighbours=["P.N. De Agua Verde", "Espiritu Santo", "Villa Verde", "Caimanes", "La Cruz", "Itacua"]
ocoro.santablancabases=["Coca Paste Factory at -15.3341:-62.1002", "Outpost at -15.4504:-61.5635", "Buchon House at -15.5785:-62.0624", "Outpost at -15.08569:-62.0012", "Outpost at -16.2793:-62.6249", "Zona Narco Prohibida at -16.2559:-62.8024", "Zona Narco Prohibido at -16.6188:-62.6831", "Outpost at -17.7547:-62.3898", "Campo Ana at -17.9125:-62.6454", "Nenma Freight Yard at -16.9689:-61.9054", "Ocoro Dispensary at -17.5588:-61.5395", "Outpost at -17.2433:-61.3126", "Checkpoint at -16.9291:-61.2724", "Outpost at -16.6983:-60.9050", "Outpost at -16.4151:-60.9018", "Outpost at -16.5376:-60.6056"]
ocoro.unidadbases=["Combat Outpost at -16.3748:-62.2485"]

pn_de_agua_verde=Province("P.N. De Agua Verde", "Influence", "True", "False")
pn_de_agua_verde.neighbours=["Tabacal", "Monte Puncu", "Espiriru Santo", "Ocoro", "Itacua", "San Mateo", "Media Luna"]
pn_de_agua_verde.santablancabases=["Alicia Town at -15.3084:-63.7158", "Checkpoint at -15.7370:-63.5427", "Paraiso Agua Verde at -15.6656:-63.3566", "Agua Verde Base at -15.6437:-62.9164", "Paraiso Casino at -15.9846:-62.8583", "Halcone House at -16.0723:-62.9748", "Outpost at -16.2908:-63.0358", "Buchon House at -15.1372:-63.0061", "Kankuta Mansion at -14.5062:-63.1301", "Patuja Mansion at -14.8957:-62.7246", "Secret Cocaine Hideout at -15.0549:-62.4858", "Outpost at -15.1433:-62.4060", "Riverine Checkpoint at -15.3060:-62.5533", "La Nube Blanca at -15.2970:-61.7613", "Outpost at -14.8217:-61.4421"]
pn_de_agua_verde.unidadbases=[]

pucara=Province("Pucara", "Influence", "True", "False")
pucara.neighbours=["Barvechos", "Itacua", "La Cruz", "Malca", "Inca Camina", "Montuyoc"]
pucara.santablancabases=["Makeshift Runway at -18.3881:-64.7597", "Outpost at -18.6159:-64.4109", "Santa Muerte Tomb at -19.2720:-64.2291", "Todos Santos Rock Quarry at -19.3039:-64.0455", "Santa Muerte Tomb at -19.0202:-63.7971", "Pucara Base at -18.7457:-63.6104", "Outpost at -19.1985:-63.2026", "Santa Muerte Tomb at -19.1008:-62.9884", "Pilca Mine at -18.9982:-62.7429", "Inca ruins at -19.0575:-62.5324"]
pucara.unidadbases=[]

remanzo=Province("Remanzo", "Smuggling", "True", "True")
remanzo.neighbours=["Media Luna", "San Mateo", "Barvechos", "Mojocoyo", "Koani"]
remanzo.santablancabases=["Poco Irrigation Tank at -14.5339:-66.1961", "Las Mulas at -14.4058:-66.0183", "Outpost at -14.3344:-65.3848", "Poco at -14.7746:-66.0344", "Remanzo Base at -14.5512:-65.2609", "Test Center at -14.7633:-65.2320", "Outpost at -15.0961:-65.6301", "Factory Electro Energy Drink at -15.3139:-65.1171", "Liquid Cocaine Lab at -15.3937:-65.3321", "Marcavi at -15.0305:-65.4757"]
remanzo.unidadbases=["F.O.B Puma at -14.6414:-657465", "Observation Post at -15.0113:-65.1084"]

san_mateo=Province("San Mateo", "Security", "True", "True")
san_mateo.neighbours=["Media Luna", "P.N. De Agua Verde", "Itacua", "Barvechos", "Remanzo"]
san_mateo.santablancabases=["Checkpoint at -14.8519:-64.1153", "Makeshift Runway at -15.0508:-64.0124", "La Carcel Del Pueblo at -15.0759:-64.3170", "San Mateo Base at -15.4109:-64.7731", "Boot Camp at -15.4594:-64.1733", "Makeshift Runway at -15.7227:-64.5883", "Sicario House at -15.6695:-63.9394", "Prison Rosario at -15.8281:-64.1761", "Outpost at -15.7918:-63.7130", "Outpost at -16.1539:-63.6894", "Outpost at -16.4589:-63.9250"]
san_mateo.unidadbases=["Checkpoint at -14.7296:-64.7802"]

tabacal=Province("Tabacal", "Production", "True", "True")
tabacal.neighbours=["Monte Puncu", "P.N. De Agua", "Media Luna"]
tabacal.santablancabases=["Outpost at -13.4809:-63.6018", "Tabacal Base at -13.3796:-63.2448", "Buchone House at -13.4780:-62.5670", "Outpost at -13.4357:-62.3699", "Secure Barn West at -13.8866:-63.6754", "Makeshift Runway at -14.0852:-63.4095", "Barrientos Coop at -13.7977:-62.5821", "Bella Selva at -13.8721:-62.2842", "Secure Barn East at -14.0802:-62.0811"]
tabacal.unidadbases=["Observation Post at -14.0835:-62.9562"]

villa_verde=Province("Villa Verde", "Production", "True", "True")
villa_verde.neighbours=["Caimanes", "Ocoro", "Espiritu Santo"]
villa_verde.santablancabases=["Villa Verde Base at -16.2215:-61.4771", "Maco at -16.1948:-61.1056", "Pyrolusite Labaratory Uno at -15.9260:-60.9159", "Outpost at -15.4119:-60.9135", "Outpost at -15.5214:-60.5060", "Precursors Storage at -15.6622:-60.3271", "Palmeros at -16.3240:-60.1760", "Leipez Cooperative at -16.2787:-59.8686", "Makeshift Runway at -15.1954:-59.9100", "Illegal Pyrolusite Mine at -15.8115:-59.4399", "Coca Drying Site at -14.9930:-59.5837", "Sicario House at -15.1617:-59.0717", "Villa Verde at -14.6590:-59.7344"]
villa_verde.unidadbases=["F.O.B Tucan at -16.0141:-59.7403", "Observation Post at -15.7172:-59.0790"]

provinces=[]
provinces.append(barvechos)
provinces.append(caimanes)
provinces.append(espiritu_santo)
provinces.append(flor_de_oro)
provinces.append(inca_camina)
provinces.append(itacua)
provinces.append(koani)
provinces.append(la_cruz)
provinces.append(libertad)
provinces.append(malca)
provinces.append(media_luna)
provinces.append(mojocoyo)
provinces.append(monte_puncu)
provinces.append(montuyoc)
provinces.append(ocoro)
provinces.append(pn_de_agua_verde)
provinces.append(pucara)
provinces.append(remanzo)
provinces.append(san_mateo)
provinces.append(tabacal)
provinces.append(villa_verde)

# create one time order specific objectives
# first
hostage_rescue=Objective("Hostage Rescue", "All", "False","First")
#rebel_spy=Objective("Rebel Spy", "All", "False", "First")

#last
kidnap=Objective("Kidnap and Interrogate\n\nExtract A HVT to a blacksite or safehouse for interrogation", "All", "False", "Last")

# create generic one time objectives
supplies=Objective("Supply Raid\n\nSteal a helicopter or plane from this province or any of it's neighbouring provinces", "All", "False", "Any")
convoy=Objective("Convoy Raid\n\nDestroy or tag a supply convoy from this province or any of it's neighbouring provinces", "All", "False", "Any")
rebel_radio=Objective("Radio Defence\n\nStart a rebel radio mission in this province or any of it's neighbouring provinces", "All", "False", "Any")

recover_intel=Objective("Recover Intel\n\nInfiltrate, remain undetected and try not to drop anyone. \nIntel likely on an officer, computer or in documentation", "All", "False", "All")
search_and_destroy=Objective("Search and Destroy\n\nDestroy valuable assets eg. Comms buildings, SAMs, Drone Jammers etc\nRemain undetected.", "All", "False", "All")
assassination=Objective("Assassinate HVT\n\nIdentify and eliminate a HVT.\nRemain undetected and exfiltrate.", "All", "False", "All")

# create region specific one time objectives


# create generic objectives
eliminate_hostiles=Objective("Eliminate All Hostiles", "All", "True", "All")


objectives=[]

objectives.append(hostage_rescue)
#objectives.append(rebel_spy)

objectives.append(kidnap)

objectives.append(convoy)
#objectives.append(supplies)
objectives.append(rebel_radio)

objectives.append(recover_intel)
objectives.append(search_and_destroy)
objectives.append(assassination)
objectives.append(eliminate_hostiles)

# choose region grouping
#dice_roll=roll20()

#pick 2 different regions seperated by at least one region
#print("Standard Op\n")

# generate 2 different neighbouring regions
try:
  province1=getRandomFromList(provinces)
  province2=getRandomFromList(province1.neighbours)

  for p in provinces:
    if p.name == province2:
      province2=p

  province3=getRandomFromList(province2.neighbours)
  for p in provinces:
    if p.name == province3:
      province3=p

  province4=getRandomFromList(province3.neighbours)
  for p in provinces:
    if p.name == province4:
      province4=p

  objective1=createMission(province1, "First")

  objective2=random.choice(["a", "b"])
  if objective2 == "a":
    objective2=createMission(province1)
  elif objective2 == "b":
    objective2=createMission(province2)

  objective3=random.choice(["a", "b"])
  if objective3 == "a":
    objective3=createMission(province2)
  elif objective3 == "b":
    objective3=createMission(province3)

  objective4=random.choice(["a", "b"])
  if objective4 == "a":
    objective4=createMission(province3, "Last")
  elif objective4 == "b":
    objective4=createMission(province4, "Last")

  print("Daily Operation")
  print("\n-----")


  print("Objective 1:\n")
  print(objective1)
  print("-----")
  print("Objective 2:\n")
  print(objective2)
  print("And/Or\n")
  print(objective3)
  print("-----")
  print("Objective 3:")
  print(objective4)
  
  
  
  #output=("```"+"Daily Operation\n\n-----\nObjective1:\n\n"+objective1+"\n-----\nObjective2:\n\n"+objective2+"\nAnd/Or\n\n"+objective3+"\n-----\nObjective3:\n\n"+objective4+"```")
  #webhook = discord_webhook.DiscordWebhook(url='', content=output)
  #webhook.execute()
  
except AttributeError as e:
  print(e)
  print("Attribute Error, @sti1ton please fix")
