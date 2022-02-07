require 'msf/core'
require 'socket'

class MetasploitModule < Msf::Auxilary
    def initialize
        super(
            'Name' => 'TamilOverflow Port Scanner!',
            'Description' => %q{
                This is just a sample Port scanner in auxiliay module!
            },
            'Author' => 'TamilOverflow',
            'License' => MSF_LICENSE
        )

        register_options(
            [
                OptString.new('Target',[true,"Eg : 127.0.0.1 ip adderess"])
                OptInt.new('Port',[false,"Eg : 80,22,443 port"])
            ]
        )
    end

   def run
        port = datastore['Port'] || 80
        host = datastore['Target'] || '127.0.0.1'
        print_status("Scanning start ......")
        print_status("Target => #{host} || Port => #{port}")
        print_status("Please wait ......")
        begin
            validate_socket = TCPSocket.new(host,port)
            status = "OPEN"
        rescue Errno::ECONNREFUSED, Errno::ETIMEDOUT
          status = "CLOSED"
        end
        print_status("Target => #{host} || Port => #{port} || Status => #{status}")
    end
end