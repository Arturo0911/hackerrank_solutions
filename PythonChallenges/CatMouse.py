#!/bin/python3








def cat_mouse(x,y,z):

    return "Cat A" if abs(x - z) < abs(y - z) else "Cat B" if abs(y-z) < abs(x-z) else "Mouse C"




"""print(cat_mouse(1 ,2 ,3))
print(cat_mouse(1,3 ,2))
print(cat_mouse(22 ,75 ,70))
print(cat_mouse(33, 86, 59))
47 29 89
18 19 82
84 17 18"""


print(cat_mouse(22, 75, 70))
print(cat_mouse(33, 86, 59))
print(cat_mouse(47, 29, 89)) # 
print(cat_mouse(18, 19, 82))
print(cat_mouse(84, 17, 18))
print(cat_mouse(100, 11, 55))
print(cat_mouse(37, 57, 75))
print(cat_mouse(47, 30, 6))
print(cat_mouse(40, 68, 50))
print(cat_mouse(26, 37, 31))
print(cat_mouse(93, 49, 20))
print(cat_mouse(84, 78, 31))
print(cat_mouse(80, 57, 86))
print(cat_mouse(57, 94, 55))
print(cat_mouse(21, 80, 4))
print(cat_mouse(1, 68, 67))
print(cat_mouse(74, 91, 23))
print(cat_mouse(85, 66, 80))
print(cat_mouse(21, 95, 58))
print(cat_mouse(86, 69, 77))
print(cat_mouse(31, 2, 46))
print(cat_mouse(45, 94, 99))
print(cat_mouse(7, 66, 36))
print(cat_mouse(63, 34, 33))
print(cat_mouse(75, 92, 65))
print(cat_mouse(90, 45, 54))
print(cat_mouse(12, 9, 10))
print(cat_mouse(43, 56, 51))
print(cat_mouse(92, 20, 56))
print(cat_mouse(97, 12, 67))
print(cat_mouse(17, 38, 86))
print(cat_mouse(85, 94, 20))
print(cat_mouse(6, 81, 53))
print(cat_mouse(77, 27, 54))
print(cat_mouse(62, 25, 37))
print(cat_mouse(56, 70, 63))
print(cat_mouse(49, 32, 16))
print(cat_mouse(4, 61, 39))
print(cat_mouse(92, 30, 61))
print(cat_mouse(41, 59, 81))
print(cat_mouse(100, 66, 83))
print(cat_mouse(16, 16, 16))
print(cat_mouse(81, 70, 30))
print(cat_mouse(11, 33, 22))
print(cat_mouse(35, 98, 18))
print(cat_mouse(43, 62, 48))
print(cat_mouse(84, 54, 69))
print(cat_mouse(73, 72, 86))
print(cat_mouse(34, 82, 49))
print(cat_mouse(16, 83, 62))
print(cat_mouse(57, 50, 53))
print(cat_mouse(36, 49, 88))
print(cat_mouse(5, 80, 42))
print(cat_mouse(20, 86, 47))
print(cat_mouse(43, 40, 41))
print(cat_mouse(72, 12, 42))
print(cat_mouse(16, 43, 29))
print(cat_mouse(11, 35, 23))
print(cat_mouse(12, 63, 37))
print(cat_mouse(84, 78, 55))
print(cat_mouse(17, 90, 78))
print(cat_mouse(28, 10, 84))
print(cat_mouse(39, 96, 67))
print(cat_mouse(22, 84, 53))
print(cat_mouse(49, 77, 63))
print(cat_mouse(77, 82, 55))
print(cat_mouse(17, 53, 35))
print(cat_mouse(79, 31, 55))
print(cat_mouse(7, 56, 31))
print(cat_mouse(2, 7, 4))
print(cat_mouse(99, 82, 60))
print(cat_mouse(20, 17, 18))
print(cat_mouse(1, 98, 49))
print(cat_mouse(91, 66, 13))
print(cat_mouse(95, 23, 1))
print(cat_mouse(87, 59, 73))
print(cat_mouse(10, 10, 56))
print(cat_mouse(61, 54, 59))
print(cat_mouse(62, 94, 78))
print(cat_mouse(49, 29, 37))
print(cat_mouse(87, 79, 83))
print(cat_mouse(72, 1, 42))
print(cat_mouse(42, 34, 38))
print(cat_mouse(52, 82, 98))
print(cat_mouse(29, 12, 43))
print(cat_mouse(81, 50, 97))
print(cat_mouse(80, 17, 43))
print(cat_mouse(88, 38, 40))
print(cat_mouse(41, 55, 84))
print(cat_mouse(48, 91, 69))
print(cat_mouse(11, 74, 23))
print(cat_mouse(84, 68, 76))
print(cat_mouse(4, 51, 80))
print(cat_mouse(51, 85, 39))
print(cat_mouse(37, 74, 55))
print(cat_mouse(15, 65, 54))
print(cat_mouse(57, 14, 56))
print(cat_mouse(43, 61, 56))
print(cat_mouse(9, 79, 35))
print(cat_mouse(4, 44, 44))


