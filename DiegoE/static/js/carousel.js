const slides = document.querySelector('.slides');
let index = 0;
const totalImages = document.querySelectorAll('.slides img').length;
const imagesPerView = 1; // Número de imágenes visibles al mismo tiempo

function showSlide(i) {
  // Calcula el porcentaje para mover las imágenes
  slides.style.transform = `translateX(${-i * 100 / imagesPerView}%)`;
}

function nextSlide() {
  index = (index + 1) % (totalImages - imagesPerView + 1); // Limita para que no avance más allá de las imágenes disponibles
  showSlide(index);
}

// Cambia la imagen automáticamente cada 3 segundos
setInterval(nextSlide, 3000);
