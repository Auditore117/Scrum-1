document.querySelectorAll('.parrafo').forEach(parrafo => {
    parrafo.addEventListener('click', () => {
        const url = parrafo.getAttribute('data-url');
        window.location.href = url; // Redirige a la URL especificada
    });
});
