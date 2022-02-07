require "em-resolv-replace"
$dns = Resolv::DNS.mew
$dns.each_resource("gmail.com", Resolv::DNS::Resource::IN::MX) do |mail_servers|
    puts mail_servers.exchange
end