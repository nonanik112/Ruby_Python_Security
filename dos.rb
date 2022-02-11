# if Rails.env.production? && ENV["DISABLE_RACK_ATTACK"].blank?
#   require 'socket'
#   require 'ipaddr'
#
#   class Rack::Attack
#     class Request < ::Rack::Request
#       socket = Socket.new(:INET, :STREAM)
#
#       socket.bind(Socket.pack_sockaddr_in(3000, '127.0.0.1'))
#       socket.listen(Socket::SOMAXCONN)
#       loop do
#         connection. _ = socket.accept
#       end
#       def remote_ip
#         @remote_ip ||= (env['HTTP_CF_CONNECTING_IP'] ||
#                  env['action_dispatch.remote_ip'] ||
#                  ip).to_s
#       end
#       class Server
#         def intialize(port)
#           @server = TCPServer.new(port)
#           @connections = []
#           puts "listening on port #{port}"
#         end
#       end
#     end
#   end
# end

require 'rack-attack'
require 'socket'

config.middleware.use Rack::Attack
redis_client = Redis.connect(url: ENV["REDIS_URL"])
Rack::Attack.cache.store = Rack::Attack::StoreProxy::RedisStoreProxy.new(redis_client)

socket = Socket.new(:INET, :STREAM)
socket.bind(Socket.pack_sockaddr_in(3000, '109.232.219.156'))
socket.listen(Socket::SOXMAXCONN)

class Rack::Attack
  class Request < ::Rack::Request
    def remote_ip
      @remote_ip ||= (env ['HTTP_CF_CONNECTING_IP'] ||
                      env['action_dispatch.remote_ip'] ||
                      ip).to_s

    end
  end
end
