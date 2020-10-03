// Defining configurations for columns of datatable
let dataTableColumns = [
  {
    // "Jogo" column
    "orderable": false,
    "className": 'number-filter'
  },
  {
    // "Pontos" column
    "orderable": false,
    "className": 'number-filter'
  },
  {
    // "Data do jogo" column
    "orderable": false,
    "className": 'search-filter'
  },
  {
    // "Max da temporada" column
    "orderable": false,
    "className": 'number-filter'
  },
  {
    // "Min da temporada" column
    "orderable": false,
    "className": 'number-filter'
  },
  {
    // "... recorde min" column
    "orderable": false,
    "className": 'bool-filter'
  },
  {
    // "... recorde max" column
    "orderable": false,
    "className": 'bool-filter'
  },
  {
    // "Ações" columns
    "orderable": false,
  },
];


function selectBoolFilter(text) {
  return '<select class="form-control">\
    <option value="all">Todos</option>\
    <option value="on">Sim</option>\
    <option value="off">Não</option>\
  </select>';
}

// Initializing datatable
$(document).ready(function() {
  // Setup - add a text input to each footer cell
  

  var table = $('#dataTable').DataTable( {
      fixedHeader: true,
      columns: dataTableColumns,
      orderable: false,
      order: [],
      language: {
        "zeroRecords": "Nenhum registro encontrado!"
      },
      initComplete: () => {
        
        $('#dataTable thead tr').clone(true).appendTo( '#dataTable thead' );
        $('#dataTable thead tr:eq(1) th').each( function (i) {
          var title = $(this).text();

          $(this).html('');

          if ($(this).hasClass('search-filter')) {
            $(this).html( '<input type="text" class="form-control" placeholder="Filtrar '+title.toLowerCase()+'" />' );
            $( 'input', this ).on( 'keyup change', function () {
              if ( table.column(i).search() !== this.value ) {
                table
                .column(i)
                .search( this.value )
                .draw();
              }
            } );
          }
          
          if ($(this).hasClass('number-filter')) {
            $(this).html( '<input type="number" min="0" class="form-control" placeholder="'+title+'" />' );
            $( 'input', this ).on( 'keyup change', function () {
              if ( table.column(i).search() !== this.value ) {
                table.column(i).search( this.value ).draw();
              }
            } );
          }

          if ($(this).hasClass('bool-filter')) {
            $(this).html(selectBoolFilter(title));
            $( 'select', this ).on( 'change', function () {
              if ( table.column(i).search() !== this.value ) {
                if (this.value == 'on') {
                  table.column(i).search('s').draw();
                } else if (this.value === 'off') {
                  table.column(i).search('n').draw();
                } else {
                  table.column(i).search('').draw();
                }
              }
            } );
          }
        } );
      }
  } );
});
