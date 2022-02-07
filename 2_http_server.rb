#!/usr/bin/env ruby

require 'webrick'
path = File.expand_path('/root/Desktop/ruby')
server = WEBrick::HTTPServer.new :Port => 8080, :DocumentRoot => path

trap 'INT' do sever.shutdown end 
server.start

