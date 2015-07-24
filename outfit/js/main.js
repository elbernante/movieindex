
$(document).ready(function () {

	var $tileGrid = $('.tile-grid');
	var transitionDuration = 400;

  	/**
	* Get YouTube ID from various YouTube URL
	* @author: takien
	* @url: http://takien.com
	*/
	function youTubeGetId(url){
	  var ID = '';
	  url = url.replace(/(>|<)/gi,'').split(/(vi\/|v=|\/v\/|youtu\.be\/|\/embed\/)/);
	  if(url[2] !== undefined) {
	    ID = url[2].split(/[^0-9a-z_\-]/i);
	    ID = ID[0];
	  }
	  else {
	    ID = url;
	  }
	    return ID;
	}

	function layoutTimer(){
		setTimeout(function(){
			$tileGrid.isotope('layout');
		}, transitionDuration);
	}

	// Show a movie trailer. callback is executed after the triailer is dissmissed.
	function showTrailer(movie, callback){
		var $modalBox = $('#videoModal');
		var youtubeid = youTubeGetId(movie['trailer']);
		var youtubeUrl = 'http://www.youtube.com/embed/' + youtubeid + '?autoplay=1&html5=1'
		$modalBox.find("iframe").attr('src', youtubeUrl);
		$modalBox.find(".modal-title").text(movie['title']);
		$modalBox.modal({});

		$modalBox.on('hidden.bs.modal', function clearTrailer(event){
			$(this).find('iframe').attr('src', '');
			$modalBox.off('hidden.bs.modal', clearTrailer);
			if ('function' === typeof callback) {
				callback(movie);
			}
		});
	}

	// Show more details of movie
	function showDetails(movie){
		var $modalBox = $('#showdetails');
		$modalBox.find('[data-role="mv-poster"]').attr('src', movie['poster']);
		$modalBox.find('[data-role="mv-title"]').text(movie['title'] + ' ');
		$modalBox.find('[data-role="mv-year"]').text(movie['year']);
		$modalBox.find('[data-role="mv-release-date"]').text(movie['release_date']);
		$modalBox.find('[data-role="mv-rating"]').text(movie['rating']);
		$modalBox.find('[data-role="mv-genre"]').text(movie['genres'].join(', '));
		$modalBox.find('[data-role="mv-plot"]').text(movie['plot']);
		$modalBox.find('[data-role="mv-synopsis"]').text(movie['synopsis']);
		$modalBox.find('[data-role="mv-actors"]').html('<li>' + movie['actors'].join('</li><li>') + '<li>');
		$modalBox.find('[data-role="mv-director"]').html('<li>' + movie['directors'].join('</li><li>') + '<li>');
		$modalBox.find('[data-role="mv-writer"]').html('<li>' + movie['writers'].join('</li><li>') + '<li>');

		$modalBox.on('click', '[data-role="mv-trailer"]', function trailerBtnClick() {
			$modalBox.off('[data-role="mv-trailer"]', trailerBtnClick)
			$modalBox.modal('hide');
			showTrailer(movie, function(){
				showDetails(movie);
			});
		})

		$modalBox.modal({});
	}

	// Sort function
	function sortTile(key, itemElem) {
		var movieid = $(itemElem).data('movieid');
		switch(key){
			case 'title': return movie_infos[movieid]['title'];
			case 'rating': return parseFloat(movie_infos[movieid]['rating']) || 0;
			case 'release_date': return (new Date(movie_infos[movieid]['release_date']));
			default: return 0;
		}
	}

	// Layout tiles
	$tileGrid.isotope({
	  itemSelector: '.tile',
	  layoutMode: 'masonry',
	  animationOptions: {
			duration: transitionDuration
		},
		getSortData: {
			title: function(itemElem){
				return sortTile('title', itemElem);
			},
			rating: function(itemElem){
				return sortTile('rating', itemElem);
			},
			release_date: function(itemElem){
				return sortTile('release_date', itemElem);
			}
		}
	});

	layoutTimer();

	$(window).resize(function(){
		layoutTimer();
	});

	$(window).load(function(){
		layoutTimer();
	});

	 // Animate in the movies when the page loads
	$('.tile').hide().first().show("fast", function showNext(){
	    $(this).next("div").show("fast", showNext);
	    layoutTimer();
	});

	// Initialize tile event behaviors
	$(document).find('.tile').each(function(index, obj){
		var $tile = $(obj);
		var movie = movie_infos[$tile.data('movieid')];
		
		// Play trailer on clicking poster image
		$tile.on('click', 'img, span.posteroverlay', function(event){
			showTrailer(movie);
		});

		// Show more details
		$tile.on('click', '.tile-title, div.moredetail button.btn-middle', function(event){
			showDetails(movie);
		});
	});

	// Tile overlay animation on mouse hover
	$('.tile').mouseenter(function(event){
		var $overlay = $(this).find('.posteroverlay');
		var $targetImage = $(this).find('img');
		var targetHeight = $targetImage.outerHeight();
		var targetWidth = $targetImage.outerWidth();
		$overlay.height(targetHeight);
		$overlay.width(targetWidth);
		
		$overlay.stop().animate({
			opacity: 0.6
		}, 'fast');

		$(this).find('.moredetail').stop().slideDown('fast');
		$(this).find('.moredetail button').animate({
			opacity: 0.9
		}, 'slow');
	});

	$('.tile').mouseleave(function(event){
		$(this).find('.posteroverlay').stop().animate({
			opacity: 0
		}, 'fast');
		$(this).find('.moredetail').stop().slideUp('fast');
		$(this).find('.moredetail button').animate({
			opacity: 0
		}, 'fast');
	});

	// Initializes the fiter and sort drop down menu
	jQuery.fn.extend({
		dropDownSelectMenu: function(onItemClick){
			var $parent = $(this);
			this.on('click', '[data-role="select-entry"]', function(event){
				var value = $(this).attr('value');
				var displayText = $(this).find('a').text();

				$parent.find('[data-role="selected-display"]').text(displayText);
				$parent.find('[data-role="select-entry"].active').removeClass('active');
				$(this).addClass('active');

				if ('function' === typeof onItemClick) {
					onItemClick(value);
				}
			});
		}
	});

	// Filter Button
	$('#genre-filter').dropDownSelectMenu(function(value){
		$tileGrid.isotope({
		  filter: function() {
		  	var mId = $(this).data('movieid');
		    return value === 'showall' ? true : 
		    	($.inArray(value, movie_infos[mId].genres) > -1);
		  }
		});
	});

	// Sort button
	$('#moviesort').dropDownSelectMenu(function(value){
		$tileGrid.isotope({
			sortBy: value,
			sortAscending: 'title' === value ? true : false
		});
	});

});
