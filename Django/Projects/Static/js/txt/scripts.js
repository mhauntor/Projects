function convertToHtml() {
    var x = CKEDITOR.instances['id_doctext'].getData();
    var y = document.getElementById('htmldata');
    y.value = x;
}