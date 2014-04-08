#!/usr/local/bin/ruby
# Zorigt Bazarragchaa
# Lab 4

$:.unshift('.')
$:.unshift(File.dirname(__FILE__))

@output = ''

class String
  def ucwords
    out = self.force_encoding('UTF-8').gsub(/\W/,' ')
    out.split(/\b\s+\b/).collect {|w| w.capitalize }.join(' ') 
  end 

  def alternating_case 
    count = 0 
    out = ''

    self.scan(/./m) do |b| 
        if count == 0 
          out << b.upcase && count = 1 
        else
          out << b.downcase && count = 0 
        end  
    end 
    out 
  end 
end

require 'cgi_helper'
include CGI_Helper

http_header

@@n = 0

crns = [73157, 74686]
cgi = CGI.new

start = Time.now

@fields = [ :number, :user_name, :password, :uid, :gid, :gcos_field,:home_directory, :login_shell]


class Student
  @@count = 0;

  attr_accessor :number,:user_name, :password, :uid, :gid, :gcos_field,:home_directory, :login_shell

  def initialize(data)
    @number = @@count + 1;
    @@count = @number;

    @user_name,@password,@uid,@gid,@gcos_field,@home_directory,@login_shell  = data
    @mangled_gcos = ''
  end
end

output = ""

all_students = []

crns.each do |crn|
	students = File.readlines('/etc/group').detect {|line| line =~ /^c#{crn}:/ }.split(':')[3].chomp.split(',').sort!
   all_students.concat(students)
end

@students_array = []

all_students.each do |student_name|
     File.new('/etc/passwd').collect do |x| 
     if x.split(':')[0] == student_name
        @students_array << Student.new(x.split(':'))
     end
   end
end

if @sort_by.nil? or @sort_by.empty?
 @sort_by = 'user_name'
end

if @sort_by == 'uid' || @sort_by == 'gid'
    @students_array =  @students_array.sort_by {|o| o.send(@sort_by.to_sym) }

else
    @students_array =  @students_array.sort_by {|o| o.send(@sort_by.downcase) }
end

students = @students_array

finish = Time.now

@for_template =  'Elapsed time: ' + (finish.to_f - start.to_f).to_s + '</pre>'

html = File.read("/students/zbazarra/public_html/cgi-bin/cs132a/temp.html")

puts render(html)   