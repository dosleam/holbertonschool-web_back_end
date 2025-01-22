// Import the process module to handle input/output
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Create a listener for standard input
process.stdin.on('data', (data) => {
  // Display the entered name
  process.stdout.write(`Your name is: ${data}`);
});

// Listener to detect the end of input (Ctrl+D or pipe)
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
