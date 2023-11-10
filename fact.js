function fact(){
    var i,num,f;
    f=1
    num=document.getElementById("num").value;
    for(i=1;i<num;i++)
    {
        f=f*i;
    }
    i=i-1;
    document.getElementById("res").innerHTML="The Factorial of the Number" + i +"is:"+f;
}