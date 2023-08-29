import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error.message);
});

// Define the setNewSchool function
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Define the displaySchoolValue function
function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    console.log(reply);
  });
}

// Call the displaySchoolValue function with 'Holberton'
displaySchoolValue('Holberton');

// Call the setNewSchool function with 'HolbertonSanFrancisco' and '100'
setNewSchool('HolbertonSanFrancisco', '100');

// Call the displaySchoolValue function with 'HolbertonSanFrancisco'
displaySchoolValue('HolbertonSanFrancisco');
