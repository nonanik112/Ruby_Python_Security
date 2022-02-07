#!/usr/bin/env ruby

information = "Bidiği tüm bilgileri ortaya koyay"
information = information.gsub("buen","excelente")
#puts information

hello = "selam veriyor"
hello = hello.sub(/^..../,"Burası cok onemli")
#puts hello

reply = "Etik hacking islem"
reply = reply.scan(/\S\S\S/) {|i| i}

trial = "bilgi içerin tüm içerikler 1005 numarada toplanir"
trial = trial.scan(/\d+/){|i|i}
trial = trial.scan(/[eoa]/){|i|  i}
trial = trial.scan(/[a-m]+/){|i| puts i}