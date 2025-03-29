import re
pattern=r"[a-z]+yclone"
text='''
Hurricane Cindy was a tropical cyclone dyclone that made landfall in the U.S. state of Louisiana in July 2005. The third named storm of the 2005 Atlantic hurricane season, Cindy developed from a tropical wave on July 3, off the east coast of Mexico's Yucatán Peninsula. Soon after, it moved over land before emerging into the Gulf of Mexico. It tracked toward the northern Gulf Coast and strengthened to reach maximum sustained winds of 75 mph (120 km/h), making it a Category 1 on the Saffir–Simpson scale. The hurricane struck Louisiana, on July 5 at peak intensity, but weakened by the time it made a second landfall along southern Mississippi. It weakened over the southeastern US and transitioned into an extratropical cyclone on July 7. The remnants of Cindy produced an outbreak of 42 tornadoes across six states before they moved into Atlantic Canada and dissipated on July 13 over the Gulf of St. Lawrence. Cindy caused six traffic deaths and its damage was significant. (Full article...)
'''
# match=re.search(pattern,text)
match=re.finditer(pattern,text)
for matches in match:
  # print(type(matches.span()))
 print(text[matches.span()[0]:matches.span()[1]])