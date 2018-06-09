
var incr = function(i){

    $("#id_rank").val( parseInt($('#id_rank').val()) + i );
}

var switchAcount = function(id){

    $('#id_tab').val(id);
}

var filter_by_map = function(){

    var filtre = $('#filter_maps_div>#id_map').val() + ':';
    var domtr = document.getElementById('tabletbody');
    var elttr = domtr.childNodes;

    elttr.forEach( function(currentValue, currentIndex, listObj){
        currentValue.hidden = (String(currentValue.id).includes(filtre))? false : true;
    });

}

var filter_by_hero = function(){

    var filtre = $('#filter_heros_div>#id_heros').val();
    var domtr = document.getElementById('tabletbody');
    var elttr = domtr.childNodes;

    filtre = $('#filter_heros_div>#id_heros option[value=#{0}]'.replace('#{0}', filtre))[0].innerText;

    elttr.forEach( function(currentValue, currentIndex, listObj){
        currentValue.hidden = (String(currentValue.id).includes(filtre))? false : true;
    });

}