window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        update_cart_itmes: function (number_input, artile, article_type, price, data) {
            price = price.match(/\d+/)[0] 
            data[artile+'_'+article_type] = {
                        'price':price,
                        'quantity':number_input,
                        'total': price*number_input
                        }
           
            let total = number_input*price
            
            return [data,  `${total.toFixed(2)} DA`
        ]
        },

    show_cart_items: function (data) {
        console.log(data)
        var arr = [];
        // const entries = Object.entries(data);
        Object.entries(data).forEach(([key, value]) => {
            console.log(
                `key: ${key}`,
                `price: ${value['price']}`,
                `quantity: ${value['quantity']}`,
                `total: ${value['total']}`,
                )
        });

    //     data.forEach((element) => arr.push(
    // console.log(element)
    //     ));
 
        
        return 'data'

    }
    },


    
});