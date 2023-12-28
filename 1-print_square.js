#!/usr/bin/node
/*
    Printing a square with size of the square
    must be the first argument 
    of the program.
*/


if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1)
}

the_size = parseInt(process.argv[2], 10)

for (let a = 0 ; a < the_size ; a ++) {
    for (let j = 0 ; j < the_size ; j ++) {
        process.stdout.write("#");
    }
    process.stdout.write("\n");
}
