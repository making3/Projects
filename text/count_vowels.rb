vowels = [ 'a', 'e', 'i', 'o', 'u' ]
print "Please enter a string to count vowels with: "
input = gets.chomp
puts "You entered: #{input}"
results = input.split("")

results.each do |c| 
    if vowels.include? c
        puts "Character found: #{c}"
    end
end
