# -*- coding:utf-8 -*-
import cookielib, urllib, urllib2, socket


class HttpClient:
    cookie = cookielib.CookieJar()
    cookieHandler = urllib2.HTTPCookieProcessor(cookie)
    proxyHandler = urllib2.ProxyHandler(proxies={'http': 'localhost:8888'})
    httpHandler = urllib2.HTTPHandler(debuglevel=0)  # 打印调试信息
    httpsHandler = urllib2.HTTPSHandler(debuglevel=0)  # 打印调试信息
    __req = urllib2.build_opener(cookieHandler, httpHandler, httpsHandler)
    __req.addheaders = [
        ('Accept', 'application/javascript, */*;q=0.8'),
        ('User-Agent',
         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36"),
        ('Referer', 'http://d.web2.qq.com/proxy.html?v=20130916001&callback=1&id=2')
    ]
    urllib2.install_opener(__req)

    def Get(self, url, refer=None):
        try:
            req = urllib2.Request(url)
            if not (refer is None):
                req.add_header('Referer', refer)
            return urllib2.urlopen(req).read()
        except urllib2.HTTPError, e:
            return e.read()

    def Post(self, url, data, refer=None):
        try:
            req = urllib2.Request(url, urllib.urlencode(data))
            if not (refer is None):
                req.add_header('Referer', refer)
            return urllib2.urlopen(req, timeout=180).read()
        except urllib2.HTTPError, e:
            return e.read()

    def Download(self, url, file):
        output = open(file, 'wb')
        output.write(urllib2.urlopen(url).read())
        output.close()

    #  def urlencode(self, data):
    #    return urllib.quote(data)

    def getCookie(self, key):
        for c in self.cookie:
            if c.name == key:
                return c.value
        return ''

    def setCookie(self, key, val, domain):
        ck = cookielib.Cookie(version=0, name=key, value=val, port=None, port_specified=False, domain=domain,
                              domain_specified=False, domain_initial_dot=False, path='/', path_specified=True,
                              secure=False, expires=None, discard=True, comment=None, comment_url=None,
                              rest={'HttpOnly': None}, rfc2109=False)
        self.cookie.set_cookie(ck)
        # self.__cookie.clear() clean cookie
        # vim : tabstop=2 shiftwidth=2 softtabstop=2 expandtab
