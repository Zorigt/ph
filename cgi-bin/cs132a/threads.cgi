#!/usr/local/bin/ruby
# Name: threads.cgi
# Creator: Zorigt Bazarragchaa
# \$Id: \$  \# This is for CVS or SVN

require 'cgi'
cgi = CGI.new

threads = []
a_array = ('a'..'z').to_a
temp = ''

puts 'Content-type: text/html'   
puts 

puts <<HTML 
<!DOCTYPE html> 
<html> 
<head> 
<title>Threads CGI</title> 
<style type="text/css">
body, p
{
border-style:solid;
border-width:0px;
position: center;
 width: 800px;
font-size: 36px;line-height:1.5
}
sub {font-size: 16px;color:black}
.thread0 {color: purple }
.thread1 {color: red }
.thread2 {color: blue }
.thread3 {color: green }
.thread4 {color: lightgreen }
.thread5 {color: magenta }
.thread6 {color: cyan }
.thread7 {color: black }
.thread8 {color: gray }
.thread9 {color: orange }
.thread10 {color: yellow }
    </style>
</head> 
<body> 
<p>
HTML
 
10.times do |j| 

	thread = Thread.new do 
		a_array.each {|i| puts "<span class=thread#{j}>#{i}<sub class=thread#{j}>#{j}</sub></span>"; $stdout.flush; sleep rand(0)}
		a_array.each {|i| puts "<span class=thread#{j}>#{i.upcase}<sub class=thread#{j}>#{j}</sub></span>" ; $stdout.flush; sleep rand(0)}
	end
	
	threads << thread
end 

threads.each {|thread| thread.join()}
puts <<HTML 
</p>
</body> 
</html> 
HTML