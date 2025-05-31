function errorPopup(message) {
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: message,
        iconColor: '#6a6926',
        confirmButtonColor: '#6a6926'
    });
}