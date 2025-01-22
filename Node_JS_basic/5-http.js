const http = require('http');
const fs = require('fs').promises;

// Function to read and analyze the CSV file
async function countStudents(path) {
  try {
    // Read the file asynchronously
    const data = await fs.readFile(path, 'utf8');
    
    // Split the file content into lines and filter out empty lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // If the file contains only the header or is empty
    if (lines.length <= 1) {
      return 'Number of students: 0';
    }

    // Extract headers (first line of the file)
    const headers = lines[0].split(',');

    // Map each subsequent line to a student object
    const students = lines.slice(1).map((line) => {
      const values = line.split(',');
      const student = {};
      headers.forEach((header, index) => {
        student[header.trim()] = values[index].trim();
      });
      return student;
    });

    // Create a string for the total number of students
    const totalStudents = `Number of students: ${students.length}`;

    // Group students by their field of study
    const fields = {};
    students.forEach((student) => {
      const { field } = student;
      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student.firstname);
      }
    });

    // Generate a string with the details of each field
    let fieldDetails = '';
    for (const [field, names] of Object.entries(fields)) {
      fieldDetails += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
    }

    // Return the combined student details
    return `${totalStudents}${fieldDetails}`;
  } catch (err) {
    // Throw an error if the file cannot be loaded
    throw new Error('Cannot load the database');
  }
}

// Create the HTTP server
const app = http.createServer(async (req, res) => {
  const { url } = req;

  if (url === '/') {
    // Respond to the root endpoint
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    // Respond to the /students endpoint
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    // Get the file path from the command line arguments
    const databasePath = process.argv[2];
    if (!databasePath) {
      res.end('This is the list of our students\nCannot load the database');
      return;
    }

    try {
      // Retrieve and send the student data
      const studentData = await countStudents(databasePath);
      res.end(`This is the list of our students\n${studentData}`);
    } catch (err) {
      // Send an error message if the file cannot be processed
      res.end('This is the list of our students\nCannot load the database');
    }
  } else {
    // Handle unknown endpoints
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

// Make the server listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

// Export the server
module.exports = app;
