function validateForm() {
    var title = document.forms[0]["title"].value;
    var tag = document.forms[0]["tag"].value;
    var description = document.forms[0]["description"].value;
    var dueDate = document.forms[0]["due_date"].value;

    if (title == "" || tag == "" || description == "" || dueDate == "") {
        alert("Всі поля повинні бути заповнені");
        return false;
    }
    return true;
}

