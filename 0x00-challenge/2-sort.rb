###
#
#  Sorting thw integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
    # skip if not integer
    next if arg !~ /^-?[0-9]+$/

    # convert to integer
    i_arg = arg.to_i

    # insert result at the right position
    is_inserted = false
    a = 0
    l = result.size
    while !is_inserted && a < l do
        if result[a] < i_arg
            a += 1
        else
            result.insert(a, i_arg)
            is_inserted = true
            break
        end
    end
    result << i_arg if !is_inserted
end

puts result
