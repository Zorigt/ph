require 'open-uri'
names = ''
uri = open('http://www.rubyinside.com/book/oliver.txt') do |f| f.each_line do |line| names += line.chomp end end
puts names.size