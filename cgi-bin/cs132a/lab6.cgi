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
   <title>Lab 6 Ruby Rails</title>
   <link rel="stylesheet" href="/~dputnam/assets/stylesheets/bootstrap.css">
</head> 
<body> 


<div class="row">
   <div class="container">
    <div class="col-md-8 col-md-offset-2">
<div class="jumbotron">
<h1>Lab 6</h1>
</div>
      <img src="../ruby/img1.png" class="img img-responsive">
	  <br>
	  <img src="../ruby/img2.jpg" class="img img-responsive">
   </div>
</div>
</div>

</body> 
</html> 
HTML