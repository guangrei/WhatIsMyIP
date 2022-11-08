# -*-coding:utf8;-*-
import droid
import requests


def getGeoIp(ip):
    try:
        r = requests.get('https://ipapi.co/'+ip+'/json/').json()
        return "Network: {network} ({org})\nLocation: {city}, {region}, {country_name} ({country_code})".format(**r)
    except BaseException as e:
        droid.toast(str(e))
        return "Can't fetch geoip information!"


def local_ip():
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except BaseException as e:
        s.close()
        droid.toast(str(e))
        return "127.0.0.1"


def public_ip():
    try:
        r = requests.get('https://api.ipify.org?format=json').json()
        ip = r['ip']
        geoip = getGeoIp(ip)
        return ip, geoip
    except BaseException as e:
        droid.toast(str(e))
        return "127.0.0.1", "Can't fetch geoip information!"


if __name__ == '__main__':
    droid.sprogress_show("What is My IP ?", "please wait ..")
    local = local_ip()
    public, publicgp = public_ip()
    result = "1. local ip {0}\n\n2. public ip {1}\n\n{2}".format(
        local, public, publicgp)
    droid.sprogress_hide()
    p = droid.alert("What is My IP ?", result,
                    button=("close", "copy 2", "copy 1"))
    if p == 'copy 1':
        droid.copy(str(local))
    elif p == 'copy 2':
        droid.copy(str(public))
