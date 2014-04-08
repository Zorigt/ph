#!/usr/local/bin/ruby
# Doug Putnam
# Lab 4: Working with system files
# Displays all of the students in CRNs 73157 abd 74686


# To use modules in the same directory as the lab4.cgi script
# we have to add the current directory to the $LOAD_PATH variable,
# also know as $:

## Good enough for quick and dirty code --- may not work if there
# are any changes of directory in the script.
#
# Add the relative path of current directory to Ruby search path
$:.unshift('.')

## Better. This is more robust and will always work.
# Add the absolute path of current directory to Ruby search path
$:.unshift(File.dirname(__FILE__))
#$LOAD_PATH.unshift(File.dirname(__FILE__))
@output = ''

##
# Add two methods to the String class
class String
  def ucwords
    # Encoding to UTF-8
    out = self.force_encoding('UTF-8').gsub(/\W/,' ')
    # out = self.gsub(/\W/,' ')
    # split on word boundaries then capitalize
    out.split(/\b\s+\b/).collect {|w| w.capitalize }.join(' ') 
  end 

  def alternating_case 
    # alternate upper and lower case characters
    count = 0 
    out = ''

    # Find every character
    self.scan(/./m) do |b| 
        if count == 0 
          out << b.upcase && count = 1 
        else
          out << b.downcase && count = 0 
        end  
    end 
    
    # return the empty string if necessary
    out 
  end 
end

require 'cgi_helper'
include CGI_Helper

def bgcolor(n)
   @@n += 15
   red   = "%02x" %  ((@@n + n) % 200).abs
   green = "%02x" % ((127 -  n) % 200).abs
   blue  = "%02x" %  ((127 + n) % 200).abs
   "#{red}#{green}#{blue}"
end

##
# Print the Content-type
http_header

@@n = 0

crns = [73157, 74686]
cgi = CGI.new




start = Time.now


## 
# A handy array of field @names for printing the HTML <th> tags in the ERB template
@fields = [ :number, :user_name, :password, :uid, :gid, :gcos_field,:home_directory, :login_shell]

##
# The Student class
class Student
  ##
  # A class variable to count the number of students
  @@count = 0;

  ##
  # Create all of the accessors
  attr_accessor :number,:user_name, :password, :uid, :gid, :gcos_field,:home_directory, :login_shell

  def initialize(data)
    @number = @@count + 1;
    @@count = @number;

    ##
    # Use parallel assignment to an array to a list to initialize each object
    @user_name,@password,@uid,@gid,@gcos_field,@home_directory,@login_shell  = data
    @mangled_gcos = ''
  end
end

output = ""

all_students = []

crns.each do |crn|
   output += "<h2>CRN #{crn}</h2>"
   # Get the group line from /etc/passwd. There are many ways to do this, but
   # some methods are more efficient than others. Ideally  you want to go through
   # the file one time only. The Ruby Enumberable::detect method will stop when
   # it detects a match.
   #
   #line = File.readlines('/etc/group').scan {|line| line =~ /77734/ }

   # Get the line containing student @names,
   # We can do this in a ridiculously long single line of code that chains methods together. You
   # can also break this single line into multiple lines if you wish.
   #               read all lines          detect line                         split it on ":", chomp,splt,sort!
   students = File.readlines('/etc/group').detect {|line| line =~ /^c#{crn}:/ }.split(':')[3].chomp.split(',').sort!
   all_students.concat(students)
end

@students_array = []

all_students.each do |student_name|
   ##
   # Use a hash to store student data. Hashes are one of the most efficient way to store and retrieve
   # data. 

   ##
   # Again, we want to go through the password file one line at a time, one time only, collecting student 
   # records along the way.
   File.new('/etc/passwd').collect do |x| 
     if x.split(':')[0] == student_name
        # Create a new Student object with each student's data)
        @students_array << Student.new(x.split(':'))
     end
   end
end

# If we're feeling ambitious we can sort the objects by attribute.
# I use @sort_by to do this, and use the "send" method to set
# the value we are sorting on. If you're really ambitions, you can
# create a toggle sort. 
#
##

# Set a default sort
if @sort_by.nil? or @sort_by.empty?
 @sort_by = 'user_name'
end

# sort by a number
if @sort_by == 'uid' || @sort_by == 'gid'
    @students_array =  @students_array.sort_by {|o| o.send(@sort_by.to_sym) }

# or sort as a string
else
    @students_array =  @students_array.sort_by {|o| o.send(@sort_by.downcase) }
end

students = @students_array
#
finish = Time.now

@for_template =  'Elapsed time: ' + (finish.to_f - start.to_f).to_s + '</pre>'
puts $LOAD_PATH
html = File.read("/students/zbazarra/public_html/cgi-bin/cs132a/temp.html")
# Collect the source code for printing in the ERB template
@source_code = <<END
<div style="background-color:black;color:#efe;">
<pre style="background-color:black;color:#efe;">

      :::            :::     :::::::::      :::::::::: 
     :+:          :+: :+:   :+:    :+:     :+:    :+:  
    +:+         +:+   +:+  +:+    +:+     +:+          
   +#+        +#++:++#++: +#++:++#+      +#++:++#+     
  +#+        +#+     +#+ +#+    +#+            +#+     
 #+#        #+#     #+# #+#    #+#     #+#    #+#      
########## ###     ### #########       ########        
      ::::::::   ::::::::  :::       :::    ::: ::::::::::: ::::::::::: ::::::::  ::::    ::: 
    :+:    :+: :+:    :+: :+:       :+:    :+:     :+:         :+:    :+:    :+: :+:+:   :+:  
   +:+        +:+    +:+ +:+       +:+    +:+     +:+         +:+    +:+    +:+ :+:+:+  +:+   
  +#++:++#++ +#+    +:+ +#+       +#+    +:+     +#+         +#+    +#+    +:+ +#+ +:+ +#+    
        +#+ +#+    +#+ +#+       +#+    +#+     +#+         +#+    +#+    +#+ +#+  +#+#+#     
#+#    #+# #+#    #+# #+#       #+#    #+#     #+#         #+#    #+#    #+# #+#   #+#+#      
########   ########  ########## ########      ###     ########### ########  ###    ####       


#http://www.network-science.de/ascii/
</pre>
</div>
END
#@source_code = File.read('lab4_source.html')
#@source_code += '<h1>Source Code</h1><div style="width:94%"><h1>lab4.cgi</h1>'
#@source_code += '<pre>'
#@source_code += CGI.escapeHTML(File.read('lab4.cgi'))
#@source_code += '</pre>'
#@source_code += '<h1>lab4_template.html.erb</h1>'
#@source_code += '<pre>'
#@source_code += CGI.escapeHTML(File.read('sorting.lab4_template.html.erb'))
#@source_code += '</pre>'
#@source_code += '<h1>cgi_helper.rb</h1>'
#@source_code += '<pre>'
#@source_code += CGI.escapeHTML(File.read('cgi_helper.rb'))
#@source_code += '</pre>'
#@source_code += '</div>'

#
#@source_code ='<div class="alert alert-info"><h5>The source code will be available one week after the assignment due date.</h5></div>'
puts render(html)   