function joinCheck() {
   
    var uid = document.getElementById("uid");
    var email= document.getElementById("email");
    var pwd = document.getElementById("pwd");
    var repwd = document.getElementById("repwd");
    var nickname = document.getElementById("nickname");
    var username = document.getElementById("username");
    var female = document.getElementById("female");
    var male = document.getElementById("male");


  
    if (uid.value == "") { //if(!uid.value)
      
      document.getElementById("noUid").innerHTML="아이디를 입력하세요.";
      uid.focus(); //focus(): 커서가 깜빡이는 현상, blur(): 커서가 사라지는 현상
      return false; //return false:  아무것도 반환하지 말아라 아래 코드부터 아무것도 진행하지 말것
    };
    if (uid.value != ""){
      document.getElementById("noUid").innerHTML=""
    }
    
    if (email.value == "") { 
      document.getElementById("noEmail").innerHTML="이메일을 입력하세요.";
      email.focus(); 
      return false; 
    };
    if (email.value != ""){
      document.getElementById("noEmail").innerHTML=""
    }
    
    if (pwd.value == "") { 
      document.getElementById("noPwd").innerHTML="비밀번호를 입력하세요.";
      pwd.focus(); 
      return false; 
    };
    if (pwd.value != ""){
      document.getElementById("noPwd").innerHTML=""
    }
   
    if (repwd.value == "") { 
      document.getElementById("noRepwd").innerHTML="비밀번호를 한번 더 입력하세요.";
      repwd.focus(); 
      return false;
    };
    if (repwd.value != ""){
      document.getElementById("noRepwd").innerHTML=""
    }
    
    if (nickname.value == "") { 
      document.getElementById("noNickname").innerHTML="별명을 입력하세요.";
      nickname.focus();
      return false; 
    };
    if (nickname.value != ""){
      document.getElementById("noNickname").innerHTML=""
    }
    
    if (username.value == "") { 
      document.getElementById("noUsername").innerHTML="이름을 입력하세요.";
      username.focus(); 
      return false; 
    };
    if (username.value != ""){
      document.getElementById("noUsername").innerHTML=""
    }
    
    if (phone.value == "") { 
      
      document.getElementById("noPhone").innerHTML="전화번호를 입력하세요.";
      phone.focus(); 
      return false; 
    };
    if (phone.value != ""){
      document.getElementById("noPhone").innerHTML=""
    }
    
    if (birth.value == "") { 
      
      document.getElementById("noBirth").innerHTML="생년월일을 입력하세요.";
      birth.focus(); 
      return false;
    };
    if (birth.value != ""){
      document.getElementById("noBirth").innerHTML=""
    }

    if (!female.checked && !male.checked) { 
      
      document.getElementById("noSex").innerHTML="성별을 체크하세요.";
      male.focus(); 
      return false;
    };
    if (female.checked || male.checked){
      document.getElementById("noSex").innerHTML=""
    }

    if (!agree1.checked||!agree2.checked||!agree3.checked) { 
      
      document.getElementById("noAgree").innerHTML="약관을 확인하세요.";
      agree.focus(); 
      return false;
    };
    if (agree1.checked&&agree2.checked&&agree3.checked){
      document.getElementById("noAgree").innerHTML=""
    }
  
    var pwdCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;

    if (!pwdCheck.test(pwd.value)) {
      alert("비밀번호는 영문자+숫자+특수문자 조합으로 8~25자리 사용해야 합니다.");
      pwd.focus();
      return false;
    };

    if (repwd.value !== pwd.value) {
      alert("비밀번호가 일치하지 않습니다.");
      repwd.focus();
      return false;
    };

    var reg = /^[0-9]+/g; //숫자만 입력하는 정규식

    if (!reg.test(phone.value)) {
    alert("전화번호는 숫자만 입력할 수 있습니다.");
    phone.focus();
    return false;
  }

  var emailRegExp = /^[A-Za-z0-9_]+[A-Za-z0-9]*[@]{1}[A-Za-z0-9]+[A-Za-z0-9]*[.]{1}[A-Za-z]{1,3}$/;
        if (!emailRegExp.test(email.value)) {
            alert("이메일 형식이 올바르지 않습니다");
            email.value = "";
            email.focus();
            return false;
        }
  //입력 값 전송
  //document.join.submit();
  location.href = "joinSuc.html";
   
    };
    
    
    
    function id_check() {
        //window.open("팝업될 문서 경로", "팝업될 문서 이름", "옵션");
        
        window.open("", "", "width=600, height=200, left=200, top=100");
       
      }
  
     