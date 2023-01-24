#write a program that reads seconds and convert into hours minutes and seconds

a=int(input("enter the seconds"))
b=a//3600
c=a%3600
d=c//60
e=c%60
 print(b,"hours",d,"minutes",e,"seconds")
 