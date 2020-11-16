for x in range(1,100):
   f = open("test"+str(x), 'w')
   w = 'spam\n'
   f.write(f'{w*100}')
   f.close()