#!/usr/local/bin/ruby
# Name: dangerous.cgi
# Creator: Zorigt Bazarragchaa
# Date: 11/03/2013
# \$Id: \$  \# This is for CVS or SVN

require 'cgi'
cgi = CGI.new
str = cgi['input']


	
	temp = str.count(';' '*' '`' '\"' '\'' '-')
	if temp > 0
		var = 'Danger!'
		var = ' <div class="alert alert-danger">
		<h1><span class="tainted">Danger!</span></h1>
		</div>'
	else 
		if str == ""
			var = ""
		else
			var ='<div class="alert alert-success">
					<h1><span class="not-tainted">Safe :)</span></h1>
					</div>'
		end
	end
	


puts 'Content-type: text/html'   
puts 

puts <<HTML 
<!DOCTYPE html> 
<html> 
<head> 
<title>dangerous CGI</title> 
<link rel="stylesheet" href="/~dputnam/assets/stylesheets/bootstrap.css" media="all">
</head> 
<body> 
 <h1>Test the Danger</h1>
    <form action="" method="POST" accept-charset="utf-8">
       <p>Enter text: <br><textarea name="input" id="input">#{str}</textarea></p>
       <p><input type="submit" value="Check here"></p>
    </form> 

HTML
 
puts <<HTML 
<p>#{var}</p>
</body> 
</html> 
HTML