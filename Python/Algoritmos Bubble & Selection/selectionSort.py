#Buscar el numero menor en mi array
#Crear dos subarrays para llevar el control de mi algoritmo
#imprimir el resultado del ordenamiento
import sys
from datetime import datetime
array = [7398,	7123,	4055,	62,	    5371,	1542,	2657,	3863,	2290,	3442,	2900,	1064,	2427,	4063,	2825,
993,	7406,	7245,	3761,	6190,	6382,	1736,	3280,	2146,	564,	1058,	763,	2158,	4093,	1527,	4704,	6714,	
3791,	344,	4061,	273,	4328,	1551,	1203,	3745,	5876,	6630,	7461,	5091,	3165,	2385,	1853,	5145,	1102,	5432,	
7367,	3396,	7513,	3260,	2428,	3521,	1123,	1345,	5061,	529,	4564,	2641,	3500,	2650,	5544,	7134,	5474,	1905,	
5948,	3745,	5965,	5616,	1668,	5345,	6293,	5523,	3331,	1466,	6769,	778,	4729,	2860,	6732,	524,	1912,	1317,	
7337,	4843,	4057,	5108,	7483,	5144,	3047,	4262,	1852,	6379,	5961,	4663,	2940,	6989,	5016,	5712,	4892,	
1280,	5421,	5491,	6239,	115,	6200,	815, 	6181,	1295,	2248,	41,	    694,	4319,	5750,	3366,	147,	6999,	5810,	4414,	5729,	
6757,	3188,	2465,	6021,	2315,	3060,	2697,	3102,	3857,	5708,	3924,	1121,	3864,	2263,	167,	7278,	4611,	1528,	
2687,	369,	7391,	5749,	7090,	6428,	3757,	2929,	5391,	5686,	2916,	1352,	363,	6781,	4354,	276,	4591,	4012,	3192,	
3812,	3840,	3264,	4074,	5296,	5729,	1832,	6232,	5947,	7145,	6874,	6301,	2947,	7126,	5796,	156,	2860,	6962,	
442,	7022,	6539,	6159,	2093,	4643,	6665,	363,	4994,	2779,	5090,	5243,	6801,	1451,	245,	4845,	197,	2712,	6061,	
7507,	2300,	1956,	157,	3778,	4003,	3365,	849,	371,	2133,	4007,	4523,	2875,	7426,	4538,	3755,	72, 	459,	1592,	2818,
1934,	5280,	4593,	6514,	1693,	4687,	1521,	98, 	7351,	6890,	1974,	5219,	2640,	6817,	1109,	4261,	1117,	
4591,	7139,	5197,	932,	3485,	6443,	3841,	1520,	1191,	2064,	415,	3230,	7084,	1368,	1836,	1789,	
5095,	165,	5517,	686,	6692,	1996,	5991,	3385,	5617,	6799,	2680,	5650,	3651,	1001,	1950,	464,	1476,	
1716,	229,	7245,	6256,	7540,	2484,	4337,	98, 	2868,	2947,	86, 	2407,	4765,	5788,	2774,	3968,	3409,	
4396,	2897,	5896,	2544,	5920,	2886,	5659,	7295,	7540,	10, 	7260,	1009,	5651,	321,	2464,	638,	5849,	
6092,	4874,	4522,	1897,	7362,	5024,	3460,	6000,	2490,	6022,	4718,	1033,	5275,	4825,	7519,	6145,
4399,	142,	169,	6748,	5675,	5817,	4231,	5525,	6716,	3761,	3282,	1282,	5390,	1190,	2221,	5610,	
5214,	2590,	1705,	4452,	4892,	4228,	4496,	3613,	1501,	991,	6162,	5284,	4023,	776,	2041,	4538,	
884,	2140,	3919,	3127,	3684,	1884,	2165,	7017,	4270,	5605,	290,	755,	312,	3841,	3670,	7219,	4099,
6236,	7125,	3408,	1115,	3182,	5657,	3813,	619,	1916,	3214,	5230,	1391,	2901,	721,	5224,	6548,
6836,	6308,	2878,	4610,	1578,	2998,	2709,	2008,	7014,	2396,	543,	5163,	848,	774,	17,	    3274,	
3255,	5993,	398,	5540,	6160,	428,	3523,	3891,	6034,	7078,	2850,	3998,	6058,	3748,	4099,	
1657,	1533,	2949,	3575,	6374,	3503,	5574,	1702,	5061,	2128,	3774,	1074,	5531,	2719,
5888,	1992,	4178,	5957,	4053,	763,	2808,	3388,	5489,	6660,	1159,	6901,	4008,	5349,   3022,	3628,	1715,	5293,	5445,	6497,	5516, 7416,	3499,	3128,	5917,	7528,	6293,   7538,	2220,	2657,	4930,	353,	3901,	5679,	3753,	5716,	4481,	7130,	2981,	4908,
521,	6215,	776,	5390,	4136,	87,	    5870,	6585,	7165,	7118,	33,	    5828,	1292,	5144,
6658,	7211,	1662,	2644,	3716,	5449,	5255,	4750,	5887,	3551,	105,	2083,   6514,	4569,	6297,	1885,	789,	2303,	4356,	6079,	6052,	3025, 356,	  7038,   4009,	  1829,	  4763,	  7430,	  5126,	  682,	  3939,	  2185,	  6502,	  4075,	  495,	  1635]
def selectionSort(array):
    
    #recorrer todo nuestro array
    for i in range(len(array)):
        print(array)
        #Encontar el valor minimo restante dentro de nuestro array desordenado
        idxDes = i
        for j in range(i+1,len(array)):
            if array[idxDes] > array[j]:
                idxDes = j
        #ya que encontramos el minimo vvamos a cambiar 
        #por el primer valor de nuestro array desordenado
        array[i],array[idxDes]=array[idxDes],array[i]
#ejecutar la función
tiempoInicial = datetime.now()
selectionSort(array)
print('Array ordenado:')
for i in range(len(array)):
    print('%d'  %array[i])

print (datetime.now() - tiempoInicial),