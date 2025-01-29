document.addEventListener("DOMContentLoaded", function () {
  function launchConfetti() {
    const duration = 3 * 1000;
    const animationEnd = Date.now() + duration;
    const colors = ["#FFD700", "#C0C0C0", "#CD7F32"];

    function randomInRange(min, max) {
      return Math.random() * (max - min) + min;
    }

    (function frame() {
      const timeLeft = animationEnd - Date.now();

      if (timeLeft <= 0) {
        return;
      }

      const particleCount = 5 * (timeLeft / duration);
      confetti({
        particleCount,
        spread: 70,
        origin: { x: randomInRange(0.2, 0.8), y: 0.6 },
        colors,
      });

      requestAnimationFrame(frame);
    })();
  }

  launchConfetti();
});
