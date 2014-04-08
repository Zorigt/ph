the_string = <<-HERE 
               this string has leading space and too    MANY tabs and sPaCes betweenX
   the indiVidual Words in each Line.X
  each Line ends with a accidentally  aDDED  X.X
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("normalizing" means   capitalizing sentences   and setting otherX
  characters to lower case)     and removes in       the extra spaces between WOrds.X
HERE

puts "\n" + "="*28 + " 1.1 squeeze " + "="*28 + "\n"*2
# String#squeeze
puts the_string.squeeze

puts "\n" + "="*28 + " 1.2 downcase " + "="*28 + "\n"*2
# String#downcase
puts the_string.downcase

puts "\n" + "="*28 + " 1.3 upcase " + "="*28 + "\n"*2
# String#upcase 
puts the_string.upcase

puts "\n" + "="*28 + " 1.4 capitalize " + "="*28 + "\n"*2
# String#capitalize
a = the_string.split(/$/)
a.each {|x| x.match(/(\W+)(\w+)(...+)/) {print $1+$2.capitalize+$3}}

puts "\n" + "="*28 + " 1.5 remove X " + "="*28 + "\n"*2
# Removing the Ending 'X'
puts the_string.gsub(/X$/, '')

puts "\n" + "="*28 + " 1.6 each_byte " + "="*28 + "\n"*2
# String#each_byte
puts "-"*10 
puts "C" "|" "Dec" "|" "Hex" 
puts "-"*10 
the_string.each_byte {|c| puts "%-1s|%3s|0x%x" % [c.chr, c.to_s, c]}

puts "\n" + "="*28 + " 1.7 split " + "="*28 + "\n"*2
# String#split
print the_string.split(" ")
puts 
puts
print the_string.split(/\s/)
puts

puts "\n" + "="*28 + " 1.8 crypt " + "="*28 + "\n"*2
# String#crypt
puts the_string.crypt("zorigt")

puts "\n" + "="*28 + " 1.9 replace " + "="*28 + "\n"*2
# String#replace
the_string[0,100]=the_string[0,100].strip.reverse.squeeze.upcase
puts the_string

puts "\n" + "="*28 + " 1.10 inspect " + "="*28 + "\n"*2
# String#inspect
puts the_string.inspect