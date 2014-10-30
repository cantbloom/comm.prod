$(function() {
    // Cookies stuff for Django
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            var csrftoken = $.cookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var runID = $('meta[name=runID]').attr('content');
    var highLifeID = false;

    // add an element to the "my order" list
    var addMyDrinkElement = function(id, amt) {
        var name = String(allDrinks[id].name) +
            (allDrinks[id].quantity == 1 ? '' : ' (' +
             allDrinks[id].quantity + ')');
        var price = allDrinks[id].clean_price * amt;

        // remove the placeholder, if it's there
        $('#my-order-list').find('#my-order-empty').remove();

        // append the HTML
        $('#my-order-list').append(
            "<div id='my-order-"+id+"' class='item'>\
              <div class='row'>\
                <span class='col-xs-10'>"+name+"</span><a \
                  class='order-increment col-xs-2 icon-chevron-up' data-drink-id=\
                  '"+id+"'></a>\
              </div>\
              <div class='row'>\
                <span class='order-count col-xs-4 col-xs-offset-1'>"+amt+"\
                  </span><span class='order-total-price col-xs-5'>$"+price+"</span><a class=\
                  'order-decrement col-xs-2 icon-chevron-down' data-drink-id=\
                  '"+id+"'></a>\
              </div>\
            </div>"
        );

        // add the handlers for the up/down arrow elements
        $('#my-order-' + id + ' .order-increment').click(function() {
            addDrink($(this).data('drink-id'));
        });
        $('#my-order-' + id + ' .order-decrement').click(function() {
            removeDrink($(this).data('drink-id'));
        });
    }

    var orderChanged = function() {
        $submit = $('#submit-order');

        var total = 0;
        for (i in myOrder) {
            total += myOrder[i] * allDrinks[i].price;
        }

        $('#drinks-price').text('$' + Math.round(total));
        $('#drinks-tax').text('$' + Math.round(total * 0.15));
        $('#total-price').text('$' + Math.round(total * 1.15));

        if (_.isEqual(myOrder, cleanOrder)) {
            $submit.slideUp(100);
            $submit.prop('disabled', true);
        } else {
            $submit.slideDown(100);
            $submit.prop('disabled', false);
        }
    }

    // add a drink to the order
    var addDrink = function(id) {
        // if the element is already present, modify it
        if (parseInt(id) in myOrder) {
            console.log(id);
            myOrder[id]++;
            console.log(myOrder[id]);
            $('#my-order-' + id + ' .order-count').text(myOrder[id]);
            $('#my-order-' + id + ' .order-total-price').text(
                "$" + (myOrder[id] * allDrinks[id].price));
        // otherwise, make it
        } else {
            myOrder[id] = 1;
            addMyDrinkElement(id, 1);
        }

        orderChanged();
    };

    // remove a drink from the order
    var removeDrink = function(id) {
        myOrder[id]--;

        if (myOrder[id] < 1) {
            delete myOrder[id];
            $('#my-order-' + id).unbind();
            $('#my-order-' + id).remove();
        } else {
            $('#my-order-' + id + ' .order-count').text(myOrder[id]);
            $('#my-order-' + id + ' .order-total-price').text(
                "$" + (myOrder[id] * allDrinks[id].price));
        }

        orderChanged();
    };

    // Get relevant data from the janky embedded JS on the page. 
    // Format is the same as the model: name, category, volume, abv, price,
    // quantity, plus clean_price and clean_volume.
    // load categories first so they can be referenced by drinks
    var categories = {};
    BEERRUN_DATA.categories.forEach(function(cat) {
            categories[cat.pk] = cat;
    });

    var addDrinkToCatalog = function(drink) {
      drinkList.append(
      "<div class='row item'>\
        <a class='drink' id='" + drink.pk + "'><i \
            class='icon-" + categories[drink.category].icon + "\
            col-xs-1'></i><span class='col-xs-7'>" + drink.name + "</span>\
          <span class='col-xs-2'>" + drink.clean_volume + "</span>\
          <span class='col-xs-2'>$" + drink.clean_price + "</span></a>\
      </div>");
    }

    // Sort functions
    var sortByName = function(drinks) { 
      drinks.sort(function(a, b) {
        if (a.name < b.name) { return -1; }
        if (a.name > b.name) { return 1; }
        return 0;
      });
    }
    var sortByPrice = function(drinks) {
      drinks.sort(function(a, b) { return a.price - b.price; });
    }
    var sortByPopular = function(drinks) {
      drinks.sort(function(a, b) {
        //TODO
        return 0;
      });
    }
    var sortByEconomy = function(drinks) {
      drinks.sort(function(a, b) {
        aVal = a.ABV * a.volume / a.price;
        bVal = b.ABV * b.volume / b.price;
        return aVal - bVal;
      });
    }

    // the current active sort function
    var sortCatalog = sortByName;

    // refresh the catalog with new filters
    var currentCatalog = Array();
    var updateCatalog = function() {
      sortCatalog(currentCatalog);
      var activeDrinks = $.map($('.drink'), function(d) { return d.id });
      console.log(activeDrinks);

      // delete all drink elements and add them back one by one.
      // TODO: only add/remove if necessary.
      $('.catalog .row.item').remove();
      currentCatalog.slice(0, 25).forEach(addDrinkToCatalog);
    }

    // load drinks next so they can be referenced by myDrinks
    var allDrinks = {};
    drinkList = $('.catalog');
    BEERRUN_DATA.allDrinks.forEach(function(drink) {
        allDrinks[drink.pk] = drink;
        if (drink.name.indexOf("High Life") != -1) { highLifeID = drink.pk; }
    });
    currentCatalog = _.map(allDrinks, _.clone);
    sortCatalog(currentCatalog);
    currentCatalog.slice(0, 25).forEach(addDrinkToCatalog);

    // hook up drink click handlers
    for (var i in allDrinks) {
        $('#' + i).click(function() {
            addDrink($(this).attr('id'));
        });
    }

    // load myDrinks last, because the object only stores ids
    var myOrder = _.clone(BEERRUN_DATA.myDrinks);
    var cleanOrder = _.clone(BEERRUN_DATA.myDrinks);
    for (var id in myOrder) {
        addMyDrinkElement(id, myOrder[id]);
    }

    orderChanged();

    /*
    $('.price-info').hover(
        function() {
            $(this).find('.info-rollover-text').fadeTo(100, 1.0);
        }, function() {
            $(this).find('.info-rollover-text').fadeTo(100, 0);
        }
    );
    */

    // update the database with the new order
    $('#submit-order').click(function() {
        $('#submit-order').prop('disabled', true);
        $('#submit-order').text('Submitting...');
        postOrder = _.clone(myOrder);
        for (var v in cleanOrder) {
            if (myOrder[v] === undefined) { postOrder[v] = 0; }
        }
        $.post(STATIC_PREFIX + '/api/update_run/' + runID, postOrder, function(d, status) {
            console.log(status);
            // disable the 'submit' button
            cleanOrder = _.clone(myOrder);
            $('#submit-order').text('Submit');
            orderChanged();
        });
    });

    // dynamic search whenever the bar input changes
    $('#search-bar-form').keyup(function() {
      var term = $.trim($('#search-bar-form').val()).toLowerCase();
      console.log(term);

      // If the bar is empty, return everything
      if (term === "") {
        currentCatalog = _.map(allDrinks, _.clone);
      } else {
        // re-build the current catalog from scratch every time
        currentCatalog = Array();
        for (id in allDrinks) {
          if (allDrinks[id].name.toLowerCase().indexOf(term) > -1)
            currentCatalog.push(_.clone(allDrinks[id]));
          else if (categories[allDrinks[id].category].name.toLowerCase().indexOf(term) > -1)
            currentCatalog.push(_.clone(allDrinks[id]));
        }
      }

      console.log(currentCatalog);
      updateCatalog();
    });

    // TODO: handles to activate sorting

    // there's only one choice for the lucky bomber
    $('#feeling-lucky').click(function() {
        rand = Math.floor(Math.random() * 10) + 1;
        for (var i=0; i < rand; i++) {
            addDrink(highLifeID);
        }
    });
});
