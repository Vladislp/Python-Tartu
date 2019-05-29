from turtle import * 
speed(10) 

colors = """snow gainsboro linen bisque moccasin cornsilk ivory 
seashell honeydew azure lavender white black gray navy 
blue turquoise cyan aquamarine green chartreuse 
khaki yellow gold goldenrod sienna peru burlywood 
beige wheat tan chocolate firebrick brown salmon 
orange coral tomato red pink maroon 
magenta violet plum orchid purple thistle snow2 snow3 
snow4 seashell2 seashell3 seashell4 AntiqueWhite1 AntiqueWhite2 
AntiqueWhite3 AntiqueWhite4 bisque2 bisque3 bisque4 PeachPuff2 
PeachPuff3 PeachPuff4 NavajoWhite2 NavajoWhite3 NavajoWhite4 
LemonChiffon2 LemonChiffon3 LemonChiffon4 cornsilk2 cornsilk3 
cornsilk4 ivory2 ivory3 ivory4 honeydew2 honeydew3 honeydew4 
LavenderBlush2 LavenderBlush3 LavenderBlush4 MistyRose2 MistyRose3 
MistyRose4 azure2 azure3 azure4 SlateBlue1 SlateBlue2 SlateBlue3 
SlateBlue4 RoyalBlue1 RoyalBlue2 RoyalBlue3 RoyalBlue4 blue2 blue4 
DodgerBlue2 DodgerBlue3 DodgerBlue4 SteelBlue1 SteelBlue2 
SteelBlue3 SteelBlue4 DeepSkyBlue2 DeepSkyBlue3 DeepSkyBlue4 
SkyBlue1 SkyBlue2 SkyBlue3 SkyBlue4 LightSkyBlue1 LightSkyBlue2 
LightSkyBlue3 LightSkyBlue4 SlateGray1 SlateGray2 SlateGray3 
SlateGray4 LightSteelBlue1 LightSteelBlue2 LightSteelBlue3 
LightSteelBlue4 LightBlue1 LightBlue2 LightBlue3 LightBlue4 
LightCyan2 LightCyan3 LightCyan4 PaleTurquoise1 PaleTurquoise2 
PaleTurquoise3 PaleTurquoise4 CadetBlue1 CadetBlue2 CadetBlue3 
CadetBlue4 turquoise1 turquoise2 turquoise3 turquoise4 cyan2 cyan3 
cyan4 DarkSlateGray1 DarkSlateGray2 DarkSlateGray3 DarkSlateGray4 
aquamarine2 aquamarine4 DarkSeaGreen1 DarkSeaGreen2 DarkSeaGreen3 
DarkSeaGreen4 SeaGreen1 SeaGreen2 SeaGreen3 PaleGreen1 PaleGreen2 
PaleGreen3 PaleGreen4 SpringGreen2 SpringGreen3 SpringGreen4 
green2 green3 green4 chartreuse2 chartreuse3 chartreuse4 
OliveDrab1 OliveDrab2 OliveDrab4 DarkOliveGreen1 DarkOliveGreen2 
DarkOliveGreen3 DarkOliveGreen4 khaki1 khaki2 khaki3 khaki4 
LightGoldenrod1 LightGoldenrod2 LightGoldenrod3 LightGoldenrod4 
LightYellow2 LightYellow3 LightYellow4 yellow2 yellow3 yellow4 
gold2 gold3 gold4 goldenrod1 goldenrod2 goldenrod3 goldenrod4 
DarkGoldenrod1 DarkGoldenrod2 DarkGoldenrod3 DarkGoldenrod4 
RosyBrown1 RosyBrown2 RosyBrown3 RosyBrown4 IndianRed1 IndianRed2 
IndianRed3 IndianRed4 sienna1 sienna2 sienna3 sienna4 burlywood1 
burlywood2 burlywood3 burlywood4 wheat1 wheat2 wheat3 wheat4 tan1 
tan2 tan4 chocolate1 chocolate2 chocolate3 firebrick1 firebrick2 
firebrick3 firebrick4 brown1 brown2 brown3 brown4 salmon1 salmon2 
salmon3 salmon4 LightSalmon2 LightSalmon3 LightSalmon4 orange2 
orange3 orange4 DarkOrange1 DarkOrange2 DarkOrange3 DarkOrange4 
coral1 coral2 coral3 coral4 tomato2 tomato3 tomato4 OrangeRed2 
OrangeRed3 OrangeRed4 red2 red3 red4 DeepPink2 DeepPink3 DeepPink4""" 

colorList = colors.split() 
colorseArv = len(colorList) 
alpha = 360/colorseArv 

left(90) 
for varv in colorList:
    pencolor(varv) 
    forward(200) 
    left(180) 
    forward(200) 
    right(180-alpha)