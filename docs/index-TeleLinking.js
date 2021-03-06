var articalSectionId = "root";
var currntTableName="Actors";


function initLoading() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "w3-light-grey";
    var tag = `<div id="myBar" class="w3-container w3-cyan w3-center" style="width:0%;max-height:20px ;">0%</div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}
function initHeader() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    // newSection.className = "w3-light-grey";
    var tag = `    <div class="header">
        <div class="wrap">
            <div class="logo">
                <a href="/"><img src="https://1.bp.blogspot.com/-PvuGbDGRFfA/YRldv-bKgiI/AAAAAAAAVgI/bn-buG7Kcs0QtVON-HR1VcxX-yedmCDeACNcBGAsYHQ/s0/logo.png" height="52" width="154" title="GroupsAndChannels"></a>
            </div>
            <div class="" id="box">
                <div class="box_content">
                    <div class="box_content_center">
                        <div class="form_content">
                            <div class="menu_box_list">
                                <ul>
                                    <li><a href="#"><span>Home</span></a></li>
                                    <li><a href="#" title="Add New Whatsapp Group"><span>Add Group</span></a></li>
                                    <li><a href="#"><span>Terms</span></a></li>
                                    <li><a href="#"><span>Privacy</span></a></li>
                                    <li><a href="#"><span>Disc</span></a></li>
                                    <li><a href="#"><span>Contact</span></a></li>
                                    <div class="clear"> </div>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>



            <div style="position: fixed; top: 200px; left: 0px; ">
                <a href="whatsapp://send?text=GroupSor - Enjoy Unlimited Whatsapp Group Links Invite to Join. Follow this link : https://groupsandchannels.telelinking.link/" data-action="share/whatsapp/share">
                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/whatsapp.png" width="26" height="26" alt="Share on Whatsapp" title="Share on Whatsapp" rel="nofollow"></a><br>
                <a href="https://twitter.com/intent/tweet?text=GroupSor - Enjoy Unlimited Whatsapp Group Links Invite to Join. Follow this link : &amp;url=https://groupsandchannels.telelinking.link/" target="_blank" rel="nofollow">
                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/twitter.jpg" width="26" height="26" alt="Share on Twitter" title="Share on Twitter"></a> <br>
            </div>




        </div>
    </div>
    <div class="clear"> </div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initAddGroup() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.id="initAddGroup";
    newSection.className = "w3-light-grey";
    var tag = `<div style="position: fixed;
     bottom: 10px;
     right: 10px;">
    <button class="addbtn" onclick="setupAddgroup();" title="Add New Whatsapp Group">+ Add Whatsapp Group</button>
</div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initDropDown() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    // newSection.className = "w3-light-grey";
    newSection.id="initDropDown";
    var tag = `<div style="margin-bottom: 10px;text-align: center">

            <select class="selectbtn" name="categoryList" onchange="loadGroups(this.value);" id="cMenu">
            <option value="">Select category</option>
        </select>
            <!-- <input type="submit" class="serbtn" value="Find" onclick="loadGroups();"> -->
        </div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}
function addGroups(tableName,data1){
    firebase.database().ref(tableName).push().set(data1);
}


function initAddNewGroup() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    // newSection.className = "w3-light-grey";
    newSection.id="addNewGroup";
    newSection.style.display="none";
    var tag = `<div style="margin-bottom: 10px;text-align: center">
                <form action="" method="post">
                    <select class="selectbtn" name="categoryList" id="addmenu">
                        <option value="">Select category</option>
                        <option value="value1">Value1</option>
                    </select><br>
                    <!-- <input type="text" name="groupLink" id="" value="piriyaraj" /> -->
                    <input type="url" name="groupLink" id="" placeholder="Telegram invite url" /><br>
                    <input type="submit" class="serbtn" value="Submit" onclick="addGroupsTest(this.form);">
                </form>

            </div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initGroupLinks() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "wrap";
    newSection.id = "results"
        // var tag = `<div id="results" style="display: none;">`;
        // newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initPreArtical() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "preArtical";
    newSection.id = "preArtical"
        // var tag = `<div id="results" style="display: none;">`;
        // newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initPostArtical() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "PostArtical";
    newSection.id = "PostArtical"
        // var tag = `<div id="results" style="display: none;">`;
        // newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initLoadMoreLink() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    // newSection.className = "LoadMoreLink";
    newSection.id="initLoadMoreLink";
    // newSection.id = "LoadMoreLink";
    var tag = `<div style="margin-top: 10px;"> 
                <button class="addbtn" id="LoadMoreLink" style="cursor: pointer;display:none;">Load more group</button>
            </div>`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

function initLoadingImage() {
    var mainContent = document.getElementById(articalSectionId);
    newSection = document.createElement('section'); //create a div
    newSection.className = "loadingImage";
    newSection.id = "loadingImage";
    // newSection.id = "LoadMoreLink";
    var tag = `<img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/loader.gif" alt="loading telegram group links" title="loading group links" srcset="">`;
    newSection.innerHTML = tag;
    mainContent.appendChild(newSection); //append to the doc.body
    mainContent.insertBefore(newSection, mainContent.lastChild)
}

var firebaseConfig = {
    apiKey: "AIzaSyCNPje1QfnH8Pg8oLzKYj_Guy1GaiiyWLs",
    authDomain: "telelinking-techfarm.firebaseapp.com",
    databaseURL: "https://telelinking-techfarm-default-rtdb.firebaseio.com",
    projectId: "telelinking-techfarm",
    storageBucket: "telelinking-techfarm.appspot.com",
    messagingSenderId: "344916823855",
    appId: "1:344916823855:web:aff753138b8af5bb579bda"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var groupBlock = `
<div>
                    <a style="color: #5a5a5a" target="_blank" href="groupLink" title="Telegram group invite link: groupName">
                        <span>
                            <img src="groupLogo" onerror="imgError(this);" class="image"  alt="groupName">
                        </span>
                    </a>
                    <a style="color: #5a5a5a;font-family: fantasy;" target="_blank" href="groupLink" title="Telegram group invite link: groupName">
                        <h2>groupName</h2>
                    </a>
                </div>
                <div class="block2">
                    <div class="post-basic-info"> 
                        <div style="color:#0088cc;">
                        <a style="font-weight: 600;"href="groupLink" title="Telegram Chaneel invite link: groupName" target="_blank">@grouplinkText</a>
                        </div>
                        <span style="padding-right:20px;">Category: groupType</span>
                        <span>subscribe/members: groupCount</span>
                        <p class="descri" style="margin-bottom: 0px">groupDescri</p>
                    </div>
                    <div class="post-info-rate-share"> <span class="joinbtn"><a class="joinbtn" href="groupLink" target="_blank" title="Click here to join groupName Telegram group" rel="nofollow">Join group</a></span>
                        <div class="post-share">
                            <div>

                                <a class="joinbtn" style="vertical-align:top" href="whatsapp://send?text=Follow this link to Join my Telegram group : groupLink %0A %0AFind more Telegram group at: https://groupsor.link/ " data-action="share/whatsapp/share" rel="nofollow">Share on</a>
                                <a href="whatsapp://send?text=Follow this link to Join my Telegram group : currentPostLink" data-action="share/whatsapp/share">
                                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/whatsapp.png" width="24" height="24" alt="Share on Whatsapp" title="Share on Whatsapp" rel="nofollow"></a>

                                <a href="https://twitter.com/intent/tweet?text=Follow this link to Join my Telegram group : &amp;url=currentPostLink" target="_blank" rel="nofollow">
                                    <img src="https://piriyaraj.github.io/TeleLinking/subdomain/GroupsAndChannels/img/twitter.jpg" width="24" height="24" alt="Share on Twitter" title="Share on Twitter"></a>
                            </div>
                        </div>
                    </div>
                </div>
`;

function imgError(image) {
    image.onerror = "";
    image.src = "https://w7.pngwing.com/pngs/419/837/png-transparent-telegram-icon-telegram-logo-computer-icons-telegram-blue-angle-triangle-thumbnail.png";
    return true;
}

function insertBlock(groupName, groupLink, groupLogo, groupCount, groupType, groupDescri) {
    var resultDiv = document.getElementById("results");
    newDiv = document.createElement('div'); //create a div
    newDiv.className = "maindiv";
    var tag = groupBlock;
    tag = tag.replaceAll('groupName', groupName);
    tag = tag.replaceAll('groupLogo', groupLogo);
    tag = tag.replaceAll('groupLink', groupLink);
    tag = tag.replaceAll('groupCount', groupCount);
    tag = tag.replaceAll('groupType', groupType);
    tag = tag.replaceAll('grouplinkText', groupLink.split("/").pop());
    tag = tag.replaceAll('groupDescri', groupDescri);
    tag = tag.replaceAll('currentPostLink', document.location.href);


    newDiv.innerHTML = tag; //add an id
    resultDiv.appendChild(newDiv); //append to the doc.body
    resultDiv.insertBefore(newDiv, resultDiv.lastChild)
}

function loadMorelink(lastcount) {
    //     alert(tableName,loadButtonid);
    tableName = currntTableName;

    firebase.database().ref(tableName).once("value", function(tableValue) {
        var dataRow = tableValue.val();
        var tableRow = Object.keys(dataRow);
        // console.log(tableValue);
        // alert(tableRow.length);
        for (var t = lastcount; t < tableRow.length; t++) {

            if (t == lastcount + 8) {
                var loadMoreButton = document.getElementById("LoadMoreLink");
                tag = "loadMorelink('" + t + "')";
                loadMoreButton.setAttribute('onclick', tag);

                // addLoadMoreButton(tableName+"buttonid",t+"sectionId");
                break;
            }
            var k = tableRow[t];
            var groupName = dataRow[k].groupName;
            var groupLink = "https://t.me/" + dataRow[k].groupLink;
            var groupLogo = dataRow[k].groupLogo;
            var groupCount = dataRow[k].groupCount;
            var groupType = dataRow[k].groupType;
            var groupDescri = dataRow[k].groupDescri;
            // insertRow(groupName, groupLink);
            insertBlock(groupName, groupLink, groupLogo, groupCount, groupType, groupDescri)
                // console.log(name, url);
            if (t == tableRow.length - 1) {
                // alert(t+" last link");
                var loadMoreButton = document.getElementById("LoadMoreLink");
                loadMoreButton.style.display = "none";
                break;
            }
        }
        // console.log(tableRow);
    });
}

function loadLinks(tableName) {
    // var i = document.title.split(" Telegram")[0];
    var i=tableName;
    // document.getElementById("tableHead").innerText = i;
    database = firebase.database();
    var ref = database.ref(i);
    ref.once("value", function(tableValue) {
        // console.log(tableValue.val());
        var dataRow = tableValue.val();
        var tableRow = Object.keys(dataRow);
        // console.log(tableRow);
        // console.log(tableValue);
        for (var t = 0; t < tableRow.length; t++) {
            if (t == 8) {
                // alert("hello");
                document.getElementById("LoadMoreLink").style.display = "initial";
                var loadMoreButton = document.getElementById("LoadMoreLink");
                tag = "loadMorelink('" + t + "')";
                loadMoreButton.setAttribute('onclick', tag);
                break;
            }
            var k = tableRow[t];
            // var url = "https://bikespeci.blogspot.com/p/gateway.html?telelink=" + dataRow[k].groupLink;
            //                 var url = "https://chat.whatsapp.com/" + dataRow[k].groupLink;
            var groupName = dataRow[k].groupName;
            var groupLink = "https://t.me/" + dataRow[k].groupLink;
            var groupLogo = dataRow[k].groupLogo;
            var groupCount = dataRow[k].groupCount;
            var groupType = dataRow[k].groupType;
            var groupDescri = dataRow[k].groupDescri;
            // insertRow(groupName, groupLink);
            insertBlock(groupName, groupLink, groupLogo, groupCount, groupType, groupDescri)
                // console.log(name, url);
        }
        // console.log(tableRow);
        document.getElementById("loadingImage").style.display="none";
    });

}


function insertDropDow(CategoryName,menuid){
    var mainContent = document.getElementById(menuid);
    newOption = document.createElement('option'); //create a div
    newOption.innerHTML=CategoryName;
    newOption.setAttribute("value",CategoryName);
    // newOption.id = "results"
    // var tag = `<option value="7">Example</option>`;
    // newSection.innerHTML = tag;
    mainContent.appendChild(newOption); //append to the doc.body
    mainContent.insertBefore(newOption, mainContent.lastChild)
}
function dropDownmaker(menuid) {
    var tableNameArray=[
    "13 reasons why",
    "4k movies",
    "Abuja",
    "Active",
    "Actors",
    "Actress",
    "Adult",
    "Africa",
    "Agriculture",
    "Aiims pg",
    "Alerts",
    "Alt balaji",
    "Amazon offers",
    "Amazon prime videos",
    "American",
    "Among us",
    "Android",
    "Animation movies",
    "Anime",
    "Anthropology",
    "Apex legends",
    "Apk",
    "Arab",
    "Artificial intelligence",
    "Artists",
    "Arts",
    "Asian",
    "Asus",
    "Australia",
    "Austria",
    "Automobile",
    "Aws",
    "Ayurveda",
    "Bachelor",
    "Bahrain",
    "Bangalore",
    "Bangkok",
    "Bangladesh",
    "Bank nifty",
    "Banking",
    "Basketball",
    "Belgium",
    "Bengali",
    "Best",
    "Bhojpuri movies",
    "Big",
    "Bihar",
    "Bikes",
    "Binance",
    "Biology",
    "Bitcoin",
    "Bollywood actors",
    "Books",
    "Bot",
    "Boys",
    "Breaking bad",
    "Bts fans",
    "Business",
    "Ca",
    "Call of duty",
    "Cambodia",
    "Canada",
    "Cars",
    "Cartoons",
    "Cat exams",
    "Celebrity",
    "Chatroom",
    "Chemistry",
    "China",
    "Chinese movies",
    "Civil engineering",
    "Clash of clans",
    "Class 10th",
    "Class 12th",
    "Clat",
    "Club factory",
    "Coin master",
    "Comedy",
    "Commerce",
    "Commodity",
    "Competitive programming",
    "Computer knowledge",
    "Computer softwares",
    "Cooking",
    "Cool",
    "Counter strike",
    "Coupons",
    "Cricket",
    "Crypto-currency",
    "Csat",
    "Css",
    "Ctet",
    "Current affairs",
    "Dark",
    "Data science",
    "Dating",
    "Deals",
    "Denmark",
    "Designers",
    "Diet plans",
    "Digital marketing",
    "Discount deals",
    "Discover",
    "Discussion",
    "Dj",
    "Doctors",
    "Drama",
    "Dream11",
    "Dubai",
    "Earn money",
    "Earning",
    "Ebooks",
    "Ece",
    "Editing",
    "Edm",
    "Education",
    "Electronics",
    "Engagement",
    "English",
    "English books",
    "English literature",
    "English movies",
    "Entertainment",
    "Epaper",
    "Europe",
    "Excel learning",
    "Famous",
    "Fan clubs",
    "Farmers",
    "Farming",
    "Fashion",
    "Finance",
    "Fitness",
    "Flash sale",
    "Food",
    "Football",
    "Foreign movies",
    "Forex",
    "Fortnite",
    "Free fire",
    "Friends",
    "Funny",
    "Furry",
    "Game of thrones",
    "Gaming",
    "Gate",
    "Germany",
    "Ghana",
    "Girls",
    "Gk",
    "Google pay",
    "Gpsc",
    "Graphic design",
    "Group d",
    "Gst",
    "Gujarati movies",
    "Haryanvi",
    "Hbo",
    "Healthy",
    "Hindi",
    "Hindi dubbed",
    "Hindi movies",
    "Hip hop",
    "History",
    "Hollywood actors",
    "Hollywood dubbed",
    "Hong kong",
    "Horror movies",
    "Hotstar",
    "Htet",
    "Html",
    "Huawei",
    "Hyderabad",
    "Ias",
    "Ibps po",
    "Ielts",
    "Ies",
    "Iit jee",
    "Indian",
    "Indian express",
    "Insights",
    "Instagram",
    "Intraday",
    "Ios",
    "Ipl",
    "Ips exams",
    "Isro",
    "It jobs",
    "Java",
    "Javascript",
    "Jee main",
    "Jobs",
    "Jokes",
    "Kannada",
    "Kashmir",
    "Kenya",
    "Kerala",
    "Kerala psc",
    "Kolkata",
    "Korean",
    "Kotlin",
    "Kuala lumpur",
    "Kuwait",
    "Law",
    "Learning",
    "Lenovo",
    "Lifestyle",
    "Linux",
    "Local",
    "Loki fans",
    "London",
    "Luxembourg",
    "Machine learning",
    "Magazines",
    "Maharashtra",
    "Malawi",
    "Malayalam movies",
    "Manchester united",
    "Manipur",
    "Marathi",
    "Marvel movies",
    "Maths",
    "Mba",
    "Mechanical engineering",
    "Media",
    "Medical",
    "Meditation",
    "Memes",
    "Miami",
    "Minecraft",
    "Mini militia",
    "Modified cars",
    "Motivational",
    "Movies",
    "Mppsc",
    "Mpsc",
    "Mrcs",
    "Mrunal",
    "Ms office",
    "Mumbai",
    "Music",
    "Mx player",
    "Nabard",
    "Nba",
    "Nda",
    "Neet",
    "Nepal",
    "Netflix",
    "Netherlands",
    "New york",
    "New zealand",
    "News",
    "Newspapers",
    "Nigeria",
    "Norway",
    "Novels",
    "Nursing",
    "Offers",
    "Old movies",
    "Oman",
    "Oneplus",
    "Online shopping",
    "Open",
    "Pakistani",
    "Paris",
    "Paytm",
    "Pc games",
    "Pdf",
    "Philippines",
    "Photoshop",
    "Php",
    "Physics",
    "Pictures",
    "Png",
    "Poetry",
    "Popular",
    "Ppsspp",
    "Premium apps",
    "Prison break",
    "Private",
    "Programmers",
    "Programming language",
    "Promo codes",
    "Psc",
    "Psc thriller",
    "Pubg",
    "Public",
    "Pune",
    "Punjabi",
    "Punjabi singers",
    "Python",
    "Quantitative aptitude",
    "Quiz",
    "Quotes",
    "Radiology",
    "Railway exams",
    "Rajasthan",
    "Rajkot",
    "Rappers",
    "Rbi grade b",
    "Real estate",
    "Real madrid",
    "Realme",
    "Recipes",
    "Reddit",
    "Ringtones",
    "Ripple",
    "Romania",
    "Rrb exams",
    "Ruby",
    "Russian",
    "Rust",
    "Samsung",
    "Sap",
    "Sarcastic",
    "Saree",
    "Satisfying videos",
    "Sbi po",
    "Scala",
    "Sci-fi movies",
    "Science",
    "ScrapData",
    "Secret",
    "Self help",
    "Seo",
    "Share market",
    "Shayari",
    "Short films",
    "Sikkim",
    "Singapore",
    "Soccer",
    "Somalia",
    "Songs",
    "Spain",
    "Spanish",
    "Splendor fans",
    "Sports",
    "Spotify",
    "Ssc",
    "Ssc cgl",
    "Status",
    "Status videos",
    "Stickers",
    "Stock market",
    "Stories",
    "Stranger things",
    "Students",
    "Study",
    "Sub4sub",
    "Sweden",
    "Swift",
    "Switzerland",
    "Tamil movie",
    "Teachers",
    "Technology",
    "Telugu actress",
    "Telugu dubbed",
    "The walking dead",
    "Tiktok",
    "Tips and tricks",
    "Tokyo",
    "Tourism",
    "Tourists",
    "Tractors",
    "Trading",
    "Travel",
    "Trending",
    "Turkey",
    "Turkish",
    "Tv shows",
    "Uae",
    "Ui ux",
    "Uk",
    "Ukraine",
    "Ullu",
    "Unacademy",
    "Unisa",
    "University students",
    "Upsc",
    "Urdu",
    "Us",
    "Usa",
    "Useful",
    "Vehicle",
    "Video songs",
    "Videos",
    "Vietnam",
    "Vikings",
    "Viral",
    "Viu",
    "Voot",
    "Wallpapers",
    "Web series",
    "Worldwide",
    "Wwe",
    "Xiaomi",
    "Yemen",
    "Youtubers",
    "Zee5",
    "Zimbabwe"
];

    // database = firebase.database();
    // var ref = database.ref();
    // ref.once("value", function(tableValue) {
    //     // console.log(tableValue.val());
    //     var dataRow = tableValue.val();
    //     // console.log(dataRow);
    //     var tableRow = Object.keys(dataRow);
    //     // console.log(tableRow);
    //     // console.log(tableValue);
    //     for (var t = 0; t < tableRow.length; t++) {
    //         var k = tableRow[t];
    //         insertDropDow(k);
    //         tableNameArray.push(k);
    //         // console.log(k);
    //     }
    //     console.log(tableNameArray);
    //     document.getElementById("loadingImage").style.display="none";

    // });
    for(var t = 0; t < tableNameArray.length; t++) {
        var k = tableNameArray[t];
        insertDropDow(k,menuid);
        // console.log(k);
    }

}

function deletechild(){
    // Get the <ul> element with id="myList"
    var list = document.getElementById("results");

    // As long as <ul> has a child node, remove it
    while (list.hasChildNodes()) {  
    list.removeChild(list.firstChild);
}

}
function loadGroups(tableName){
    if(tableName!=""){
        document.getElementById("loadingImage").style.display="block";
        currntTableName=tableName;
        deletechild();
        loadLinks(tableName);

    }
}

function setupAddgroup(){
    initAddNewGroup();
    dropDownmaker("addmenu");
    document.getElementById("initAddGroup").style.display="none";
    document.getElementById("results").style.display="none";
    document.getElementById("initLoadMoreLink").style.display="none";
    document.getElementById("initDropDown").style.display="none";
    document.getElementById("addNewGroup").style.display="block";
}
// initPreArtical();
initHeader();
initDropDown();
initGroupLinks();
initAddGroup();
initLoadMoreLink();
initLoadingImage();
// // initPostArtical();
loadLinks(currntTableName);
dropDownmaker("cMenu");


// data1={
//     groupName:'piriyaraj',
//     groupLink:'link3'
// };
// addGroups("testing/",data1)
function addGroupsTest(resultSet){
    tableName=resultSet.categoryList.value;
    groupLink=resultSet.groupLink.value;
    alert(tableName);
    alert(groupLink);
}

