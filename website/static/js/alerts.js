function errorPopup(message) {
    return Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: message,
        iconColor: '#6a6926',
        confirmButtonColor: '#6a6926',
        scrollbarPadding: false,
        heightAuto: false,
    });
}


function successPopup(message) {
    return Swal.fire({
        icon: 'success',
        title: '¡Listo!',
        text: message,
        iconColor: '#6a6926',
        confirmButtonColor: '#6a6926',
        scrollbarPadding: false,
        heightAuto: false,
    });
}