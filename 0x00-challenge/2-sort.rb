###
#
#  Sorting the integer arguments (ascending) 
#
###

res = []
ARGV.each do |arg|
    # skipping non_integer
    next if arg !~ /^-?[0-9]+$/

    # converting to integer
    i_arg = arg.to_i

    # result at the right position
    _inserted = false
    a = 0
    i = res.size
    while !_inserted && a < i do
        if result[i] < i_arg
            a += 1
        else
            res.insert(a, i_arg)
            _inserted = true
            break
        end
    end
    res << i_arg if !_inserted
end

puts res
