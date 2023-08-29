const kue = require('kue'); // Import the kue module

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  // ... (other objects)
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

const queue = kue.createQueue(); // This is the line where you declare the queue

for (const jobData of jobs) {
  const job = queue.create('push_notification_code_2', jobData)
    .save(err => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
      }
    });

  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', err => {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  job.on('progress', (progress, data) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });
}
