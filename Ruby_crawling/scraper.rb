require 'nokogiri'
require 'open-uri'

doc = Nokogiri::HTML(open('https://www.gencayyildiz.com/blog/'))

body = doc.css('body.home').css('div.wrapper')
open('test.csv', 'w') do |arg|
body.search('h1').each do |h1|
  body = h1.css('site-title').css.('p').text
  note = p.css('custom-logo-link').css('p').text
  arg.puts %("#{title.chomp}";"#{note.chomp }")
  next if main['class'] == 'page-title hu-pad group'
 end
end
