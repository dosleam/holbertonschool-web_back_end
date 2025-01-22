const fs = require('fs').promises;

async function countStudents(path) {
  try {
    // Read the file asynchronously
    const data = await fs.readFile(path, 'utf8');

    // Split the file content into lines
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // If the file contains no students (empty lines or only the header)
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // Extract the headers (first line of the file)
    const headers = lines[0].split(',');

    // Map each line of the file to a student (as an object)
    const students = lines.slice(1).map((line) => {
      const values = line.split(',');
      const student = {};
      headers.forEach((header, index) => {
        student[header.trim()] = values[index].trim();
      });
      return student;
    });

    // Display the total number of students
    console.log(`Number of students: ${students.length}`);

    // Create an object to group students by field
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

    // Display the number of students per field and the list of their first names
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (err) {
    // If the file is not found or an error occurs, reject with an error message
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
