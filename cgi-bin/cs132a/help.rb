#!/usr/local/bin/ruby

require 'rubygems'
require 'cgi'
require 'erb'
module CGI_Helper


  # This is a good function for printing HTML safely
  def h(html)
    CGI.escapeHTML(html)
  end

  # This is a convenience function that prints the Content-type, DOCTYPE, and <html> tag.
  def http_header(mode='text/html',doc=:html5)
    puts 'Content-type: ' + mode
    puts
    # puts doctype()
  end

  # This method will process text as ERB code and return the result. 
  def render(html)
    require 'erb'
    erb = ERB.new(html)
    erb.result
  end

  

end

if $0 == 'cgi_helper.rb'
  include CGI_Helper
  http_header('text/html','html5')
html = <<HTML
This will be the HTML that I want to print. Any Ruby code
will be embedded with ERB tags (&lt;% #ruby code %&gt;).
HTML
puts render(html)
end