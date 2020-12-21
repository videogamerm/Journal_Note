#!/usr/bin/ruby

x = 1

time = 1
while time< 3000  do
   

   if x == 1
      puts "-"
      x+=1
      sleep(0.001)
   elsif x == 2 
      puts "/"
      x += 1
      sleep(0.001)
   elsif x == 3 
      puts "|"
      x += 1
      sleep(0.001)
   elsif x == 4
      puts '\\'
   \
   sleep(0.001)
      x = 1
   
   
   end
time +=1
end