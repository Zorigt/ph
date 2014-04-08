#!/usr/local/bin/ruby
# encoding: utf-8
ENV['GEM_HOME'] = "/students/zbazarra/mygems"

require "cgi"
require 'bluecloth'

puts 'Content-type: text/html'  
puts 


str = File.open("/students/zbazarra/public_html/ruby/oliver.markdown.txt")
s=""
str.each do |w|
s << w
end

puts <<HTML 
<!DOCTYPE html> 
<html> 
<head> 
<title>BlueClothing CGI</title> 
</head> 
<body> 
HTML

puts BlueCloth.new(s).to_html

puts <<HTML 
</body> 
</html> 
HTML

