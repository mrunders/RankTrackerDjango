
var incr = function(i){ $("#id_rank").val( parseInt($('#id_rank').val()) + i );}
var switchAcount = function(id){  $('#id_tab').val(id); }
var getTableList = function(){ return document.getElementById('tabletbody').childNodes;}

var get_selected_filter_map = function(){ return $('#filter_maps_div>#id_map').val() + ':'; }
var get_selected_filter_hero = function(){ 
    var filtre = $('#filter_heros_div>#id_heros').val();
    return $('#filter_heros_div>#id_heros option[value=#{0}]'.replace('#{0}', filtre))[0].innerText;
}

var filter_merge = function(filtre){

    getTableList().forEach( function(currentValue, currentIndex, listObj){
        currentValue.hidden = (String(currentValue.id).includes(filtre))? false : true;
    });
}

var filter_double_merge = function(filtre_hero,filtre_map){

    getTableList().forEach( function(currentValue, currentIndex, listObj){
        currentValue.hidden = (String(currentValue.id).includes(filtre_hero) && String(currentValue.id).includes(filtre_map))? false : true;
    });
}

var filter_by_map = function(){ filter_merge(get_selected_filter_map());}
var filter_by_hero = function(){ filter_merge(get_selected_filter_hero());}
var filter_by_all = function(){ filter_double_merge(get_selected_filter_hero(),get_selected_filter_map());}
var reset = function(){ filter_merge('');}