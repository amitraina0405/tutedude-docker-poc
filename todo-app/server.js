const express = require('express');
const path = require('path');
const app = express();
const port = 3000;
// Serve static files
app.use(express.static(path.join(__dirname, 'public')));
// Home page route
app.get('/', (req, res) => {
   res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
// Start server
app.listen(port, () => {
   console.log(`Front-end server running at http://localhost:${port}`);
});
