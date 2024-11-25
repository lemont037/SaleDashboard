
function changeType(id) {
    document.getElementById(id).type = "datetime-local";
    return
}

let saleChannels = [];

    // Função para formatar as datas no formato correto
    function formatDate(dateString) {
        if (!dateString) {
            return "";
        }
        // Converte a string ISO para um objeto Date
        const date = new Date(dateString);
        // Extrai as partes da data e hora
        const day = String(date.getDate()).padStart(2, '0');       // Dia com zero à esquerda
        const month = String(date.getMonth() + 1).padStart(2, '0'); // Mês com zero à esquerda (0-11)
        const year = date.getFullYear();                           // Ano completo
        const hours = String(date.getHours()).padStart(2, '0');    // Horas com zero à esquerda
        const minutes = String(date.getMinutes()).padStart(2, '0');// Minutos com zero à esquerda

        return `${day}/${month}/${year} ${hours}:${minutes}:00`;
    }

    // Função para buscar os dados da API
    async function fetchSalesData() {
        const periodFrom = formatDate(document.getElementById('periodFrom').value);
        const periodTo = formatDate(document.getElementById('periodTo').value);
        const state = document.getElementById('stateFilter').value;
        const saleChannel = document.getElementById('saleChannelFilter').value;

        // Construir a URL com filtros
        let url = `http://localhost:8000/api/sales/?period_from=${periodFrom}&period_to=${periodTo}&state=${state}&sale_channel=${saleChannel}`;
        
        try {
            const response = await fetch(url);
            const sales = await response.json();

            if (sales.error && sales.details) {
                showError(sales.details);
                return
            }

            let totalPrice = 0;
            let totalProfit = 0;
            let totalSales = sales.length;

            sales.forEach(sale => {
                totalPrice += parseFloat(sale.price);
                totalProfit += parseFloat(sale.price) - parseFloat(sale.cost);
            });

            document.getElementById('totalPrice').textContent = `R$ ${totalPrice.toFixed(2)}`;
            document.getElementById('totalProfit').textContent = `R$ ${totalProfit.toFixed(2)}`;
            document.getElementById('totalSales').textContent = totalSales;

            const stateSalesCount = {};

            sales.forEach(sale => {
                const state = sale.state;
                if (stateSalesCount[state]) {
                    stateSalesCount[state] += 1;
                } else {
                    stateSalesCount[state] = 1;
                }
            });

            const sortedStates = Object.entries(stateSalesCount)
                .sort((a, b) => b[1] - a[1])
                .slice(0, 3);

            const labels = sortedStates.map(item => item[0]);
            const salesData = sortedStates.map(item => item[1]);

            renderPodiumChart(labels, salesData);

        } catch (error) {
            console.error('Erro ao buscar dados das vendas:', error);
        }
    }

    let chartInstance = null; // Declare a variable to store the chart instance

function renderPodiumChart(labels, data) {
    const ctx = document.getElementById('salesByStateChart').getContext('2d');

    // Check if a chart already exists, and if so, destroy it
    if (chartInstance) {
        chartInstance.destroy();
    }

    // Create a new chart instance
    chartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Quantidade de Vendas',
                data: data,
                backgroundColor: ['gold', 'silver', '#cd7f32'],
                borderWidth: 0,
                borderRadius: 20,
                barThickness: 100,
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Estados',
                        color: '#333',
                        font: {
                            weight: 'bold',
                        }
                    },
                    ticks: {
                        display: true,
                        color: '#333',
                        font: {
                            weight: 'bold',
                        }
                    },
                },
                y: {
                    display: false,
                    ticks: {
                        display: false,
                    },
                    grid: {
                        display: false,
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    enabled: false
                },
                datalabels: {
                    display: true,
                    color: '#fff',
                    font: {
                        weight: 'bold',
                        size: 18
                    },
                    formatter: (value) => {
                        return `${value}`;
                    }
                }
            },
            layout: {
                padding: 0
            }
        },
        plugins: [ChartDataLabels]
    });
}

    // Função para preencher os canais de venda
    async function fetchSaleChannels() {
        try {
            const response = await fetch('http://localhost:8000/api/sales/');
            const sales = await response.json();
            const channels = new Set();
            
            sales.forEach(sale => {
                channels.add(sale.sale_channel);
            });

            saleChannels = Array.from(channels).map(channel => channel.charAt(0).toUpperCase() + channel.slice(1));
            const saleChannelFilter = document.getElementById('saleChannelFilter');
            saleChannels.forEach(channel => {
                const option = document.createElement('option');
                option.value = channel;
                option.textContent = channel;
                saleChannelFilter.appendChild(option);
            });
        } catch (error) {
            console.error('Erro ao buscar canais de vendas:', error);
        }
    }

    function showError(message) {
        const popup = document.getElementById('errorPopup');
        const messageElement = document.getElementById('errorMessage');
    
        // Define a mensagem de erro
        messageElement.textContent = message;
    
        // Exibe o popup
        popup.classList.remove('hidden');
    
        // Remove o popup após 3 segundos
        setTimeout(() => {
            popup.classList.add('hidden');
        }, 10000);
    }

    // Inicializando
    fetchSaleChannels();
    fetchSalesData();