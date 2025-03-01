document.addEventListener("DOMContentLoaded", function() {
    const deleteLinks = document.querySelectorAll("a.delete");

    deleteLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            const confirmation = confirm("Are you sure you want to delete this student?");
            if (!confirmation) {
                event.preventDefault();
            }
        });
    });
}); 