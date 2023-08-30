const express = require('express');
const app = express();
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();

const hgetAsync = promisify(client.hget).bind(client);
const hsetAsync = promisify(client.hset).bind(client);

// Define the product data
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

// Middleware to parse JSON requests
app.use(express.json());

// Route to get the list of all products
app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

// Route to get details of a specific product
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = listProducts.find(item => item.itemId === itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({ ...product, currentQuantity });
  }
});

// Route to reserve a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    if (currentQuantity > 0) {
      await reserveStockById(itemId, currentQuantity - 1);
	res.json({ status: 'Reservation confirmed', itemId });
    } else {
	res.json({ status: 'Not enough stock available', itemId });
    }
  }
});

// Start the server
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Function to reserve stock by item id
async function reserveStockById(itemId, newStock) {
  await hsetAsync('item:' + itemId, 'stock', newStock);
}

// Function to get current reserved stock by item id
async function getCurrentReservedStockById(itemId) {
  const currentStock = await hgetAsync('item:' + itemId, 'stock');
	if (currentStock >= 0 && currentStock !== null) {
		return parseInt(currentStock);
	} else {
		return getItemById(itemId).initialAvailableQuantity;
	}
}

function getItemById(id) {
  return listProducts.find(item => item.itemId === id);
}
