(function(){
    console.log("JS CARGADO!!")
    const btnEliminar = document.querySelectorAll(".btnEliminar");
    btnEliminar.forEach(btn =>{
        btn.addEventListener('click',(e) =>{
            const confirmation = confirm('Esta seguro de eliminar el Cliente?');
            if (!confirmation){
                e.preventDefault();
            }
        });
    });
})();