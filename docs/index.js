var articalSectionId = "root";
var firebaseConfig = {
    apiKey: "AIzaSyAQUijW2WS2RuC6mIagywLjRHaAg750GHs",
    authDomain: "all-bike-specification.firebaseapp.com",
    databaseURL: "https://all-bike-specification-default-rtdb.firebaseio.com",
    projectId: "all-bike-specification",
    storageBucket: "all-bike-specification.appspot.com",
    messagingSenderId: "239553656833",
    appId: "1:239553656833:web:fa0d06a30434c0aa516800"
};

var tabelStart=`<table>
            <thead>
                <tr>
                    <th colspan="2"><strong>Table_Name</strong></th>
                </tr>
            </thead>
            <tbody>
                
                <tr>`;
var tableBody=`<tr>
                    <td><b>Key_Name</b></td>
                    <td>Value_Name</td>
                </tr>`;


firebase.initializeApp(firebaseConfig);
// Add custom description for the post
function putMetaDescri(bikeName){
    let descri=bikeName+" Price,colors,millage,Engine,transmission,Chassis,suspension,brakes,wheels,Physical measures and capacities details are available"
    var meta = document.createElement('meta');
    meta.name = "description";
    meta.content = descri;
    document.getElementsByTagName('head')[0].appendChild(meta);
}
// intalize tables that contain all data about the bike

function initTables(tableData) {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "tables";
    newSection.id = "tables";
    var tag = tableData;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

// load datas form firebase give input as catogory with bike name ex:"Acabion/Acabion Da Vinci 650-VI" output tableName and data
function loadDataFromFirebase(bikeName) {
    // var i = document.title.split(" Telegram")[0];
    var allTable=``;
    var i=bikeName;
    // document.getElementById("tableHead").innerText = i;
    database = firebase.database();
    var ref = database.ref(i);

    ref.once("value", function(tableValue) {
        // console.log(tableValue.val());
        var dataRow = tableValue.val();
        var tableRow = Object.keys(dataRow);

        // console.log(tableRow[0])
        // console.log(dataRow[tableRow[0]]);
        for (var t = 0; t < tableRow.length; t++) {
            var bikeTableName = dataRow[tableRow[t]];
            // console.log(tableRow[t]);
            if(allTable!=``){
                // alert(tableRow[t]);
                
                allTable+=`</table>`;
            }
            allTable+=tabelStart.replaceAll('Table_Name', tableRow[t]);
            
            for (let key in bikeTableName) {
                // console.log(key, bikeTableName[key]);
                allTable+=tableBody.replace("Key_Name",key).replace("Value_Name",bikeTableName[key]);
                // allTable+=tableBody.replace("Value_Name",bikeTableName[key]);
                // console.log(allTable);
}
        }
        initTables(allTable);
        return allTable;
    });
    
}

// inilaize pre post section
function initPreArtical(bikeName) {
    let data='<p>If you searching for the bike '+bikeName+` then is the correct place to find all details about `+bikeName+`. you can find price, colors, mileage, Engine, transmission, Chassis, suspension, brakes, wheels, Physical measures, capacities, and many other things. Now we will move on to the specific features.</p>`
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "preArtical";
    newSection.id = "preArtical";
    var tag = data;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

// inilaize post post section
function initPostArtical() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "postArtical";
    newSection.id = "postArtical";
    var tag = ``;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

bikeName=document.title;
initPreArtical(bikeName);
category=bikeName.split(" ")[0];
tablePath=category+"/"+bikeName ;  // firebase table path for speific bike
var tableDatas=loadDataFromFirebase(tablePath);
putMetaDescri(bikeName)
// initPreArtical();

// initPostArtical();