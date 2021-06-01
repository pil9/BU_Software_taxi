let map; //구글맵 initMap에 쓰일 변수

// 구글 맵 생성함수 
function initMap() {
    
    const uluru = { lat: 36.84022875274761, lng: 127.18320432480536 };
   
    //지도생성
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15,
      center: uluru,
    });
    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
    });
  }

/**참여게시판 테이블 생성 함수 */
function tableMaker(name, departure, destination, deadline) {

    //tbody태그와 tr태그 생성
    document.write("<tr>");

    //모집자 이름 생성
    document.write("<td class= col-md-1'>");
    document.write(name);
    document.write("</td>");

    //모집 마감시간 생성
    document.write("<td class= col-md-1'>");
    document.write(deadline);
    document.write("</td>");

    //현재 모집인원 생성 (임시로 만듬,, 서버와 연동해서 값 조정되야함)
    document.write("<td class= col-md-1'>");
    document.write("1/4");
    document.write("</td>");

    //출발지 생성
    document.write("<td class= col-md-1'>");
    document.write(departure);
    document.write("</td>");

    //도착지 생성
    document.write("<td class= col-md-1'>");
    document.write(destination);
    document.write("</td>");

    //예상 총액 생성 (임시로 만듬,, 거리에 따라 자동으로 값이 변동되야함, 구글맵 사용하면 가능할듯)
    document.write("<td class= col-md-1'>");
    document.write(12000 + "원");
    document.write("</td>");

    //참여 버튼 생성
    document.write("<td class= col-md-1'>");
    document.write("<button onclick='test(); return false;'>참여하기</button>");
    document.write("</td>");

    //tbody 닫는태그와 tr 닫는태그 생성
    document.write("</tr>");
}

/**블랙리스트 테이블 생성 함수 */
function blackListMaker(bName, bReason, bDate) {

    //tbody태그와 tr태그 생성
    document.write("<tr>");

    //신고 날짜
    document.write("<td>");
    document.write(bDate);
    document.write("</td>");

    //불량유저 이름
    document.write("<td>");
    document.write(bName);
    document.write("</td>");

    //신고 사유
    document.write("<td>");
    document.write(bReason);
    document.write("</td>");

    //tbody 닫는태그와 tr 닫는태그 생성
    document.write("</tr>");
}

/**모집하기.html에서 모집시작버튼을 누르면 실행되는 함수 */
function recruitValues() { //모집하기 화면에서 데이터가 넘어옴
    //변수 xx에 'info' form 데이터 배열 형식으로 저장
    var create = document.getElementById("reqruitInfo");

    //필요한 변수 선언 
    var userName = "";
    var userDeparture = "";
    var userDestination = "";
    var userDeadline = 0;

    // 각각 이름, 출발지, 도착지, 마감시간 변수에 해당하는 값 저장 
    userName = create.elements[0].value;
    userDeparture = create.elements[1].value;
    userDestination = create.elements[2].value;
    userDeadline = create.elements[3].value;

    window.open("메인메뉴.html?" + userName + ":" + userDeparture + ":" + userDestination + ":" + userDeadline);

    //모집완료 알람
    //alert('이름 '+userName+'\n출발지 '+userDeparture+'\n목적지 '+userDestination+'\n마감시간 '+userDeadline);    
}

/**신고하기.html에서 신고하기 버튼을 누르면 실행되는 함수 */
function blackValues() {

    var today = new Date();
    var year = today.getFullYear(); // 년도
    var month = today.getMonth() + 1;  // 월
    var day = today.getDate();  // 날짜
    var date = year+"-"+month+"-"+day;

    var blackUser = document.getElementById("blackUserInfo"); //배열로 신고사항 폼에 있는 데이터를 받는다

    var bUserName = "";
    var bUserReason = "";

    bUserName = blackUser.elements[0].value;
    bUserReason = blackUser.elements[1].value;

    window.open("블랙리스트.html?" + bUserName + ":" + bUserReason + ":" + date);
}

/**로그인 함수입니다 */
function login() {
    var idpwd = document.getElementById("loginInfo");

    var userId = "";
    var userPw = "";

    userId = idpwd.elements[0].value;
    userPw = idpwd.elements[1].value;

    /*일단 덤프값으로 아이디 비번 모두 test로 해놨습니다*/
    if (userId == "test" && userPw == "test") {
        location.href = "메인메뉴.html";

    }
    else {
        alert("잘못된 회원정보입니다.");
    }
}

/**메인화면의 게시판 목록에서 '참여하기' 버튼을 누르면 참여중 화면으로 넘어가는 함수*/
function joinTaxi() {
    location.href = "참여중.html";
}

/**메인메뉴 화면 우측상단에 포인트를 띄워주는 함수*/
function myPoint(money) {
    document.write("[내 포인트 = "+money+"원]");
}

/**충전하기 화면에서 값을 넘겨받는 함수, 진짜 은행 거래는 구현 안됨*/
function chargePoint(){
    var inputMoney = document.getElementById("charge");

    var point="";
    var dump="0";

    point = inputMoney.elements[0].value;
    window.open("메인메뉴.html?" + dump + ":" + point);
}