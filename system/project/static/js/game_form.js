$(window).on('load', ()=>{
    $('#id_game_date')
        .attr('autocomplete', 'off')
        .datepicker({
            dateFormat: "dd/mm/yy",
            buttonText: "Choose"
        });
});

