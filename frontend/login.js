function validate()
{
    var Username = document.getElementById("Username").Value;
    var password = document.getElementById("password").Value;
    var Email = document.getElementById("Email").Value;
    var FullName = document.getElementById("FullName").Value;

    if(Username == "admin", password == "user")
    {
        alert("Log in completed");
        return false;
    }
    else
    {
        alert("Login Terminated");
    }
}
