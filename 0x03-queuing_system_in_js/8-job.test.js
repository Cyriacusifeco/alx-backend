const { expect } = require('chai');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

// Set up the test queue in test mode
const queue = kue.createQueue({ disableSearch: true, testMode: true });

// Write the test suite
describe('createPushNotificationsJobs', () => {
  afterEach(() => {
    // Clear the queue and exit test mode after each test
    queue.testMode.clear();
  });

  it('should display an error message if jobs is not an array', () => {
    try {
      createPushNotificationsJobs('invalid-jobs', queue);
    } catch (error) {
      expect(error).to.be.an.instanceOf(Error);
      expect(error.message).to.equal('Jobs is not an array');
    }
  });

  it('should create two new jobs to the queue', () => {
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

    setTimeout(() => {
	   expect(queue.testMode.jobs.length).to.equal(2);
	   done();
	}, 1000); 
  });

  // Can Add more test cases if I need to
});
