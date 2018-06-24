
var incr = function(i){

    $("#id_rank").val( parseInt($('#id_rank').val()) + i );
}

var switchAcount = function(id){

    $('#id_tab').val(id);
}

var filter_merge = function(filtre){

    var domtr = document.getElementById('tabletbody');
    var elttr = domtr.childNodes;

    elttr.forEach( function(currentValue, currentIndex, listObj){
        currentValue.hidden = (String(currentValue.id).includes(filtre))? false : true;
    });
}

var filter_by_map = function(){

    var filtre = $('#filter_maps_div>#id_map').val() + ':';

    filter_merge(filtre);
}

var filter_by_hero = function(){

    var filtre = $('#filter_heros_div>#id_heros').val();
    filtre = $('#filter_heros_div>#id_heros option[value=#{0}]'.replace('#{0}', filtre))[0].innerText;
    filter_merge(filtre);
}

var reset_by_hero = function(){

    filter_merge('');
}

var reset_by_map = function(){

    filter_merge('');
}