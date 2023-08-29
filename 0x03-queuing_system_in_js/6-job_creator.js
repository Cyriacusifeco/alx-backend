import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification.'
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData)
  .save((error) => {
    if (!error) {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// Event listeners for job completion and failure
job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
