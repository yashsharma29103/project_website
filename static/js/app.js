function onClickedEstimatedPrice(){
  console.log("Estimated Price button clicked")
  var date1 = document.getElementById('date')
  var estP = document.getElementById("uiEstimatedPrice")

  var url = 'https://noble-honey-kilometer.glitch.me/predict_stock_price'

  $.post(url, {
      date : date1.value
  }, function(data, status){
      console.log(data.estimated_price)
      estP.innerHTML = "<h2>Predicted Price is : $"+data.estimated_price.toString()+"</h2>"
      console.log(status)
  })

}

// function([string1, string2],target id,[color1,color2])    
consoleText(['Stock Price Prediction', 'AI/ML Using Python', 'Made By Yash Sharma'], 'text', ['rgb(0,20,58']);

function consoleText(words, id, colors) {
  if (colors === undefined) colors = ['#fff'];
  var visible = true;
  var con = document.getElementById('console-container');
  var letterCount = 1;
  var x = 1;
  var waiting = false;
  var target = document.getElementById(id)
  target.setAttribute('style', 'color:' + colors[0])
  window.setInterval(function () {

    if (letterCount === 0 && waiting === false) {
      waiting = true;
      target.innerHTML = words[0].substring(0, letterCount)
      window.setTimeout(function () {
        var usedColor = colors.shift();
        colors.push(usedColor);
        var usedWord = words.shift();
        words.push(usedWord);
        x = 1;
        target.setAttribute('style', 'color:' + colors[0])
        letterCount += x;
        waiting = false;
      }, 1000)
    } else if (letterCount === words[0].length + 1 && waiting === false) {
      waiting = true;
      window.setTimeout(function () {
        x = -1;
        letterCount += x;
        waiting = false;
      }, 1000)
    } else if (waiting === false) {
      target.innerHTML = words[0].substring(0, letterCount)
      letterCount += x;
    }
  }, 120)
  window.setInterval(function () {
    if (visible === true) {
      con = document.getElementById('d1')
      con.className = 'console-underscore hidden'
      visible = false;

    } else {
      con = document.getElementById('d1')
      con.className = 'console-underscore'

      visible = true;
    }
  }, 400)
}