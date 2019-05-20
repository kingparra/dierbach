# Let's Try It, page 52
num = 10
num
# OUT: 10
id(num)
# OUT: 139670230932416
num = 20
num
# OUT: 20
id(num)
# OUT: 139670230932736
k = num
k
# OUT: 20
id(k)
# OUT: 139670230932736
id(num)
# OUT: 139670230932736
# They reference the same id, or memory location.
k = 30
k
# OUT: 30
num
# OUT: 20
id(k)
# OUT: 139670230933056
id(num)
# OUT: 139670230932736
k = k + 1
k
# OUT: 31
id(num)
# OUT: 139670230932736
id(k)
# OUT: 139670230933088