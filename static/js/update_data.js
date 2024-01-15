document.addEventListener('DOMContentLoaded', function() {
    setInterval(updateData, 5000);
});

function updateData() {
    // Reload the page to fetch new data
    location.reload();
}

function updateCryptoData(cryptoData) {
    const cryptoList = document.getElementById('cryptoList');
    cryptoList.innerHTML = '';

    for (const [symbol, price] of Object.entries(cryptoData)) {
        const listItem = document.createElement('li');
        listItem.textContent = `${symbol}: $${price}`;
        cryptoList.appendChild(listItem);
    }
}

function updateEtfData(etfData) {
    const etfList = document.getElementById('etfList');
    etfList.innerHTML = '';

    for (const [symbol, value] of Object.entries(etfData)) {
        const listItem = document.createElement('li');
        listItem.textContent = `${symbol}: $${value}`;
        etfList.appendChild(listItem);
    }
}