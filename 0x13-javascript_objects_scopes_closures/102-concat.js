#!/usr/bin/node

const fs = require('fs');

const args = process.argv;

// Check if the correct number of arguments is provided
if (args.length !== 5) {
  console.error('Usage: ./script.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const fileA = args[2];
const fileB = args[3];
const fileC = args[4];

// Read the content of the source files
const contentA = fs.readFileSync(fileA, 'utf-8');
const contentB = fs.readFileSync(fileB, 'utf-8');

// Concatenate the content
const concatenatedContent = contentA + contentB;

// Write the concatenated content to the destination file (fileC)
fs.writeFileSync(fileC, concatenatedContent);
