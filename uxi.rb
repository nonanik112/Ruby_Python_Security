require "msf/core"
class MetasploitModule < Msf::Auxiliary
    include Msf::Auxiliary::Report
    def initialize(info = {})
     super( update_info(info,
            'Name' => 'my first aux',
            'Description' => %q{
              my first auxiliary
            },
            'Author' => ['nonanik <narco112@gmail.com>'],
            'license' => MSF_LICENSE,
            'Version' => '1.0'
        ))
        register_options(
            [
             
             OptString.new('NAME',[true,'your name']),
             OptString.new('AGE',[true,'your age']),

            ],self.class)
    end
    def run
        puts datastore['NAME']
        puts datastore['AGE']
    end
    
end