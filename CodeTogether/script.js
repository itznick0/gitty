// Aggiungi funzionalità future qui
// Per ora, solo un esempio di toggle per le lezioni bloccate

document.addEventListener('DOMContentLoaded', function() {
  const lockedCards = document.querySelectorAll('.lesson-card.locked');
  
  lockedCards.forEach(card => {
    card.addEventListener('click', function(e) {
      if (e.target.closest('.btn-action')) return;
      alert("Questa lezione è bloccata. Abbonati per sbloccarla!");
    });
  });
});