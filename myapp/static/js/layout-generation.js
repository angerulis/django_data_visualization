// Load the Visualization API and the corechart package.
//google.charts.load('current', {'packages':['corechart', 'controls', 'table']});

function createBlocs(rowNbr = 3){
    var blocList = [];
    for(i = 0; i < rowNbr; i++){
        var bloc = document.createElement('div');
        bloc.className = 'row ' + 'bloc_' + i ;
        bloc.id = 'bloc' + i;
        blocList.push(bloc);
    }
    return blocList;
}

function createCard(type, id, size = 4, add_className = '') {
    var el0 = document.createElement('div');
    var el2 = document.createElement('div');
    var el3 = document.createElement('div');
    var el4 = document.createElement('div');
    el0.className = 'col-lg-' + size + ' ' + add_className;
    el2.className = "card mb-4";
    el3.className = "card-header chart-title text-center";
    el4.className = "card-body " + type;
    el4.id = '' + id;

    if(type === 'number'){
        el0.className = 'col-sm-' + size + ' ' + add_className;
        el2.className = "card mb-4 number-card";
        el3.className = 'card-header countupLabel text-center';
        el4.className+= ' countup text-center h2 fw-light';
    }
    el2.append(el3);
    el2.append(el4);
    el0.appendChild(el2);
    return el0;
}

function createCards(cardNbr = 2, cardTypes = ['other','other']) {
    var cardList = [];
    for (i = 0; i < cardNbr; i++) {
        var card = createCard(cardTypes[i],(i+1), (12/cardNbr))
        cardList.push(card);
    }
    return cardList;
}

function createLayout(layout, hasHeader = false){

     var chartList = {};
    var main = document.createElement("main");

    var container = document.createElement('div');
    container.className = 'container-fluid px-4';
    container.id = 'dashboard_div';

    var blocNbr =  Object.keys(layout).length;
    let i = 1;
    for(const value1 of Object.values(layout) ){
        let j = 1;
        var cardNbr = Object.keys(value1).length;
        var bloc = createBloc(i);
        for(const value2 of Object.values(value1) ){
            bloc.append(createCard(value2.toString(), i + "_" + j, 12/cardNbr, '').cloneNode(true))
            chartList[i + "_" + j] = value2.toString();
            j++;
        }
        container.append(bloc);
        i++;
    }
    main.append(container);

 /*   if(hasHeader)
        createHeader('Tableau de bord', 3);*/
    document.body.querySelector('#layoutSidenav_content').insertBefore(main.cloneNode(true), document.body.querySelector('footer'));
    return chartList;
}

function createBloc(Id){
    var bloc = document.createElement('div');
    bloc.className = 'row ' + 'bloc_' + Id ;
    bloc.id = 'bloc' + Id;
    return bloc;
}

function createSidebar(){
    var wrapper = document.createElement('div');
    wrapper.id  = 'sidebarMenu';
    wrapper.className = 'wrapper';
    var nav = document.createElement('nav');
    nav.id = 'sidebar';
    nav.className = "col-md-3 col-lg-2 d-md-block bg-light sidebar collapse";
    var header = document.createElement('div')
    header.className = 'sidebar-header';
    header.innerHTML = '<h3>Bootstrap Sidebar</h3>'
    var list = document.createElement('ul');
    list.className = "list-unstyled components";
    var dHead = document.createElement('p');
    dHead.innerText = 'Dummy Heading';
    var active = document.createElement('li');
    active.className = 'active';
    var dropdown = document.createElement('a');
    dropdown.className = 'dropdown-toggle';
    dropdown.href = '#homeSubmenu';
    dropdown.setAttribute('data-toggle',"collapse");
    dropdown.setAttribute('aria-expanded', "false");
    dropdown.innerText = 'Home';
    var homeSubmenu = document.createElement('ul');
    homeSubmenu.className = 'collapse list-unstyled';
    homeSubmenu.id = 'homeSubmenu';
    var sub = document.createElement('li');
    sub.innerHTML = '<a href="#">Home 1</a>';
    homeSubmenu.append(sub);
    active.append(dropdown);
    active.append(homeSubmenu)
    list.append(dHead);
    list.append(active);
    nav.append(header);
    nav.append(list);
    wrapper.append(nav);
    var mainNode = document.body.querySelector('main');
    //mainNode.className = 'col-md-9 ms-sm-auto col-lg-10 px-md-4';
    document.querySelector("body").insertBefore(wrapper, mainNode);
}

function addHeader(){

    var nav = document.createElement('nav');
    nav.className = "sb-topnav navbar navbar-expand navbar-dark bg-dark";

    var title = document.createElement('a');
    title.className = 'navbar-brand ps-3';
    title.href = 'index.html';
    title.innerText = 'Start bootstrap';

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.id = 'sidebarToggle';
    btn.className = 'btn btn-link btn-sm order-1 order-lg-0 me-4 me-lg-0';
    btn.innerHTML = '<svg class="svg-inline--fa fa-bars" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="bars" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M0 96C0 78.33 14.33 64 32 64H416C433.7 64 448 78.33 448 96C448 113.7 433.7 128 416 128H32C14.33 128 0 113.7 0 96zM0 256C0 238.3 14.33 224 32 224H416C433.7 224 448 238.3 448 256C448 273.7 433.7 288 416 288H32C14.33 288 0 273.7 0 256zM416 448H32C14.33 448 0 433.7 0 416C0 398.3 14.33 384 32 384H416C433.7 384 448 398.3 448 416C448 433.7 433.7 448 416 448z"></path>\n' +
        '</svg>';

    var list =  document.createElement('ul');
    list.className = "navbar-nav ms-auto ms-md-0 me-3 me-lg-4";
    var dropdown =  document.createElement('li');
    dropdown.className = "nav-item dropdown";

    var link = document.createElement('a');
    link.className = 'nav-link dropdown-toggle';
    link.id = 'navbarDropdown';
    link.href = '#';
    link.setAttribute('role', 'button');
    link.setAttribute("data-bs-toggle","dropdown");
    link.setAttribute('aria-expanded', "false");
    link.innerHTML = '<svg class="svg-inline--fa fa-user fa-fw" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" data-fa-i2svg=""><path fill="currentColor" d="M224 256c70.7 0 128-57.31 128-128s-57.3-128-128-128C153.3 0 96 57.31 96 128S153.3 256 224 256zM274.7 304H173.3C77.61 304 0 381.6 0 477.3c0 19.14 15.52 34.67 34.66 34.67h378.7C432.5 512 448 496.5 448 477.3C448 381.6 370.4 304 274.7 304z"></path>\n' +
        '                        </svg>';
    var dropdown2 = document.createElement("ul");
    dropdown2.className = "dropdown-menu dropdown-menu-end";
    dropdown.setAttribute('aria-labelledby',"navbarDropdown")

    var list2 = document.createElement('li');
    var link2 = document.createElement('a');
    link2.className = 'dropdown-item';
    link2.innerText = 'setting';
    link2.href = '#!';
    list2.append(link2);

    var list3 = document.createElement('li');
    var link3 = document.createElement('a');
    link3.className = 'dropdown-item';
    link3.innerText = 'setting';
    link3.href = '#!';
    list3.append(link3);

    dropdown2.append(list2);
    dropdown2.append(list3);
    dropdown.append(link);
    dropdown.append(dropdown2);
    list.append(dropdown);
    nav.append(title);
    nav.append(btn);
    nav.append(list);
    document.body.insertBefore(nav, document.body.querySelector('main'))
}

function createHeader(title, filterNbr){
    var el0 = document.createElement('div');
    var el1 = document.createElement('div');
    var el2 = document.createElement('div');
    var el3 = document.createElement('div');
    var el4 = document.createElement('div');

    el0.id = "";
    el0.className = "content";
    el1.className = 'container text-left';
    el2.className = 'row justify-content-center';
    el3.className = "col-md-3";
    el3.id = 'row_filter';
    el4.className = "data-picked font-weight-light";
    el2.append(el4);
    var filterTitle = document.createElement('h2');

    for (let i = 0; i < filterNbr; i++) {
        filterTitle.innerText = "Filter " + i;
        el0.append(filterTitle);
        el3.id = 'row_filter' + 1;
        el0.appendChild(el1).appendChild(el2).appendChild(el3);
        document.body.append(el0.cloneNode(true));
    }
}

function createChart(chartType, containerId, title = 'Sans titre', hAxisTitle = 'hTitre', vAxisTitle = 'vTitre'){
    var option = {
        title: title,
        isStacked: false,
        hAxis: {
            title: hAxisTitle,
            format: '',
        },
        vAxis: {
            title: vAxisTitle
        }
    }
    var chart = new google.visualization.ChartWrapper({
        "containerId" : containerId,
        "chartType" : chartType,
        "options" :  option
    });
    return chart;
}

function drawChart(chartdict = {0:0}){
    try{
        var tempdata = new google.visualization.arrayToDataTable(mydata);
        var view = new google.visualization.DataView(tempdata);
        // Create a dashboard.
        var dashboard = new google.visualization.Dashboard(
        document.getElementById('dashboard_div'));

        // Create a range slider, passing some options

        var yearRangeSlider = new google.visualization.ControlWrapper({
            'controlType': 'CategoryFilter',
            'containerId': 'filter_div',
            'options': {
                'filterColumnLabel': columns_labels[0],
                'ui': {
                    'labelStacking': 'vertical',
                    'allowTyping': true,
                    'allowMultiple': true,
                    'allowNone': true
                }
            }
        });

        //generate chart
        var chart = [];
        for(const key of Object.keys(chartdict) ){
            if(!(chartdict[key] === 'number' || chartdict[key] === 'other')){
                chart.push(createChart(chartdict[key], key.toString(), "Chiffre de l'Education National",'Année', 'nombre'));
                console.log(chartdict[key] +' ' + key.toString());
            }
        }
        dashboard.bind(yearRangeSlider, chart);

        //select all checkboxes then insert the checked ones values in viewColumn series
        var viewColumn = view.getViewColumns();
        var boxValues = [0];

        //Select all checkboxes by classname
        boxValues = boxValues.concat(getFilterValues('.yearbox'));

        //Get all inputs value then only display them in the dataview
        var viewRow = view.getViewRows();
        var optionValues = []; //get checkbox values
        var optionValues_label = ''; //get checkbox values Label

        //Select all checked value in rubriquebox (values and labels)
        optionValues = getFilterValues('.rubriquebox');
        optionValues_label = getFilterValues('.rubriquebox', true);
        //Display selected rubriques
        document.querySelector('.data-picked').innerHTML =  optionValues_label;

        if (boxValues.length > 1){
            viewColumn = boxValues; //Update column to show
        }
        if(optionValues.length > 0){
            viewRow = optionValues; //Update rows to show
        }
        setAnimatedNumber(viewRow, view); //display number by selected filter

        //set new selected columns and row in the dataView to be shown
        view.setColumns(viewColumn);
        view.setRows(viewRow);

        // Draw the dashboard.
        dashboard.draw(view);
        }catch (e) {console.log(e.message)
    }
}