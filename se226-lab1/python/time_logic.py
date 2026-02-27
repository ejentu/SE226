x = int(input("Enter a large integer : "))

hours = x/3600
minutes = (x%3600)/60
seconds = (x%3600)%60






print(x , " seconds is ", int(hours) , " hours ", minutes, " minutes " , seconds , " seconds" )