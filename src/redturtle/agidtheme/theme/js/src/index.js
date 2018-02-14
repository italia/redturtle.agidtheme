require([
  'jquery',
  'ellipsed',
  'fa'
], function ($, ellipsed, fa) {
  'use strict';

  var ellipsis = ellipsed.ellipsis;

  // adding some <i> via js for fontawesome icons
  var icons = [
    {
      selector: '#breadcrumbs-home a',
      icon: 'fas fa-home',
      prepend: true,
    },
    {
      selector: '.template-album_view .photoAlbumEntry.photoAlbumFolder .photoAlbumEntryTitle',
      icon: 'fas fa-folder-open',
      prepend: true,
    },
    {
      selector: '.footer-social .fb',
      icon: 'fab fa-facebook-f',
      prepend: true,
    },
    {
      selector: '.footer-social .ig',
      icon: 'fab fa-instagram',
      prepend: true,
    },
    {
      selector: '.footer-social .tw',
      icon: 'fab fa-twitter',
      prepend: true,
    },
    {
      selector: '.footer-social .tg',
      icon: 'fab fa-telegram',
      prepend: true,
    },
    {
      selector: '.footer-social .yt',
      icon: 'fab fa-youtube',
      prepend: true,
    },
    {
      selector: '.footer-social .in',
      icon: 'fab fa-linkedin-in',
      prepend: true,
    },
    {
      selector: '.footer-social .gp',
      icon: 'fab fa-google-plus-g',
      prepend: true,
    },
    {
      selector: '.footer-social .pi',
      icon: 'fab fa-pinterest',
      prepend: true,
    },
    {
      selector: '.footer-social .po',
      icon: 'fab fa-get-pocket',
      prepend: true,
    },
    {
      selector: '.footer-social .rss',
      icon: 'fas fa-rss',
      prepend: true,
    },
    {
      selector: '.navigationTile a.navTreeFolderish:not(.navTreeCurrentNode):not(.navTreeItemInPath), .portletNavigationTree a.navTreeFolderish:not(.navTreeCurrentNode):not(.navTreeItemInPath)',
      icon: 'far fa-angle-down',
      prepend: false,
    },
    {
      selector: '.navigationTile a.navTreeFolderish.navTreeCurrentNode, .navigationTile a.navTreeFolderish.navTreeItemInPath, .portletNavigationTree a.navTreeFolderish.navTreeCurrentNode, .portletNavigationTree a.navTreeFolderish.navTreeItemInPath',
      icon: 'far fa-angle-up',
      prepend: false,
    },
  ];

  $(document).ready(function () {
    $('#breadcrumbs-home a').text('');

    // init fontawesome icons
    icons.forEach(function(i) {
      var $el = $(i.selector);

      if (i.prepend) {
        $el.prepend('<i class="' + i.icon + '"></i>');
      }
      else {
        $el.append('<i class="' + i.icon + '"></i>');
      }
    });

    fa.init();

    /*
     *  return-to-top arrow
     */
    $(window).scroll(function () {
      if ($(this).scrollTop() >= 50) {
        $('#return-to-top').fadeIn(200);
      } else {
        $('#return-to-top').fadeOut(200);
      }
    });

    $('#return-to-top').click(function () {
      $('body,html').animate({
        scrollTop: 0,
      }, 500);
    });


    /*
     *  share button position
     */
    var $share = $('.share');
    if ($('.news-column').length) {
      $('.news-column').prepend($share);
      $share.addClass('share-visible');
    }
    else if ($('#portal-column-two').length) {
      $('#portal-column-two').prepend($share);
      $share.addClass('share-visible');
    }


    /*
     * share button behavior
     */
    $('.share .share-toggle').on('click', function(e) {
      e.preventDefault();
      $share.toggleClass('open');
    });


    /*
     * mobile: search button action
     */
    $('#search-toggle').on('click', function(e) {
      $('#portal-searchbox').toggleClass('open');
      $('#search-toggle').toggleClass('open');
      $('body').toggleClass('searchOpened');

      if ($('#portal-searchbox').hasClass('open')) {
        $('#searchGadget').focus();
      }
    });


    /*
     * mobile: menu toggle click
     */
    $('button.plone-navbar-toggle').on('click', function(e) {
      $('#portal-globalnav-wrapper').toggleClass('open');
    });


    /*
     * gestione click fuori per chiudere menu, ricerca e condividi
     */
    $(document).on('click', function(e) {
      if ((!$(e.target).closest('#portal-searchbox').length && !$(e.target).closest('button#search-toggle').length) && $(window).width() <= 991) {
        $('#portal-searchbox').removeClass('open');
        $('#search-toggle').removeClass('open');
        $('body').removeClass('searchOpened');
      }

      if (!$(e.target).closest('.share').length) {
        $share.removeClass('open');
      }

      if ((!$(e.target).closest('#portal-globalnav-wrapper').length && !$(e.target).closest('button.plone-navbar-toggle').length) && $(window).width() <= 991) {
        $('#portal-globalnav-wrapper').removeClass('open');
      }
    });

    /*
     * On tiles loaded:
     * - gestito tabIndex news collection collapse
     * - multi lined ellipsis for news collection items
     */
    $('.pat-tiles-management').on('rtTilesLoaded', function(e) {
      ellipsis('.tile-collection .collectionItemDescription', 4, { responsive: true });
      ellipsis('.news-highlight .news-description', 4, { responsive: true });
      ellipsis('.news-big-photo .news-description', 4, { responsive: true });
    });

    $(document).on('patSliderInit', function(e) {
      $(e.originalEvent.detail).find('.slick-dots').attr('aria-hidden', true);
    });

  });
});