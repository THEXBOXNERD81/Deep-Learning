{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello\n"
     ]
    }
   ],
   "source": [
    "print('Hello')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pt\n",
    "import numpy as np\n",
    "import requests\n",
    "from bs4 import BeautifulSoup as Bsoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "def fetch_website_content(url):\n",
    "    try:\n",
    "        response = requests.get(url)\n",
    "        # Check if the request was successful (status code 200)\n",
    "        if response.status_code == 200:\n",
    "            return response.content\n",
    "        else:\n",
    "            print(\n",
    "                f\"Failed to fetch website. Status code: {response.status_code}\")\n",
    "    except requests.exceptions.RequestException as e:\n",
    "        print(f\"An error occurred: {e}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Replace \"https://www.example.com\" with the website URL you want to call\n",
    "website_url = \"https://www.windy.com/sv/-CAPE-index-cape?cape,55.930,13.239,10,m:fdTagxj\"\n",
    "website_content = fetch_website_content(website_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html>\n",
      "<html id=\"device-mobile\" lang=\"en\"><head><title>Windy: Wind map &amp; weather forecast</title><base href=\"/\"/><link href=\"https://www.windy.com\" rel=\"canonical\"/><meta content=\"text/html; charset=utf-8\" http-equiv=\"Content-Type\"/><meta content=\"width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover\" name=\"viewport\"/><link href=\"v/39.1.3.ind.ea0e/index.css\" rel=\"stylesheet\" type=\"text/css\"/><script>window.W={version:\"39.1.3\",assets:\"39.1.3.ind.ea0e\",target:\"index\",build:\"2023-07-07, 09:03\",startTs:Date.now(),detectedDevice:\"mobile\"};try{!function(){var e=window.screen.width,t=window.screen.height,i=Math.min(e,t),e=Math.max(e,t),t=/iPhone|iPod|iPad|ios|android/i.test(window.navigator.userAgent),n=\"ontouchstart\"in window||0<navigator.maxTouchPoints,e=\"mobile\"===window.W.target?i<=500?\"mobile\":\"tablet\":e<=600||e<=960&&i<=600||i<=500&&t?\"mobile\":(e<=1024||i<=1080)&&t&&n?\"tablet\":\"desktop\";document.documentElement.id=\"device-\"+e,document.documentElement.className=\"target-index\",window.W.detectedDevice=e}()}catch(e){}</script><meta content='{\"v\":\"2.3\",\"ref\":\"2023-07-20T00:00:00Z\",\"update\":\"2023-07-20T07:27:06Z\",\"dst\":[[3,3,90],[3,93,144],[6,150,240]],\"info\":\"2023061206\",\"premium\":true,\"primary_refs\":[0,12],\"secondary_refs\":[6,18],\"secondary_ref_length\":90}' name=\"minifest-ecmwf-hres\"/><meta content='{\"v\":\"2.3\",\"ref\":\"2023-07-20T06:00:00Z\",\"update\":\"2023-07-20T12:47:06Z\",\"dst\":[[1,1,90],[3,93,138],[6,144,234]],\"info\":\"2023061206\",\"premium\":true,\"primary_refs\":[0,12],\"secondary_refs\":[6,18],\"secondary_ref_length\":90}' name=\"minifest-ecmwf-hres1h\"/><meta content=\"ecmwf\" name=\"model\"/><meta content=\"188.148.106.190,56.0449,12.6920,SE,Helsingborg\" name=\"geoip\"/><meta content=\"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2ODk4NTg4MzksImluZiI6eyJpcCI6IjE4OC4xNDguMTA2LjE5MCIsInVhIjoicHl0aG9uLXJlcXVlc3RzXC8yLjI4LjEifSwiZXhwIjoxNjkwMDMxNjM5fQ.qSDBasFXcd_IVgOaZEbr8teGrWPGde8JQitWC44tAT4\" name=\"token\"/><script src=\"js/leaflet140_patched_tileLayer.v17.js\"></script><script>Array.prototype.includes&&Object.assign&&window.Promise||document.write('<script src=\"js/polyfills.v13.js\"><\\/script>')</script><script async=\"\" src=\"v/39.1.3.ind.ea0e/index.js\"></script><link href=\"https://node.windy.com\" rel=\"dns-prefetch\"/><link href=\"https://account.windy.com\" rel=\"dns-prefetch\"/><link href=\"https://tiles.windy.com\" rel=\"dns-prefetch\"/><link href=\"https://ims.windy.com\" rel=\"dns-prefetch\"/><link href=\"https://ims-s.windy.com\" rel=\"dns-prefetch\"/><link href=\"https://img.windy.com\" rel=\"dns-prefetch\"/><meta content=\"Weather radar, wind and waves forecast for kiters, surfers, paragliders, pilots, sailors and anyone else. Worldwide animated weather map, with easy to use layers and precise spot forecast. METAR, TAF and NOTAMs for any airport in the World. SYNOP codes from weather stations and buoys. Forecast models ECMWF, GFS, NAM and NEMS\" name=\"description\"/><meta content=\"Windyty, Windytv, windy app, wind map, windfinder, windguru, wind forecast, weather forecast, GFS, ECMWF, NEMS, METAR, TAF\" name=\"keywords\"/><meta content=\"Windyty, SE\" name=\"author\"/><meta content=\"Windy.com\" name=\"application-name\"/><meta content=\"426030704216458\" property=\"fb:app_id\"/><meta content=\"Windy as forecasted\" property=\"og:title\"/><meta content=\"article\" property=\"og:type\"/><meta content=\"https://www.windy.com/img/socialshare3.jpg\" property=\"og:image\"/><meta content=\"800\" property=\"og:image:width\"/><meta content=\"373\" property=\"og:image:height\"/><meta content=\"https://www.windy.com/\" property=\"og:url\"/><meta content=\"Wind map and weather forecast\" property=\"og:description\"/><meta content=\"Windy.com/\" property=\"og:site_name\"/><meta content=\"\" property=\"article:published_time\"/><meta content=\"summary_large_image\" name=\"twitter:card\"/><meta content=\"Windy as forecasted\" name=\"twitter:title\"/><meta content=\"@windycom\" name=\"twitter:site\"/><meta content=\"@windycom\" name=\"twitter:creator\"/><meta content=\"https://www.windy.com/\" name=\"twitter:url\"/><meta content=\"Wind map and weather forecast\" name=\"twitter:description\"/><meta content=\"https://www.windy.com/img/socialshare3.jpg\" name=\"twitter:image\"/><link href=\"/favicon.ico\" rel=\"shortcut icon\"/><link href=\"img/favicons/apple-touch-icon-57x57.png\" rel=\"apple-touch-icon\" sizes=\"57x57\"/><link href=\"img/favicons/apple-touch-icon-114x114.png\" rel=\"apple-touch-icon\" sizes=\"114x114\"/><link href=\"img/favicons/apple-touch-icon-72x72.png\" rel=\"apple-touch-icon\" sizes=\"72x72\"/><link href=\"img/favicons/apple-touch-icon-144x144.png\" rel=\"apple-touch-icon\" sizes=\"144x144\"/><link href=\"img/favicons/apple-touch-icon-60x60.png\" rel=\"apple-touch-icon\" sizes=\"60x60\"/><link href=\"img/favicons/apple-touch-icon-120x120.png\" rel=\"apple-touch-icon\" sizes=\"120x120\"/><link href=\"img/favicons/apple-touch-icon-76x76.png\" rel=\"apple-touch-icon\" sizes=\"76x76\"/><link href=\"img/favicons/apple-touch-icon-152x152.png\" rel=\"apple-touch-icon\" sizes=\"152x152\"/><link href=\"img/favicons/apple-touch-icon-180x180.png\" rel=\"apple-touch-icon\" sizes=\"180x180\"/><meta content=\"#666666\" name=\"msapplication-TileColor\"/><meta content=\"img/favicons/mstile-144x144.png\" name=\"msapplication-TileImage\"/><meta content=\"img/favicons/browserconfig.xml\" name=\"msapplication-config\"/><link href=\"https://chrome.google.com/webstore/detail/kfboghlfmbkcjhddfklnbpobkajncacl\" rel=\"chrome-webstore-item\"/><meta content=\"app-id=1161387262\" name=\"apple-itunes-app\"/><meta content=\"yes\" name=\"apple-mobile-web-app-capable\"/><meta content=\"#9d0300\" name=\"theme-color\"/></head><body class=\"onweather\"><section id=\"map-container\" style=\"position: absolute; top: 0; bottom: 0; left: 0; right: 0; width: 100%; height: 100%;\"><div id=\"leaflet-map\" style=\"position: absolute; top: 0; bottom: 0; left: 0; right: 0; width: 100%; height: 100%; background-color: grey;\"></div><div id=\"picker-dot\"><svg viewbox=\"0 0 100 100\"><path d=\"M 25,50 L 0,50 M 75,50 L 100,50\" stroke-width=\"8\"></path><path d=\"M 50,25 L 50,0 M 50,75 L 50,100\" stroke-width=\"8\"></path><circle cx=\"50\" cy=\"50\" r=\"4\"></circle></svg></div></section><a class=\"mobilehide\" href=\"http://www.openstreetmap.org/copyright\" id=\"contrib\" target=\"_blank\">© OpenStreetMap contributors</a><section id=\"bottom-wrapper\"><nav id=\"mobile-menu\"><span data-icon=\"]\" id=\"icon-home\"></span><span data-do=\"bcast,openSearch\" data-icon=\"\"></span> <span data-do=\"rqstOpen,fav-layers\" data-icon=\"\" data-plugin=\"fav-layers\"></span> <span data-do=\"rqstOpen,favs\" data-icon=\"k\" id=\"mobile-avatar\"></span><div class=\"iconfont boxshadow bg-red\" data-do=\"rqstOpen,menu\" data-icon=\"d\" id=\"menu-burger\"><div id=\"menu-warning-badge\">!</div></div></nav><nav id=\"plugins-bottom\"></nav><div id=\"plugins-bellow-bottom\"></div><div class=\"metric-legend\" id=\"legend-mobile\"></div></section><nav class=\"shy left-border right-border\" id=\"plugins-bottom-desktop\"></nav><div class=\"mobilehide inlined\" data-icon-after=\"k\" data-t=\"DEVELOPED\" id=\"bottom-credits\"></div><span data-plugin=\"detail-rhpane\"></span><div class=\"top-border left-border right-border\" id=\"logo-wrapper\"><a class=\"clickable notap animated-windy-logo\" data-do=\"bcast,back2home\" id=\"logo\" target=\"_top\"><div class=\"w-sprite\"></div><img alt=\"Windy.com\" class=\"text\" src=\"img/logo201802/logo-text-windycom-white.svg\"/></a></div><a class=\"open-in-app top-border desktophide boxshadow\" data-do=\"bcast,openapp\" data-t=\"MENU_MOBILE\" id=\"open-in-app\"></a><div id=\"top-messages\"></div><div class=\"shy top-border right-border mobiletablethide\" id=\"rh-icons\"><div data-plugin=\"user-menu\" id=\"user\"></div><div id=\"login-and-premium\"><div class=\"premium-button size-s\" data-do=\"rqstOpen,subscription\" data-t=\"SUB_GO\"></div><div class=\"button login-button\" data-do=\"rqstOpen,login\" data-icon=\"p\" data-t=\"JUST_LOGIN\"></div></div></div><div class=\"shy\" id=\"plugins\"></div><div class=\"shy left-border top-border\" id=\"search\"><div id=\"search-weather-bg\"><div id=\"search-top-wrapper\"><div class=\"mobiletablethide tooltip-down\" data-do=\"rqstOpen,tools\" data-tooltipsrc=\"MENU\" id=\"menu-burger2\"><div class=\"iconfont clickable-size\">d</div></div><input autocapitalize=\"off\" autocomplete=\"off\" autocorrect=\"off\" data-placeholder=\"SEARCH\" id=\"q\" spellcheck=\"false\" type=\"text\"/><div class=\"mobiletablethide tooltip-down iconfont\" data-do=\"rqstOpen,share\" data-tooltipsrc=\"SHARE\" id=\"share\">F</div><div class=\"fav-lines shy\" id=\"fav\"><div class=\"fav-line fav-off iconfont clickable-size tooltip-down\" data-do=\"rqstOpen,fav-alert-menu\" data-tooltipsrc=\"D_FAVORITES\">m</div><div class=\"fav-line fav-on iconfont clickable-size tooltip-down\" data-do=\"rqstOpen,fav-alert-menu\" data-tooltipsrc=\"D_FAVORITES2\">k</div><span data-plugin=\"fav-alert-menu\"></span></div><div class=\"noselect shy iconfont\" id=\"search-my-loc\">j</div><div class=\"iconfont\" id=\"cancel-search\"></div></div><span data-plugin=\"hp-weather\"></span></div><div class=\"weather-box animation flex-container\" id=\"warnings\" style=\"display: none\"></div><div class=\"weather-box animation\" id=\"articles\" style=\"display: none\"></div><span data-plugin=\"search\"></span></div><div class=\"fullscreen bg-red\" id=\"unlegal-embed\" style=\"display: none;\"><a class=\"size-xxxl\" href=\"https://www.windy.com\" target=\"_top\">www.windy.com</a></div></body></html>\n"
     ]
    }
   ],
   "source": [
    "# Create a Beautiful Soup object with the website content\n",
    "soup = Bsoup(website_content, \"html.parser\")\n",
    "\n",
    "# Extract information from the parsed HTML\n",
    "# For example, let's say the website has a <title> tag\n",
    "website_title = soup.title.text\n",
    "\n",
    "# Print the title of the website\n",
    "#print(f\"Website Title: {website_title}\")\n",
    "print(soup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The span with class 'highlight' was not found.\n"
     ]
    }
   ],
   "source": [
    "# Using find() to locate the first span with the class \"highlight\"\n",
    "target_span = soup.find(\"big\", attrs={\"data-do\": \"changeMetric\"})\n",
    "\n",
    "# Check if the target_span is found and extract its text\n",
    "if target_span:\n",
    "    span_text = target_span.text\n",
    "    print(f\"Found span with class 'highlight': {span_text}\")\n",
    "else:\n",
    "    print(\"The span with class 'highlight' was not found.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
