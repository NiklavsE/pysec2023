# To demonstrate use of loops, html is parsed, and a schedule dictionary is created for days of the September month and respective of the day
from bs4 import BeautifulSoup

html = """
<table width="100%" border="0" cellpadding="0" cellspacing="0">
  <tr>
    <td width="270" align="left" valign="top"><div id="navig"><input id="men_prev" type="button" name="Button" value="&lt; Iepriekšējais" class="poga_men" onClick="men_prev()">
      <input id="men_next" type="button" name="Button2" value="Nākamais &gt;" class="poga_men" onClick="men_next()">
      <input id="print" type="button" name="print" value="Drukāt" class="poga" onclick="open_print('lekcijas')" /></div>
    </td>
    <td align="center" valign="top"><h1 class="h2_men">Septembris 2023, KI1</h1></td>
    <td width="330" align="left" valign="top">
      <div class="majas"><div class="laiks_3">Tiešsaiste</div></div>
      <div class="majas"><div class="laiks_2">Cēsu iela 4</div></div>
      <div class="majas"><div class="laiks_1">Tērbatas iela 10</div></div>
    </td>
  </tr>
</table>
<div class="kal">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
    <th width="15%">Pirmdiena</th>
    <th width="15%">Otrdiena</th>
    <th width="15%">Trešdiena</th>
    <th width="15%">Ceturtdiena</th>
    <th width="15%">Piektdiena</th>
    <th width="15%">Sestdiena</th>
    <th>Svētdiena</th>
  </tr>
  <tr>
    <td class="tukss">&nbsp;</td>
    <td class="tukss">&nbsp;</td>
    <td class="tukss">&nbsp;</td>
    <td class="tukss">&nbsp;</td>
    <td class="datums"><div class="cipars">1</div></td>
    <td class="datums"><div class="cipars">2</div></td>
    <td class="datums"><div class="cipars">3</div></td>
  </tr>
  <tr>
    <td class="datums"><div class="cipars">4</div></td>
    <td class="datums"><div class="cipars">5</div></td>
    <td class="datums"><div class="cipars">6</div></td>
    <td class="datums"><div class="cipars">7</div></td>
    <td class="datums"><div class="cipars">8</div><div class="laiks_3">17:30 - 20:40<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Informācijas drošības risku pārvaldība (I.MURĀNE)</div></td>
    <td class="datums"><div class="cipars">9</div><div class="laiks_3">09:45 - 13:00<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Pitons drošības testētājiem (K.FELZENBERGS)</div><div class="laiks_3">14:00 - 17:15<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Pitons drošības testētājiem (K.FELZENBERGS)</div></td>
    <td class="datums"><div class="cipars">10</div></td>
  </tr>
  <tr>
    <td class="datums"><div class="cipars">11</div></td>
    <td class="datums"><div class="cipars">12</div></td>
    <td class="datums"><div class="cipars">13</div></td>
    <td class="datums"><div class="cipars">14</div></td>
    <td class="datums"><div class="cipars">15</div><div class="laiks_3">17:30 - 20:40<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Pitons drošības testētājiem (K.FELZENBERGS)</div></td>
    <td class="datums"><div class="cipars_sodien">16</div><div class="laiks_3">09:45 - 13:00<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Pitons drošības testētājiem (K.FELZENBERGS)</div><div class="laiks_3">14:00 - 17:15<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Pitons drošības testētājiem (K.FELZENBERGS)</div></td>
    <td class="datums"><div class="cipars">17</div></td>
  </tr>
  <tr>
    <td class="datums"><div class="cipars">18</div></td>
    <td class="datums"><div class="cipars">19</div></td>
    <td class="datums"><div class="cipars">20</div></td>
    <td class="datums"><div class="cipars">21</div></td>
    <td class="datums"><div class="cipars">22</div><div class="laiks_3">17:30 - 20:40<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Informācijas drošības risku pārvaldība (I.MURĀNE)</div></td>
    <td class="datums"><div class="cipars">23</div><div class="laiks_3">09:45 - 13:00<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Pitons drošības testētājiem (K.FELZENBERGS)</div><div class="laiks_3">14:00 - 20:40<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Drošības incidentu pārvaldība (E.BUŠS)</div></td>
    <td class="datums"><div class="cipars">24</div></td>
  </tr>
  <tr>
    <td class="datums"><div class="cipars">25</div></td>
    <td class="datums"><div class="cipars">26</div></td>
    <td class="datums"><div class="cipars">27</div></td>
    <td class="datums"><div class="cipars">28</div></td>
    <td class="datums"><div class="cipars">29</div><div class="laiks_3">17:30 - 20:40<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Pienākumi, tiesības un atbildība internetā (J.PŪCE)</div></td>
    <td class="datums"><div class="cipars">30</div><div class="laiks_3">09:45 - 13:00<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Informācijas drošības risku pārvaldība (I.MURĀNE)</div><div class="laiks_3">14:00 - 17:15<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Informācijas drošības risku pārvaldība (I.MURĀNE)</div><div class="laiks_3">17:30 - 20:40<b>tiešsaistē 5 MS Teams</b> <b>KI1</b><br />Drošības incidentu pārvaldība (E.BUŠS)</div></td>
    <td class="tukss">&nbsp;</td>
  </tr>
</table>
</div>
"""

soup = BeautifulSoup(html, 'html.parser')
schedule = {}

days = soup.find_all("td", {"class": "datums"})
print("September planned class schedule")
for day in days:
    onlineClasses = day.find_all("div", {"class": "laiks_3"})

    if (len(onlineClasses) > 0):
        day = day.div.contents[0]
        classes = []

        for n in range(len(onlineClasses)):
            classes.append(onlineClasses[n].get_text())
    else:
        continue

    schedule[day] = classes

days = list(schedule)
i = 0
while i < len(days):
    print("Day: ", days[i])
    print("List of classes: ", schedule[days[i]])
    i+=1
