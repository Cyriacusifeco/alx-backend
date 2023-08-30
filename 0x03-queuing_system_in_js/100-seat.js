const redis = require('redis');
const { promisify } = require('util');
const kue = require('kue');
const express = require('express');
const app = express();

const port = 1245;

const queue = kue.createQueue();

// Create a Redis client
const redisClient = redis.createClient();

// Promisify Redis commands
const hgetAsync = promisify(redisClient.hget).bind(redisClient);
const hsetAsync = promisify(redisClient.hset).bind(redisClient);

// Initialize available seats and reservation status
const INITIAL_AVAILABLE_SEATS = 50;
let reservationEnabled = true;

// Initialize available seats in Redis
async function initializeAvailableSeats() {
  await hsetAsync('available_seats', 'count', INITIAL_AVAILABLE_SEATS);
}

// Call this function when starting the application.
initializeAvailableSeats();

async function reserveSeat(number) {
  await hsetAsync('available_seats', 'count', number);
}

async function getCurrentAvailableSeats() {
  const currentSeats = await hgetAsync('available_seats', 'count');
  return parseInt(currentSeats) || 0;
}

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});


app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }

  // Create and queue a job in the reserve_seat queue
  const job = queue.create('reserve_seat').save(async (err) => {
    if (err) {
      console.error(`Error creating reservation job: ${err}`);
      return res.json({ status: 'Reservation failed' });
    }

    console.log(`Seat reservation job ${job.id} created`);
    res.json({ status: 'Reservation in process' });
  });
});

// Event listeners to the reserve_seat job
queue.on('job complete', (id) => {
  console.log(`Seat reservation job ${id} completed`);
});

queue.on('job failed', (id, err) => {
  console.error(`Seat reservation job ${id} failed: ${err}`);
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  // Process the queue reserve_seat (async)
  queue.process('reserve_seat', async (job, done) => {
    const availableSeats = await getCurrentAvailableSeats();
    if (availableSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      const newStock = availableSeats - 1;
      await reserveSeat(newStock);
      if (newStock === 0) {
        reservationEnabled = false;
      }
      done();
    }
  });
});
