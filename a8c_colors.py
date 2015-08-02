'''Automattic-oriented colors

These colors are based on this page:
https://wordpress.com/design-handbook/colors/

'''

from itertools import cycle

a8c_blue             = '#0087be'
a8c_blue_light       = '#78dcfa'
a8c_blue_medium      = '#00aadc'
a8c_blue_dark        = '#005082'
a8c_gray             = '#87a6bc'
a8c_gray_light       = '#f3f6f8'
a8c_gray_lighten30   = '#e9eff3'
a8c_gray_lighten20   = '#c8d7e1'
a8c_gray_lighten10   = '#a8bece'
a8c_gray_darken_10   = '#668eaa'
a8c_gray_darken_20   = '#4f748e'
a8c_gray_darken_30   = '#3d596d'
a8c_gray_dark        = '#2e4453'
a8c_orange           = '#d54e21'
a8c_orange_fire      = '#d54e21'
a8c_orange_jazzy     = '#f0821e'
a8c_green            = '#4ab866'
a8c_yellow            = '#f0b849'
a8c_red              = '#d94f4f'

# color aliases
a8c_black = a8c_gray_dark
r = a8c_red
g = a8c_green
b = a8c_blue
y = a8c_yellow
k = a8c_black
w = a8c_gray_light


default = [a8c_blue,
           a8c_green,
           a8c_yellow,
           a8c_red,
           a8c_blue_dark,
           a8c_orange_jazzy]

default_cycle = cycle(default)

grays = [
a8c_gray_lighten30,
a8c_gray_lighten20,
a8c_gray_lighten10,
a8c_gray_darken_10,
a8c_gray_darken_20,
a8c_gray_darken_30,
a8c_gray_dark]
gray_cycle = cycle(grays)


intense = ["#8B27CB",
	"#189EC6",
	"#B27E01",
	"#FAFB50",
	"#CD9CCF",
	"#FD75E4",
	"#39AD84",
	"#9C6A3E",
	"#A0ED98",
	"#9361B5",
	"#B96273"]
intense_cycle = cycle(intense)


a8c_blue_tint = '#93BFD4'
a8c_red_tint = '#C2A9A1'
a8c_green_tint = '#B5CFA5'


blue_tint = [
    a8c_blue_tint,
    "#528D90",
    "#031F22",
    "#438084",
    "#347479",
    "#677B75",
    "#283F3F"
]
blue_tint_cycle = cycle(blue_tint)


red_tint = [
    a8c_red_tint,
    "#EEC2CB",
    "#AA7D97",
    "#7D646B",
    "#A7898D",
    "#CE9DB5",
    "#503B45"]
red_tint_cycle = cycle(red_tint)
