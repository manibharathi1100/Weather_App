
  
  var Search = document.getElementById("search");

  //event
  Search.addEventListener('keyup', e => {
      if(e.keyCode === 13){
          var getCityName = e.target.value;
      }
      getWeather(getCityName);
  });

  function getWeather(getCityName){
      const weatherApi= `http://api.openweathermap.org/data/2.5/weather?q=${getCityName}&&mode=json&units=metric&APPID=217599e58d445ca67484ce8a6e43c79a`;
      window.fetch(weatherApi)
      .then(data => {
          data.json()

          .then(weather => {
              var output = "";
              console.log(weather);//if u remove this we dont gt the array in console
              //aaray here
                var weatherData = weather.weather;
                for(let x of weatherData){
                    output+=`
                    <div class="col-md-4 offset-4 mt-4 card">
                        <div class="card-body">
                        <h1>${weather.name}</h1>
                        <span class="icon"><img src="http://openweathermap.org/img/wn/${x.icon}.png"/></span>
                        <p><span>temp:</span>
                        <span class="temp"> ${weather.main.temp}&deg;c</span>
                        </p>
                        <p><span class="des">${x.description}</span></p>
                        <p><span class="tes">${x.main}</span></p>
                        
                        </div>
                        </div>`;
                        document.getElementById("templete").innerHTML=output;
                    
                }
          }).catch(err => console.log(err));
      }).catch(err => console.log(err));

  }