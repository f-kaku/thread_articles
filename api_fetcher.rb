require 'net/http'
require 'json'

urls = [
  'http://localhost:5000/api/endpoint1',
  'http://localhost:5000/api/endpoint2',
  'http://localhost:5000/api/endpoint3',
  'http://localhost:5000/api/endpoint4'
]

start_time = Time.now

threads = urls.map do |url|
  Thread.new do
    response = Net::HTTP.get(URI(url))
    puts JSON.parse(response)["message"]
  end
end

threads.each(&:join)

puts "Total Time: #{Time.now - start_time} seconds"