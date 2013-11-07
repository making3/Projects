#require 'io/console'
contents = IO.read('./words.txt')
puts "File contents: #{contents}"
results = contents.split(" ")

puts "Result words: "
results.each do |word|
    puts word
end
