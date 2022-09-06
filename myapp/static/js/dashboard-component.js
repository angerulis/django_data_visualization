/*This script contains the function to display
components and filters used in the dashbard
 */

/*
This function display the column label as well as the rows value as checkbox input
 and dropdown list by generating HTML tag for proper displaying
*/
function displayCol(colArray, rowArray = row_list, col_container = 'column_Filter',
                    row_container = 'row_filter'){
    //generate html to display filter for columns
    if(colArray !== 'undefined'){
        document.getElementById(col_container).className = "breadcrumb mb4";
        var button = document.createElement("button");
        button.type = "button";
        button.className = "btn-sm btn-primary";
        button.id = "selectAllYear";
        button.value = "0";
        button.innerText = "Désélectionner";
        button.addEventListener('click', function (){
            var bt = document.getElementById('selectAllYear');
            if(bt.value === "1"){
                document.querySelectorAll('.yearbox').forEach(function (box){
                box.checked = true;});
                bt.value = "0";
                button.innerText = "Désélectionner";
            }else{
                document.querySelectorAll('.yearbox').forEach(function (box){
                box.checked = false;});
                button.value = "1";
                button.innerText = "Tout sélectionner";
            }
            reload_dashboard();
        });

        document.getElementById(col_container).appendChild(button);
        document.getElementById(col_container).appendChild(document.createElement('br'))
        for(i = 1; i < colArray.length; i++){

            var div = document.createElement("div");
            div.className = "form-check form-check-inline";
            //div.id  = "checkbox_filter";
            var input = document.createElement("input");
            input.className = "form-check-input yearbox";
            input.id = "year" + colArray[i];
            input.type = "checkbox";
            input.value = i;
            input.checked = colArray[i].toString() ===  new Date().getFullYear().toString();
            input.addEventListener('change', function (){
                reload_dashboard();
            })
            var label = document.createElement("label");
            label.htmlFor =  "year" + colArray[i];
            label.className = "form-check-label";
            label.innerHTML = colArray[i].toString().replace("_","");
            div.innerHTML = label.outerHTML;
            document.getElementById(col_container).appendChild(div).appendChild(input);
        }

    }
    //generate html to display filter for rows from the first columns
    if(row_list !== 'undefined'){
        var select = document.createElement("select");
        select.name = "basic[]";
        select.multiple = "multiple";
        select.className = "3col active form-control";
        select.id = "rubriques_select";
        //iterate rows
        for(i = 0; i < row_list.length; i++){
            var option = document.createElement("option");
            option.value = i;
            option.innerHTML = row_list[i];
            option.className = "rubrique_box";
            option.addEventListener('change', reload_dashboard)
            select.appendChild(option);
        }
        //Insert options in select tag
        document.getElementById(row_container).appendChild(select);

    }
}
//set all animated numbers to 'Aucune donnée' as default value or error value
function set_default_counter(){
      document.querySelectorAll('.number-card').forEach(function (number){
          number.querySelector('.countupLabel').innerHTML = "Aucune donnée sélectionnée";
          number.querySelector('.countup').innerHTML = 'Aucune donnée';
      });
}
//Add download dropdown button in card headers for charts only
function add_download(class_name, list_item = [] ){
    try {
        let j = 0;
            document.querySelectorAll(class_name).forEach(function (node){
        /*if(node.className.toString().search('table') > 0){

        }*/
        var dropbtn = document.createElement('button');
        dropbtn.className = "btn btn-secondary dropdown-toggle float-end";
        dropbtn.type = 'button';
        dropbtn.setAttribute('data-bs-toggle','dropdown');
        //dropbtn.setAttribute('aria-haspopup','true');
        dropbtn.setAttribute('aria-expanded','false');
        dropbtn.id="dropdownMenuButton" + (j++);
        dropbtn.innerHTML = 'Télécharger';
        //link.href = '#';

        var list = document.createElement('div');
        list.className = "dropdown-menu";
        list.setAttribute("aria-labelledby","dropdownMenuButton");
        for (i = 0; i < list_item.length; i++){
             var a = document.createElement('a');
             a.className = "dropdown-item download-link";
             a.href="#";
             a.innerHTML = list_item[i];
             if(a.innerHTML.toString().toLowerCase().search('image') > -1){
                 a.addEventListener('click', function (){
                     var card_body = this;
                     while(card_body.getElementsByClassName('card-body').length <= 0){
                         console.log(card_body);
                         card_body = card_body.parentNode;
                     }
                     genChartLinks(card_body.querySelector('.card-body'), card_body.innerText);
             });
             }else if(a.innerHTML.toString().toLowerCase().search('excel') > -1){
                 a.className += " to-excel ";
                 a.addEventListener('click',ExportToExcel);
             }else if(a.innerHTML.toString().toLowerCase().search('csv') > -1){
                 a.className += " to-csv ";
                 a.addEventListener('click', ExportToCsv);
             }

             list.appendChild(a);
        }
        node.appendChild(dropbtn)
        node.appendChild(list);
    });
    }catch (e) {
        console.log(e.message);
    }


}
//Generate link to download and open the chart as png type image
function genChartLinks(chartDiv_node, link_title = ''){
    try {
        if(chartDiv_node.hasChildNodes()){
        html2canvas(chartDiv_node).then(canvas => {
            return canvas.toDataURL("image/png");
        }).then(image =>{
            var link = document.createElement('a');
            link.href = image.toString();
            link.download = link_title.replaceAll(' ', '_').replaceAll('Télécharger','_') + '.png';
            link.click();
            window.open(link.href, 'blank');
        });
        //console.log(result);

    }else {console.log('Error in generating link');}
    }catch (e){console.log(e.message)}
}

//Get selected values in the filter from a specific class
function getFilterValues(input_class_name = '.rubriquebox', isLabel = false){
    var optionValues = [];
    var optionValues_label = '';
    document.querySelectorAll(input_class_name).forEach(function (option_box){
        if(option_box.checked){
            if(isLabel)
                optionValues_label += '<span class="text-success">' + option_box.parentNode.textContent + " </span>|";
            else
                optionValues.push(parseInt(option_box.value));
        }
    });
    if(isLabel)
        return optionValues_label;


    return optionValues;
}

//set animated counter number
function setAnimatedNumber(viewRow = [], view = [], containerClass ='.number-card',
                           labelClass ='.countupLabel', numberClass = '.countup' ){

    var numberAnimated = []; //count number value
    var numberAnimated_label = []; //count number label

    try{
        //get animated numbers and labels from viewRow
        for(i = 0; i < viewRow.length; i++){
            if(i === document.getElementsByClassName('number-card').length)
                break;
            numberAnimated.push((view.getValue(view.getViewRowIndex(viewRow[i]), parseInt(view.getViewColumnIndex(13)))));
            numberAnimated_label.push(view.getValue(view.getViewRowIndex(viewRow[i]), 0));
        }
        //set number and label into containers
        document.querySelectorAll(containerClass).forEach(function (number, i = 0){
        if(i < viewRow.length){
            number.querySelector(labelClass).innerHTML = numberAnimated_label[i] + " " + new Date().getFullYear();
            number.querySelector(numberClass).innerHTML = numberAnimated[i];
            i++;
        }else {
            //if not value set default value
            number.querySelector(labelClass).innerHTML = 'Aucune données';
            number.querySelector(numberClass).innerHTML = 'Aucune données';
        }
    });
        runAnimations();
    }catch (e) {
        console.log(e.message)};
}

function ExportToCsv(){
    try{
              /* Callback invoked when the button is clicked */
      /* Create worksheet from HTML DOM TABLE */
      const table = document.querySelector('.Table table');
      const wb = XLSX.utils.table_to_book(table);
      /* Export to file (start a download) */
    var csv = XLSX.utils.sheet_to_csv(wb);
    XLSX.writeFile(wb, "données_CSV.csv");
    }catch (e) {
        console.log(e.message);
        alert('Impossible de télécharger le ficher CSV')
    }

}

//Export HTML table to excel
function ExportToExcel(props) {
    try{
          /* Callback invoked when the button is clicked */
      /* Create worksheet from HTML DOM TABLE */
      const table = document.querySelector('.Table table');
      const wb = XLSX.utils.table_to_book(table);
      /* Export to file (start a download) */
      XLSX.writeFile(wb, "données_tableau.xlsx");
    }catch (e) {
        console.log(e.message);
        alert("Impossible de télécharger le fichier Excel")
    }

}




