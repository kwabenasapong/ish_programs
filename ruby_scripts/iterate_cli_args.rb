#!/usr/bin/env ruby
result = []
##sum = 0
ARGV.each do |arg|

  next if arg !~/^-?[0-9]+$/

  i_arg = arg.to_i

  #puts "Argument: #{arg}"

  #sum += i_arg
  is_inserted = false
  i = 0
  l = result.size

  while !is_inserted && i < l do
    if result[i] < i_arg
      i += 1
      puts 'ok'
    else
      result.insert(i, i_arg)
      is_inserted = true
      puts 'swap'
      break
    end
  end

  result << i_arg if !is_inserted

end

  #puts sum
  puts result
