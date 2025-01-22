const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
  // Set response headers
  res.statusCode = 200; // 200 = OK
  res.setHeader('Content-Type', 'text/plain'); // Response in plain text

  // Response content
  res.end('Hello Holberton School!');
});

// Make the server listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

// Export the server for reuse
module.exports = app;
