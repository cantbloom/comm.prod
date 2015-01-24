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

    var run = BEERRUN_DATA.run;
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
                <span class='col-xs-10'>"+name+"</span><a\
                  class='order-increment col-xs-2 glyphicon glyphicon-chevron-up'\
                  data-drink-id='"+id+"'></a>\
              </div>\
              <div class='row'>\
                <span class='order-count col-xs-4 col-xs-offset-1'>"+amt+"\
                  </span><span class='order-total-price col-xs-5'>$"+price+"</span>\
                  <a class='order-decrement col-xs-2 glyphicon glyphicon-chevron-down'\
                  data-drink-id='"+id+"'></a>\
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

    // Handler for whenever the user adds/removes an item - mostly updates the
    // price elements
    var orderChanged = function() {
        $submit = $('#submit-order');

        var total = 0;
        for (i in myOrder) {
            total += myOrder[i] * allDrinks[i].price;
        }

        $('#drinks-price').text('$' + Math.round(total));
        $('#drinks-tax').text('$' + Math.round(total * 0.15));
        $('#total-price').text('$' + Math.round(total * 1.15));

        // If the local cart is synced with the server, remove the 'submit' button.
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

    // Depending on the contents of the 
    var dataFor = function(drink) {

    }

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
            class='icon-" + categories[drink.category[0]].icon + "\
            col-xs-1'></i><span class='col-xs-7'>" + drink.name + "</span>\
          <span class='col-xs-2'>$" + drink.clean_price + "</span>\
          <span class='col-xs-2 drink-data'>" + dataFor(drink) + "</span></a>\
      </div>");
    }

    // if 1, sort ascending; -1, descending
    sortDir = 1;
    // Object containing sort functions
    var sort_funcs = {
      // alphabetical
      name: function(drinks) { 
        drinks.sort(function(a, b) {
          if (a.name < b.name) { return -1 * sortDir; }
          if (a.name > b.name) { return 1 * sortDir; }
          return 0;
        });
      },

      // price, lo-hi or hi-lo
      price: function(drinks) {
        drinks.sort(function(a, b) { return (a.price - b.price) * sortDir; });
      },

      // abv * volume / price
      economy: function(drinks) {
        drinks.sort(function(a, b) {
          aVal = a.ABV * a.volume / a.price;
          bVal = b.ABV * b.volume / b.price;
          return (aVal - bVal) * sortDir;
        });
      },

      // alcohol percentage
      abv: function(drinks) {
        drinks.sort(function(a, b) { return (a.abv - b.abv) * sortDir; });
      }
      
      // popularity (TODO)
      //popular: function(drinks) {
        //drinks.sort(function(a, b) {
          //return 0;
        //});
      //}
    }

    // the current active sort function
    var sortCatalog = sort_funcs.name;

    // all drinks currently filtered
    var currentCatalog = Array();
    // number of drinks to show per page
    var DRINKS_PER_PAGE = 10;
    
    // refresh the catalog with new filters and re-sort
    var updateCatalog = function() {
      currentCatalog = _.map(allDrinks, _.clone);
      sortCatalog(currentCatalog);
      console.log(allDrinks);
      console.log(currentCatalog);
      console.log(sortCatalog);

      // delete all drink elements and add them back one by one.
      // TODO: only add/remove if necessary.
      $('.catalog .row.item').remove();
      currentCatalog.slice(0, DRINKS_PER_PAGE).forEach(addDrinkToCatalog);
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
    currentCatalog.slice(0, DRINKS_PER_PAGE).forEach(addDrinkToCatalog);

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
    // TODO: add a timeout and such
    $('#submit-order').click(function() {
        $('#submit-order').prop('disabled', true);
        $('#submit-order').text('Submitting...');

        postOrder = _.clone(myOrder);
        for (var v in cleanOrder) {
            if (myOrder[v] === undefined) { postOrder[v] = 0; }
        }

        $.post(STATIC_PREFIX + '/api/update_run/' + run.pk, postOrder, function(d, status) {
            console.log(status);
            // disable the 'submit' button
            cleanOrder = _.clone(myOrder);
            $('#submit-order').text('Submit');
            orderChanged();
        });
    });

    // dynamic search whenever the bar input changes
    $('#drink-search-form').keyup(function() {
      var term = $.trim($('#drink-search-form').val()).toLowerCase();
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
          else {
            for (var j = 0; j < allDrinks[id].category.length; j++) {
              var c = allDrinks[id].category[j];
              if (categories[c].name.toLowerCase().indexOf(term) > -1) {
                currentCatalog.push(_.clone(allDrinks[id]));
                break;
              }
            }
          }
        }
      }

      console.log(currentCatalog);
      updateCatalog();
    });

    // attach handlers to the sort buttons: sort and reload elements on each click
    $('.sort-link').each(function() {
      // grab the name of the button
      var f = $(this).attr('data');

      $(this).click(function() {
        if (sort_funcs[f] == sortCatalog) {
          sortDir *= -1;
        } else {
          sortDir = 1;
          sortCatalog = sort_funcs[f];
        }
        // re-sort the catalog
        updateCatalog();
      });
    });

    // there's only one choice for the lucky bomber
    $('#feeling-lucky').click(function() {
        rand = Math.floor(Math.random() * 10) + 1;
        for (var i=0; i < rand; i++) {
            addDrink(highLifeID);
        }
    });
});
