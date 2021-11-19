import Leadstools as lead
import streetleagueheatmakerV2 as street


exceldocname = street.maketxtfile()

racedata = street.getxlsx(exceldocname)
#racedata = lead.getxlsx(exceldocname)

street.checkfor0time(racedata)

racersraw = street.makeracers(racedata)

racersupdated = street.giveroundpoints(racersraw)

racerssorted = street.firstsort(racersupdated[0])

finallist = street.finalsort(racerssorted, racersupdated[1])

newdataframe = street.makedataframe(finallist, racedata)

street.exporttoxl(newdataframe, racedata, exceldocname)