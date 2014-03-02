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
    // Let's create the iFrame used to send our data
    var iframe = document.createElement("iframe");
    iframe.name = "myTarget";

    // Next, attach the iFrame to the main document
    window.addEventListener("load", function () {
      iframe.style.display = "none";
      document.body.appendChild(iframe);
    });

    // This is the function used to actually send the data
    // It takes one parameter, which is an object populated with key/value pairs.
    function sendData(data) {
      var name,
          form = document.createElement("form"),
          node = document.createElement("input");

      // Define what should happen when the response is loaded
      iframe.addEventListener("load", function () {
        document.getElementById('show').innerHTML = "data sent";
        document.getElementById('show').style.display = "block";
      });

      form.action = "https://agent.electricimp.com/B1iqTo1VR_He";
      form.target = iframe.name;

      for(name in data) {
        node.name  = name;
        node.value = data[name].toString();
        form.appendChild(node.cloneNode());
      }

      // To be sent, the form needs to be attached to the main document.
      form.style.display = "none";
      document.body.appendChild(form);

      form.submit();

      // But once the form is sent, it's useless to keep it.
      document.body.removeChild(form);
    }
    function sendRequest(){
       var value = document.getElementById('options').value;
       if(value !== ""){
            sendData({led: parseInt(value)});
       }
    }
</script>
    <select id="options" onchange="sendRequest()">
        <option value="">please choose</option>
"""
    for i in range(0, 36):
        s += "\no        <option value=\"{0}\">{0}</option>".format(i)
    s += """
    </select>
<div id="show" style="display:none;"></div>
</body>
</html>
"""
    return s
