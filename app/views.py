from app import app

@app.route('/')
@app.route('/index')
def index():
    s = """
<html>
<head>
<title>Molley Weasley Clock</title>
</head>
<body>
<script type="text/javascript">
    function showText(){
       var value = document.getElementById('options').value;
       if(value != ""){
            document.getElementById('show').innerHTML = value;
            document.getElementById('show').style.display = "block";
       }
    }
</script>
    <select id="options" onchange="showText()">
"""
    for i in range(1, 37):
        s += "\no        <option value=\"{0}\">{0}</option>".format(i)
    s += """
    </select>
<div id="show" style="display:none;"></div>
</body>
</html>
"""
    return s
