
import re

# Resolutions
vres = re.compile(r'(360|480|720|1080|2160|4320)([pi])', re.IGNORECASE)

# Sources
tv = re.compile(r'([sph]d).?tv|tv(rip|mux)', re.IGNORECASE)
dvd = re.compile(r'(hd)dvd|dvd(rip|mux)', re.IGNORECASE)
web = re.compile(r'web.?(dl)|web(rip|mux|hd)', re.IGNORECASE)
bluray = re.compile(r'(blue?-?ray|b[rd](?:rip|mux))', re.IGNORECASE)
sat = re.compile(r'(dsr|satrip)', re.IGNORECASE)
itunes = re.compile(r'(itunes)', re.IGNORECASE)
hrws = re.compile(r'(hr.ws.pdtv).[xh].?26[45]', re.IGNORECASE)
raw = re.compile(r'(1080[pi].hdtv)', re.IGNORECASE)

# Codecs
avc = re.compile(r'([xh].?26[45])', re.IGNORECASE)
xvid = re.compile(r'(xvid|divx)', re.IGNORECASE)
mpeg = re.compile(r'(mpeg-?2)', re.IGNORECASE)
