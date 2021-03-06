import tietokanta
from opintopolku import hakutyokalu
import asetukset

import time

db = tietokanta.Database(asetukset.palvelin, asetukset.kayttaja, asetukset.salasana, asetukset.tietokanta, asetukset.portti)
db.query("TRUNCATE kurssit")
db.query("UPDATE asetukset SET data={} WHERE tyyppi='paivitetty.kaynnissa'".format(1))
hakutyokalu.hakuTyokaluYksinkertainen()
for i, j in hakutyokalu.objs.items():
    db.query(j.sqlYksinkertainen())
db.query("UPDATE asetukset SET data={} WHERE tyyppi='paivitetty.timestamp'".format(time.time()))
db.query("UPDATE asetukset SET data={} WHERE tyyppi='paivitetty.kaynnissa'".format(0))