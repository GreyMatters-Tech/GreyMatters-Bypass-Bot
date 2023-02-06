from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<!DOCTYPE html>
<!-- Created By CodingLab - www.codinglabweb.com -->
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <!-- Fontawesome CDN Link -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css"/>
       <!--<title> Working Subscribe Button | CodingLab </title>-->
   </head>
<body>
  <div class="container">
    <input type="radio" id="hide">
    <div class="box">
      <label for="hide"><i class="fas fa-times"></i></label>
      <div class="logo">
        <!--<img src="logo.png" alt="">-->
      </div>
      <div class="right">
        <div class="text-1">CodingLab</div>
        <div class="text-2">Subscribe Our YouTube Channel</div>
        <a href="https://www.youtube.com/channel/UCBlr2jG1onljL-gUy9bbhJw?sub_confirmation=1" target="_blank">Subscribe</a>
      </div>
    </div>
  </div>

</body>
</html>
'


if __name__ == "__main__":
    app.run()
