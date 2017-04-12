file = open("data.txt","w")

i = 0
while (i < 1000):
    file.write("%s\n" % i)
    i=i+1
file.close()
print "File Berhasil Dibuat"
