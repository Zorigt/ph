#!/usr/local/bin/ruby
# encoding: utf-8
ENV['GEM_HOME'] = "/students/zbazarra/mygems"

require "cgi"

puts 'Content-type: text/html'  
puts 

puts <<HTML 
<!DOCTYPE html> 
<html> 
<head> 
	<meta charset='utf-8'>
   <title>Lab 8 Ruby Rails</title>
   <link rel="stylesheet" href="/~dputnam/assets/stylesheets/bootstrap.css">
</head> 
<body> 


<h1>Lab 8</h1>
<p>Zorigt Heroku App</p>
<a href="http://salty-woodland-2694.herokuapp.com/">http://salty-woodland-2694.herokuapp.com/</a>

</body> 
</html> 
HTML