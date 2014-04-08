#!/usr/local/bin/ruby
# encoding: utf-8
ENV['GEM_HOME'] = "/students/zbazarra/mygems"

require 'bluecloth'

puts 'Content-type: text/html'  
puts 


str = File.open("text.txt")

str.each do |w|
puts BlueCloth.new(w).to_html
end

