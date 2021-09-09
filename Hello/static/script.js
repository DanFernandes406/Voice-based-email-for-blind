if(annyang) {        	
    var commands = {
        'night mode' : function(){
            let root = document.documentElement;
            root.style.setProperty('--white','#000');
            root.style.setProperty('--black','#fff');
            console.log('yed');

        },
        'write username *tag' : function(variable){
            let uname = document.getElementById('username')
            console.log(uname)
            let res ='@gmail.com'
            uname.value = variable.split(" ").join("") + res;

        },
        'write password *tag' : function(variable){
            let uname = document.getElementById('password')
            uname.value = variable.split(" ").join("");

        },
        'write action *tag' : function(variable){
            let uname = document.getElementById('action')
            uname.value = variable.split(" ").join("");

        },
        'submit form' : function(){
            document.reg.submit();

        }

}

annyang.addCommands(commands);
annyang.start();
}