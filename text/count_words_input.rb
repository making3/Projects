print "Please enter a short sentence to count the number of words inputted: "
input = gets.chomp
puts "You entered: #{input}"
results = input.split(" ")

puts "Result words: "
results.each do |word|
    puts word
end
