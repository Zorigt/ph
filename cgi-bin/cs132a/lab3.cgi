#!/usr/local/bin/ruby
# encoding: utf-8
# Name: Zorigt Bazarragchaa
# CRN: CS132A-832
# Assignment: 3
# File: lab3.cgi
puts "Content-type: text/html"
puts

puts <<HTML 
<!DOCTYPE html> 
<html> 
<head> 
<meta charset="utf-8">
<title>Ruby Assignment 3: Zorigt Bazarragchaa</title> 
</head> 
<body> 
<div id="main" style="width: 640px; margin: 0 auto; padding: 4em">
<center><h1>Assignment 3: Zorigt Bazarragchaa</h1></center>
HTML

stop_words = File.open("../../ruby/stop_words.txt").read().split(/\W+/)


Dir.glob("../../ruby/speeches/*.txt").each do |file|
    lines = File.readlines(file)
	line_count = lines.size
	text = lines.join
	
	character_count = text.length
	character_count_nospaces = text.force_encoding('UTF-8').gsub(/\s+/, '').length
	
	word_count = text.split.length
	sentence_count = text.split(/\.|\?|!/).length
	paragraph_count = text.split(/\n\n/).length
	
	all_words = text.scan(/\w+/)
	good_words = all_words.select{ |word| !stop_words.include?(word.downcase) }
	good_words = good_words.map {|i| i.downcase}
	good_percentage = ((good_words.length.to_f / all_words.length.to_f) * 100).to_i
	
	sentences = text.gsub(/\s+/, ' ').strip.split(/\.|\?|\!/)
	sentences_sorted = sentences.sort_by { |sentence| sentence.length }
	one_third = sentences_sorted.length / 3
	ideal_sentences = sentences_sorted.slice(one_third - 1 , 7)
	
	counter = {}
	good_words.each { |w|
		if counter.include?(w)
		   counter[w] += 1
		else
		   counter[w] = 1
		end
	}
	ary=Hash[counter.sort{ |a,b| a[1] <=> b[1]}].to_a
	ary = ary.slice(-10 .. -1)
	
	puts "<hr>"
	puts "<center><h2>#{File.basename(file, ".txt")} speech</h2></center>"
	puts "#{line_count} lines<br>"
	puts "#{character_count} characters<br>"
	puts "#{character_count_nospaces} characters (excluding spaces)<br>"
	puts "#{word_count} words<br>"
	puts "#{sentence_count} sentences<br>"
	puts "#{paragraph_count} paragraphs<br>"
	puts "#{sentence_count / paragraph_count} sentences per paragraph<br>"
	puts "#{word_count / sentence_count} words per sentence<br>"
	puts "#{good_percentage}% of words are non-fluff words<br>"
	puts "<h5>Seven Sentence Abstract:</h5>" + ideal_sentences.join(".<br><br>") + "." 
	puts "<h5>Ten Most Common Words</h5>"
	puts ary.reverse
end

puts <<HTML 
</div>
</body> 
</html> 
HTML