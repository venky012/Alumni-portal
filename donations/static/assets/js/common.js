//----SMOOTH SCROLL---//
function init() {
    if (document.body) {
        var e = document.body,
            t = document.documentElement,
            n = window.innerHeight,
            o = e.scrollHeight;
        if (root = document.compatMode.indexOf("CSS") >= 0 ? t : e, activeElement = e, initdone = !0, top != self) frame = !0;
        else if (o > n && (e.offsetHeight <= n || t.offsetHeight <= n)) {
            var r = !1,
                a = function() {
                    r || t.scrollHeight == document.height || (r = !0, setTimeout(function() {
                        t.style.height = document.height + "px", r = !1
                    }, 500))
                };
            if (t.style.height = "", setTimeout(a, 10), addEvent("DOMNodeInserted", a), addEvent("DOMNodeRemoved", a), root.offsetHeight <= n) {
                var i = document.createElement("div");
                i.style.clear = "both", e.appendChild(i)
            }
        }
        if (document.URL.indexOf("mail.google.com") > -1) {
            var l = document.createElement("style");
            l.innerHTML = ".iu { visibility: hidden }", (document.getElementsByTagName("head")[0] || t).appendChild(l)
        }
        fixedback || disabled || (e.style.backgroundAttachment = "scroll", t.style.backgroundAttachment = "scroll")
    }
}

function scrollArray(e, t, n, o) {
    if (o || (o = 1e3), directionCheck(t, n), acceleration) {
        var r = +new Date,
            a = r - lastScroll;
        if (accelDelta > a) {
            var i = (1 + 30 / a) / 2;
            i > 1 && (i = Math.min(i, accelMax), t *= i, n *= i)
        }
        lastScroll = +new Date
    }
    if (que.push({
            x: t,
            y: n,
            lastX: 0 > t ? .99 : -.99,
            lastY: 0 > n ? .99 : -.99,
            start: +new Date
        }), !pending) {
        var l = e === document.body,
            c = function() {
                for (var r = +new Date, a = 0, i = 0, s = 0; s < que.length; s++) {
                    var d = que[s],
                        u = r - d.start,
                        m = u >= animtime,
                        f = m ? 1 : u / animtime;
                    pulseAlgorithm && (f = pulse(f));
                    var h = d.x * f - d.lastX >> 0,
                        p = d.y * f - d.lastY >> 0;
                    a += h, i += p, d.lastX += h, d.lastY += p, m && (que.splice(s, 1), s--)
                }
                l ? window.scrollBy(a, i) : (a && (e.scrollLeft += a), i && (e.scrollTop += i)), t || n || (que = []), que.length ? requestFrame(c, e, o / framerate + 1) : pending = !1
            };
        requestFrame(c, e, 0), pending = !0
    }
}

function wheel(e) {
    initdone || init();
    var t = e.target,
        n = overflowingAncestor(t);
    if (!n || e.defaultPrevented || isNodeName(activeElement, "embed") || isNodeName(t, "embed") && /\.pdf/i.test(t.src)) return !0;
    var o = e.wheelDeltaX || 0,
        r = e.wheelDeltaY || 0;
    o || r || (r = e.wheelDelta || 0), Math.abs(o) > 1.2 && (o *= stepsize / 120), Math.abs(r) > 1.2 && (r *= stepsize / 120), scrollArray(n, -o, -r), e.preventDefault()
}

function keydown(e) {
    var t = e.target,
        n = e.ctrlKey || e.altKey || e.metaKey || e.shiftKey && e.keyCode !== key.spacebar;
    if (/input|textarea|select|embed/i.test(t.nodeName) || t.isContentEditable || e.defaultPrevented || n) return !0;
    if (isNodeName(t, "button") && e.keyCode === key.spacebar) return !0;
    var o, r = 0,
        a = 0,
        i = overflowingAncestor(activeElement),
        l = i.clientHeight;
    switch (i == document.body && (l = window.innerHeight), e.keyCode) {
        case key.up:
            a = -arrowscroll;
            break;
        case key.down:
            a = arrowscroll;
            break;
        case key.spacebar:
            o = e.shiftKey ? 1 : -1, a = -o * l * .9;
            break;
        case key.pageup:
            a = .9 * -l;
            break;
        case key.pagedown:
            a = .9 * l;
            break;
        case key.home:
            a = -i.scrollTop;
            break;
        case key.end:
            var c = i.scrollHeight - i.scrollTop - l;
            a = c > 0 ? c + 10 : 0;
            break;
        case key.left:
            r = -arrowscroll;
            break;
        case key.right:
            r = arrowscroll;
            break;
        default:
            return !0
    }
    scrollArray(i, r, a), e.preventDefault()
}

function mousedown(e) {
    activeElement = e.target
}

function setCache(e, t) {
    for (var n = e.length; n--;) cache[uniqueID(e[n])] = t;
    return t
}

function overflowingAncestor(e) {
    var t = [],
        n = root.scrollHeight;
    do {
        var o = cache[uniqueID(e)];
        if (o) return setCache(t, o);
        if (t.push(e), n === e.scrollHeight) {
            if (!frame || root.clientHeight + 10 < n) return setCache(t, document.body)
        } else if (e.clientHeight + 10 < e.scrollHeight && (overflow = getComputedStyle(e, "").getPropertyValue("overflow-y"), "scroll" === overflow || "auto" === overflow)) return setCache(t, e)
    } while (e = e.parentNode)
}

function addEvent(e, t, n) {
    window.addEventListener(e, t, n || !1)
}

function removeEvent(e, t, n) {
    window.removeEventListener(e, t, n || !1)
}

function isNodeName(e, t) {
    return (e.nodeName || "").toLowerCase() === t.toLowerCase()
}

function directionCheck(e, t) {
    e = e > 0 ? 1 : -1, t = t > 0 ? 1 : -1, (direction.x !== e || direction.y !== t) && (direction.x = e, direction.y = t, que = [], lastScroll = 0)
}

function pulse_(e) {
    var t, n, o;
    return e *= pulseScale, 1 > e ? t = e - (1 - Math.exp(-e)) : (n = Math.exp(-1), e -= 1, o = 1 - Math.exp(-e), t = n + o * (1 - n)), t * pulseNormalize
}

function pulse(e) {
    return e >= 1 ? 1 : 0 >= e ? 0 : (1 == pulseNormalize && (pulseNormalize /= pulse_(1)), pulse_(e))
}
if (!jQuery(".enable_smoothscroll").length && jQuery(window).width() > 1024) {
    var framerate = 150,
        animtime = 4e3,
        stepsize = 200,
        pulseAlgorithm = !0,
        pulseScale = 25,
        pulseNormalize = 1,
        acceleration = !1,
        accelDelta = 10,
        accelMax = 1,
        keyboardsupport = !0,
        disableKeyboard = !1,
        arrowscroll = 50,
        exclude = "",
        disabled = !1,
        frame = !1,
        direction = {
            x: 0,
            y: 0
        },
        initdone = !1,
        fixedback = !0,
        root = document.documentElement,
        activeElement, key = {
            left: 37,
            up: 38,
            right: 39,
            down: 40,
            spacebar: 32,
            pageup: 33,
            pagedown: 34,
            end: 35,
            home: 36
        },
        que = [],
        pending = !1,
        lastScroll = +new Date,
        cache = {};
    setInterval(function() {
        cache = {}
    }, 1e4);
    var uniqueID = function() {
            var e = 0;
            return function(t) {
                return t.uniqueID || (t.uniqueID = e++)
            }
        }(),
        requestFrame = function() {
            return window.requestAnimationFrame || window.webkitRequestAnimationFrame || function(e, t, n) {
                window.setTimeout(e, n || 1e3 / 60)
            }
        }();
    addEvent("mousedown", mousedown), addEvent("mousewheel", wheel), addEvent("load", init)
}

/*! WOW - v1.1.2 - 2015-04-07
* Copyright (c) 2015 Matthieu Aussaguel; Licensed MIT */(function(){var a,b,c,d,e,f=function(a,b){return function(){return a.apply(b,arguments)}},g=[].indexOf||function(a){for(var b=0,c=this.length;c>b;b++)if(b in this&&this[b]===a)return b;return-1};b=function(){function a(){}return a.prototype.extend=function(a,b){var c,d;for(c in b)d=b[c],null==a[c]&&(a[c]=d);return a},a.prototype.isMobile=function(a){return/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(a)},a.prototype.createEvent=function(a,b,c,d){var e;return null==b&&(b=!1),null==c&&(c=!1),null==d&&(d=null),null!=document.createEvent?(e=document.createEvent("CustomEvent"),e.initCustomEvent(a,b,c,d)):null!=document.createEventObject?(e=document.createEventObject(),e.eventType=a):e.eventName=a,e},a.prototype.emitEvent=function(a,b){return null!=a.dispatchEvent?a.dispatchEvent(b):b in(null!=a)?a[b]():"on"+b in(null!=a)?a["on"+b]():void 0},a.prototype.addEvent=function(a,b,c){return null!=a.addEventListener?a.addEventListener(b,c,!1):null!=a.attachEvent?a.attachEvent("on"+b,c):a[b]=c},a.prototype.removeEvent=function(a,b,c){return null!=a.removeEventListener?a.removeEventListener(b,c,!1):null!=a.detachEvent?a.detachEvent("on"+b,c):delete a[b]},a.prototype.innerHeight=function(){return"innerHeight"in window?window.innerHeight:document.documentElement.clientHeight},a}(),c=this.WeakMap||this.MozWeakMap||(c=function(){function a(){this.keys=[],this.values=[]}return a.prototype.get=function(a){var b,c,d,e,f;for(f=this.keys,b=d=0,e=f.length;e>d;b=++d)if(c=f[b],c===a)return this.values[b]},a.prototype.set=function(a,b){var c,d,e,f,g;for(g=this.keys,c=e=0,f=g.length;f>e;c=++e)if(d=g[c],d===a)return void(this.values[c]=b);return this.keys.push(a),this.values.push(b)},a}()),a=this.MutationObserver||this.WebkitMutationObserver||this.MozMutationObserver||(a=function(){function a(){"undefined"!=typeof console&&null!==console&&console.warn("MutationObserver is not supported by your browser."),"undefined"!=typeof console&&null!==console&&console.warn("WOW.js cannot detect dom mutations, please call .sync() after loading new content.")}return a.notSupported=!0,a.prototype.observe=function(){},a}()),d=this.getComputedStyle||function(a){return this.getPropertyValue=function(b){var c;return"float"===b&&(b="styleFloat"),e.test(b)&&b.replace(e,function(a,b){return b.toUpperCase()}),(null!=(c=a.currentStyle)?c[b]:void 0)||null},this},e=/(\-([a-z]){1})/g,this.WOW=function(){function e(a){null==a&&(a={}),this.scrollCallback=f(this.scrollCallback,this),this.scrollHandler=f(this.scrollHandler,this),this.resetAnimation=f(this.resetAnimation,this),this.start=f(this.start,this),this.scrolled=!0,this.config=this.util().extend(a,this.defaults),this.animationNameCache=new c,this.wowEvent=this.util().createEvent(this.config.boxClass)}return e.prototype.defaults={boxClass:"wow",animateClass:"animated",offset:0,mobile:!0,live:!0,callback:null},e.prototype.init=function(){var a;return this.element=window.document.documentElement,"interactive"===(a=document.readyState)||"complete"===a?this.start():this.util().addEvent(document,"DOMContentLoaded",this.start),this.finished=[]},e.prototype.start=function(){var b,c,d,e;if(this.stopped=!1,this.boxes=function(){var a,c,d,e;for(d=this.element.querySelectorAll("."+this.config.boxClass),e=[],a=0,c=d.length;c>a;a++)b=d[a],e.push(b);return e}.call(this),this.all=function(){var a,c,d,e;for(d=this.boxes,e=[],a=0,c=d.length;c>a;a++)b=d[a],e.push(b);return e}.call(this),this.boxes.length)if(this.disabled())this.resetStyle();else for(e=this.boxes,c=0,d=e.length;d>c;c++)b=e[c],this.applyStyle(b,!0);return this.disabled()||(this.util().addEvent(window,"scroll",this.scrollHandler),this.util().addEvent(window,"resize",this.scrollHandler),this.interval=setInterval(this.scrollCallback,50)),this.config.live?new a(function(a){return function(b){var c,d,e,f,g;for(g=[],c=0,d=b.length;d>c;c++)f=b[c],g.push(function(){var a,b,c,d;for(c=f.addedNodes||[],d=[],a=0,b=c.length;b>a;a++)e=c[a],d.push(this.doSync(e));return d}.call(a));return g}}(this)).observe(document.body,{childList:!0,subtree:!0}):void 0},e.prototype.stop=function(){return this.stopped=!0,this.util().removeEvent(window,"scroll",this.scrollHandler),this.util().removeEvent(window,"resize",this.scrollHandler),null!=this.interval?clearInterval(this.interval):void 0},e.prototype.sync=function(){return a.notSupported?this.doSync(this.element):void 0},e.prototype.doSync=function(a){var b,c,d,e,f;if(null==a&&(a=this.element),1===a.nodeType){for(a=a.parentNode||a,e=a.querySelectorAll("."+this.config.boxClass),f=[],c=0,d=e.length;d>c;c++)b=e[c],g.call(this.all,b)<0?(this.boxes.push(b),this.all.push(b),this.stopped||this.disabled()?this.resetStyle():this.applyStyle(b,!0),f.push(this.scrolled=!0)):f.push(void 0);return f}},e.prototype.show=function(a){return this.applyStyle(a),a.className=a.className+" "+this.config.animateClass,null!=this.config.callback&&this.config.callback(a),this.util().emitEvent(a,this.wowEvent),this.util().addEvent(a,"animationend",this.resetAnimation),this.util().addEvent(a,"oanimationend",this.resetAnimation),this.util().addEvent(a,"webkitAnimationEnd",this.resetAnimation),this.util().addEvent(a,"MSAnimationEnd",this.resetAnimation),a},e.prototype.applyStyle=function(a,b){var c,d,e;return d=a.getAttribute("data-wow-duration"),c=a.getAttribute("data-wow-delay"),e=a.getAttribute("data-wow-iteration"),this.animate(function(f){return function(){return f.customStyle(a,b,d,c,e)}}(this))},e.prototype.animate=function(){return"requestAnimationFrame"in window?function(a){return window.requestAnimationFrame(a)}:function(a){return a()}}(),e.prototype.resetStyle=function(){var a,b,c,d,e;for(d=this.boxes,e=[],b=0,c=d.length;c>b;b++)a=d[b],e.push(a.style.visibility="visible");return e},e.prototype.resetAnimation=function(a){var b;return a.type.toLowerCase().indexOf("animationend")>=0?(b=a.target||a.srcElement,b.className=b.className.replace(this.config.animateClass,"").trim()):void 0},e.prototype.customStyle=function(a,b,c,d,e){return b&&this.cacheAnimationName(a),a.style.visibility=b?"hidden":"visible",c&&this.vendorSet(a.style,{animationDuration:c}),d&&this.vendorSet(a.style,{animationDelay:d}),e&&this.vendorSet(a.style,{animationIterationCount:e}),this.vendorSet(a.style,{animationName:b?"none":this.cachedAnimationName(a)}),a},e.prototype.vendors=["moz","webkit"],e.prototype.vendorSet=function(a,b){var c,d,e,f;d=[];for(c in b)e=b[c],a[""+c]=e,d.push(function(){var b,d,g,h;for(g=this.vendors,h=[],b=0,d=g.length;d>b;b++)f=g[b],h.push(a[""+f+c.charAt(0).toUpperCase()+c.substr(1)]=e);return h}.call(this));return d},e.prototype.vendorCSS=function(a,b){var c,e,f,g,h,i;for(h=d(a),g=h.getPropertyCSSValue(b),f=this.vendors,c=0,e=f.length;e>c;c++)i=f[c],g=g||h.getPropertyCSSValue("-"+i+"-"+b);return g},e.prototype.animationName=function(a){var b;try{b=this.vendorCSS(a,"animation-name").cssText}catch(c){b=d(a).getPropertyValue("animation-name")}return"none"===b?"":b},e.prototype.cacheAnimationName=function(a){return this.animationNameCache.set(a,this.animationName(a))},e.prototype.cachedAnimationName=function(a){return this.animationNameCache.get(a)},e.prototype.scrollHandler=function(){return this.scrolled=!0},e.prototype.scrollCallback=function(){var a;return!this.scrolled||(this.scrolled=!1,this.boxes=function(){var b,c,d,e;for(d=this.boxes,e=[],b=0,c=d.length;c>b;b++)a=d[b],a&&(this.isVisible(a)?this.show(a):e.push(a));return e}.call(this),this.boxes.length||this.config.live)?void 0:this.stop()},e.prototype.offsetTop=function(a){for(var b;void 0===a.offsetTop;)a=a.parentNode;for(b=a.offsetTop;a=a.offsetParent;)b+=a.offsetTop;return b},e.prototype.isVisible=function(a){var b,c,d,e,f;return c=a.getAttribute("data-wow-offset")||this.config.offset,f=window.pageYOffset,e=f+Math.min(this.element.clientHeight,this.util().innerHeight())-c,d=this.offsetTop(a),b=d+a.clientHeight,e>=d&&b>=f},e.prototype.util=function(){return null!=this._util?this._util:this._util=new b},e.prototype.disabled=function(){return!this.config.mobile&&this.util().isMobile(navigator.userAgent)},e}()}).call(this);


//---- PARALLAX ---//
/*
Plugin: jQuery Parallax
Version 1.1.3
Author: Ian Lunn
Twitter: @IanLunn
Author URL: http://www.ianlunn.co.uk/
Plugin URL: http://www.ianlunn.co.uk/plugins/jquery-parallax/

Dual licensed under the MIT and GPL licenses:
http://www.opensource.org/licenses/mit-license.php
http://www.gnu.org/licenses/gpl.html
*/

(function($) {
    var $window = $(window);
    var windowHeight = $window.height();

    $window.resize(function() {
        windowHeight = $window.height();
    });

    $.fn.parallax = function(xpos, speedFactor, outerHeight) {
        var $this = $(this);
        var getHeight;
        var firstTop;
        var paddingTop = 0;

        //get the starting position of each element to have parallax applied to it	
        function update() {

            $this.each(function() {

                firstTop = $this.offset().top;
            });

            if (outerHeight) {
                getHeight = function(jqo) {
                    return jqo.outerHeight(true);
                };
            } else {
                getHeight = function(jqo) {
                    return jqo.height();
                };
            }

            // setup defaults if arguments aren't specified
            if (arguments.length < 1 || xpos === null) xpos = "50%";
            if (arguments.length < 2 || speedFactor === null) speedFactor = 0.5;
            if (arguments.length < 3 || outerHeight === null) outerHeight = true;

            // function to be called whenever the window is scrolled or resized

            var pos = $window.scrollTop();

            $this.each(function() {
                var $element = $(this);
                var top = $element.offset().top;
                var height = getHeight($element);

                // Check if totally above or totally below viewport
                if (top + height < pos || top > pos + windowHeight) {
                    return;
                }

                $this.css('backgroundPosition', xpos + " " + Math.round((firstTop - pos) * speedFactor) + "px");

            });
        }

        $window.bind('scroll', update).resize(update);
        update();
    };
})(jQuery);


// =============================================
// Parallax Init
// =============================================

jQuery(window).bind('load', function() {
    parallaxInit();
});

function parallaxInit() {
    jQuery('.parallax').each(function() {
        jQuery(this).parallax("30%", 0.3);
    });
}

function parallax() {
    var scrollPosition = $(window).scrollTop();
    $('#parallax').css('top', (0 - (scrollPosition * 0.3)) + 'px'); // bg image moves at 30% of scrolling speed
    $('#hero').css('opacity', ((100 - scrollPosition / 2) * 0.01));
}


	jQuery(document).ready(function($){

		/*	Parallax
		================================================== */

		$(window).on('scroll', function(e) {
			parallax();
		});

		/*	Wow Anim
		================================================== */		
		new WOW().init();	

		/*	Local Scroll
		================================================== */

		jQuery('.navbar').localScroll({
			offset: -80,
			duration: 500
		});

		/*	Active Menu
		================================================== */

		jQuery(function() {
			var sections = jQuery('section');
			var navigation_links = jQuery('nav a');
			sections.waypoint({
				handler: function(direction) {
					var active_section;
					active_section = jQuery(this);
					if (direction === "up") active_section = active_section.prev();
					var active_link = jQuery('nav a[href="#' + active_section.attr("id") + '"]');
					navigation_links.parent().removeClass("active");
					active_link.parent().addClass("active");
					active_section.addClass("active-section");
				},
				offset: '35%'
			});
		});

		/*	Gallery
		================================================== */		
			$('#gallery').magnificPopup({
				delegate: 'a',
				type: 'image',
				tLoading: 'Loading image #%curr%...',
				mainClass: 'mfp-img-mobile',
				gallery: {
					enabled: true,
					navigateByImgClick: true,
					preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
				},
				image: {
					tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
					titleSrc: function(item) {
						return item.el.attr('title') + '<small></small>';
					}
				}
			});		


		/*	Bootstrap Carousel
		================================================== */

		jQuery('.carousel').carousel()


	});
	
