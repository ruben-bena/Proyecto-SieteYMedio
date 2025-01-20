const cartas = [
    {nombre: '1', valor: 1},
    {nombre: '2', valor: 2},
    {nombre: '3', valor: 3},
    {nombre: '4', valor: 4},
    {nombre: '5', valor: 5},
    {nombre: '6', valor: 6},
    {nombre: '7', valor: 7},
  
    {nombre: 'Sota', valor: 0.5},
    {nombre: 'Caballo', valor: 0.5},
    {nombre: 'Rey', valor: 0.5}
  ];
  
  function calcularPuntaje(cartasJugadas) {
    let puntajeTotal = 0;
  
    for (let i = 0; i < cartasJugadas.length; i++) {
      const carta = cartasJugadas[i];
      puntajeTotal += carta.valor;
    }
  
    if (puntajeTotal > 7.5) {
      return 'Has superado los 7.5 puntos, has perdido';
    }
  
    if (puntajeTotal === 7.5) {
      return 'Felicidades, has obtenido 7.5 puntos';
    }
  
    return puntajeTotal;
  }
  
  function repartirCartas() {
  
    const cartasSeleccionadas = [];
    for (let i = 0; i < 3; i++) {
      const cartaAleatoria = cartas[Math.floor(Math.random() * cartas.length)];
      cartasSeleccionadas.push(cartaAleatoria);
    }
  
  
    let resultadoHTML = '<h3>Cartas seleccionadas:</h3><ul>';
    cartasSeleccionadas.forEach(carta => {
      resultadoHTML += `<li>${carta.nombre} (Valor: ${carta.valor})</li>`;
    });
    resultadoHTML += '</ul>';
  
    const puntaje = calcularPuntaje(cartasSeleccionadas);
    resultadoHTML += `<h3>Puntaje total: ${puntaje}</h3>`;
  
    document.getElementById('resultado').innerHTML = resultadoHTML;
  }  