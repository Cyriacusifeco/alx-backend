const kue = require('kue');

// Connect to the Redis server where the Kue data is stored
const queue = kue.createQueue();

// Function to send notifications
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Set up the queue process
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done(); // Call this to indicate that the job processing is done
});

console.log('Job processor is listening for new jobs...');
