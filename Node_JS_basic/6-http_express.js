const express = require('express');

// Create an Express application
const app = express();

// Handle the "/" endpoint
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Make the server listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Export the application
module.exports = app;
