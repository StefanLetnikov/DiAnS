// Creating map options
    //41.99594, 21.43147
    var longitude = "21.43147";
    var latitude = "41.99594";
    var map;

    var mapOptions = {
        center: [latitude, longitude],
        zoom: 14
    }

    // Creating a map object
    var map = new L.map('map', mapOptions);

    //var marker = L.marker([41.9945784, 21.4338471]).addTo(map);
    //marker.bindPopup("<b>Anhoch Market</b><br>GTC.").openPopup();
    // Creating a Layer object
    var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

    // Adding layer to the map
    map.addLayer(layer);


    window.onclick = e => {
        //console.log(e.target);  // to get the element
        var collection = e.target;
        var value = collection.children;
        //console.log(value)
        longitude = value[0].children[1].innerText
        //console.log(longitude)
        latitude = value[0].children[2].innerText
        var shop_name = value[0].children[3].innerText
        var shop_address = value[0].children[4].innerText


        mapOptions = {
            center: [latitude, longitude],
            zoom: 16
        }
        //destroying the old map object
        map.off();
        map.remove();
         //Creating a map object
        map = new L.map('map', mapOptions);

        marker = L.marker([longitude, latitude]).addTo(map);
        markerInfo = shop_name + '\n ' + shop_address;
        marker.bindPopup(markerInfo).openPopup();
        // Creating a Layer object
        layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

        // Adding layer to the map
        map.addLayer(layer);

        //console.log(latitude)
    }