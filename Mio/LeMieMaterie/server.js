const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
const PORT = 3000;
const DATA_FILE = path.join(__dirname, 'data.json');

app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Carica dati
function loadData() {
  try {
    return JSON.parse(fs.readFileSync(DATA_FILE));
  } catch {
    return { materie: [] };
  }
}

// Salva dati
function saveData(data) {
  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
}

// API per leggere dati
app.get('/api/data', (req, res) => {
  res.json(loadData());
});

// API per salvare dati
app.post('/api/data', (req, res) => {
  saveData(req.body);
  res.json({ status: 'ok' });
});

// Avvio server
app.listen(PORT, () => {
  console.log(`Server in ascolto su http://localhost:${PORT}`);
});
