const kue = require('kue');
const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach(jobData => {
    const job = queue.create('push_notification_code_3', jobData).save(err => {
      if (err) {
        console.error(`Error creating job: ${err}`);
        return;
      }
      console.log(`Notification job created: ${job.id}`);

      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });

      job.on('failed', error => {
        console.error(`Notification job ${job.id} failed: ${error}`);
      });

      job.on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    });
  });
}

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  }
];

createPushNotificationsJobs(jobs, queue);
