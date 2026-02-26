# cb_dx_pre

---

This little script will help you find out what the current coverage is like on the CB frequency.

---
### First 

First make a link to local bin folder, and use it. 

```bash
λ> git clone https://github.com/zsoltibaba37/cb_dx_pre.git
λ> sudo ln -s /home/USERNAME/cb_dx_pre/cb_check.py /usr/local/bin/dxcheck  
    or whatever you want
λ> dxcheck

:Product: Daily Solar Data            DSD.txt
:Issued: 0225 UT 26 Feb 2026
#
#  Prepared by the U.S. Dept. of Commerce, NOAA, Space Weather Prediction Center
#  Please send comments and suggestions to SWPC.Webmaster@noaa.gov
#
#                Last 30 Days Daily Solar Data
#
#                         Sunspot       Stanford GOES15
#           Radio  SESC     Area          Solar  X-Ray  ------ Flares ------
#           Flux  Sunspot  10E-6   New     Mean  Bkgd    X-Ray      Optical
#  Date     10.7cm Number  Hemis. Regions Field  Flux   C  M  X  S  1  2  3
#--------------------------------------------------------------------------- 
2026 01 27  144    100      300      2    -999      *   6  0  0  3  0  0  0  <- GOOD
2026 01 28  133    135      360      3    -999      *   2  0  0  0  0  0  0  <- GOOD
2026 01 29  129    117      280      2    -999      *   3  0  0  0  0  0  0  <- GOOD
2026 01 30  128    112      300      3    -999      *  10  0  0  0  1  0  0  <- GOOD
2026 01 31  141    126      400      2    -999      *  19  0  0  4  0  1  0  <- GOOD
2026 02 01  162     97      790      1    -999      *   2 17  2  0  0  1  0  <- GOOD
2026 02 02  174    131     1020      2    -999      *   1 15  2  0  1  1  0  <- EXELLENT
2026 02 03  178    171     1385      1    -999      *   5 11  1  5  6  0  0  <- EXELLENT
2026 02 04  167    166     1340      0    -999      *   6 12  1  5  2  1  0  <- EXELLENT
2026 02 05  176    139     1430      0    -999      *  13  9  0  6  3  0  0  <- EXELLENT
2026 02 06  164    132     1510      1    -999      *  12  0  0  7  1  0  0  <- EXELLENT
2026 02 07  169    128     1560      0    -999      *   6  0  0  0  0  0  0  <- EXELLENT
2026 02 08  167    118     1470      0    -999      *   6  3  0  8  4  1  0  <- EXELLENT
2026 02 09  144    107     1490      1    -999      *  10  1  0  2  1  0  0  <- GOOD
2026 02 10  142    105     1385      0    -999      *   8  1  0  0  0  0  0  <- GOOD
2026 02 11  129     84      570      1    -999      *  10  2  0  5  0  0  0  <- GOOD
2026 02 12  129     82      480      0    -999      *   3  1  0  0  0  0  0  <- GOOD
2026 02 13  117     50      430      0    -999      *   0  1  0  1  0  0  0  <- WEAK
2026 02 14  117     60      430      2    -999      *   2  0  0  0  0  0  0  <- WEAK
2026 02 15  118     65      410      0    -999      *   2  0  0  1  0  0  0  <- WEAK
2026 02 16  118     69      400      0    -999      *   1  1  0  1  0  0  0  <- WEAK
2026 02 17  122     63      360      0    -999      *   3  0  0  3  0  0  0  <- GOOD
2026 02 18  119     43      240      0    -999      *   2  0  0  0  0  0  0  <- WEAK
2026 02 19  116     39      235      0    -999      *   3  0  0  0  0  0  0  <- WEAK
2026 02 20  111     34      170      0    -999      *   1  0  0  1  0  0  0  <- WEAK
2026 02 21  110     11      120      0    -999      *   0  0  0  0  0  0  0  <- WEAK
2026 02 22  110      0        0      0    -999      *   4  0  0  0  0  0  0  <- WEAK
2026 02 23  108      0        0      0    -999      *   0  0  0  0  0  0  0  <- WEAK
2026 02 24  120      0        0      0    -999      *   3  0  0  0  0  0  0  <- WEAK
2026 02 25  125     25      190      2    -999      *  11  1  0  1  0  0  0  <- WEAK
```
---
2026
