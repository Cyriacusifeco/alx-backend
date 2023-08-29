import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error('Redis client not connected to the server:', error.message);
});

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

// Define the setNewSchool function
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Define the displaySchoolValue function using async/await
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the displaySchoolValue function with 'Holberton'
displaySchoolValue('Holberton');

// Call the setNewSchool function with 'HolbertonSanFrancisco' and '100'
setNewSchool('HolbertonSanFrancisco', '100');

// Call the displaySchoolValue function with 'HolbertonSanFrancisco'
displaySchoolValue('HolbertonSanFrancisco');
