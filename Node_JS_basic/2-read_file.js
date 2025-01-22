const fs = require('fs');

function countStudents(path) {
  try {
    // Synchronously read the file
    const data = fs.readFileSync(path, 'utf8');

    // Split the file content into lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Check if the file contains a header
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // Extract headers and data
    const headers = lines[0].split(',');
    const students = lines.slice(1).map((line) => {
      const values = line.split(',');
      const student = {};
      headers.forEach((header, index) => {
        student[header.trim()] = values[index].trim();
      });
      return student;
    });

    // Count the number of students
    console.log(`Number of students: ${students.length}`);

    // Group students by field
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

    // Display the results for each field
    for (const [field, names] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
      );
    }
  } catch (err) {
    // In case of an error, throw an exception
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
