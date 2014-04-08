# Zorigt Bazarragchaa
# Assignment 1

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

=begin
[zbazarra@hills ~]$ ruby $HOME/public_html/cgi-bin/cs132a/assignment1.rb

============================ 1.1 squeeze ============================

 this string has leading space and to MANY tabs and sPaCes betwenX
 the indiVidual Words in each Line.X
 each Line ends with a acidentaly aDED X.X
 in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
 ("normalizing" means capitalizing sentences and seting otherX
 characters to lower case) and removes in the extra spaces betwen WOrds.X

============================ 1.2 downcase ============================

               this string has leading space and too    many tabs and spaces betweenx
   the individual words in each line.x
  each line ends with a accidentally  added  x.x
            in this lab you will write code that "sanitizes" this string by normalizingx
   ("normalizing" means   capitalizing sentences   and setting otherx
  characters to lower case)     and removes in       the extra spaces between words.x

============================ 1.3 upcase ============================

               THIS STRING HAS LEADING SPACE AND TOO    MANY TABS AND SPACES BETWEENX
   THE INDIVIDUAL WORDS IN EACH LINE.X
  EACH LINE ENDS WITH A ACCIDENTALLY  ADDED  X.X
            IN THIS LAB YOU WILL WRITE CODE THAT "SANITIZES" THIS STRING BY NORMALIZINGX
   ("NORMALIZING" MEANS   CAPITALIZING SENTENCES   AND SETTING OTHERX
  CHARACTERS TO LOWER CASE)     AND REMOVES IN       THE EXTRA SPACES BETWEEN WORDS.X

============================ 1.4 capitalize ============================

               This string has leading space and too    MANY tabs and sPaCes betweenX
   The indiVidual Words in each Line.X
  Each Line ends with a accidentally  aDDED  X.X
            In this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("Normalizing" means   capitalizing sentences   and setting otherX
  Characters to lower case)     and removes in       the extra spaces between WOrds.X
============================ 1.5 remove X ============================

               this string has leading space and too    MANY tabs and sPaCes between
   the indiVidual Words in each Line.
  each Line ends with a accidentally  aDDED  X.
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizing
   ("normalizing" means   capitalizing sentences   and setting other
  characters to lower case)     and removes in       the extra spaces between WOrds.

============================ 1.6 each_byte ============================

----------
C|Dec|Hex
----------
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
t|116|0x74
h|104|0x68
i|105|0x69
s|115|0x73
 | 32|0x20
s|115|0x73
t|116|0x74
r|114|0x72
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
h|104|0x68
a| 97|0x61
s|115|0x73
 | 32|0x20
l|108|0x6c
e|101|0x65
a| 97|0x61
d|100|0x64
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
s|115|0x73
p|112|0x70
a| 97|0x61
c| 99|0x63
e|101|0x65
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
t|116|0x74
o|111|0x6f
o|111|0x6f
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
M| 77|0x4d
A| 65|0x41
N| 78|0x4e
Y| 89|0x59
 | 32|0x20
t|116|0x74
a| 97|0x61
b| 98|0x62
s|115|0x73
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
s|115|0x73
P| 80|0x50
a| 97|0x61
C| 67|0x43
e|101|0x65
s|115|0x73
 | 32|0x20
b| 98|0x62
e|101|0x65
t|116|0x74
w|119|0x77
e|101|0x65
e|101|0x65
n|110|0x6e
X| 88|0x58

| 10|0xa
 | 32|0x20
 | 32|0x20
 | 32|0x20
t|116|0x74
h|104|0x68
e|101|0x65
 | 32|0x20
i|105|0x69
n|110|0x6e
d|100|0x64
i|105|0x69
V| 86|0x56
i|105|0x69
d|100|0x64
u|117|0x75
a| 97|0x61
l|108|0x6c
 | 32|0x20
W| 87|0x57
o|111|0x6f
r|114|0x72
d|100|0x64
s|115|0x73
 | 32|0x20
i|105|0x69
n|110|0x6e
 | 32|0x20
e|101|0x65
a| 97|0x61
c| 99|0x63
h|104|0x68
 | 32|0x20
L| 76|0x4c
i|105|0x69
n|110|0x6e
e|101|0x65
.| 46|0x2e
X| 88|0x58

| 10|0xa
 | 32|0x20
 | 32|0x20
e|101|0x65
a| 97|0x61
c| 99|0x63
h|104|0x68
 | 32|0x20
L| 76|0x4c
i|105|0x69
n|110|0x6e
e|101|0x65
 | 32|0x20
e|101|0x65
n|110|0x6e
d|100|0x64
s|115|0x73
 | 32|0x20
w|119|0x77
i|105|0x69
t|116|0x74
h|104|0x68
 | 32|0x20
a| 97|0x61
 | 32|0x20
a| 97|0x61
c| 99|0x63
c| 99|0x63
i|105|0x69
d|100|0x64
e|101|0x65
n|110|0x6e
t|116|0x74
a| 97|0x61
l|108|0x6c
l|108|0x6c
y|121|0x79
 | 32|0x20
 | 32|0x20
a| 97|0x61
D| 68|0x44
D| 68|0x44
E| 69|0x45
D| 68|0x44
 | 32|0x20
 | 32|0x20
X| 88|0x58
.| 46|0x2e
X| 88|0x58

| 10|0xa
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
i|105|0x69
n|110|0x6e
 | 32|0x20
t|116|0x74
h|104|0x68
i|105|0x69
s|115|0x73
 | 32|0x20
l|108|0x6c
a| 97|0x61
b| 98|0x62
 | 32|0x20
y|121|0x79
o|111|0x6f
u|117|0x75
 | 32|0x20
w|119|0x77
i|105|0x69
l|108|0x6c
L| 76|0x4c
 | 32|0x20
W| 87|0x57
R| 82|0x52
I| 73|0x49
T| 84|0x54
E| 69|0x45
 | 32|0x20
c| 99|0x63
o|111|0x6f
d|100|0x64
e|101|0x65
 | 32|0x20
t|116|0x74
h|104|0x68
a| 97|0x61
t|116|0x74
 | 32|0x20
"| 34|0x22
s|115|0x73
A| 65|0x41
n|110|0x6e
I| 73|0x49
T| 84|0x54
i|105|0x69
z|122|0x7a
E| 69|0x45
S| 83|0x53
"| 34|0x22
 | 32|0x20
t|116|0x74
h|104|0x68
i|105|0x69
s|115|0x73
 | 32|0x20
s|115|0x73
t|116|0x74
r|114|0x72
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
b| 98|0x62
y|121|0x79
 | 32|0x20
n|110|0x6e
o|111|0x6f
r|114|0x72
m|109|0x6d
a| 97|0x61
l|108|0x6c
i|105|0x69
z|122|0x7a
i|105|0x69
n|110|0x6e
g|103|0x67
X| 88|0x58

| 10|0xa
 | 32|0x20
 | 32|0x20
 | 32|0x20
(| 40|0x28
"| 34|0x22
n|110|0x6e
o|111|0x6f
r|114|0x72
m|109|0x6d
a| 97|0x61
l|108|0x6c
i|105|0x69
z|122|0x7a
i|105|0x69
n|110|0x6e
g|103|0x67
"| 34|0x22
 | 32|0x20
m|109|0x6d
e|101|0x65
a| 97|0x61
n|110|0x6e
s|115|0x73
 | 32|0x20
 | 32|0x20
 | 32|0x20
c| 99|0x63
a| 97|0x61
p|112|0x70
i|105|0x69
t|116|0x74
a| 97|0x61
l|108|0x6c
i|105|0x69
z|122|0x7a
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
s|115|0x73
e|101|0x65
n|110|0x6e
t|116|0x74
e|101|0x65
n|110|0x6e
c| 99|0x63
e|101|0x65
s|115|0x73
 | 32|0x20
 | 32|0x20
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
s|115|0x73
e|101|0x65
t|116|0x74
t|116|0x74
i|105|0x69
n|110|0x6e
g|103|0x67
 | 32|0x20
o|111|0x6f
t|116|0x74
h|104|0x68
e|101|0x65
r|114|0x72
X| 88|0x58

| 10|0xa
 | 32|0x20
 | 32|0x20
c| 99|0x63
h|104|0x68
a| 97|0x61
r|114|0x72
a| 97|0x61
c| 99|0x63
t|116|0x74
e|101|0x65
r|114|0x72
s|115|0x73
 | 32|0x20
t|116|0x74
o|111|0x6f
 | 32|0x20
l|108|0x6c
o|111|0x6f
w|119|0x77
e|101|0x65
r|114|0x72
 | 32|0x20
c| 99|0x63
a| 97|0x61
s|115|0x73
e|101|0x65
)| 41|0x29
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
a| 97|0x61
n|110|0x6e
d|100|0x64
 | 32|0x20
r|114|0x72
e|101|0x65
m|109|0x6d
o|111|0x6f
v|118|0x76
e|101|0x65
s|115|0x73
 | 32|0x20
i|105|0x69
n|110|0x6e
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
 | 32|0x20
t|116|0x74
h|104|0x68
e|101|0x65
 | 32|0x20
e|101|0x65
x|120|0x78
t|116|0x74
r|114|0x72
a| 97|0x61
 | 32|0x20
s|115|0x73
p|112|0x70
a| 97|0x61
c| 99|0x63
e|101|0x65
s|115|0x73
 | 32|0x20
b| 98|0x62
e|101|0x65
t|116|0x74
w|119|0x77
e|101|0x65
e|101|0x65
n|110|0x6e
 | 32|0x20
W| 87|0x57
O| 79|0x4f
r|114|0x72
d|100|0x64
s|115|0x73
.| 46|0x2e
X| 88|0x58

| 10|0xa

============================ 1.7 split ============================

["this", "string", "has", "leading", "space", "and", "too", "MANY", "tabs", "and", "sPaCes", "betweenX", "the", "indiVidual", "Words", "in", "each", "Line.X", "each", "Line", "ends", "with", "a", "accidentally", "aDDED", "X.X", "in", "this", "lab", "you", "wilL", "WRITE", "code", "that", "\"sAnITizES\"", "this", "string", "by", "normalizingX", "(\"normalizing\"", "means", "capitalizing", "sentences", "and", "setting", "otherX", "characters", "to", "lower", "case)", "and", "removes", "in", "the", "extra", "spaces", "between", "WOrds.X"]

["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "this", "string", "has", "leading", "space", "and", "too", "", "", "", "MANY", "tabs", "and", "sPaCes", "betweenX", "", "", "", "the", "indiVidual", "Words", "in", "each", "Line.X", "", "", "each", "Line", "ends", "with", "a", "accidentally", "", "aDDED", "", "X.X", "", "", "", "", "", "", "", "", "", "", "", "", "in", "this", "lab", "you", "wilL", "WRITE", "code", "that", "\"sAnITizES\"", "this", "string", "by", "normalizingX", "", "", "", "(\"normalizing\"", "means", "", "", "capitalizing", "sentences", "", "", "and", "setting", "otherX", "", "", "characters", "to", "lower", "case)", "", "", "", "", "and", "removes", "in", "", "", "", "", "", "", "the", "extra", "spaces", "between", "WOrds.X"]

============================ 1.8 crypt ============================

zozrGf.n8T1LQ

============================ 1.9 replace ============================

DIVIDNI EHT 
XNEWTEB SECAPS DNA SBAT YNAM OT DNA ECAPS GNIDAEL SAH GNIRTS SIHTual Words in each Line.X
  each Line ends with a accidentally  aDDED  X.X
            in this lab you wilL WRITE code that "sAnITizES" this string by normalizingX
   ("normalizing" means   capitalizing sentences   and setting otherX
  characters to lower case)     and removes in       the extra spaces between WOrds.X

============================ 1.10 inspect ============================

"DIVIDNI EHT \nXNEWTEB SECAPS DNA SBAT YNAM OT DNA ECAPS GNIDAEL SAH GNIRTS SIHTual Words in each Line.X\n  each Line ends with a accidentally  aDDED  X.X\n            in this lab you wilL WRITE code that \"sAnITizES\" this string by normalizingX\n   (\"normalizing\" means   capitalizing sentences   and setting otherX\n  characters to lower case)     and removes in       the extra spaces between WOrds.X\n"
[zbazarra@hills ~]$ 
=end