require 'socket'

# PORT = #ARGV[0] || 80 
# HOST = "10.0.2.255"#ARGV[1] || 'Localhost'

# begin 
#     socket =  TCPSocket.new(HOST, PORT),
#     status = "acik"
# rescue Errno::ECONNREFUSED, Errno::ETIMEDOUT
#     status = "kapali"
# end

# puts "Liman:  #{PORT} ve #{status}"

TIMEOUT = 2

def scan_port(puerto)
    socket = Socket.new(:INET,:STREAM)
    ip = Socket.sockaddr_in(port, '100.0.2.255')

    begin
        socket.connect_nonblock(ip)
    rescue Errno::EINPROGRESS
    end
    _, sockets, _= IO.select(nill, [socket],nill,TIMEOUT)
    if sockets
        puts "Baslangic #{port} Acik"
    else
       puts "Baslangic #{puerto} Kapali"
    end
end

ports = [21,22,23,53,80,443,3306,8080]
threads = []

ports.each {|i| threads << Thread.new{scan_port(i)}}
threads.each(&:join)
