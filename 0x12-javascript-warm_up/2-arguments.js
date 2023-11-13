#!/usr/bin/node

const args = process.argv.slice(2);
let arg_l = args.length;

if (arg_l === 0)
{
  console.log('No argument');
}
else if (arg_l === 1)
{
  console.log('Argument found');
}
else
{
  console.log('Arguments found');
}

console.log(arg_l)
