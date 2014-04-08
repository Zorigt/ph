#!/usr/local/bin/ruby
$:.unshift('.')

$:.unshift(File.dirname(__FILE__))
@output = ''


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



finish = Time.now

@for_template =  'Elapsed time: ' + (finish.to_f - start.to_f).to_s + '</pre>'
html = File.read('html')

puts render(html)   