#!/usr/local/bin/ruby

# Name: lab2.cgi
# Creator: Zorigt Bazarragchaa
# Date: 09/21/2013
# \$Id: \$  \# This is for CVS or SVN

puts 'Content-type: text/html'   
puts 
puts <<HTML 
<!DOCTYPE html> 
<html> 
<head> 
<title>Ruby Assignment 2: Zorigt Bazarragchaa</title> 
</head> 
<body> 
HTML

# It makes it easier for me to list HTML titles
three	= "#3 Contents Of Part One"
four 	= "#4 Contents of Part Two"
five 	= "#5 Set of Common Elements"
six 	= "#6 Difference between Parts One and Two"
seven 	= "#7 Difference between Parts Two and One"
eight 	= "#8 Elements at end of Parts One and Two"
nine	= "#9 Elements at front of Parts One and Two"
ten		= "#10 Part Two, Upcased with White Space Removed, inserted into One at Index 100, and flattened"
eleven	= "#11 The new array with Spaces Removed"
twelve	= "#12 After adding a '!' to each element"
thirteen	= "#13 Popped this element"
fourteen	= "#14 Inserted the popped element at index 0"
fifteen		= "#15 The final array with all the elements containing lower-case letters removed"

the_string = <<-HERE 
               this string has leading space and too    MANY tabs and sPaCes betweenX
   the indiVidual Words in each Line.X
  each Line ends with a accidentally  aDDED  X.X
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("normalizing" means   capitalizing sentences   and setting otherX
  characters to lower case)     and removes in       the extra spaces between WOrds.X
HERE

array = the_string.scan(/./m)
oneThird = array.count/3

puts "<ul>"
puts "<li><h3>"+three+"</h3><pre>"
print ary1 = array[0, oneThird]
puts "</pre></li>"

puts "<li><h3>"+four+"</h3><pre>"
print ary2 = array[oneThird, array.count]
puts "</pre></li>"

puts "<li><h3>"+five+"</h3><pre>"
print ary1 & ary2
puts "</pre></li>"

puts "<li><h3>"+six+"</h3><pre>"
print ary1 - ary2
puts "</pre></li>"

puts "<li><h3>"+seven+"</h3><pre>"
print ary2 - ary1
puts "</pre></li>"

puts "<li><h3>"+eight+"</h3><pre>"
puts "One: " + ary1.at(-1).inspect
puts "Two: " + ary2.at(-1).inspect
puts "</pre></li>"

puts "<li><h3>"+nine+"</h3><pre>"
puts "One: " + ary1.at(0).inspect
puts "Two: " + ary2.at(0).inspect
puts "</pre></li>"

puts "<li><h3>"+ten+"</h3><pre>"
ary2.map! {|x| x.upcase}
ary2.keep_if {|v| v =~ /\S/}
print ary1.insert(100, ary2).flatten!
puts "</pre></li>"

puts "<li><h3>"+eleven+"</h3><pre>"
print ary1.keep_if {|v| v =~ /\S/}
puts "</pre></li>"

puts "<li><h3>"+twelve+"</h3><pre>"
print ary1.collect! {|x| x + "!"}
puts "</pre></li>"

puts "<li><h3>"+thirteen+"</h3><pre>"
print popOff = ary1.pop
print "\nThe Remains of the array: " + ary1.inspect
puts "</pre></li>"

puts "<li><h3>"+fourteen+"</h3><pre>"
print ary1.insert(0, popOff)

puts "<li><h3>"+fifteen+"</h3><pre>"
print ary1.select! {|x| x =~ /[A-Z]/}

puts "</ul>"
puts <<HTML 
</body> 
</html> 
HTML