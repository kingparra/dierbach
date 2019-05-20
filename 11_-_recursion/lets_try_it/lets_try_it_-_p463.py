#bpython version 0.17.1 on top of Python 3.7.2 /usr/bin/python3
def rfunc(n):
    print(n)
    if n > 0:
        rfunc(n - 1)

rfunc(4)
#OUT: 4
#OUT: 3
#OUT: 2
#OUT: 1
#OUT: 0
rfunc(0)
#OUT: 0
rfunc(100)
#OUT: 100
#OUT: 99
#OUT: 98
#OUT: 97
#OUT: 96
#OUT: 95
#OUT: 94
#OUT: 93
#OUT: 92
#OUT: 91
#OUT: 90
#OUT: 89
#OUT: 88
#OUT: 87
#OUT: 86
#OUT: 85
#OUT: 84
#OUT: 83
#OUT: 82
#OUT: 81
#OUT: 80
#OUT: 79
#OUT: 78
#OUT: 77
#OUT: 76
#OUT: 75
#OUT: 74
#OUT: 73
#OUT: 72
#OUT: 71
#OUT: 70
#OUT: 69
#OUT: 68
#OUT: 67
#OUT: 66
#OUT: 65
#OUT: 64
#OUT: 63
#OUT: 62
#OUT: 61
#OUT: 60
#OUT: 59
#OUT: 58
#OUT: 57
#OUT: 56
#OUT: 55
#OUT: 54
#OUT: 53
#OUT: 52
#OUT: 51
#OUT: 50
#OUT: 49
#OUT: 48
#OUT: 47
#OUT: 46
#OUT: 45
#OUT: 44
#OUT: 43
#OUT: 42
#OUT: 41
#OUT: 40
#OUT: 39
#OUT: 38
#OUT: 37
#OUT: 36
#OUT: 35
#OUT: 34
#OUT: 33
#OUT: 32
#OUT: 31
#OUT: 30
#OUT: 29
#OUT: 28
#OUT: 27
#OUT: 26
#OUT: 25
#OUT: 24
#OUT: 23
#OUT: 22
#OUT: 21
#OUT: 20
#OUT: 19
#OUT: 18
#OUT: 17
#OUT: 16
#OUT: 15
#OUT: 14
#OUT: 13
#OUT: 12
#OUT: 11
#OUT: 10
#OUT: 9
#OUT: 8
#OUT: 7
#OUT: 6
#OUT: 5
#OUT: 4
#OUT: 3
#OUT: 2
#OUT: 1
#OUT: 0
def rfunc(n):
    if n == 1:
        return 1
    else:
        return n + rfunc(n - 1)

rfunc(1)
#OUT: 1
rfunc(3)
#OUT: 6
rfunc(100)
#OUT: 5050

