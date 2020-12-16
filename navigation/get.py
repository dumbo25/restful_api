  [Restored contents truncated]
simple-fan.service                                                                           loaded active running   run fan when hot                                                                      
pi@rpiGarageOpener:~ $ systemctl status simple-fan.service -l
● simple-fan.service - run fan when hot
   Loaded: loaded (/lib/systemd/system/simple-fan.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2020-12-02 14:26:37 CST; 1min 5s ago
 Main PID: 2823 (python)
    Tasks: 1 (limit: 881)
   CGroup: /system.slice/simple-fan.service
           └─2823 /usr/bin/python /home/pi/simple-fan.py

Dec 02 14:26:37 rpiGarageOpener systemd[1]: Started run fan when hot.
pi@rpiGarageOpener:~ $ systemctl | grep running | grep simple-fan
simple-fan.service                                                                           loaded active running   run fan when hot                                                                      
pi@rpiGarageOpener:~ $ sudo journalctl -u simple-fan.service
-- Logs begin at Mon 2020-11-30 15:55:40 CST, end at Wed 2020-12-02 14:28:44 CST. --
Dec 02 14:20:00 rpiGarageOpener systemd[1]: /lib/systemd/system/simple-fan.service:9: Failed to parse service restart specifier, ignoring: Always
Dec 02 14:26:37 rpiGarageOpener systemd[1]: Started run fan when hot.
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ ls -l
total 136
drwxr-xr-x 3 pi   pi    4096 Nov 30 19:38 api
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:40 Bookshelf
-rw-r--r-- 1 pi   pi   10701 Nov 22 08:59 check_apache.html
-rw-r--r-- 1 pi   pi    1974 Nov 29 07:24 createDB.sh
-rw-r--r-- 1 pi   pi      24 Nov 27 17:13 dead.letter
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Desktop
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Documents
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Downloads
-rwxr-xr-x 1 root root   682 Nov 27 17:03 emailTry.py
-rw-r--r-- 1 pi   pi     727 Nov 30 14:18 getScripts2.sh
-rw-r--r-- 1 pi   pi     453 Nov 30 14:19 getScripts.sh
-rw-r--r-- 1 pi   pi     815 Nov 28 22:03 getWebsite.sh
-rwxr-xr-x 1 root root   178 Nov 26 16:19 hello.py
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Music
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Pictures
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Public
-rwxr-xr-x 1 root root   218 Nov 26 12:46 pushGarageRemote.py
-rwxr-xr-x 1 root root  1564 Nov 30 15:16 read.py
-rw-rw-rw- 1 pi   pi   21338 Dec  2 10:57 rpi-echo.log
-rw-r--r-- 1 root root   456 Nov 29 19:13 rpi-echo.service
-rwxr-xr-x 1 root root  3230 Nov 30 18:23 simple-fan.py
-rw-r--r-- 1 root root  3230 Dec  2 14:10 simple-fan.py.1
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Templates
-rw-r--r-- 1 pi   pi    1471 Nov 22 09:51 tls2.sh
-rw-r--r-- 1 root root  1224 Nov 22 09:33 tls.sh
-rwxr-xr-x 1 root root   972 Nov 22 08:24 unused_rpi.sh
drwxr-xr-x 2 pi   pi    4096 Aug 20 05:55 Videos
pi@rpiGarageOpener:~ $ sudo nano simple.fan.py
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo systemctl stop simple-fan.service
pi@rpiGarageOpener:~ $ sudo systemctl start simple-fan.service
pi@rpiGarageOpener:~ $ sudo journalctl -u simple-fan.service
-- Logs begin at Mon 2020-11-30 15:55:40 CST, end at Wed 2020-12-02 14:35:26 CST. --
Dec 02 14:20:00 rpiGarageOpener systemd[1]: /lib/systemd/system/simple-fan.service:9: Failed to parse service restart specifier, ignoring: Always
Dec 02 14:26:37 rpiGarageOpener systemd[1]: Started run fan when hot.
Dec 02 14:35:06 rpiGarageOpener systemd[1]: Stopping run fan when hot...
Dec 02 14:35:06 rpiGarageOpener systemd[1]: simple-fan.service: Main process exited, code=killed, status=15/TERM
Dec 02 14:35:06 rpiGarageOpener systemd[1]: simple-fan.service: Succeeded.
Dec 02 14:35:06 rpiGarageOpener systemd[1]: Stopped run fan when hot.
Dec 02 14:35:16 rpiGarageOpener systemd[1]: Started run fan when hot.
Dec 02 14:35:17 rpiGarageOpener python[3426]: /home/pi/simple-fan.py:86: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) 
Dec 02 14:35:17 rpiGarageOpener python[3426]:   GPIO.setup(GPIOfan, GPIO.OUT)
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ vcgencmd measure_temp
temp=31.5'C
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo systemctl stop simple-fan.service
pi@rpiGarageOpener:~ $ sudo systemctl start simple-fan.service
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 1 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo python simple-fan.py
simple-fan.py:86: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(GPIOfan, GPIO.OUT)
Temperature from vcgencmd: 32.6
Turning on fan = 26
Temperature from vcgencmd: 31.5
Turning on fan = 26
Temperature from vcgencmd: 32.0
Turning on fan = 26
Temperature from vcgencmd: 31.5
Turning on fan = 26
Temperature from vcgencmd: 31.5
Turning on fan = 26
Temperature from vcgencmd: 32.0
Turning on fan = 26
^CTraceback (most recent call last):
  File "simple-fan.py", line 112, in <module>
    sleep(10)
KeyboardInterrupt
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo python simple-fan.py
simple-fan.py:86: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(GPIOfan, GPIO.OUT)
Temperature from vcgencmd: 32.6
Turning on fan = 26
Temperature from vcgencmd: 32.0
Turning on fan = 26
^CTraceback (most recent call last):
  File "simple-fan.py", line 112, in <module>
    sleep(10)
KeyboardInterrupt
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 32 1
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 26 1
pi@rpiGarageOpener:~ $ gpio mode out 32
mode: Invalid mode: 32. Should be in/out/pwm/clock/up/down/tri
pi@rpiGarageOpener:~ $ gpio 32 mode out 
gpio: Unknown command: 32.
pi@rpiGarageOpener:~ $ gpio mode 32 out 
pi@rpiGarageOpener:~ $ gpio write 32 1
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio mode 26 out 
pi@rpiGarageOpener:~ $ gpio write 26 1
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 26 1
pi@rpiGarageOpener:~ $ gpio write 32 1
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 26 0
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ history | grep vg
  121  history | grep vg
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ vcgencmd measure_temp
temp=29.3'C
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ nano pushGarageRemote.py
pi@rpiGarageOpener:~ $ ls /usr/local/bin/*.py
/usr/local/bin/close.py   /usr/local/bin/fauxmo.py  /usr/local/bin/open.py      /usr/local/bin/sleep.py
/usr/local/bin/disarm.py  /usr/local/bin/mylog.py   /usr/local/bin/rpi-echo.py  /usr/local/bin/toggle.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/open.py 
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo python3 simple-fan.py
  File "simple-fan.py", line 99
    print 'Temperature from vcgencmd: {}'.format(temp)
                                        ^
SyntaxError: invalid syntax
pi@rpiGarageOpener:~ $ sudo python simple-fan.py
simple-fan.py:86: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(GPIOfan, GPIO.OUT, initial=GPIO.LOW)
Temperature from vcgencmd: 29.3
Turning on fan = 26 value = 1
Temperature from vcgencmd: 28.8
Turning on fan = 26 value = 1
Temperature from vcgencmd: 28.2
Turning on fan = 26 value = 1
Temperature from vcgencmd: 28.2
Turning on fan = 26 value = 1
^CTraceback (most recent call last):
  File "simple-fan.py", line 112, in <module>
    sleep(10)
KeyboardInterrupt
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ sudo python simple-fan.py
simple-fan.py:86: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(GPIOfan, GPIO.OUT, initial=GPIO.LOW)
Temperature from vcgencmd: 28.2
Turning on fan = 26 value = 1
Temperature from vcgencmd: 28.2
Turning on fan = 26 value = 1
Temperature from vcgencmd: 28.2
Turning on fan = 26 value = 1
Temperature from vcgencmd: 28.2
Turning on fan = 26 value = 1
^CTraceback (most recent call last):
  File "simple-fan.py", line 112, in <module>
    sleep(10)
KeyboardInterrupt
pi@rpiGarageOpener:~ $ gpio write 26 0
pi@rpiGarageOpener:~ $ sudo python simple-fan.py
simple-fan.py:86: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(GPIOfan, GPIO.OUT, initial=GPIO.LOW)
Temperature from vcgencmd: 29.9
Turning on fan = 26 value = 1
Temperature from vcgencmd: 29.3
Turning on fan = 26 value = 1
^CTraceback (most recent call last):
  File "simple-fan.py", line 112, in <module>
    sleep(10)
KeyboardInterrupt
pi@rpiGarageOpener:~ $ history | grep systemcctl
  137  history | grep systemcctl
pi@rpiGarageOpener:~ $ history | grep systemctl
   62  sudo systemctl daemon-reload
   63  sudo systemctl enable simple-fan.service
   64  systemctl list-unit-files | grep enabled | grep simple 
   65  $ systemctl | grep running | grep fan
   66  systemctl status simple-fan.service -l
   68  sudo systemctl daemon-reload
   69  sudo systemctl enable simple-fan.service
   70  systemctl list-unit-files | grep enabled | grep simple 
   71  $ systemctl | grep running | grep fan
   72  systemctl | grep running | grep fan
   73* systemctl | grep running | grep sim
   74  systemctl status simple-fan.service -l
   77  sudo systemctl daemon-reload
   78  sudo systemctl enable simple-fan.service
   79  sudo systemctl start simple-fan.service
   80  systemctl list-unit-files | grep enabled | grep simple 
   81  systemctl | grep running | grep fan
   82  systemctl status simple-fan.service -l
   83  systemctl | grep running | grep simple-fan
   89  sudo systemctl stop simple-fan.service
   90  sudo systemctl start simple-fan.service
   95  sudo systemctl stop simple-fan.service
   96  sudo systemctl start simple-fan.service
  138  history | grep systemctl
pi@rpiGarageOpener:~ $ sudo systemctl stop simple-fan.service
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ history | grep gpio
   43  gpio read 17
   44  which which gpio
   45  /usr/bin/gpio read 17
   97  gpio readall
  101  gpio readall
  104  gpio readall
  105  gpio write 32 1
  106  gpio readall
  107  gpio write 26 1
  108  gpio mode out 32
  109  gpio 32 mode out 
  110  gpio mode 32 out 
  111  gpio write 32 1
  112  gpio readall
  113  gpio mode 26 out 
  114  gpio write 26 1
  115  gpio readall
  116  gpio write 26 1
  117  gpio write 32 1
  118  gpio readall
  119  gpio write 26 0
  120  gpio readall
  133  gpio readall
  135  gpio write 26 0
  140  gpio readall
  141  history | grep gpio
pi@rpiGarageOpener:~ $ gpio write 26 1
pi@rpiGarageOpener:~ $  gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 26 high
pi@rpiGarageOpener:~ $ gpio write 26 1
pi@rpiGarageOpener:~ $ gpio write 26 high
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 26 1
pi@rpiGarageOpener:~ $ gpio mode out 29
mode: Invalid mode: 29. Should be in/out/pwm/clock/up/down/tri
pi@rpiGarageOpener:~ $ gpio mode out 21
mode: Invalid mode: 21. Should be in/out/pwm/clock/up/down/tri
pi@rpiGarageOpener:~ $ gpio mode 29 out
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 0 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpi write 29 1
-bash: gpi: command not found
pi@rpiGarageOpener:~ $ gpio write 29 1
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 29 0
pi@rpiGarageOpener:~ $ gpio mode in 29
mode: Invalid mode: 29. Should be in/out/pwm/clock/up/down/tri
pi@rpiGarageOpener:~ $ gpio mode 29 in
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 29 0
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 21 0
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 21 1
pi@rpiGarageOpener:~ $ gpio mode 29 out
pi@rpiGarageOpener:~ $ gpio write 21 1
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 29 1
pi@rpiGarageOpener:~ $ gpio write 29 0
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 29 0
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | OUT  | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio mode 29 IN
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 29 0
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 29 0
pi@rpiGarageOpener:~ $ gpio readall
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
 |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
 |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
 |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 0 | IN   | TxD     | 15  | 14  |
 |     |     |      0v |      |   |  9 || 10 | 1 | IN   | RxD     | 16  | 15  |
 |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
 |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
 |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 1 | IN   | GPIO. 4 | 4   | 23  |
 |     |     |    3.3v |      |   | 17 || 18 | 1 | IN   | GPIO. 5 | 5   | 24  |
 |  10 |  12 |    MOSI |   IN | 0 | 19 || 20 |   |      | 0v      |     |     |
 |   9 |  13 |    MISO |   IN | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
 |  11 |  14 |    SCLK |   IN | 0 | 23 || 24 | 1 | IN   | CE0     | 10  | 8   |
 |     |     |      0v |      |   | 25 || 26 | 1 | IN   | CE1     | 11  | 7   |
 |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
 |   5 |  21 | GPIO.21 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 1 | OUT  | GPIO.26 | 26  | 12  |
 |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
 |  19 |  24 | GPIO.24 |   IN | 0 | 35 || 36 | 0 | IN   | GPIO.27 | 27  | 16  |
 |  26 |  25 | GPIO.25 |  OUT | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
 |     |     |      0v |      |   | 39 || 40 | 1 | IN   | GPIO.29 | 29  | 21  |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
 +-----+-----+---------+------+---+-Pi ZeroW-+---+------+---------+-----+-----+
pi@rpiGarageOpener:~ $ gpio write 29 1
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Wed Dec  2 14:10:15 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ history
    1  which php
    2  sudo apt install --dry-run php7.4
    3  sudo apt install  php7.3
    4  sudo apt install --dry-run php7.4-sqlite3
    5  sudo apt install --dry-run php7.3-sqlite3
    6  sudo apt install  php7.3 php7.3-sqlite3
    7  nano createDB.sh
    8  sudo bash createDB.sh
    9  nano createDB.sh
   10  sudo bash createDB.sh
   11  nano createDB.sh
   12  sudo bash createDB.sh
   13  nano createDB.sh
   14  sudo bash createDB.sh
   15  nano createDB.sh
   16  sudo bash createDB.sh
   17  nano createDB.sh
   18  sudo bash createDB.sh
   19  nano createDB.sh
   20  sudo bash createDB.sh
   21  nano createDB.sh
   22  sudo bash createDB.sh
   23  nano createDB.sh
   24  sqlite3 /var/www/db/garagedoor.db
   25  nano createDB.sh
   26  ls
   27  nano push_garage_opener.py
   28  mv push_garage_opener.py pushGarageRemote.py
   29  nano createDB.sh
   30  wget "https://raw.githubusercontent.com/dumbo25/garageDoorOpener2/main/garage.sh"
   31  ls -l
   32  ls /usr/local/bin
   33  chmod UG+x garage.sh
   34  chmod ug+x garage.sh
   35  ls -l
   36  mv garage.sh /usr/local/bin/garage.sh
   37  sudo mv garage.sh /usr/local/bin/garage.sh
   38  ls /usr/local/bin
   39  ls -l /usr/local/bin
   40  nano /var/www/db/garage.sh
   41  nano /usr/local/bin/garage.sh
   42  ls
   43  gpio read 17
   44  which which gpio
   45  /usr/bin/gpio read 17
   46  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   47  sudo apt-get update -y
   48  sudo apt-get upgrade -y
   49  sudo nano /etc/ssmtp/ssmtp.conf
   50  sudo nano /etc/ssmtp/revaliases
   51  sudo chmod og+x /etc/ssmtp/ssmtp.conf
   52  nano emailTry.py
   53  python emailTry.py
   54  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   55  history
pi@rpiGarageOpener:~ $ history | grep service
   56  history | grep service
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Thu Dec  3 08:04:40 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/Simple-fna.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/simple-fan.py
pi@rpiGarageOpener:~ $ ls /usr/local/bin
close.py  disarm.py  fauxmo.py  fauxmo.pyc  garage.sh  mylog.py  mylog.pyc  open.py  rpi-echo.py  sleep.py  toggle.py
pi@rpiGarageOpener:~ $ sudo nano /lib/systemd/system/simple-fan.service
pi@rpiGarageOpener:~ $ nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ ls -l *.py
-rwxr-xr-x 1 root root  682 Nov 27 17:03 emailTry.py
-rwxr-xr-x 1 root root  178 Nov 26 16:19 hello.py
-rwxr-xr-x 1 root root  218 Nov 26 12:46 pushGarageRemote.py
-rwxr-xr-x 1 root root 1564 Nov 30 15:16 read.py
-rwxr-xr-x 1 root root 2813 Dec  3 10:28 simple-fan.py
pi@rpiGarageOpener:~ $ sudo chown pi:pi simple-fan.py
pi@rpiGarageOpener:~ $ ls -l *.py
-rwxr-xr-x 1 root root  682 Nov 27 17:03 emailTry.py
-rwxr-xr-x 1 root root  178 Nov 26 16:19 hello.py
-rwxr-xr-x 1 root root  218 Nov 26 12:46 pushGarageRemote.py
-rwxr-xr-x 1 root root 1564 Nov 30 15:16 read.py
-rwxr-xr-x 1 pi   pi   2813 Dec  3 10:28 simple-fan.py
pi@rpiGarageOpener:~ $ history | grep stop
   64  history | grep stop
pi@rpiGarageOpener:~ $ sudo systemctl start stop-fan.service
Failed to start stop-fan.service: Unit stop-fan.service not found.
pi@rpiGarageOpener:~ $ sudo python simple-fan.py
^CTraceback (most recent call last):
  File "simple-fan.py", line 102, in <module>
    sleep(10)
KeyboardInterrupt
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ sudo python simple-fan.py
simple-fan.py:86: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(Fan, GPIO.OUT)
^CTraceback (most recent call last):
  File "simple-fan.py", line 105, in <module>
    sleep(10)
KeyboardInterrupt
pi@rpiGarageOpener:~ $ sudo nano simple-fan.py
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ udo shutdown -h 0
-bash: udo: command not found
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Thu Dec  3 10:23:07 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ sudo shutdown -h 0
Shutdown scheduled for Fri 2020-12-04 07:26:34 CST, use 'shutdown -c' to cancel.
pi@rpiGarageOpener:~ $ Connection to rpigarageopener.local closed by remote host.
Connection to rpigarageopener.local closed.
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec  4 07:27:28 2020
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ do shutdown -h 0
-bash: syntax error near unexpected token `do'
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec  4 11:26:46 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ sudo shutdown -h 0
Shutdown scheduled for Fri 2020-12-04 15:43:32 CST, use 'shutdown -c' to cancel.
pi@rpiGarageOpener:~ $ Connection to rpigarageopener.local closed by remote host.
Connection to rpigarageopener.local closed.
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec  4 15:44:22 2020
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ls
Applications		api.json		onOff.py
Creative Cloud Files	api.png			onOff.service
Desktop			ca-security.cer		rest_client.py
Documents		client.crt		rest_server.py
Downloads		client.key		rpi-echo.py
Justinmind		client.p12		rpi-echo.service
Library			fauxmo.py		server.crt
Movies			favicon.ico		server.key
Music			favicon.png		wemo-info.nse
Pictures		iCloud Drive (Archive)
Public			mylog.py
Jeffs-MBP:~ jeff$ pwd
/Users/jeff
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec  4 16:38:04 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ ls
api                Downloads       Pictures             simple-fan.py.1
Bookshelf          emailTry.py     Public               Templates
check_apache.html  getScripts2.sh  pushGarageRemote.py  tls2.sh
createDB.sh        getScripts.sh   read.py              tls.sh
dead.letter        getWebsite.sh   rpi-echo.log         unused_rpi.sh
Desktop            hello.py        rpi-echo.service     Videos
Documents          Music           simple-fan.py
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.py  server.crt
client.key  restful_api  server_cron.sh  server.key
pi@rpiGarageOpener:~/api $ $ python3 rest_server.py
-bash: $: command not found
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.py  server.crt
client.key  restful_api  server_cron.sh  server.key
pi@rpiGarageOpener:~/api $ ls ..
api                Downloads       Pictures             simple-fan.py.1
Bookshelf          emailTry.py     Public               Templates
check_apache.html  getScripts2.sh  pushGarageRemote.py  tls2.sh
createDB.sh        getScripts.sh   read.py              tls.sh
dead.letter        getWebsite.sh   rpi-echo.log         unused_rpi.sh
Desktop            hello.py        rpi-echo.service     Videos
Documents          Music           simple-fan.py
pi@rpiGarageOpener:~/api $ ls ../*.py
../emailTry.py  ../pushGarageRemote.py  ../simple-fan.py
../hello.py     ../read.py
pi@rpiGarageOpener:~/api $ ls *.py
rest_server.py
pi@rpiGarageOpener:~/api $ $ python3 rest_server.py
-bash: $: command not found
pi@rpiGarageOpener:~/api $ python3 rest_server.py
Traceback (most recent call last):
  File "rest_server.py", line 128, in <module>
    import distro
ModuleNotFoundError: No module named 'distro'
pi@rpiGarageOpener:~/api $ python rest_server.py
Traceback (most recent call last):
  File "rest_server.py", line 128, in <module>
    import distro
ImportError: No module named distro
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.py  server.crt
client.key  restful_api  server_cron.sh  server.key
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python
Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
[GCC 8.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import distro
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named distro
>>> exit()
pi@rpiGarageOpener:~/api $ pip3 install distro
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting distro
  Downloading https://files.pythonhosted.org/packages/25/b7/b3c4270a11414cb22c6352ebc7a83aaa3712043be29daa05018fd5a5c956/distro-1.5.0-py2.py3-none-any.whl
Installing collected packages: distro
  The script distro is installed in '/home/pi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed distro-1.5.0
pi@rpiGarageOpener:~/api $ python rest_server.py
Traceback (most recent call last):
  File "rest_server.py", line 128, in <module>
    import distro
ImportError: No module named distro
pi@rpiGarageOpener:~/api $ pip install distro
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting distro
  Using cached https://files.pythonhosted.org/packages/25/b7/b3c4270a11414cb22c6352ebc7a83aaa3712043be29daa05018fd5a5c956/distro-1.5.0-py2.py3-none-any.whl
Installing collected packages: distro
  The script distro is installed in '/home/pi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed distro-1.5.0
pi@rpiGarageOpener:~/api $ python rest_server.py
Traceback (most recent call last):
  File "rest_server.py", line 129, in <module>
    from http.server import BaseHTTPRequestHandler, HTTPServer
ImportError: No module named http.server
pi@rpiGarageOpener:~/api $ python3 rest_server.py

^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server_cron.sh  server.key
client.key  restful_api  rest_server.py   server.crt
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/05 20:10:58 - Starting REST server
2020/12/05 20:10:58 - Command line arguments:
2020/12/05 20:10:58 -   Input file  = 
2020/12/05 20:10:58 -   Log file = /home/pi/api/rest_server.log
2020/12/05 20:10:58 -   Port = 9080
2020/12/05 20:10:58 -   Use cert = False
2020/12/05 20:10:58 -   Use HTTPS = False
2020/12/05 20:10:58 -   Use multithreading = False

2020/12/05 20:10:58 - Web Server:
2020/12/05 20:10:58 -   Server name = rpiGarageOpener
2020/12/05 20:10:58 -   Server IP = 127.0.1.1

2020/12/05 20:25:37 - Closing REST server
pi@rpiGarageOpener:~/api $ history | grep reset_server
   76  history | grep reset_server
pi@rpiGarageOpener:~/api $ $ python3 rest_server.py
-bash: $: command not found
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server_cron.sh  server.key
client.key  restful_api  rest_server.py   server.crt
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls /home/pi
api                Downloads       Pictures             simple-fan.py.1
Bookshelf          emailTry.py     Public               Templates
check_apache.html  getScripts2.sh  pushGarageRemote.py  tls2.sh
createDB.sh        getScripts.sh   read.py              tls.sh
dead.letter        getWebsite.sh   rpi-echo.log         unused_rpi.sh
Desktop            hello.py        rpi-echo.service     Videos
Documents          Music           simple-fan.py
pi@rpiGarageOpener:~/api $ ls /var/www
db  html
pi@rpiGarageOpener:~/api $ ls /var/www/html
css  GarageDoor.pdf  img  index2.html  index.php  old  schedule.php
pi@rpiGarageOpener:~/api $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sat Dec  5 15:30:29 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ lx *.py
-bash: lx: command not found
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ nano simple-fan.py
pi@rpiGarageOpener:~ $ history | grep systemctl
   58  history | grep systemctl
pi@rpiGarageOpener:~ $ sudo reboot
pi@rpiGarageOpener:~ $ Connection to rpigarageopener.local closed by remote host.
Connection to rpigarageopener.local closed.
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sun Dec  6 07:18:33 2020
pi@rpiGarageOpener:~ $ ls
api                Downloads       Pictures             simple-fan.py.1
Bookshelf          emailTry.py     Public               Templates
check_apache.html  getScripts2.sh  pushGarageRemote.py  tls2.sh
createDB.sh        getScripts.sh   read.py              tls.sh
dead.letter        getWebsite.sh   rpi-echo.log         unused_rpi.sh
Desktop            hello.py        rpi-echo.service     Videos
Documents          Music           simple-fan.py
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server_cron.sh  server.key
client.key  restful_api  rest_server.py   server.crt
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server_cron.sh  server.key
client.key  restful_api  rest_server.py   server.crt
pi@rpiGarageOpener:~/api $ scp pi@home-hub.local/home/pi/client.crt .
cp: cannot stat 'pi@home-hub.local/home/pi/client.crt': No such file or directory
pi@rpiGarageOpener:~/api $ scp pi@home-hub.local/home/pi/api/client.crt .
cp: cannot stat 'pi@home-hub.local/home/pi/api/client.crt': No such file or directory
pi@rpiGarageOpener:~/api $ hostname
rpiGarageOpener
pi@rpiGarageOpener:~/api $ scp pi@home-hub.local:/home/pi/api/client.crt .
ssh: Could not resolve hostname home-hub.local: Name or service not known
pi@rpiGarageOpener:~/api $ history | grep rest
   62  history | grep rest
pi@rpiGarageOpener:~/api $  python3 rest_server.py
^Cpi@rpiGarageOpener:~/api ls
client.crt  favicon.png  rest_server.log  server_cron.sh  server.key
client.key  restful_api  rest_server.py   server.crt
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/06 07:41:24 - Starting REST server
2020/12/06 07:41:24 - Command line arguments:
2020/12/06 07:41:24 -   Input file  = 
2020/12/06 07:41:24 -   Log file = /home/pi/api/rest_server.log
2020/12/06 07:41:24 -   Port = 9080
2020/12/06 07:41:24 -   Use cert = False
2020/12/06 07:41:24 -   Use HTTPS = False
2020/12/06 07:41:24 -   Use multithreading = False

2020/12/06 07:41:24 - Web Server:
2020/12/06 07:41:24 -   Server name = rpiGarageOpener
2020/12/06 07:41:24 -   Server IP = 127.0.1.1

2020/12/06 07:42:00 - Closing REST server
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server_cron.sh  server.key
client.key  restful_api  rest_server.py   server.crt
pi@rpiGarageOpener:~/api $ wget "https://raw.githubusercontent.com/dumbo25/restful_api/master/rest_server.py"
--2020-12-06 07:43:49--  https://raw.githubusercontent.com/dumbo25/restful_api/master/rest_server.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14842 (14K) [text/plain]
Saving to: ‘rest_server.py.1’

rest_server.py.1    100%[===================>]  14.49K  --.-KB/s    in 0.006s  

2020-12-06 07:43:49 (2.55 MB/s) - ‘rest_server.py.1’ saved [14842/14842]

pi@rpiGarageOpener:~/api $ wget https://github.com/dumbo25/restful_api/blob/master/favicon.png
--2020-12-06 07:44:02--  https://github.com/dumbo25/restful_api/blob/master/favicon.png
Resolving github.com (github.com)... 140.82.113.4
Connecting to github.com (github.com)|140.82.113.4|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘favicon.png.1’

favicon.png.1           [ <=>                ]  87.70K  --.-KB/s    in 0.1s    

2020-12-06 07:44:02 (640 KB/s) - ‘favicon.png.1’ saved [89807]

pi@rpiGarageOpener:~/api $ ls
client.crt   favicon.png.1    rest_server.py    server.crt
client.key   restful_api      rest_server.py.1  server.key
favicon.png  rest_server.log  server_cron.sh
pi@rpiGarageOpener:~/api $ git clone https://github.com/dumbo25/restful_api
fatal: destination path 'restful_api' already exists and is not an empty directory.
pi@rpiGarageOpener:~/api $ ls
client.crt   favicon.png.1    rest_server.py    server.crt
client.key   restful_api      rest_server.py.1  server.key
favicon.png  rest_server.log  server_cron.sh
pi@rpiGarageOpener:~/api $ ls restful_api
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api $ ls restful_api/server
cpu   get.backup  get.py   memory  reboot  uptime
disk  get.json    get.txt  os      time
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ sudo ufw disable
Firewall stopped and disabled on system startup
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ sudo systemctl stop apache2.service
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api ls
client.crt   favicon.png.1    rest_server.py    server.crt
client.key   restful_api      rest_server.py.1  server.key
favicon.png  rest_server.log  server_cron.sh
pi@rpiGarageOpener:~/api $ cat *.log
2020/12/06 07:52:44 - Starting REST server
2020/12/06 07:52:44 - Command line arguments:
2020/12/06 07:52:44 -   Input file  = 
2020/12/06 07:52:44 -   Log file = /home/pi/api/rest_server.log
2020/12/06 07:52:44 -   Port = 9080
2020/12/06 07:52:44 -   Use cert = False
2020/12/06 07:52:44 -   Use HTTPS = False
2020/12/06 07:52:44 -   Use multithreading = False

2020/12/06 07:52:44 - Web Server:
2020/12/06 07:52:44 -   Server name = rpiGarageOpener
2020/12/06 07:52:44 -   Server IP = 127.0.1.1

2020/12/06 07:53:20 - Closing REST server
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt   favicon.png.1    rest_server.py    server.crt
client.key   restful_api      rest_server.py.1  server.key
favicon.png  rest_server.log  server_cron.sh
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ \
> 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls restful_api
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api $ cd restful_api
pi@rpiGarageOpener:~/api/restful_api $ ls
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api/restful_api $ ls
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api/restful_api $ ls server
cpu   get.backup  get.py   memory  reboot  uptime
disk  get.json    get.txt  os      time
pi@rpiGarageOpener:~/api/restful_api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api/restful_api $ 
pi@rpiGarageOpener:~/api/restful_api $ ls
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api/restful_api $ cat ../*.log
2020/12/06 08:01:27 - Starting REST server
2020/12/06 08:01:27 - Command line arguments:
2020/12/06 08:01:27 -   Input file  = 
2020/12/06 08:01:27 -   Log file = /home/pi/api/rest_server.log
2020/12/06 08:01:27 -   Port = 9080
2020/12/06 08:01:27 -   Use cert = False
2020/12/06 08:01:27 -   Use HTTPS = False
2020/12/06 08:01:27 -   Use multithreading = False

2020/12/06 08:01:27 - Web Server:
2020/12/06 08:01:27 -   Server name = rpiGarageOpener
2020/12/06 08:01:27 -   Server IP = 127.0.1.1

2020/12/06 08:01:54 - Closing REST server
pi@rpiGarageOpener:~/api/restful_api $ python3 rest_server.py -msc
Traceback (most recent call last):
  File "rest_server.py", line 437, in <module>
    main(sys.argv)
  File "rest_server.py", line 414, in main
    context.load_cert_chain(certfile=ServerCertFile, keyfile=ServerKeyFile)
ssl.SSLError: [X509: KEY_VALUES_MISMATCH] key values mismatch (_ssl.c:3845)
pi@rpiGarageOpener:~/api/restful_api $ ls
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api/restful_api $ cd ..
pi@rpiGarageOpener:~/api $ ls
client.crt   favicon.png.1    rest_server.py    server.crt
client.key   restful_api      rest_server.py.1  server.key
favicon.png  rest_server.log  server_cron.sh
pi@rpiGarageOpener:~/api $ python3 rest_server.py -msc
Traceback (most recent call last):
  File "rest_server.py", line 437, in <module>
    main(sys.argv)
  File "rest_server.py", line 414, in main
    context.load_cert_chain(certfile=ServerCertFile, keyfile=ServerKeyFile)
ssl.SSLError: [X509: KEY_VALUES_MISMATCH] key values mismatch (_ssl.c:3845)
pi@rpiGarageOpener:~/api $ cd ..
pi@rpiGarageOpener:~ $ rm api
rm: cannot remove 'api': Is a directory
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ rm *
rm: cannot remove 'restful_api': Is a directory
pi@rpiGarageOpener:~/api $ rm * -R
rm: remove write-protected regular file 'restful_api/.git/objects/39/41389b10c2e39bb96149d584f21539cbfeb1d7'? ^C
pi@rpiGarageOpener:~/api $ sudo rm * -R
pi@rpiGarageOpener:~/api $ ls
pi@rpiGarageOpener:~/api $ cd
pi@rpiGarageOpener:~ $ pwd
/home/pi
pi@rpiGarageOpener:~ $ ls
api                Downloads       Pictures             simple-fan.py.1
Bookshelf          emailTry.py     Public               Templates
check_apache.html  getScripts2.sh  pushGarageRemote.py  tls2.sh
createDB.sh        getScripts.sh   read.py              tls.sh
dead.letter        getWebsite.sh   rpi-echo.log         unused_rpi.sh
Desktop            hello.py        rpi-echo.service     Videos
Documents          Music           simple-fan.py
pi@rpiGarageOpener:~ $ rm api -R
pi@rpiGarageOpener:~ $ ls
Bookshelf          emailTry.py     Public               Templates
check_apache.html  getScripts2.sh  pushGarageRemote.py  tls2.sh
createDB.sh        getScripts.sh   read.py              tls.sh
dead.letter        getWebsite.sh   rpi-echo.log         unused_rpi.sh
Desktop            hello.py        rpi-echo.service     Videos
Documents          Music           simple-fan.py
Downloads          Pictures        simple-fan.py.1
pi@rpiGarageOpener:~ $ mkdir api
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ git clone https://github.com/dumbo25/restful_api
Cloning into 'restful_api'...
remote: Enumerating objects: 72, done.
remote: Total 72 (delta 0), reused 0 (delta 0), pack-reused 72
Unpacking objects: 100% (72/72), done.
pi@rpiGarageOpener:~/api $ ls
restful_api
pi@rpiGarageOpener:~/api $ ls
restful_api
pi@rpiGarageOpener:~/api $ openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
Generating a RSA private key
................................................................^C
pi@rpiGarageOpener:~/api $ hostname
rpiGarageOpener
pi@rpiGarageOpener:~/api $ openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
Generating a RSA private key
....................++++
....++++
writing new private key to 'server.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:rpiGarageOpener.local
Email Address []:
pi@rpiGarageOpener:~/api $ ls
restful_api  server.crt  server.key
pi@rpiGarageOpener:~/api $ openssl req -x509 -newkey rsa:4096 -nodes -out client.crt -keyout client.key -days 365
Generating a RSA private key
.................................................++++
...............++++
writing new private key to 'client.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:rpiGarageOpener.local
Email Address []:
pi@rpiGarageOpener:~/api $ ls
client.crt  client.key  restful_api  server.crt  server.key
pi@rpiGarageOpener:~/api $ python3 rest_server.py -msc
python3: can't open file 'rest_server.py': [Errno 2] No such file or directory
pi@rpiGarageOpener:~/api $ ls
client.crt  client.key  restful_api  server.crt  server.key
pi@rpiGarageOpener:~/api $ ls restful_api
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api $ wget "https://raw.githubusercontent.com/dumbo25/restful_api/master/rest_server.py"
--2020-12-06 08:57:05--  https://raw.githubusercontent.com/dumbo25/restful_api/master/rest_server.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 14842 (14K) [text/plain]
Saving to: ‘rest_server.py’

rest_server.py      100%[===================>]  14.49K  --.-KB/s    in 0.005s  

2020-12-06 08:57:05 (2.70 MB/s) - ‘rest_server.py’ saved [14842/14842]

pi@rpiGarageOpener:~/api $ wget https://github.com/dumbo25/restful_api/blob/master/favicon.png
--2020-12-06 08:57:17--  https://github.com/dumbo25/restful_api/blob/master/favicon.png
Resolving github.com (github.com)... 140.82.114.4
Connecting to github.com (github.com)|140.82.114.4|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘favicon.png’

favicon.png             [ <=>                ]  87.71K  --.-KB/s    in 0.1s    

2020-12-06 08:57:17 (628 KB/s) - ‘favicon.png’ saved [89815]

pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server.crt
client.key  restful_api  rest_server.py   server.key
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server.crt
client.key  restful_api  rest_server.py   server.key
pi@rpiGarageOpener:~/api $ ls restful_api
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api $ ls restful_api/server
cpu   get.backup  get.py   memory  reboot  uptime
disk  get.json    get.txt  os      time
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ ls restful_api/server/cpu
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server.crt
client.key  restful_api  rest_server.py   server.key
pi@rpiGarageOpener:~/api $ history | grep stop
   76  sudo systemctl stop apache2.service
  132  history | grep stop
pi@rpiGarageOpener:~/api $ sudo systemctl stop apache2.service
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ python3 rest_server.py
_api/server/cpu^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server.crt
client.key  restful_api  rest_server.py   server.key
pi@rpiGarageOpener:~/api $ cat *.log
2020/12/06 09:05:44 - Starting REST server
2020/12/06 09:05:44 - Command line arguments:
2020/12/06 09:05:44 -   Input file  = 
2020/12/06 09:05:44 -   Log file = /home/pi/api/rest_server.log
2020/12/06 09:05:44 -   Port = 9080
2020/12/06 09:05:44 -   Use cert = False
2020/12/06 09:05:44 -   Use HTTPS = False
2020/12/06 09:05:44 -   Use multithreading = False

2020/12/06 09:05:44 - Web Server:
2020/12/06 09:05:44 -   Server name = rpiGarageOpener
2020/12/06 09:05:44 -   Server IP = 127.0.1.1

2020/12/06 09:10:01 - Closing REST server
pi@rpiGarageOpener:~/api $ ls
client.crt  favicon.png  rest_server.log  server.crt
client.key  restful_api  rest_server.py   server.key
pi@rpiGarageOpener:~/api $ cd restful_api
pi@rpiGarageOpener:~/api/restful_api $ ls
favicon.png  get.txt     README.md       server
get.json     navigation  rest_server.py  server_cron.sh
pi@rpiGarageOpener:~/api/restful_api $ mv * ../.
pi@rpiGarageOpener:~/api/restful_api $ ls
pi@rpiGarageOpener:~/api/restful_api $ cd ..
pi@rpiGarageOpener:~/api $ ls
client.crt   get.json    README.md        rest_server.py  server.crt
client.key   get.txt     restful_api      server          server.key
favicon.png  navigation  rest_server.log  server_cron.sh
pi@rpiGarageOpener:~/api $ cd restful_api
pi@rpiGarageOpener:~/api/restful_api $ ls
pi@rpiGarageOpener:~/api/restful_api $ cd ../server
pi@rpiGarageOpener:~/api/server $ ls
cpu   get.backup  get.py   memory  reboot  uptime
disk  get.json    get.txt  os      time
pi@rpiGarageOpener:~/api/server $ mv * ../.
pi@rpiGarageOpener:~/api/server $ ls
pi@rpiGarageOpener:~/api/server $ ls
pi@rpiGarageOpener:~/api/server $ cd ..
pi@rpiGarageOpener:~/api $ ls
client.crt   get.backup  navigation   rest_server.log  server.key
client.key   get.json    os           rest_server.py   time
cpu          get.py      README.md    server           uptime
disk         get.txt     reboot       server_cron.sh
favicon.png  memory      restful_api  server.crt
pi@rpiGarageOpener:~/api $ python3 rest_server.py

^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> i = rand(36)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'rand' is not defined
>>> random()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'random' is not defined
>>> import random
>>> import random
>>> random()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
>>> random.random()
0.6813765958159983
>>> random.randint()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: randint() missing 2 required positional arguments: 'a' and 'b'
>>> exit()
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ nano id_gen.py
pi@rpiGarageOpener:~/api $ python id_gen.py
23
17
4
0
10
17
pi@rpiGarageOpener:~/api $ python id_gen.py
30
9
31
15
1
19
pi@rpiGarageOpener:~/api $ nano id_gen.py
pi@rpiGarageOpener:~/api $ python3 
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'N' is not defined
>>> N=''
>>> ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> N=6
>>> ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <genexpr>
NameError: name 'random' is not defined
>>> import random
>>> ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <genexpr>
NameError: name 'string' is not defined
>>> string=''
>>> ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 1, in <genexpr>
AttributeError: 'str' object has no attribute 'ascii_uppercase'
>>> import string
>>> ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
'GWF9AU'
>>> exit()
pi@rpiGarageOpener:~/api $ nano id_gen.py
pi@rpiGarageOpener:~/api $ python3 id_gen.py
Traceback (most recent call last):
  File "id_gen.py", line 6, in <module>
    ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))
NameError: name 'N' is not defined
pi@rpiGarageOpener:~/api $ nano id_gen.py
pi@rpiGarageOpener:~/api $ python3 id_gen.py
pi@rpiGarageOpener:~/api $ nano id_gen.py
pi@rpiGarageOpener:~/api $ python3 id_gen.py
DWV6MC
pi@rpiGarageOpener:~/api $ nano id_gen.py
pi@rpiGarageOpener:~/api $ cd ..
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ nano emailTry.py
pi@rpiGarageOpener:~ $ nano emailTry.py
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ sudo python emailTry.py
  File "emailTry.py", line 5
SyntaxError: Non-ASCII character '\xe2' in file emailTry.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ sudo python emailTry.py
  File "emailTry.py", line 15
SyntaxError: Non-ASCII character '\xe2' in file emailTry.py on line 15, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ sudo python emailTry.py
text message sent
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ sudo python emailTry.py
text message sent
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ nano simple-fan.py
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ cat heelo.py
cat: heelo.py: No such file or directory
pi@rpiGarageOpener:~ $ cat hello.py
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello world'
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
pi@rpiGarageOpener:~ $ cat read.py
#!/susr/bin/python

#########################
#
# open.py opens a garage door by electronically closing a push button on
# a universla remote
#
# if the garage door is already open then no action is taken
#
# The complete project is described here:
#  https://sites.google.com/site/cartwrightraspberrypiprojects/home/home-automation-categories/access-control/garage-door-opener
#
# open.py is used in conjunction with fauxmo and Amazon Echo to control
# the garage door.
#
# The system requires a remote control, relay and a sensor
#
# open.py was tested on a Raspberry Pi Zero WH running Raspberry Pi OS
#
# The connections are as shown below:
#   RPi0 GND (physical pin 6) to Relay GND
#   RPi0 BCM GPIO 23 (physical pin 16, Wiring Pi pin 4) to Relay IN2
#   RPi0 5v (pin 2 or 4) to Relay VCC
#   Relay NO to Header Pin on Remote
#   Relay Power to 12V+ on Remote
#   RPi0 3.3v (physical pin1) to Sensor GND
#   RPi0 BCM GPIO 24 (physical pin 18, Wiring Pi pin 5) to Sensor output
#
# open.py is called rpi-echo.py
# rpi-echo.py starts automatically using systemd
#
#########################

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

PRESS = 23
SENSOR = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(PRESS, GPIO.OUT)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# wait for sensor pin to reach steady state before reading
sleep(1)

open = GPIO.input(SENSOR)
print ("open = " + str(open))
#if open == 1:
#    GPIO.output(PRESS, GPIO.LOW)
#    sleep(1)
#    GPIO.output(PRESS, GPIO.HIGH)
#    sleep(1)

GPIO.cleanup()

pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ ls *.sh
createDB.sh  getScripts2.sh  getScripts.sh  getWebsite.sh  tls2.sh  tls.sh  unused_rpi.sh
pi@rpiGarageOpener:~ $ ls /usr/local/bin
close.py  disarm.py  fauxmo.py  fauxmo.pyc  garage.sh  mylog.py  mylog.pyc  open.py  rpi-echo.py  sleep.py  toggle.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/rpi-echo.py
pi@rpiGarageOpener:~ $ cat /usr/local/bin/garage.sh
#!/bin/bash
# check if the garage door is open.
# enter a  crontab: */5 * * * * sudo /usr/local/bin/garage.sh
# If open send an alert and write to syslog
up=0
mobile='5127139980@txt.att.net'

sensor=5
gpio -g mode $sensor down
sleep 1

door=$(gpio read $sensor)

# get current time
currTime=`date +%k%M`


# get whether or not on vacation
# I get emails when SQLITE_BUSY occurs. So, changed timeout from 1000 to 20000. Seems like recommended solution.
vacation=$(sqlite3 -init <(echo .timeout 20000) /var/www/db/garagedoor.db "SELECT value FROM status WHERE name = \"vacation\"";)


# # if on vacation
if [ "$vacation" == "yes" ]
then
	# and door is up
	if [ "$door" -eq "$up" ]; then
		logger rpiGarageOpener: Garage Door Open
		echo "close the garage door" | mail -s "Garage Door Open and on vacation" $mobile
        fi
# if not on vacation and time is between 10pm and midnight
elif [ "$vacation" == "no" ]
then
        if [ $currTime -gt 2200 -a $currTime -lt 2400 ]
        then
                if [ "$door" -eq "$up" ]
	        then
                        logger rpiGarageOpener: Garage Door Open
                        echo "close the garage door" | mail -s "Garage Door Open late at night" $mobile
                fi
        # or, if time is less then 7:00am
        elif [ $currTime -gt 0 -a $currTime -lt 700 ]
        then
                if [ "$door" -eq "$up" ]
        	then
                        logger rpiGarageOpener: Garage Door Open
                        echo "close the garage door" | mail -s "Garage Door Open to early" $mobile
                fi
        fi
fi

# some debug outputs
# echo "up = $up"
# echo "door = $door"
# echo "vacation = #vacation"
# echo "time = $currtIme"
exit 0
pi@rpiGarageOpener:~ $ ls /usr/local/bin
close.py  disarm.py  fauxmo.py  fauxmo.pyc  garage.sh  mylog.py  mylog.pyc  open.py  rpi-echo.py  sleep.py  toggle.py
pi@rpiGarageOpener:~ $ cat /usr/local/bin/*.py | grep sendmail
pi@rpiGarageOpener:~ $ cat *.py | grep sendmail
mail.sendmail("cell", gmail_address, message)
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/garage.sh
pi@rpiGarageOpener:~ $ history | grep gen
  154  nano id_gen.py
  155  python id_gen.py
  156  nano id_gen.py
  158  nano id_gen.py
  159  python3 id_gen.py
  160  nano id_gen.py
  161  python3 id_gen.py
  162  nano id_gen.py
  163  python3 id_gen.py
  164  nano id_gen.py
  192  history | grep gen
pi@rpiGarageOpener:~ $ python3 id_gen.py
python3: can't open file 'id_gen.py': [Errno 2] No such file or directory
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ ls api
client.crt  cpu   favicon.png  get.json  get.txt    memory      os         reboot       rest_server.log  server          server.crt  time
client.key  disk  get.backup   get.py    id_gen.py  navigation  README.md  restful_api  rest_server.py   server_cron.sh  server.key  uptime
pi@rpiGarageOpener:~ $ history
    1  which php
    2  sudo apt install --dry-run php7.4
    3  sudo apt install  php7.3
    4  sudo apt install --dry-run php7.4-sqlite3
    5  sudo apt install --dry-run php7.3-sqlite3
    6  sudo apt install  php7.3 php7.3-sqlite3
    7  nano createDB.sh
    8  sudo bash createDB.sh
    9  nano createDB.sh
   10  sudo bash createDB.sh
   11  nano createDB.sh
   12  sudo bash createDB.sh
   13  nano createDB.sh
   14  sudo bash createDB.sh
   15  nano createDB.sh
   16  sudo bash createDB.sh
   17  nano createDB.sh
   18  sudo bash createDB.sh
   19  nano createDB.sh
   20  sudo bash createDB.sh
   21  nano createDB.sh
   22  sudo bash createDB.sh
   23  nano createDB.sh
   24  sqlite3 /var/www/db/garagedoor.db
   25  nano createDB.sh
   26  ls
   27  nano push_garage_opener.py
   28  mv push_garage_opener.py pushGarageRemote.py
   29  nano createDB.sh
   30  wget "https://raw.githubusercontent.com/dumbo25/garageDoorOpener2/main/garage.sh"
   31  ls -l
   32  ls /usr/local/bin
   33  chmod UG+x garage.sh
   34  chmod ug+x garage.sh
   35  ls -l
   36  mv garage.sh /usr/local/bin/garage.sh
   37  sudo mv garage.sh /usr/local/bin/garage.sh
   38  ls /usr/local/bin
   39  ls -l /usr/local/bin
   40  nano /var/www/db/garage.sh
   41  nano /usr/local/bin/garage.sh
   42  ls
   43  gpio read 17
   44  which which gpio
   45  /usr/bin/gpio read 17
   46  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   47  sudo apt-get update -y
   48  sudo apt-get upgrade -y
   49  sudo nano /etc/ssmtp/ssmtp.conf
   50  sudo nano /etc/ssmtp/revaliases
   51  sudo chmod og+x /etc/ssmtp/ssmtp.conf
   52  nano emailTry.py
   53  python emailTry.py
   54  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   55  ls
   56  cd api
   57  ls
   58  scp pi@home-hub.local/home/pi/client.crt .
   59  scp pi@home-hub.local/home/pi/api/client.crt .
   60  hostname
   61  scp pi@home-hub.local:/home/pi/api/client.crt .
   62  history | grep rest
   63  ls
   64  cat rest_server.log
   65  ls
   66  wget "https://raw.githubusercontent.com/dumbo25/restful_api/master/rest_server.py"
   67  wget https://github.com/dumbo25/restful_api/blob/master/favicon.png
   68  ls
   69  git clone https://github.com/dumbo25/restful_api
   70  ls
   71  ls restful_api
   72  ls restful_api/server
   73  python3 rest_server.py
   74  sudo ufw disable
   75  python3 rest_server.py
   76  sudo systemctl stop apache2.service
   77  python3 rest_server.py
   78  ls
   79  cat *.log
   80  python3 rest_server.py
   81  ls
   82  \
   83  ls restful_api
   84  cd restful_api
   85  ls
   86  ls server
   87  python3 rest_server.py
   88  ls
   89  cat ../*.log
   90  python3 rest_server.py -msc
   91  ls
   92  cd ..
   93  ls
   94  python3 rest_server.py -msc
   95  cd ..
   96  rm api
   97  cd api
   98  rm *
   99  rm * -R
  100  sudo rm * -R
  101  ls
  102  cd
  103  pwd
  104  ls
  105  rm api -R
  106  ls
  107  mkdir api
  108  cd api
  109  git clone https://github.com/dumbo25/restful_api
  110  ls
  111  openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
  112  hostname
  113  openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
  114  ls
  115  openssl req -x509 -newkey rsa:4096 -nodes -out client.crt -keyout client.key -days 365
  116  ls
  117  python3 rest_server.py -msc
  118  ls
  119  ls restful_api
  120  wget "https://raw.githubusercontent.com/dumbo25/restful_api/master/rest_server.py"
  121  wget https://github.com/dumbo25/restful_api/blob/master/favicon.png
  122  python3 rest_server.py
  123  ls
  124  python3 rest_server.py
  125  ls
  126  ls restful_api
  127  ls restful_api/server
  128  python3 rest_server.py
  129  ls restful_api/server/cpu
  130  python3 rest_server.py
  131  ls
  132  history | grep stop
  133  sudo systemctl stop apache2.service
  134  python3 rest_server.py
  135  ls
  136  cat *.log
  137  ls
  138  cd restful_api
  139  ls
  140  mv * ../.
  141  ls
  142  cd ..
  143  ls
  144  cd restful_api
  145  ls
  146  cd ../server
  147  ls
  148  mv * ../.
  149  ls
  150  cd ..
  151  ls
  152  python3 rest_server.py
  153  python3
  154  nano id_gen.py
  155  python id_gen.py
  156  nano id_gen.py
  157  python3 
  158  nano id_gen.py
  159  python3 id_gen.py
  160  nano id_gen.py
  161  python3 id_gen.py
  162  nano id_gen.py
  163  python3 id_gen.py
  164  nano id_gen.py
  165  cd ..
  166  ls
  167  nano emailTry.py
  168  sudo nano emailTry.py
  169  sudo python emailTry.py
  170  sudo nano emailTry.py
  171  sudo python emailTry.py
  172  sudo nano emailTry.py
  173  sudo python emailTry.py
  174  sudo nano emailTry.py
  175  sudo python emailTry.py
  176  ls
  177  sudo nano emailTry.py
  178  nano simple-fan.py
  179  cat heelo.py
  180  cat hello.py
  181  cat read.py
  182  ls
  183  ls *.py
  184  ls *.sh
  185  ls /usr/local/bin
  186  sudo nano /usr/local/bin/rpi-echo.py
  187  cat /usr/local/bin/garage.sh
  188  ls /usr/local/bin
  189  cat /usr/local/bin/*.py | grep sendmail
  190  cat *.py | grep sendmail
  191  sudo nano /usr/local/bin/garage.sh
  192  history | grep gen
  193  python3 id_gen.py
  194  ls
  195  ls *.py
  196  ls api
  197  history
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Documents    getScripts2.sh  hello.py  Public               rpi-echo.log      simple-fan.py.1  tls.sh
Bookshelf          dead.letter  Downloads    getScripts.sh   Music     pushGarageRemote.py  rpi-echo.service  Templates        unused_rpi.sh
check_apache.html  Desktop      emailTry.py  getWebsite.sh   Pictures  read.py              simple-fan.py     tls2.sh          Videos
pi@rpiGarageOpener:~ $ ls api/*.py
api/get.py  api/id_gen.py  api/rest_server.py
pi@rpiGarageOpener:~ $ mv api/id_gen.py .
pi@rpiGarageOpener:~ $ ls
api                dead.letter  emailTry.py     hello.py   Public               rpi-echo.service  tls2.sh
Bookshelf          Desktop      getScripts2.sh  id_gen.py  pushGarageRemote.py  simple-fan.py     tls.sh
check_apache.html  Documents    getScripts.sh   Music      read.py              simple-fan.py.1   unused_rpi.sh
createDB.sh        Downloads    getWebsite.sh   Pictures   rpi-echo.log         Templates         Videos
pi@rpiGarageOpener:~ $ mv gen_id.py genID.py
mv: cannot stat 'gen_id.py': No such file or directory
pi@rpiGarageOpener:~ $ ls
api                dead.letter  emailTry.py     hello.py   Public               rpi-echo.service  tls2.sh
Bookshelf          Desktop      getScripts2.sh  id_gen.py  pushGarageRemote.py  simple-fan.py     tls.sh
check_apache.html  Documents    getScripts.sh   Music      read.py              simple-fan.py.1   unused_rpi.sh
createDB.sh        Downloads    getWebsite.sh   Pictures   rpi-echo.log         Templates         Videos
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  hello.py  id_gen.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ mv id_gen.py genID.py
pi@rpiGarageOpener:~ $ python3 genID.py
SL9ZXP
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/garage.sh
pi@rpiGarageOpener:~ $ sudo bash /usr/local/bin/garage.sh
-- Loading resources from /dev/fd/63
pi@rpiGarageOpener:~ $ ls
api                dead.letter  emailTry.py     getWebsite.sh  Public               rpi-echo.service  tls2.sh
Bookshelf          Desktop      genID.py        hello.py       pushGarageRemote.py  simple-fan.py     tls.sh
check_apache.html  Documents    getScripts2.sh  Music          read.py              simple-fan.py.1   unused_rpi.sh
createDB.sh        Downloads    getScripts.sh   Pictures       rpi-echo.log         Templates         Videos
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/garage.sh
pi@rpiGarageOpener:~ $ cat /usr/local/bin/garage.sh
#!/bin/bash
# check if the garage door is open.
# enter a  crontab: */5 * * * * sudo /usr/local/bin/garage.sh
# If open send an alert and write to syslog
up=0
gmail='cartwright25@gmail.com'
id='SL9ZXP'

sensor=5
gpio -g mode $sensor down
sleep 1

door=$(gpio read $sensor)

# get current time
currTime=`date +%k%M`


# get whether or not on vacation
# I get emails when SQLITE_BUSY occurs. So, changed timeout from 1000 to 20000. Seems like recommended solution.
vacation=$(sqlite3 -init <(echo .timeout 20000) /var/www/db/garagedoor.db "SELECT value FROM status WHERE name = \"vacation\"";)


# # if on vacation
if [ "$vacation" == "yes" ]
then
	# and door is up
	if [ "$door" -eq "$up" ]; then
		logger rpiGarageOpener: Garage Door Open
		subj = id + " Garage: open while vacationing"
		echo "close the garage door" | mail -s $subj $gmail
        fi
# if not on vacation and time is between 10pm and midnight
elif [ "$vacation" == "no" ]
then
        if [ $currTime -gt 2200 -a $currTime -lt 2400 ]
        then
                if [ "$door" -eq "$up" ]
	        then
                        logger rpiGarageOpener: Garage Door Open
	                subj = id + " Garage: open too late"
        	        echo "close the garage door" | mail -s $subj $gmail
                fi
        # or, if time is less then 7:00am
        elif [ $currTime -gt 0 -a $currTime -lt 700 ]
        then
                if [ "$door" -eq "$up" ]
        	then
                        logger rpiGarageOpener: Garage Door Open
	                subj = id + " Garage: open too early"
        	        echo "close the garage door" | mail -s $subj $gmail
                fi
        fi
fi

# some debug outputs
# echo "up = $up"
# echo "door = $door"
# echo "vacation = #vacation"
# echo "time = $currtIme"
exit 0
pi@rpiGarageOpener:~ $ echo "close the garage door" | mail -s 'SL9ZXP Garage: open too late' 'cartwright25@gmail.com'
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ sudo echo "close the garage door" | mail -s 'SL9ZXP Garage: open too late' 'cartwright25@gmail.com'
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ mail -s 'SL9ZXP Garage: open too late' cartwright25@gmail.com
xx
;
^C
(Interrupt -- one more to kill letter)
^Cpi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ sudo echo "close garage door" | mail -s 'SL9ZXP Garage: open too late' cartwright25@gmail.com
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ mail -h
mail: invalid option -- 'h'
usage: mail [-dEIinv] [-a header] [-b bcc-addr] [-c cc-addr] [-r from-addr] [-s subject] [--] to-addr ...
       mail [-dEIiNnv] -f [name]
       mail [-dEIiNnv] [-u user]
pi@rpiGarageOpener:~ $ mail -help
mail: invalid option -- 'h'
usage: mail [-dEIinv] [-a header] [-b bcc-addr] [-c cc-addr] [-r from-addr] [-s subject] [--] to-addr ...
       mail [-dEIiNnv] -f [name]
       mail [-dEIiNnv] [-u user]
pi@rpiGarageOpener:~ $ man mail
pi@rpiGarageOpener:~ $ sudo echo "close garage door" | mail -s 'SL9ZXP Garage: open too late' cartwright25@gmail.com
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ mail -s 'SL9ZXP Garage: open too late' cartwright25@gmail.com
Cc: 
Null message body; hope that's ok
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ sudo mail -s 'SL9ZXP Garage: open too late' cartwright25@gmail.com
Cc:   
Null message body; hope that's ok
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ sudo bash mail -s 'SL9ZXP Garage: open too late' cartwright25@gmail.com
/usr/bin/mail: /usr/bin/mail: cannot execute binary file
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/garage.sh
pi@rpiGarageOpener:~ $ sudo nano b.sh
pi@rpiGarageOpener:~ $ sudo bash b.sh
b.sh: line 9: subj: command not found
mail: You must specify to-addr recipients when using -s, -c, -b, or -r
pi@rpiGarageOpener:~ $ sudo nano b.sh
pi@rpiGarageOpener:~ $ sudo bash b.sh
b.sh: line 9: subj: command not found
mail: You must specify to-addr recipients when using -s, -c, -b, or -r
pi@rpiGarageOpener:~ $ man mail 
pi@rpiGarageOpener:~ $ sudo nano b.sh
pi@rpiGarageOpener:~ $ sudo bash b.sh
b.sh: line 9: subj: command not found
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ sudo nano b.sh
pi@rpiGarageOpener:~ $ sudo nano b.sh
pi@rpiGarageOpener:~ $ sudo bash b.sh
b.sh: line 9:  Garage: open while vacationing: command not found
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ sudo nano b.sh
pi@rpiGarageOpener:~ $ sudo bash b.sh
send-mail:  (rpiGarageOpener)
Can't send mail: sendmail process failed with error code 1
pi@rpiGarageOpener:~ $ cat b.sh
#!/bin/bash
# check if the garage door is open.
# enter a  crontab: */5 * * * * sudo /usr/local/bin/garage.sh
# If open send an alert and write to syslog
up=0
gmail='cartwright25@gmail.com'
id='SL9ZXP'

subj=$id' Garage: open while vacationing'
echo "close the garage door" | mail -s $subj -r $gmail

pi@rpiGarageOpener:~ $ mail
Mail version 8.1.2 01/15/2001.  Type ? for help.
"/var/mail/pi": 1 message 1 new
>N  1 Mailer-Daemon@rpi  Fri Nov 27 16:47   58/1837  Mail delivery failed: returning message to sender
& Held 1 message in /var/mail/pi
pi@rpiGarageOpener:~ $ mail -I
Mail version 8.1.2 01/15/2001.  Type ? for help.
"/var/mail/pi": 1 message 1 unread
>U  1 Mailer-Daemon@rpi  Fri Nov 27 16:47   59/1847  Mail delivery failed: returning message to sender
& ?
& 
At EOF
& 
At EOF
& ^CInterrupt
& ^CInterrupt
& Held 1 message in /var/mail/pi
You have mail in /var/mail/pi
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ ls /var
backups  cache  lib  local  lock  log  mail  opt  run  spool  swap  tmp  www
pi@rpiGarageOpener:~ $ ls /var/local
pi@rpiGarageOpener:~ $ ls /var/log
alternatives.log    btmp             dpkg.log           kern.log.1     mail.info.2.gz  messages.2.gz   syslog.3.gz  user.log.2.gz
alternatives.log.1  btmp.1           dpkg.log.1         kern.log.2.gz  mail.log        mod_evasive     syslog.4.gz  wtmp
apache2             chkrootkit       exim4              lastlog        mail.log.1      private         syslog.5.gz  Xorg.0.log
apt                 daemon.log       fail2ban.log       lightdm        mail.log.2.gz   rkhunter.log    syslog.6.gz  Xorg.0.log.old
auth.log            daemon.log.1     fail2ban.log.1     mail.err       mail.warn       rkhunter.log.1  syslog.7.gz
auth.log.1          daemon.log.2.gz  fail2ban.log.2.gz  mail.err.1     mail.warn.1     rpimonitor.log  ufw.log
auth.log.2.gz       debug            faillog            mail.err.2.gz  mail.warn.2.gz  syslog          ufw.log.1
boot.log            debug.1          fontconfig.log     mail.info      messages        syslog.1        user.log
bootstrap.log       debug.2.gz       kern.log           mail.info.1    messages.1      syslog.2.gz     user.log.1
pi@rpiGarageOpener:~ $ ls /var/local
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Downloads       getScripts.sh  Pictures             rpi-echo.log      Templates      Videos
Bookshelf          dead.letter  emailTry.py     getWebsite.sh  Public               rpi-echo.service  tls2.sh
b.sh               Desktop      genID.py        hello.py       pushGarageRemote.py  simple-fan.py     tls.sh
check_apache.html  Documents    getScripts2.sh  Music          read.py              simple-fan.py.1   unused_rpi.sh
pi@rpiGarageOpener:~ $ nano myID.txt
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/garage.sh
pi@rpiGarageOpener:~ $ nano myID.txt
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  genID.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ nano emailTry.py
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ sudo python3 emailTry.py
  File "emailTry.py", line 26
    print 'text message sent'
                            ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('text message sent')?
pi@rpiGarageOpener:~ $ sudo python emailTry.py
Traceback (most recent call last):
  File "emailTry.py", line 22, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python2.7/smtplib.py", line 623, in login
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, '5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials j204sm182324oih.15 - gsmtp')
pi@rpiGarageOpener:~ $ sudo python emailTry.py
Traceback (most recent call last):
  File "emailTry.py", line 22, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python2.7/smtplib.py", line 623, in login
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, '5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials w131sm2507554oif.8 - gsmtp')
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ cat myID.txt
SL9ZXP

pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ sudo python emailTry.py
text message sent
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
^C
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@GarageOpener.local
The authenticity of host 'garageopener.local (fe80::6d0d:978c:46ef:e1c2%en0)' can't be established.
ECDSA key fingerprint is SHA256:yHfLn4kwccKQrwlycEJQMb17gZysras2hL2OxvhLbxY.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'garageopener.local,fe80::6d0d:978c:46ef:e1c2%en0' (ECDSA) to the list of known hosts.
pi@garageopener.local's password: 
Linux garageopener 4.14.62-v7+ #1134 SMP Tue Aug 14 17:10:10 BST 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sun Sep 16 17:59:33 2018 from 2600:1700:130:b3d0:fc8d:3660:3a39:7a54
pi@garageopener:~ $ ls
cert-auth  Documents  MagPi  oldconffiles  Public        run-fan.log  Templates
Desktop    Downloads  Music  Pictures      python_games  run-fan.py   Videos
pi@garageopener:~ $ ls /usr/local/bin
pi@garageopener:~ $ sudo raspi-config
Connection to garageopener.local closed by remote host.
Connection to garageopener.local closed.
Jeffs-MBP:~ jeff$ ssh pi@rpiUnused.local
^C      
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@GarageOpener.local
^C  
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Tue Dec  8 06:17:42 2020
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~ $ ls api
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~ $ ls api/cpu
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~ $ ls /www/html
ls: cannot access '/www/html': No such file or directory
pi@rpiGarageOpener:~ $ ls /www
ls: cannot access '/www': No such file or directory
pi@rpiGarageOpener:~ $ ls /var
backups  cache  lib  local  lock  log  mail  opt  run  spool  swap  tmp  www
pi@rpiGarageOpener:~ $ ls /var/www
db  html
pi@rpiGarageOpener:~ $ ls /var/www/html
css  GarageDoor.pdf  img  index2.html  index.php  old  schedule.php
pi@rpiGarageOpener:~ $ cp api/cpu  /var/www/html.
cp: -r not specified; omitting directory 'api/cpu'
pi@rpiGarageOpener:~ $ cp -r api/cpu  /var/www/html.
pi@rpiGarageOpener:~ $ ls /var/www/html
css  GarageDoor.pdf  img  index2.html  index.php  old  schedule.php
pi@rpiGarageOpener:~ $ cp -r api/cpu  /var/www/html/.
cp: cannot create directory '/var/www/html/./cpu': Permission denied
pi@rpiGarageOpener:~ $ sudo cp -r api/cpu  /var/www/html/.
pi@rpiGarageOpener:~ $ ls /var/www/html
cpu  css  GarageDoor.pdf  img  index2.html  index.php  old  schedule.php
pi@rpiGarageOpener:~ $ ls /var/www/html/cpu
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Tue Dec  8 07:19:12 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ sudo ufw show added
Added user rules (see 'ufw status' for running firewall):
ufw limit 22/tcp
ufw allow 443/tcp
ufw allow 80/tcp
ufw allow from 192.168.0.0/24
pi@rpiGarageOpener:~ $ sudo ufw allow 9080
Rules updated
Rules updated (v6)
pi@rpiGarageOpener:~ $ sudo ufw show added
Added user rules (see 'ufw status' for running firewall):
ufw limit 22/tcp
ufw allow 443/tcp
ufw allow 80/tcp
ufw allow from 192.168.0.0/24
ufw allow 9080
pi@rpiGarageOpener:~ $ history | grep rest
   58  history | grep rest
pi@rpiGarageOpener:~ $ history | grep server
   59  history | grep server
pi@rpiGarageOpener:~ $ python3 rest_server.py
python3: can't open file 'rest_server.py': [Errno 2] No such file or directory
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ pwd
/home/pi/api
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ sudo python3 rest_server.py
Traceback (most recent call last):
  File "rest_server.py", line 128, in <module>
    import distro
ModuleNotFoundError: No module named 'distro'
pi@rpiGarageOpener:~/api $ sudo python rest_server.py
Traceback (most recent call last):
  File "rest_server.py", line 128, in <module>
    import distro
ImportError: No module named distro
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py
Traceback (most recent call last):
  File "rest_server.py", line 128, in <module>
    import distro
ModuleNotFoundError: No module named 'distro'
pi@rpiGarageOpener:~/api $ history |grep distro
   70  history |grep distro
pi@rpiGarageOpener:~/api $ sudo pip3 install distro
Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
Collecting distro
  Downloading https://files.pythonhosted.org/packages/25/b7/b3c4270a11414cb22c6352ebc7a83aaa3712043be29daa05018fd5a5c956/distro-1.5.0-py2.py3-none-any.whl
Installing collected packages: distro
Successfully installed distro-1.5.0
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ ls multi
ls: cannot access 'multi': No such file or directory
pi@rpiGarageOpener:~/api $ ls os
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py -s
Traceback (most recent call last):
  File "rest_server.py", line 437, in <module>
    main(sys.argv)
  File "rest_server.py", line 409, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py 
^Cpi@rpiGarageOpener:~/api $ cat /etc/hosts
127.0.0.1	localhost
::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters

127.0.1.1	rpiGarageOpener
pi@rpiGarageOpener:~/api $ sudo nano /etc/apache2/apache2.conf
pi@rpiGarageOpener:~/api $ sudo nano /etc/apache2/conf-enabled/*.conf
pi@rpiGarageOpener:~/api $ sudo nano /etc/apache2/sites-enabled/*.conf
pi@rpiGarageOpener:~/api $ ls /usr/bin
'['                                       gettext                            python3.7m
 2to3-2.7                                 gettext.sh                         python3.7m-config
 ab                                       ginstall-info                      python3-config
 aconnect                                 gio                                python3m
 addpart                                  gio-querymodules                   python3m-config
 addr2line                                git                                python-config
 agnostics                                git-receive-pack                   pyvenv
 alacarte                                 git-shell                          pyvenv-3.7
 alsabat                                  git-upload-archive                 pyversions
 alsaloop                                 git-upload-pack                    qpdfview
 alsamixer                                glib-compile-schemas               qt5ct
 alsatplg                                 gnome-www-browser                  qt-faststart
 alsaucm                                  gold                               qvlc
 amidi                                    gpasswd                            rake
 amixer                                   gpg                                ranlib
 aplay                                    gpg-agent                          raspi-config
 aplaymidi                                gpgcompose                         raspi-gpio
 appres                                   gpgconf                            raspinfo
 apropos                                  gpg-connect-agent                  raspistill
 apt                                      gpgparsemail                       raspivid
 apt-cache                                gpgsm                              raspividyuv
 apt-cdrom                                gpgsplit                           raspiyuv
 apt-config                               gpgtar                             rc_gui
 apt-extracttemplates                     gpgv                               rcp
 apt-ftparchive                           gpg-wks-server                     rctest
 apt-get                                  gpg-zip                            rdma
 aptitude                                 gpic                               rdoc
 aptitude-create-state-bundle             gpio                               rdoc2.5
 aptitude-curses                          gprof                              rds-ctl
 aptitude-run-state-bundle                gresource                          readelf
 apt-key                                  groff                              readmsg
 apt-listchanges                          grog                               readmsg.mailutils
 apt-mark                                 grops                              realpath
 apt-sortpkgs                             grotty                             rename.ul
 ar                                       groups                             renice
 arandr                                   gsettings                          reset
 arch                                     gtbl                               resizepart
 arecord                                  gtf                                resolvectl
 arecordmidi                              gtk-update-icon-cache              rest_server.py
 arm-linux-gnueabihf-addr2line            h2ph                               rev
 arm-linux-gnueabihf-ar                   h2xs                               rfcomm
 arm-linux-gnueabihf-as                   hardlink                           rgrep
 arm-linux-gnueabihf-c++filt              hciattach                          ri
 arm-linux-gnueabihf-cpp                  hcitool                            ri2.5
 arm-linux-gnueabihf-cpp-8                hd                                 rkhunter
 arm-linux-gnueabihf-dwp                  head                               rlogin
 arm-linux-gnueabihf-elfedit              helpztags                          rngtest
 arm-linux-gnueabihf-g++                  hex2hcd                            rotatelogs
 arm-linux-gnueabihf-g++-8                hexdump                            routef
 arm-linux-gnueabihf-gcc                  host                               routel
 arm-linux-gnueabihf-gcc-8                hostid                             rp-bookshelf
 arm-linux-gnueabihf-gcc-ar               hostnamectl                        rpcgen
 arm-linux-gnueabihf-gcc-ar-8             htcacheclean                       rpcinfo
 arm-linux-gnueabihf-gcc-nm               htdbm                              rpi-eeprom-config
 arm-linux-gnueabihf-gcc-nm-8             htdigest                           rpi-eeprom-update
 arm-linux-gnueabihf-gcc-ranlib           htop                               rpimonitord
 arm-linux-gnueabihf-gcc-ranlib-8         htpasswd                           rpi-update
 arm-linux-gnueabihf-gcov                 iceauth                            rp-prefapps
 arm-linux-gnueabihf-gcov-8               iconv                              rsh
 arm-linux-gnueabihf-gcov-dump            id                                 rst2html
 arm-linux-gnueabihf-gcov-dump-8          iecset                             rst2html4
 arm-linux-gnueabihf-gcov-tool            info                               rst2html5
 arm-linux-gnueabihf-gcov-tool-8          infobrowser                        rst2latex
 arm-linux-gnueabihf-gold                 infocmp                            rst2man
 arm-linux-gnueabihf-gprof                infotocap                          rst2odt
 arm-linux-gnueabihf-ld                   install                            rst2odt_prepstyles
 arm-linux-gnueabihf-ld.bfd               install-info                       rst2pseudoxml
 arm-linux-gnueabihf-ld.gold              instmodsh                          rst2s5
 arm-linux-gnueabihf-nm                   ionice                             rst2xetex
 arm-linux-gnueabihf-objcopy              ipcmk                              rst2xml
 arm-linux-gnueabihf-objdump              ipcrm                              rst-buildhtml
 arm-linux-gnueabihf-pkg-config           ipcs                               rstpep2html
 arm-linux-gnueabihf-python2.7-config     iptables-xml                       rsync
 arm-linux-gnueabihf-python2-config       irb                                RTIMULibCal
 arm-linux-gnueabihf-python3.7-config     irb2.5                             RTIMULibDrive11
 arm-linux-gnueabihf-python3.7m-config    ir-ctl                             rtstat
 arm-linux-gnueabihf-python3-config       ischroot                           ruby
 arm-linux-gnueabihf-python3m-config      ispell-wrapper                     ruby2.5
 arm-linux-gnueabihf-python-config        ivtv-ctl                           runcon
 arm-linux-gnueabihf-ranlib               join                               run-mailcap
 arm-linux-gnueabihf-readelf              json_pp                            run-with-aspell
 arm-linux-gnueabihf-run                  json_xs                            rview
 arm-linux-gnueabihf-size                 kbdinfo                            rvlc
 arm-linux-gnueabihf-strings              kbxutil                            savelog
 arm-linux-gnueabihf-strip                kernel-install                     scp
 arm-unknown-linux-gnueabihf-pkg-config   keyring                            screendump
 as                                       killall                            script
 aseqdump                                 l2ping                             scriptreplay
 aseqnet                                  l2test                             scrot
 aspell                                   laptop-detect                      sdiff
 aspell-import                            last                               sdptool
 awk                                      lastb                              see
 axfer                                    lastlog                            select-default-iwrap
 b2sum                                    lcf                                select-editor
 base32                                   ld                                 sensible-browser
 base64                                   ld.bfd                             sensible-editor
 basename                                 ldd                                sensible-pager
 bashbug                                  ld.gold                            seq
 bccmd                                    less                               sessreg
 bdaddr                                   lessecho                           setarch
 bluealsa                                 lessfile                           setcifsacl
 bluealsa-aplay                           lesskey                            setkeycodes
 bluemoon                                 lesspipe                           setleds
 bluetoothctl                             lexgrog                            setlogcons
 bootctl                                  lft                                setmetamode
 bsd-from                                 lft.db                             setpci
 bsd-mailx                                libnetcfg                          setpriv
 bsd-write                                libpng16-config                    setsid
 btattach                                 libpng-config                      setterm
 bthelper                                 link                               setvtrgb
 btmgmt                                   linux32                            setxkbmap
 btmon                                    linux64                            sftp
 btuart                                   linux-check-removal                sg
 busctl                                   linux-update-symlinks              sha1sum
 bwrap                                    linux-version                      sha224sum
 c++                                      listres                            sha256sum
 c89                                      lnstat                             sha384sum
 c89-gcc                                  loadkeys                           sha512sum
 c99                                      loadunimap                         shasum
 c99-gcc                                  locale                             showconsolefont
 cal                                      localectl                          showkey
 calendar                                 localedef                          showrgb
 captoinfo                                logger                             shred
 catchsegv                                logilab-pytest3                    shuf
 catman                                   logname                            sieve
 cc                                       logresolve                         size
 cec-compliance                           look                               skill
 cec-ctl                                  lorder                             slabtop
 cec-follower                             lsattr                             slogin
 c++filt                                  lsb_release                        snice
 chage                                    lscpu                              soelim
 chardet                                  lsinitramfs                        sort
 chardet3                                 lsipc                              sotruss
 chardetect                               lslocks                            speaker-test
 chardetect3                              lslogins                           splain
 chattr                                   lsmem                              split
 chcon                                    lsns                               splitfont
 checkgid                                 lsof                               sprof
 check-language-support                   lspci                              sqldiff
 chfn                                     lspgpot                            sqlite3
 choom                                    lsusb                              ssh
 chromium-browser                         lua                                ssh-add
 chrt                                     lua5.1                             ssh-agent
 chsh                                     luac                               ssh-argv0
 cifscreds                                luac5.1                            ssh-copy-id
 ciptool                                  luajit                             ssh-import-id
 ckbcomp                                  luit                               ssh-import-id-gh
 cksum                                    lxappearance                       ssh-import-id-lp
 clear                                    lxclipboard                        ssh-keygen
 clear_console                            lxde-logout                        ssh-keyscan
 cmp                                      lxde-pi-shutdown-helper            startlxde
 codepage                                 lxhotkey                           startlxde-pi
 col                                      lxinput                            startx
 colcrt                                   lxpanel                            stat
 colour_to_gtk3                           lxpanelctl                         stdbuf
 colour_to_obconf                         lxpolkit                           strace
 colrm                                    lxrandr                            strace-log-merge
 column                                   lxsession                          strings
 comm                                     lxsession-db                       strip
 compose                                  lxsession-default                  stubgen
 convert-dtsv0                            lxsession-default-terminal         sudo
 corelist                                 lxsession-edit                     sudoedit
 cpan                                     lxsession-logout                   sudoreplay
 cpan5.28-arm-linux-gnueabihf             lxsession-xdg-autostart            sum
 cpp                                      lxtask                             svlc
 cpp-8                                    lxterminal                         symcryptrun
 c_rehash                                 lzcat                              symilar3
 crontab                                  lzcmp                              systemd-analyze
 csplit                                   lzdiff                             systemd-cat
 ctstat                                   lzegrep                            systemd-cgls
 curl                                     lzfgrep                            systemd-cgtop
 cut                                      lzgrep                             systemd-delta
 cvlc                                     lzless                             systemd-detect-virt
 cvt                                      lzma                               systemd-id128
 cvtsudoers                               lzmainfo                           systemd-mount
 cx18-ctl                                 lzmore                             systemd-path
 dbus-cleanup-sockets                     mail                               systemd-resolve
 dbus-daemon                              Mail                               systemd-run
 dbus-launch                              mail.mailutils                     systemd-socket-activate
 dbus-monitor                             mailx                              systemd-stdio-bridge
 dbus-run-session                         make                               systemd-umount
 dbus-send                                make-first-existing-target         tabs
 dbus-update-activation-environment       man                                tac
 dbus-uuidgen                             mandb                              tail
 dc                                       manpath                            tasksel
 ddcmon                                   mapscrn                            taskset
 deallocvt                                mawk                               tbl
 debconf                                  mcookie                            tee
 debconf-apt-progress                     md5sum                             test
 debconf-communicate                      md5sum.textutils                   thonny
 debconf-copydb                           media-ctl                          tic
 debconf-escape                           mesg                               timedatectl
 debconf-getlang                          messages                           timeout
 debconf-get-selections                   messages.mailutils                 tload
 debconf-loadtemplate                     migrate-pubring-from-classic-gpg   toe
 debconf-mergetemplate                    mimeview                           top
 debconf-set-selections                   miniterm                           touch
 debconf-show                             mkfifo                             tput
 debian-reference                         mk_modmap                          tr
 deb-systemd-helper                       mkpasswd                           traceproto
 deb-systemd-invoke                       mousepad                           traceproto.db
 decode-dimms                             movemail                           traceroute
 decode-edid                              movemail.mailutils                 traceroute6
 decode_tm6000                            mpris-proxy                        traceroute6.db
 decode-vaio                              mtrace                             traceroute.db
 delpart                                  mypy                               traceroute-nanog
 desktop-file-edit                        namei                              tree
 desktop-file-install                     nawk                               troff
 desktop-file-validate                    ncal                               truncate
 dh_bash-completion                       ncdu                               tset
 dh_installxmlcatalogs                    neqn                               tsort
 dh_numpy                                 newgrp                             tty
 dh_numpy3                                ngettext                           tvservice
 dh_pypy                                  nice                               tzselect
 dh_python2                               nl                                 ucf
 dh_python3                               nm                                 ucfq
 diff                                     nohup                              ucfr
 diff3                                    nproc                              udisksctl
 dircolors                                nroff                              ul
 dirmngr                                  nsenter                            unexpand
 dirmngr-client                           nstat                              unicode_stop
 dirname                                  ntfsdecrypt                        uniq
 dm-tool                                  numfmt                             unlink
 dmypy                                    nvlc                               unlzma
 dotlock                                  obamenu                            unmkinitramfs
 dotlockfile                              obconf                             unpigz
 dotlock.mailutils                        obexctl                            unshare
 dpkg                                     objcopy                            unxrandr
 dpkg-architecture                        objdump                            unxz
 dpkg-buildflags                          obxprop                            unzip
 dpkg-buildpackage                        od                                 unzipsfx
 dpkg-checkbuilddeps                      omxplayer                          update-alternatives
 dpkg-deb                                 omxplayer.bin                      update-desktop-database
 dpkg-distaddfile                         openbox                            update-mime-database
 dpkg-divert                              openbox-lxde                       uptime
 dpkg-genbuildinfo                        openbox-lxde-pi                    usb-devices
 dpkg-genchanges                          openbox-session                    usbhid-dump
 dpkg-gencontrol                          openssl                            usbreset
 dpkg-gensymbols                          pager                              users
 dpkg-maintscript-helper                  paperconf                          utmpdump
 dpkg-mergechangelogs                     parsechangelog                     uuid
 dpkg-name                                parse-edid                         v4l2-compliance
 dpkg-parsechangelog                      partx                              v4l2-ctl
 dpkg-query                               passwd                             v4l2-sysfs-path
 dpkg-scanpackages                        paste                              vcdbg
 dpkg-scansources                         patch                              vcgencmd
 dpkg-shlibdeps                           pathchk                            vchiq_test
 dpkg-source                              pbr                                vi
 dpkg-split                               pcimodules                         view
 dpkg-statoverride                        pcmanfm                            viewres
 dpkg-trigger                             pdb                                vim.tiny
 dpkg-vendor                              pdb2                               vlc
 dtc                                      pdb2.7                             vlc-wrapper
 dtdiff                                   pdb3                               vmstat
 dtmerge                                  pdb3.7                             vncagent
 dtoverlay                                peekfd                             vncagent-raspi
 dtoverlay-post                           perf                               vncinitconfig
 dtoverlay-pre                            perl                               vnclicense
 dtparam                                  perl5.28.1                         vnclicensehelper
 du                                       perl5.28-arm-linux-gnueabihf       vnclicensewiz
 dumpkeys                                 perlbug                            vncpamhelper
 dwp                                      perldoc                            vncpasswd
 edidparser                               perlivp                            vncpipehelper
 edit                                     perlthanks                         vncserver
 editor                                   pgrep                              vncserverui
 editres                                  pgzrun                             vncserver-virtual
 eject                                    phar                               vncserver-virtuald
 elfedit                                  phar7.3                            vncserver-x11
 enc2xs                                   phar.phar                          vncserver-x11-core
 encguess                                 phar.phar7.3                       vncserver-x11-serviced
 env                                      php                                volname
 envsubst                                 php7.3                             w
 epylint3                                 pic                                wall
 eqn                                      piclone                            watch
 erb                                      pico                               watchgnupg
 erb2.5                                   piconv                             wc
 ex                                       pig2vcd                            wget
 expand                                   pigpiod                            whatis
 expiry                                   pi-gpk-dbus-service                whereis
 expr                                     pi-gpk-install-local-file          which
 f2py                                     pi-gpk-log                         whiptail
 f2py2.7                                  pi-gpk-prefs                       who
 f2py3                                    pi-gpk-update-viewer               whoami
 f2py3.7                                  pigs                               whois
 factor                                   pigz                               word-list-compress
 fail2ban-client                          pinentry                           wpa_passphrase
 fail2ban-python                          pinentry-curses                    w.procps
 fail2ban-regex                           pinky                              write
 fail2ban-server                          pinout                             X
 fail2ban-testcases                       pip                                X11
 faillog                                  pip2                               xarchiver
 faked-sysv                               pip3                               xargs
 faked-tcp                                pi-packages                        xauth
 fakeroot                                 pipanel                            xcmsdb
 fakeroot-sysv                            piwiz                              xcompmgr
 fakeroot-tcp                             pkaction                           xdg-dbus-proxy
 fallocate                                pkcheck                            xdg-desktop-icon
 fc-cache                                 pkexec                             xdg-desktop-menu
 fc-cat                                   pkg-config                         xdg-email
 fc-conflist                              pkill                              xdg-icon-resource
 fcgistarter                              pkttyagent                         xdg-mime
 fc-list                                  pl2pm                              xdg-open
 fc-match                                 pldd                               xdg-screensaver
 fc-pattern                               pmap                               xdg-settings
 fc-query                                 pngfix                             xdg-user-dir
 fc-scan                                  png-fix-itxt                       xdg-user-dirs-update
 fc-validate                              pod2html                           xdpyinfo
 fdtdump                                  pod2man                            xdriinfo
 fdtget                                   pod2text                           xev
 fdtoverlay                               pod2usage                          xfd
 fdtput                                   podchecker                         xfontsel
 ffmpeg                                   podselect                          xgamma
 ffplay                                   pr                                 xhost
 ffprobe                                  precat                             xinit
 file                                     preconv                            xinput
 fincore                                  preunzip                           xkbbell
 find                                     prezip                             xkbcomp
 fio                                      prezip-bin                         xkbevd
 fio2gnuplot                              print                              xkbprint
 fio-btrace2fio                           printenv                           xkbvleds
 fio-dedupe                               printerbanner                      xkbwatch
 fio_generate_plots                       printf                             xkeystone
 fio-genzipf                              prlimit                            xkill
 flask                                    prove                              xlsatoms
 flock                                    proxy                              xlsclients
 fmt                                      prtstat                            xlsfonts
 fold                                     psfaddtable                        xmessage
 free                                     psfgettable                        xmodmap
 frm                                      psfstriptable                      Xorg
 frm.mailutils                            psfxtable                          xprop
 from                                     pslog                              xrandr
 from.mailutils                           pstree                             xrdb
 funzip                                   pstree.x11                         xrefresh
 g++                                      ptar                               xsel
 g++-8                                    ptardiff                           x-session-manager
 galculator                               ptargrep                           xset
 gapplication                             ptx                                xsetmode
 gatttool                                 pwdx                               xsetpointer
 gcc                                      py3clean                           xsetroot
 gcc-8                                    py3compile                         xstdcmap
 gcc-ar                                   py3versions                        xsubpp
 gcc-ar-8                                 pybuild                            x-terminal-emulator
 gcc-nm                                   pyclean                            xvidtune
 gcc-nm-8                                 pycompile                          xvinfo
 gcc-ranlib                               pydoc                              Xvnc
 gcc-ranlib-8                             pydoc2                             Xvnc-core
 gcore                                    pydoc2.7                           x-window-manager
 gcov                                     pydoc3                             xwininfo
 gcov-8                                   pydoc3.7                           x-www-browser
 gcov-dump                                pygettext                          xxd
 gcov-dump-8                              pygettext2                         xz
 gcov-tool                                pygettext2.7                       xzcat
 gcov-tool-8                              pygettext3                         xzcmp
 gdb                                      pygettext3.7                       xzdiff
 gdb-add-index                            pygmentize                         xzegrep
 gdbtui                                   pyjwt                              xzfgrep
 gdbus                                    pyjwt3                             xzgrep
 gdialog                                  pylint3                            xzless
 gdm-control                              pypy                               xzmore
 geany                                    pypyclean                          yes
 gem                                      pypycompile                        zdump
 gem2.5                                   pyreverse3                         zenity
 gencat                                   python                             zip
 genfio                                   python2                            zipcloak
 geqn                                     python2.7                          zipdetails
 getcifsacl                               python2.7-config                   zipgrep
 getconf                                  python2-config                     zipinfo
 get-edid                                 python2-pbr                        zipnote
 getent                                   python3                            zipsplit
 getkeycodes                              python3.7
 getopt                                   python3.7-config
pi@rpiGarageOpener:~/api $ ls /usr/bin/rest_server.py
/usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ ls -l /usr/bin/rest_server.py
-rwxr-xr-x 1 root root 14842 Nov 30 19:38 /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ ps -aux | grep rest
root      1188  0.1  3.1  21836 14088 ?        S    15:30   0:02 python3 /usr/bin/rest_server.py -msc
pi        3680  1.0  0.4   7336  2020 pts/0    S+   16:07   0:00 grep --color=auto rest
pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ ls -l
total 124
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 cpu
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 memory
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 navigation
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   495 Dec  8 16:10 rest_server.log
-rwxr-xr-x 1 pi pi 14842 Dec  6 08:11 rest_server.py
drwxr-xr-x 2 pi pi  4096 Dec  6 09:13 server
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 time
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 uptime
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/08 16:10:03 - Starting REST server
2020/12/08 16:10:03 - Command line arguments:
2020/12/08 16:10:03 -   Input file  = 
2020/12/08 16:10:03 -   Log file = /home/pi/api/rest_server.log
2020/12/08 16:10:03 -   Port = 9443
2020/12/08 16:10:03 -   Use cert = True
2020/12/08 16:10:03 -   Use HTTPS = True
2020/12/08 16:10:03 -   Use multithreading = True

2020/12/08 16:10:03 - Web Server:
2020/12/08 16:10:03 -   Server name = rpiGarageOpener
2020/12/08 16:10:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ ls ../*.log
../rpi-echo.log
pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ pwd
/home/pi/api
pi@rpiGarageOpener:~/api $ ls -l
total 124
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 cpu
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 memory
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 navigation
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   495 Dec  8 16:10 rest_server.log
-rwxr-xr-x 1 pi pi 14842 Dec  6 08:11 rest_server.py
drwxr-xr-x 2 pi pi  4096 Dec  6 09:13 server
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 time
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 uptime
pi@rpiGarageOpener:~/api $ ps -aux | grep rest
root      1188  0.1  3.1  21836 14088 ?        S    15:30   0:03 python3 /usr/bin/rest_server.py -msc
pi        4110  0.0  0.4   7336  1952 pts/0    S+   16:13   0:00 grep --color=auto rest
pi@rpiGarageOpener:~/api $ netstat -lptn
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.1.1:9443          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
pi@rpiGarageOpener:~/api $ netstat --tcp --listening --programs --numeric
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.1.1:9443          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
pi@rpiGarageOpener:~/api $ sudo ufw status
Status: inactive
pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ cat /home/pi/api/server_cron.sh
#!/bin/bash

HOME="/user/pi/api"
PIDFILE="$HOME/rest_server.pid"
# echo $PIDFILE

if [ -e "${PIDFILE}" ] && (ps -u $(whoami) -opid= | grep -P "^\s*$(cat ${PIDFILE})$" &> /dev/null); then
  # "rest_server.py is already running."
  # echo "already running"
  exit 99
fi

# echo "starting restserver"
/usr/bin/rest_server.py -msc
pi@rpiGarageOpener:~/api $ ls *.pid
ls: cannot access '*.pid': No such file or directory
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $  rest_server.logcat 
-bash: rest_server.logcat: command not found
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/08 16:20:04 - Starting REST server
2020/12/08 16:20:04 - Command line arguments:
2020/12/08 16:20:04 -   Input file  = 
2020/12/08 16:20:04 -   Log file = /home/pi/api/rest_server.log
2020/12/08 16:20:04 -   Port = 9443
2020/12/08 16:20:04 -   Use cert = True
2020/12/08 16:20:04 -   Use HTTPS = True
2020/12/08 16:20:04 -   Use multithreading = True

2020/12/08 16:20:04 - Web Server:
2020/12/08 16:20:04 -   Server name = rpiGarageOpener
2020/12/08 16:20:04 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ do nano /home/pi/api/server_cron.sh
-bash: syntax error near unexpected token `do'
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Tue Dec  8 15:18:49 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ sudo crontab -e
No modification made
pi@rpiGarageOpener:~ $ sudo nano api/server_cron.sh
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ rm rest_)server.py
-bash: syntax error near unexpected token `)'
pi@rpiGarageOpener:~/api $ rm rest_server.py
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu   favicon.png  get.json  get.txt  navigation  README.md  restful_api      server          server.crt  time
client.key  disk  get.backup   get.py    memory   os          reboot     rest_server.log  server_cron.sh  server.key  uptime
pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ ps -aux | grep rest
root      1188  0.0  3.0  21836 13440 ?        S    Dec08   0:33 python3 /usr/bin/rest_server.py -msc
pi       30068  0.0  0.4   7336  1952 pts/0    S+   07:09   0:00 grep --color=auto rest
pi@rpiGarageOpener:~/api $ sudo kill 1188
pi@rpiGarageOpener:~/api $ ps -aux | grep rest
pi       30093  0.0  0.4   7336  2024 pts/0    S+   07:09   0:00 grep --color=auto rest
pi@rpiGarageOpener:~/api $ ps -aux | grep rest
root     30166 21.0  3.1  21836 14112 ?        S    07:10   0:01 python3 /usr/bin/rest_server.py -msc
pi       30179  0.0  0.4   7336  2020 pts/0    S+   07:10   0:00 grep --color=auto rest
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu   favicon.png  get.json  get.txt  navigation  README.md  restful_api      server          server.crt  time
client.key  disk  get.backup   get.py    memory   os          reboot     rest_server.log  server_cron.sh  server.key  uptime
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:10:03 - Starting REST server
2020/12/09 07:10:03 - Command line arguments:
2020/12/09 07:10:03 -   Input file  = 
2020/12/09 07:10:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:10:03 -   Port = 9443
2020/12/09 07:10:03 -   Use cert = True
2020/12/09 07:10:03 -   Use HTTPS = True
2020/12/09 07:10:03 -   Use multithreading = True

2020/12/09 07:10:03 - Web Server:
2020/12/09 07:10:03 -   Server name = rpiGarageOpener
2020/12/09 07:10:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:10:03 - Starting REST server
2020/12/09 07:10:03 - Command line arguments:
2020/12/09 07:10:03 -   Input file  = 
2020/12/09 07:10:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:10:03 -   Port = 9443
2020/12/09 07:10:03 -   Use cert = True
2020/12/09 07:10:03 -   Use HTTPS = True
2020/12/09 07:10:03 -   Use multithreading = True

2020/12/09 07:10:03 - Web Server:
2020/12/09 07:10:03 -   Server name = rpiGarageOpener
2020/12/09 07:10:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:10:03 - Starting REST server
2020/12/09 07:10:03 - Command line arguments:
2020/12/09 07:10:03 -   Input file  = 
2020/12/09 07:10:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:10:03 -   Port = 9443
2020/12/09 07:10:03 -   Use cert = True
2020/12/09 07:10:03 -   Use HTTPS = True
2020/12/09 07:10:03 -   Use multithreading = True

2020/12/09 07:10:03 - Web Server:
2020/12/09 07:10:03 -   Server name = rpiGarageOpener
2020/12/09 07:10:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:10:03 - Starting REST server
2020/12/09 07:10:03 - Command line arguments:
2020/12/09 07:10:03 -   Input file  = 
2020/12/09 07:10:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:10:03 -   Port = 9443
2020/12/09 07:10:03 -   Use cert = True
2020/12/09 07:10:03 -   Use HTTPS = True
2020/12/09 07:10:03 -   Use multithreading = True

2020/12/09 07:10:03 - Web Server:
2020/12/09 07:10:03 -   Server name = rpiGarageOpener
2020/12/09 07:10:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:15:03 - Starting REST server
2020/12/09 07:15:03 - Command line arguments:
2020/12/09 07:15:03 -   Input file  = 
2020/12/09 07:15:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:15:03 -   Port = 9443
2020/12/09 07:15:03 -   Use cert = True
2020/12/09 07:15:03 -   Use HTTPS = True
2020/12/09 07:15:03 -   Use multithreading = True

2020/12/09 07:15:03 - Web Server:
2020/12/09 07:15:03 -   Server name = rpiGarageOpener
2020/12/09 07:15:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:15:03 - Starting REST server
2020/12/09 07:15:03 - Command line arguments:
2020/12/09 07:15:03 -   Input file  = 
2020/12/09 07:15:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:15:03 -   Port = 9443
2020/12/09 07:15:03 -   Use cert = True
2020/12/09 07:15:03 -   Use HTTPS = True
2020/12/09 07:15:03 -   Use multithreading = True

2020/12/09 07:15:03 - Web Server:
2020/12/09 07:15:03 -   Server name = rpiGarageOpener
2020/12/09 07:15:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~/api $ ifconfig
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.227  netmask 255.255.255.0  broadcast 192.168.1.255
        ether b8:27:eb:4f:bd:e9  txqueuelen 1000  (Ethernet)
        RX packets 224785  bytes 50471977 (48.1 MiB)
        RX errors 0  dropped 2  overruns 0  frame 0
        TX packets 18547  bytes 2572952 (2.4 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:40:03 - Starting REST server
2020/12/09 07:40:03 - Command line arguments:
2020/12/09 07:40:03 -   Input file  = 
2020/12/09 07:40:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:40:03 -   Port = 9443
2020/12/09 07:40:03 -   Use cert = True
2020/12/09 07:40:03 -   Use HTTPS = True
2020/12/09 07:40:03 -   Use multithreading = True

2020/12/09 07:40:03 - Web Server:
2020/12/09 07:40:03 -   Server name = rpiGarageOpener
2020/12/09 07:40:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~/api $ ls restful_api
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 07:45:03 - Starting REST server
2020/12/09 07:45:03 - Command line arguments:
2020/12/09 07:45:03 -   Input file  = 
2020/12/09 07:45:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 07:45:03 -   Port = 9443
2020/12/09 07:45:03 -   Use cert = True
2020/12/09 07:45:03 -   Use HTTPS = True
2020/12/09 07:45:03 -   Use multithreading = True

2020/12/09 07:45:03 - Web Server:
2020/12/09 07:45:03 -   Server name = rpiGarageOpener
2020/12/09 07:45:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/09 08:00:03 - Starting REST server
2020/12/09 08:00:03 - Command line arguments:
2020/12/09 08:00:03 -   Input file  = 
2020/12/09 08:00:03 -   Log file = /home/pi/api/rest_server.log
2020/12/09 08:00:03 -   Port = 9443
2020/12/09 08:00:03 -   Use cert = True
2020/12/09 08:00:03 -   Use HTTPS = True
2020/12/09 08:00:03 -   Use multithreading = True

2020/12/09 08:00:03 - Web Server:
2020/12/09 08:00:03 -   Server name = rpiGarageOpener
2020/12/09 08:00:03 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Wed Dec  9 06:56:49 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ sudo shutdown -h 0
Shutdown scheduled for Fri 2020-12-11 06:55:30 CST, use 'shutdown -c' to cancel.
pi@rpiGarageOpener:~ $ Connection to rpigarageopener.local closed by remote host.
Connection to rpigarageopener.local closed.
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec 11 06:56:22 2020
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec 11 12:55:50 2020
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ cat rest_server.log
cat: rest_server.log: No such file or directory
pi@rpiGarageOpener:~ $ cat /var/log/apache/error.log
cat: /var/log/apache/error.log: No such file or directory
pi@rpiGarageOpener:~ $ ls -l /var/log/apache2
total 120
-rw-r----- 1 root adm    0 Dec 11 00:00 access.log
-rw-r----- 1 root adm  167 Dec 10 17:22 access.log.1
-rw-r----- 1 root adm 2657 Nov 29 18:48 access.log.10.gz
-rw-r----- 1 root adm 1790 Nov 28 22:07 access.log.11.gz
-rw-r----- 1 root adm  129 Nov 27 17:47 access.log.12.gz
-rw-r----- 1 root adm  396 Nov 26 17:57 access.log.13.gz
-rw-r----- 1 root adm  112 Nov 25 12:13 access.log.14.gz
-rw-r----- 1 root adm  115 Dec  9 17:13 access.log.2.gz
-rw-r----- 1 root adm  115 Dec  8 15:54 access.log.3.gz
-rw-r----- 1 root adm  131 Dec  5 22:57 access.log.4.gz
-rw-r----- 1 root adm  112 Dec  4 17:47 access.log.5.gz
-rw-r----- 1 root adm  114 Dec  3 17:23 access.log.6.gz
-rw-r----- 1 root adm  129 Dec  2 17:06 access.log.7.gz
-rw-r----- 1 root adm  115 Dec  1 12:35 access.log.8.gz
-rw-r----- 1 root adm  113 Nov 30 07:01 access.log.9.gz
-rw-r----- 1 root adm  905 Dec 11 12:55 error.log
-rw-r----- 1 root adm  880 Dec 11 00:00 error.log.1
-rw-r----- 1 root adm  584 Dec  1 00:00 error.log.10.gz
-rw-r----- 1 root adm 4812 Nov 30 00:00 error.log.11.gz
-rw-r----- 1 root adm 3545 Nov 29 00:00 error.log.12.gz
-rw-r----- 1 root adm  493 Nov 28 00:00 error.log.13.gz
-rw-r----- 1 root adm  508 Nov 27 00:00 error.log.14.gz
-rw-r----- 1 root adm  469 Dec 10 00:00 error.log.2.gz
-rw-r----- 1 root adm  467 Dec  9 00:00 error.log.3.gz
-rw-r----- 1 root adm  294 Dec  6 07:52 error.log.4.gz
-rw-r----- 1 root adm  501 Dec  6 00:00 error.log.5.gz
-rw-r----- 1 root adm  578 Dec  5 00:00 error.log.6.gz
-rw-r----- 1 root adm  464 Dec  4 00:00 error.log.7.gz
-rw-r----- 1 root adm  501 Dec  3 00:00 error.log.8.gz
-rw-r----- 1 root adm  465 Dec  2 00:00 error.log.9.gz
-rw-r----- 1 root adm    0 Nov 22 08:59 other_vhosts_access.log
pi@rpiGarageOpener:~ $ ls -l /var/log/apache2/error.log
-rw-r----- 1 root adm 905 Dec 11 12:55 /var/log/apache2/error.log
pi@rpiGarageOpener:~ $ cat /var/log/apache2/error.log
[Fri Dec 11 00:00:10.289598 2020] [mpm_prefork:notice] [pid 456] AH00163: Apache/2.4.38 (Raspbian) mod_wsgi/4.6.5 Python/2.7 configured -- resuming normal operations
[Fri Dec 11 00:00:10.289873 2020] [core:notice] [pid 456] AH00094: Command line: '/usr/sbin/apache2'
[Fri Dec 11 06:55:39.559383 2020] [mpm_prefork:notice] [pid 456] AH00169: caught SIGTERM, shutting down
[Fri Dec 11 06:56:18.689960 2020] [mpm_prefork:notice] [pid 455] AH00163: Apache/2.4.38 (Raspbian) mod_wsgi/4.6.5 Python/2.7 configured -- resuming normal operations
[Fri Dec 11 06:56:18.921885 2020] [core:notice] [pid 455] AH00094: Command line: '/usr/sbin/apache2'
[Fri Dec 11 12:55:48.016536 2020] [mpm_prefork:notice] [pid 479] AH00163: Apache/2.4.38 (Raspbian) mod_wsgi/4.6.5 Python/2.7 configured -- resuming normal operations
[Fri Dec 11 12:55:48.083915 2020] [core:notice] [pid 479] AH00094: Command line: '/usr/sbin/apache2'
pi@rpiGarageOpener:~ $ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/root        15G  3.1G   11G  23% /
devtmpfs        184M     0  184M   0% /dev
tmpfs           216M     0  216M   0% /dev/shm
tmpfs           216M  3.2M  213M   2% /run
tmpfs           5.0M  4.0K  5.0M   1% /run/lock
tmpfs           216M     0  216M   0% /sys/fs/cgroup
/dev/mmcblk0p1  253M   55M  198M  22% /boot
tmpfs            44M     0   44M   0% /run/user/1000
pi@rpiGarageOpener:~ $ ls -l/
ls: invalid option -- '/'
Try 'ls --help' for more information.
pi@rpiGarageOpener:~ $ ls -l /
total 72
drwxr-xr-x   2 root root  4096 Aug 20 05:36 bin
drwxr-xr-x   5 root root  3584 Dec 31  1969 boot
drwxr-xr-x  16 root root  3640 Dec 11 12:55 dev
drwxr-xr-x 116 root root  4096 Nov 28 16:22 etc
drwxr-xr-x   3 root root  4096 Aug 20 05:31 home
drwxr-xr-x  17 root root  4096 Nov 22 08:41 lib
drwx------   2 root root 16384 Aug 20 05:53 lost+found
drwxr-xr-x   2 root root  4096 Aug 20 05:26 media
drwxr-xr-x   2 root root  4096 Aug 20 05:26 mnt
drwxr-xr-x   4 root root  4096 Aug 20 05:38 opt
dr-xr-xr-x 127 root root     0 Dec 31  1969 proc
drwx------   5 root root  4096 Nov 30 15:23 root
drwxr-xr-x  29 root root   880 Dec 11 12:56 run
drwxr-xr-x   2 root root  4096 Nov 21 21:41 sbin
drwxr-xr-x   2 root root  4096 Aug 20 05:26 srv
dr-xr-xr-x  12 root root     0 Dec 31  1969 sys
drwxrwxrwt  12 root root  4096 Dec 11 14:39 tmp
drwxr-xr-x  10 root root  4096 Nov 22 08:26 usr
drwxr-xr-x  12 root root  4096 Nov 22 08:58 var
pi@rpiGarageOpener:~ $ ls /etc
adduser.conf            fake-hwclock.data  libnl-3         passwd            selinux
aliases                 fb.modes           libpaper.d      passwd-           sensors3.conf
alsa                    fonts              lightdm         paxctld.conf      sensors.d
alternatives            fstab              lighttpd        perl              services
apache2                 fuse.conf          locale.alias    php               sgml
apparmor.d              gai.conf           locale.gen      pip.conf          shadow
apt                     gdb                localtime       plymouth          shadow-
avahi                   ghostscript        logcheck        polkit-1          shells
bash.bashrc             glvnd              login.defs      ppp               skel
bash_completion         gnome              logrotate.conf  profile           ssh
bash_completion.d       groff              logrotate.d     profile.d         ssl
bindresvport.blacklist  group              logwatch        protocols         ssmtp
binfmt.d                group-             machine-id      pulse             subgid
bluetooth               gshadow            magic           python            subuid
ca-certificates         gshadow-           magic.mime      python2.7         sudoers
ca-certificates.conf    gss                mailcap         python3           sudoers.d
calendar                gtk-2.0            mailcap.order   python3.7         sysctl.conf
chkrootkit.conf         gtk-3.0            mailname        rc0.d             sysctl.d
chromium-browser        host.conf          mail.rc         rc1.d             systemd
cifs-utils              hostname           manpath.config  rc2.d             terminfo
console-setup           hosts              menu-methods    rc3.d             timezone
cron.d                  hosts.allow        mime.types      rc4.d             timidity
cron.daily              hosts.deny         mke2fs.conf     rc5.d             tmpfiles.d
cron.hourly             idmapd.conf        modprobe.d      rc6.d             triggerhappy
cron.monthly            ifplugd            modules         rc.local          ucf.conf
crontab                 init               modules-load.d  rcS.d             udev
cron.weekly             init.d             monit           request-key.conf  udisks2
dbus-1                  initramfs-tools    motd            request-key.d     ufw
debconf.conf            inputrc            mtab            resolv.conf       update-motd.d
debian_version          insserv.conf.d     mysql           resolvconf        usb_modeswitch.conf
default                 iproute2           nanorc          resolv.conf.bak   usb_modeswitch.d
deluser.conf            issue              netconfig       resolvconf.conf   vdpau_wrapper.cfg
dhcp                    issue.net          network         rkhunter.conf     vim
dhcpcd.conf             kernel             networks        rmt               vnc
dictionaries-common     ldap               nsswitch.conf   rpc               vulkan
dphys-swapfile          ld.so.cache        openal          rpi-issue         wgetrc
dpkg                    ld.so.conf         opt             rpimonitor        wpa_supplicant
emacs                   ld.so.conf.d       os-release      rsyslog.conf      X11
email-addresses         ld.so.preload      PackageKit      rsyslog.d         xattr.conf
environment             libaudit.conf      pam.conf        RTIMULib.ini      xdg
exim4                   libblockdev        pam.d           securetty         xml
fail2ban                libibverbs.d       papersize       security
pi@rpiGarageOpener:~ $ ls /etc/systemd
journald.conf  network        resolved.conf  system       timesyncd.conf  user.conf
logind.conf    networkd.conf  sleep.conf     system.conf  user
pi@rpiGarageOpener:~ $ ls /etc/systemd/network
99-default.link
pi@rpiGarageOpener:~ $ ls /etc/network
if-down.d  if-post-down.d  if-pre-up.d  if-up.d  interfaces  interfaces.d
pi@rpiGarageOpener:~ $ history | grep nano | grep conf
   49  sudo nano /etc/ssmtp/ssmtp.conf
   82  sudo nano /etc/apache2/apache2.conf
   83  sudo nano /etc/apache2/conf-enabled/*.conf
   84  sudo nano /etc/apache2/sites-enabled/*.conf
  117  history | grep nano | grep conf
pi@rpiGarageOpener:~ $ sudo nano /etc/fail2ban/jail.local
pi@rpiGarageOpener:~ $ cat /var/log/fail2ban.log
2020-12-06 00:00:10,553 fail2ban.server         [408]: INFO    rollover performed on /var/log/fail2ban.log
2020-12-06 07:17:49,973 fail2ban.server         [408]: INFO    Shutdown in progress...
2020-12-06 07:17:49,977 fail2ban.server         [408]: INFO    Stopping all jails
2020-12-06 07:17:49,980 fail2ban.filter         [408]: INFO    Removed logfile: '/var/log/auth.log'
2020-12-06 07:17:50,489 fail2ban.actions        [408]: NOTICE  [sshd] Flush ticket(s) with iptables-multiport
2020-12-06 07:17:50,492 fail2ban.jail           [408]: INFO    Jail 'sshd' stopped
2020-12-06 07:17:50,497 fail2ban.database       [408]: INFO    Connection to database closed.
2020-12-06 07:17:50,499 fail2ban.server         [408]: INFO    Exiting Fail2ban
2020-12-06 07:18:39,405 fail2ban.server         [399]: INFO    --------------------------------------------------
2020-12-06 07:18:39,448 fail2ban.server         [399]: INFO    Starting Fail2ban v0.10.2
2020-12-06 07:18:39,585 fail2ban.database       [399]: INFO    Connected to fail2ban persistent database '/var/lib/fail2ban/fail2ban.sqlite3'
2020-12-06 07:18:39,686 fail2ban.jail           [399]: INFO    Creating new jail 'sshd'
2020-12-06 07:18:40,349 fail2ban.jail           [399]: INFO    Jail 'sshd' uses pyinotify {}
2020-12-06 07:18:40,463 fail2ban.jail           [399]: INFO    Initiated 'pyinotify' backend
2020-12-06 07:18:40,487 fail2ban.filter         [399]: INFO      maxLines: 1
2020-12-06 07:18:42,190 fail2ban.server         [399]: INFO    Jail sshd is not a JournalFilter instance
2020-12-06 07:18:42,242 fail2ban.filter         [399]: INFO    Added logfile: '/var/log/auth.log' (pos = 69969, hash = 8f440a6da5614f7005c06b85e29e00b5f6d43745)
2020-12-06 07:18:42,397 fail2ban.filter         [399]: INFO      encoding: UTF-8
2020-12-06 07:18:42,401 fail2ban.filter         [399]: INFO      maxRetry: 5
2020-12-06 07:18:42,414 fail2ban.filter         [399]: INFO      findtime: 600
2020-12-06 07:18:42,429 fail2ban.actions        [399]: INFO      banTime: 600
2020-12-06 07:18:42,481 fail2ban.jail           [399]: INFO    Jail 'sshd' started
2020-12-08 06:17:49,258 fail2ban.server         [406]: INFO    --------------------------------------------------
2020-12-08 06:17:49,306 fail2ban.server         [406]: INFO    Starting Fail2ban v0.10.2
2020-12-08 06:17:49,591 fail2ban.database       [406]: INFO    Connected to fail2ban persistent database '/var/lib/fail2ban/fail2ban.sqlite3'
2020-12-08 06:17:49,697 fail2ban.jail           [406]: INFO    Creating new jail 'sshd'
2020-12-08 06:17:50,300 fail2ban.jail           [406]: INFO    Jail 'sshd' uses pyinotify {}
2020-12-08 06:17:50,389 fail2ban.jail           [406]: INFO    Initiated 'pyinotify' backend
2020-12-08 06:17:50,416 fail2ban.filter         [406]: INFO      maxLines: 1
2020-12-08 06:17:52,057 fail2ban.server         [406]: INFO    Jail sshd is not a JournalFilter instance
2020-12-08 06:17:52,075 fail2ban.filter         [406]: INFO    Added logfile: '/var/log/auth.log' (pos = 538250, hash = 8f440a6da5614f7005c06b85e29e00b5f6d43745)
2020-12-08 06:17:52,210 fail2ban.filter         [406]: INFO      encoding: UTF-8
2020-12-08 06:17:52,214 fail2ban.filter         [406]: INFO      maxRetry: 5
2020-12-08 06:17:52,223 fail2ban.filter         [406]: INFO      findtime: 600
2020-12-08 06:17:52,229 fail2ban.actions        [406]: INFO      banTime: 600
2020-12-08 06:17:52,284 fail2ban.jail           [406]: INFO    Jail 'sshd' started
2020-12-11 06:55:39,499 fail2ban.server         [406]: INFO    Shutdown in progress...
2020-12-11 06:55:39,508 fail2ban.server         [406]: INFO    Stopping all jails
2020-12-11 06:55:39,511 fail2ban.filter         [406]: INFO    Removed logfile: '/var/log/auth.log'
2020-12-11 06:55:40,023 fail2ban.actions        [406]: NOTICE  [sshd] Flush ticket(s) with iptables-multiport
2020-12-11 06:55:40,131 fail2ban.jail           [406]: INFO    Jail 'sshd' stopped
2020-12-11 06:55:40,138 fail2ban.database       [406]: INFO    Connection to database closed.
2020-12-11 06:55:40,141 fail2ban.server         [406]: INFO    Exiting Fail2ban
2020-12-11 06:56:28,124 fail2ban.server         [392]: INFO    --------------------------------------------------
2020-12-11 06:56:28,166 fail2ban.server         [392]: INFO    Starting Fail2ban v0.10.2
2020-12-11 06:56:28,722 fail2ban.database       [392]: INFO    Connected to fail2ban persistent database '/var/lib/fail2ban/fail2ban.sqlite3'
2020-12-11 06:56:28,849 fail2ban.jail           [392]: INFO    Creating new jail 'sshd'
2020-12-11 06:56:29,804 fail2ban.jail           [392]: INFO    Jail 'sshd' uses pyinotify {}
2020-12-11 06:56:29,989 fail2ban.jail           [392]: INFO    Initiated 'pyinotify' backend
2020-12-11 06:56:30,027 fail2ban.filter         [392]: INFO      maxLines: 1
2020-12-11 06:56:32,619 fail2ban.server         [392]: INFO    Jail sshd is not a JournalFilter instance
2020-12-11 06:56:32,638 fail2ban.filter         [392]: INFO    Added logfile: '/var/log/auth.log' (pos = 1225855, hash = 8f440a6da5614f7005c06b85e29e00b5f6d43745)
2020-12-11 06:56:32,920 fail2ban.filter         [392]: INFO      encoding: UTF-8
2020-12-11 06:56:32,938 fail2ban.filter         [392]: INFO      maxRetry: 5
2020-12-11 06:56:32,944 fail2ban.filter         [392]: INFO      findtime: 600
2020-12-11 06:56:32,959 fail2ban.actions        [392]: INFO      banTime: 600
2020-12-11 06:56:33,059 fail2ban.jail           [392]: INFO    Jail 'sshd' started
2020-12-11 12:55:59,491 fail2ban.server         [387]: INFO    --------------------------------------------------
2020-12-11 12:55:59,537 fail2ban.server         [387]: INFO    Starting Fail2ban v0.10.2
2020-12-11 12:55:59,792 fail2ban.database       [387]: INFO    Connected to fail2ban persistent database '/var/lib/fail2ban/fail2ban.sqlite3'
2020-12-11 12:55:59,969 fail2ban.jail           [387]: INFO    Creating new jail 'sshd'
2020-12-11 12:56:01,253 fail2ban.jail           [387]: INFO    Jail 'sshd' uses pyinotify {}
2020-12-11 12:56:01,524 fail2ban.jail           [387]: INFO    Initiated 'pyinotify' backend
2020-12-11 12:56:01,587 fail2ban.filter         [387]: INFO      maxLines: 1
2020-12-11 12:56:04,474 fail2ban.server         [387]: INFO    Jail sshd is not a JournalFilter instance
2020-12-11 12:56:04,496 fail2ban.filter         [387]: INFO    Added logfile: '/var/log/auth.log' (pos = 1282429, hash = 8f440a6da5614f7005c06b85e29e00b5f6d43745)
2020-12-11 12:56:06,443 fail2ban.filter         [387]: INFO      encoding: UTF-8
2020-12-11 12:56:06,456 fail2ban.filter         [387]: INFO      maxRetry: 5
2020-12-11 12:56:06,465 fail2ban.filter         [387]: INFO      findtime: 600
2020-12-11 12:56:06,493 fail2ban.actions        [387]: INFO      banTime: 600
2020-12-11 12:56:06,565 fail2ban.jail           [387]: INFO    Jail 'sshd' started
pi@rpiGarageOpener:~ $ fail2ban-client status
 Permission denied to socket: /var/run/fail2ban/fail2ban.sock, (you must be root)
pi@rpiGarageOpener:~ $ sudo fail2ban-client status
Status
|- Number of jail:	1
`- Jail list:	sshd
pi@rpiGarageOpener:~ $ sudo fail2ban-client status sshd
Status for the jail: sshd
|- Filter
|  |- Currently failed:	0
|  |- Total failed:	0
|  `- File list:	/var/log/auth.log
`- Actions
   |- Currently banned:	0
   |- Total banned:	0
   `- Banned IP list:	
pi@rpiGarageOpener:~ $ pwd
/home/pi
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~ $ ls -li 
total 152
257072 drwxr-xr-x 12 pi   pi    4096 Dec  9 06:58 api
  1309 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:40 Bookshelf
  5664 -rw-r--r--  1 root root   301 Dec  6 15:16 b.sh
  2213 -rw-r--r--  1 pi   pi   10701 Nov 22 08:59 check_apache.html
  2328 -rw-r--r--  1 pi   pi    1974 Nov 29 07:24 createDB.sh
  4944 -rw-r--r--  1 pi   pi     119 Dec  6 15:06 dead.letter
257030 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Desktop
257044 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Documents
257041 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Downloads
  4945 -rwxr-xr-x  1 root root   686 Dec  6 20:12 emailTry.py
267874 -rw-r--r--  1 pi   pi     163 Dec  6 11:13 genID.py
  5655 -rw-r--r--  1 pi   pi     727 Nov 30 14:18 getScripts2.sh
  4866 -rw-r--r--  1 pi   pi     453 Nov 30 14:19 getScripts.sh
  5043 -rw-r--r--  1 pi   pi     815 Nov 28 22:03 getWebsite.sh
  5227 -rwxr-xr-x  1 root root   178 Nov 26 16:19 hello.py
257045 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Music
  5684 -rw-r--r--  1 pi   pi       8 Dec  6 17:48 myID.txt
257046 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Pictures
257043 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Public
  5215 -rwxr-xr-x  1 root root   218 Nov 26 12:46 pushGarageRemote.py
  5330 -rwxr-xr-x  1 root root  1564 Nov 30 15:16 read.py
  5643 -rw-rw-rw-  1 pi   pi   25467 Dec 11 12:55 rpi-echo.log
  5644 -rw-r--r--  1 root root   456 Nov 29 19:13 rpi-echo.service
  5658 -rwxr-xr-x  1 pi   pi    2907 Dec  6 07:17 simple-fan.py
  5139 -rw-r--r--  1 root root  3230 Dec  2 14:10 simple-fan.py.1
257042 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Templates
  2590 -rw-r--r--  1 pi   pi    1471 Nov 22 09:51 tls2.sh
  3468 -rw-r--r--  1 root root  1224 Nov 22 09:33 tls.sh
  2367 -rwxr-xr-x  1 root root   972 Nov 22 08:24 unused_rpi.sh
257047 drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Videos
pi@rpiGarageOpener:~ $ ls -la
total 216
drwxr-xr-x 16 pi   pi    4096 Dec 11 12:55 .
drwxr-xr-x  3 root root  4096 Aug 20 05:31 ..
drwxr-xr-x 12 pi   pi    4096 Dec  9 06:58 api
-rw-------  1 pi   pi    2405 Dec  8 20:40 .bash_history
-rw-r--r--  1 pi   pi     220 Aug 20 05:31 .bash_logout
-rw-r--r--  1 pi   pi    3523 Aug 20 05:31 .bashrc
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:40 Bookshelf
-rw-r--r--  1 root root   301 Dec  6 15:16 b.sh
drwxr-xr-x  6 pi   pi    4096 Dec  5 15:47 .cache
-rw-r--r--  1 pi   pi   10701 Nov 22 08:59 check_apache.html
drwx------  3 pi   pi    4096 Aug 20 05:55 .config
-rw-r--r--  1 pi   pi    1974 Nov 29 07:24 createDB.sh
-rw-r--r--  1 pi   pi     119 Dec  6 15:06 dead.letter
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Desktop
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Documents
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Downloads
-rwxr-xr-x  1 root root   686 Dec  6 20:12 emailTry.py
-rw-r--r--  1 pi   pi     163 Dec  6 11:13 genID.py
-rw-r--r--  1 pi   pi     727 Nov 30 14:18 getScripts2.sh
-rw-r--r--  1 pi   pi     453 Nov 30 14:19 getScripts.sh
-rw-r--r--  1 pi   pi     815 Nov 28 22:03 getWebsite.sh
drwx------  3 pi   pi    4096 Aug 20 05:55 .gnupg
-rwxr-xr-x  1 root root   178 Nov 26 16:19 hello.py
drwxr-xr-x  5 pi   pi    4096 Dec  5 15:47 .local
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Music
-rw-r--r--  1 pi   pi       8 Dec  6 17:48 myID.txt
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Pictures
-rw-r--r--  1 pi   pi     807 Aug 20 05:31 .profile
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Public
-rwxr-xr-x  1 root root   218 Nov 26 12:46 pushGarageRemote.py
-rw-------  1 pi   pi     715 Dec  6 11:12 .python_history
-rwxr-xr-x  1 root root  1564 Nov 30 15:16 read.py
-rw-rw-rw-  1 pi   pi   25467 Dec 11 12:55 rpi-echo.log
-rw-r--r--  1 root root   456 Nov 29 19:13 rpi-echo.service
-rwxr-xr-x  1 pi   pi    2907 Dec  6 07:17 simple-fan.py
-rw-r--r--  1 root root  3230 Dec  2 14:10 simple-fan.py.1
-rw-------  1 pi   pi     917 Nov 29 13:47 .sqlite_history
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Templates
-rw-r--r--  1 pi   pi    1471 Nov 22 09:51 tls2.sh
-rw-r--r--  1 root root  1224 Nov 22 09:33 tls.sh
-rwxr-xr-x  1 root root   972 Nov 22 08:24 unused_rpi.sh
drwxr-xr-x  2 pi   pi    4096 Aug 20 05:55 Videos
-rw-r--r--  1 pi   pi     215 Dec  6 08:57 .wget-hsts
-rw-------  1 pi   pi     116 Dec 11 12:55 .Xauthority
-rw-------  1 pi   pi    2317 Dec 11 12:56 .xsession-errors
-rw-------  1 pi   pi    2317 Dec 11 06:56 .xsession-errors.old
pi@rpiGarageOpener:~ $ sudo nano /etc/host.conf
pi@rpiGarageOpener:~ $ sudo nano /etc/sysctl.conf
pi@rpiGarageOpener:~ $ cat /etc/cron.weekly/
cat: /etc/cron.weekly/: Is a directory
pi@rpiGarageOpener:~ $ ls /etc/cron.weekly/
00logwatch  chkrootkit  man-db  rkhunter_run  rkhunter_update
pi@rpiGarageOpener:~ $ ls /etc/cron.weekly/00logwatch
/etc/cron.weekly/00logwatch
pi@rpiGarageOpener:~ $ cat /etc/cron.weekly/00logwatch
#!/bin/bash

#Check if removed-but-not-purged
test -x /usr/share/logwatch/scripts/logwatch.pl || exit 0

#execute
# /usr/sbin/logwatch --output mail
/usr/sbin/logwatch --output mail --range 'between -7 days and -1 days'

#Note: It's possible to force the recipient in above command
#Just pass --mailto address@a.com instead of --output mail
pi@rpiGarageOpener:~ $ openssl ciphers -v | awk '{print $2}' | sort | uniq
SSLv3
TLSv1
TLSv1.2
TLSv1.3
pi@rpiGarageOpener:~ $ history | grep server
   59  history | grep server
   60  python3 rest_server.py
   64  python3 rest_server.py
   66  python3 rest_server.py
   67  sudo python3 rest_server.py
   68  sudo python rest_server.py
   69  sudo python3 rest_server.py
   72  sudo python3 rest_server.py
   76  nano rest_server.py
   78  nano rest_server.py
   79  sudo python3 rest_server.py -s
   80  sudo python3 rest_server.py 
   86  ls /usr/bin/rest_server.py
   87  ls -l /usr/bin/rest_server.py
   89  sudo nano /usr/bin/rest_server.py
   92  cat rest_server.log
   94  sudo nano /usr/bin/rest_server.py
  101  sudo nano /usr/bin/rest_server.py
  102  cat /home/pi/api/server_cron.sh
  105  cat rest_server.log
  134  history | grep server
pi@rpiGarageOpener:~ $ ls /var
backups  cache  lib  local  lock  log  mail  opt  run  spool  swap  tmp  www
pi@rpiGarageOpener:~ $ ls /var/html
ls: cannot access '/var/html': No such file or directory
pi@rpiGarageOpener:~ $ ls /www
ls: cannot access '/www': No such file or directory
pi@rpiGarageOpener:~ $ ls /www
ls: cannot access '/www': No such file or directory
pi@rpiGarageOpener:~ $ ls /var/www
db  html  html.
pi@rpiGarageOpener:~ $ ls /var/www/html
cpu  css  GarageDoor.pdf  img  index2.html  index.php  old  schedule.php
pi@rpiGarageOpener:~ $ ls /var/www/html/cpu
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~ $ pwd
/home/pi
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~ $ ls api
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~/api $ python3 rest_server.py
python3: can't open file 'rest_server.py': [Errno 2] No such file or directory
pi@rpiGarageOpener:~/api $ ls ..
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~/api $ ls ../rest*
ls: cannot access '../rest*': No such file or directory
pi@rpiGarageOpener:~/api $ ls ../rest*.py
ls: cannot access '../rest*.py': No such file or directory
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~/api $ ls server
pi@rpiGarageOpener:~/api $ ls restful_api
pi@rpiGarageOpener:~/api $ ls /usr/local/bin
close.py   distro     fauxmo.pyc  mylog.py   open.py      sleep.py
disarm.py  fauxmo.py  garage.sh   mylog.pyc  rpi-echo.py  toggle.py
pi@rpiGarageOpener:~/api $ ls /usr/local/
bin  etc  games  include  lib  man  sbin  share  src
pi@rpiGarageOpener:~/api $ ls /var/www
db  html  html.
pi@rpiGarageOpener:~/api $ ls /var/www/html
cpu  css  GarageDoor.pdf  img  index2.html  index.php  old  schedule.php
pi@rpiGarageOpener:~/api $ ls /var/www/html.
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ sudo rm /var/www/html.
rm: cannot remove '/var/www/html.': Is a directory
pi@rpiGarageOpener:~/api $ sudo rm -r /var/www/html.
pi@rpiGarageOpener:~/api $ ls /var/www
db  html
pi@rpiGarageOpener:~/api $ ls /var/www/html
cpu  css  GarageDoor.pdf  img  index2.html  index.php  old  schedule.php
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server.crt  uptime
client.key  favicon.png  get.py    navigation  reboot       server           server.key
cpu         get.backup   get.txt   os          restful_api  server_cron.sh   time
pi@rpiGarageOpener:~/api $ ls ..
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~/api $ ls /usr
bin  games  include  lib  local  sbin  share  src
pi@rpiGarageOpener:~/api $ ls /usr/sbin
a2disconf              ebtables                     iptables-translate          setvesablank
a2dismod               ebtables-nft                 ispell-autobuildhash        split-logfile
a2dissite              ebtables-nft-restore         ldattach                    sshd
a2enconf               ebtables-nft-save            lightdm                     ssmtp
a2enmod                ebtables-restore             lightdm-gtk-greeter         start-statd
a2ensite               ebtables-save                locale-gen                  tarcat
a2query                fdformat                     logrotate                   tcptraceroute
accessdb               filefrag                     logwatch                    tcptraceroute.db
addgnupghome           flashrom                     maidag                      th-cmd
addgroup               genl                         mailq                       thd
add-shell              gnome-menus-blacklist        make-ssl-cert               traceroute
adduser                groupadd                     mkinitramfs                 tzconfig
alsabat-test           groupdel                     mklost+found                ufw
alsactl                groupmems                    mountstats                  unhide
alsa-info              groupmod                     newaliases                  unhide-linux
apache2                grpck                        newusers                    unhide-posix
apache2ctl             grpconv                      nfnl_osf                    unhide.rb
apachectl              grpunconv                    nfsidmap                    unhide_rb
applygnupgdefaults     httxt2dbm                    nfsiostat                   unhide-tcp
arp                    i2cdetect                    nfsstat                     update-ca-certificates
arpd                   i2cdump                      nologin                     update-catalog
arptables              i2cget                       pam-auth-update             update-default-aspell
arptables-nft          i2cset                       pam_getenv                  update-default-ispell
arptables-nft-restore  i2c-stub-from-dump           pam_timestamp_check         update-default-wordlist
arptables-nft-save     i2ctransfer                  paperconfig                 update-dictcommon-aspell
arptables-restore      iconvconfig                  phpdismod                   update-dictcommon-hunspell
arptables-save         in.identtestd                phpenmod                    update-icon-caches
aspell-autobuildhash   install-sgmlcatalog          phpquery                    update-info-dir
avahi-daemon           invoke-rc.d                  pi-greeter                  update-initramfs
blkmapd                ip6tables                    plymouth-set-default-theme  update-locale
bluetoothd             ip6tables-apply              pwck                        update-mime
check_forensic         ip6tables-legacy             pwconv                      update-passwd
chgpasswd              ip6tables-legacy-restore     pwunconv                    update-pciids
chklastlog             ip6tables-legacy-save        readprofile                 update-rc.d
chkrootkit             ip6tables-nft                remove-default-ispell       update-xmlcatalog
chkwtmp                ip6tables-nft-restore        remove-default-wordlist     usb_modeswitch
chmem                  ip6tables-nft-save           remove-shell                usb_modeswitch_dispatcher
chpasswd               ip6tables-restore            rfkill                      useradd
chroot                 ip6tables-restore-translate  rmt                         userdel
cifs.idmap             ip6tables-save               rmt-tar                     usermod
cifs.upcall            ip6tables-translate          rngd                        v4l2-dbg
cpgr                   iptables                     rpcdebug                    validlocale
cppw                   iptables-apply               rpc.gssd                    vcstime
cron                   iptables-legacy              rpc.idmapd                  vigr
delgroup               iptables-legacy-restore      rpcinfo                     vipw
deluser                iptables-legacy-save         rpc.svcgssd                 visudo
dmidecode              iptables-nft                 rsyslogd                    xtables-legacy-multi
dpkg-preconfigure      iptables-nft-restore         rtcwake                     xtables-monitor
dpkg-reconfigure       iptables-nft-save            select-default-ispell       xtables-nft-multi
e2freefrag             iptables-restore             select-default-wordlist     zic
e4crypt                iptables-restore-translate   sendmail
e4defrag               iptables-save                service
pi@rpiGarageOpener:~/api $ ls /usr
bin  games  include  lib  local  sbin  share  src
pi@rpiGarageOpener:~/api $ ls /usr/bin
'['                                       gettext                            python3.7m
 2to3-2.7                                 gettext.sh                         python3.7m-config
 ab                                       ginstall-info                      python3-config
 aconnect                                 gio                                python3m
 addpart                                  gio-querymodules                   python3m-config
 addr2line                                git                                python-config
 agnostics                                git-receive-pack                   pyvenv
 alacarte                                 git-shell                          pyvenv-3.7
 alsabat                                  git-upload-archive                 pyversions
 alsaloop                                 git-upload-pack                    qpdfview
 alsamixer                                glib-compile-schemas               qt5ct
 alsatplg                                 gnome-www-browser                  qt-faststart
 alsaucm                                  gold                               qvlc
 amidi                                    gpasswd                            rake
 amixer                                   gpg                                ranlib
 aplay                                    gpg-agent                          raspi-config
 aplaymidi                                gpgcompose                         raspi-gpio
 appres                                   gpgconf                            raspinfo
 apropos                                  gpg-connect-agent                  raspistill
 apt                                      gpgparsemail                       raspivid
 apt-cache                                gpgsm                              raspividyuv
 apt-cdrom                                gpgsplit                           raspiyuv
 apt-config                               gpgtar                             rc_gui
 apt-extracttemplates                     gpgv                               rcp
 apt-ftparchive                           gpg-wks-server                     rctest
 apt-get                                  gpg-zip                            rdma
 aptitude                                 gpic                               rdoc
 aptitude-create-state-bundle             gpio                               rdoc2.5
 aptitude-curses                          gprof                              rds-ctl
 aptitude-run-state-bundle                gresource                          readelf
 apt-key                                  groff                              readmsg
 apt-listchanges                          grog                               readmsg.mailutils
 apt-mark                                 grops                              realpath
 apt-sortpkgs                             grotty                             rename.ul
 ar                                       groups                             renice
 arandr                                   gsettings                          reset
 arch                                     gtbl                               resizepart
 arecord                                  gtf                                resolvectl
 arecordmidi                              gtk-update-icon-cache              rest_server.py
 arm-linux-gnueabihf-addr2line            h2ph                               rev
 arm-linux-gnueabihf-ar                   h2xs                               rfcomm
 arm-linux-gnueabihf-as                   hardlink                           rgrep
 arm-linux-gnueabihf-c++filt              hciattach                          ri
 arm-linux-gnueabihf-cpp                  hcitool                            ri2.5
 arm-linux-gnueabihf-cpp-8                hd                                 rkhunter
 arm-linux-gnueabihf-dwp                  head                               rlogin
 arm-linux-gnueabihf-elfedit              helpztags                          rngtest
 arm-linux-gnueabihf-g++                  hex2hcd                            rotatelogs
 arm-linux-gnueabihf-g++-8                hexdump                            routef
 arm-linux-gnueabihf-gcc                  host                               routel
 arm-linux-gnueabihf-gcc-8                hostid                             rp-bookshelf
 arm-linux-gnueabihf-gcc-ar               hostnamectl                        rpcgen
 arm-linux-gnueabihf-gcc-ar-8             htcacheclean                       rpcinfo
 arm-linux-gnueabihf-gcc-nm               htdbm                              rpi-eeprom-config
 arm-linux-gnueabihf-gcc-nm-8             htdigest                           rpi-eeprom-update
 arm-linux-gnueabihf-gcc-ranlib           htop                               rpimonitord
 arm-linux-gnueabihf-gcc-ranlib-8         htpasswd                           rpi-update
 arm-linux-gnueabihf-gcov                 iceauth                            rp-prefapps
 arm-linux-gnueabihf-gcov-8               iconv                              rsh
 arm-linux-gnueabihf-gcov-dump            id                                 rst2html
 arm-linux-gnueabihf-gcov-dump-8          iecset                             rst2html4
 arm-linux-gnueabihf-gcov-tool            info                               rst2html5
 arm-linux-gnueabihf-gcov-tool-8          infobrowser                        rst2latex
 arm-linux-gnueabihf-gold                 infocmp                            rst2man
 arm-linux-gnueabihf-gprof                infotocap                          rst2odt
 arm-linux-gnueabihf-ld                   install                            rst2odt_prepstyles
 arm-linux-gnueabihf-ld.bfd               install-info                       rst2pseudoxml
 arm-linux-gnueabihf-ld.gold              instmodsh                          rst2s5
 arm-linux-gnueabihf-nm                   ionice                             rst2xetex
 arm-linux-gnueabihf-objcopy              ipcmk                              rst2xml
 arm-linux-gnueabihf-objdump              ipcrm                              rst-buildhtml
 arm-linux-gnueabihf-pkg-config           ipcs                               rstpep2html
 arm-linux-gnueabihf-python2.7-config     iptables-xml                       rsync
 arm-linux-gnueabihf-python2-config       irb                                RTIMULibCal
 arm-linux-gnueabihf-python3.7-config     irb2.5                             RTIMULibDrive11
 arm-linux-gnueabihf-python3.7m-config    ir-ctl                             rtstat
 arm-linux-gnueabihf-python3-config       ischroot                           ruby
 arm-linux-gnueabihf-python3m-config      ispell-wrapper                     ruby2.5
 arm-linux-gnueabihf-python-config        ivtv-ctl                           runcon
 arm-linux-gnueabihf-ranlib               join                               run-mailcap
 arm-linux-gnueabihf-readelf              json_pp                            run-with-aspell
 arm-linux-gnueabihf-run                  json_xs                            rview
 arm-linux-gnueabihf-size                 kbdinfo                            rvlc
 arm-linux-gnueabihf-strings              kbxutil                            savelog
 arm-linux-gnueabihf-strip                kernel-install                     scp
 arm-unknown-linux-gnueabihf-pkg-config   keyring                            screendump
 as                                       killall                            script
 aseqdump                                 l2ping                             scriptreplay
 aseqnet                                  l2test                             scrot
 aspell                                   laptop-detect                      sdiff
 aspell-import                            last                               sdptool
 awk                                      lastb                              see
 axfer                                    lastlog                            select-default-iwrap
 b2sum                                    lcf                                select-editor
 base32                                   ld                                 sensible-browser
 base64                                   ld.bfd                             sensible-editor
 basename                                 ldd                                sensible-pager
 bashbug                                  ld.gold                            seq
 bccmd                                    less                               sessreg
 bdaddr                                   lessecho                           setarch
 bluealsa                                 lessfile                           setcifsacl
 bluealsa-aplay                           lesskey                            setkeycodes
 bluemoon                                 lesspipe                           setleds
 bluetoothctl                             lexgrog                            setlogcons
 bootctl                                  lft                                setmetamode
 bsd-from                                 lft.db                             setpci
 bsd-mailx                                libnetcfg                          setpriv
 bsd-write                                libpng16-config                    setsid
 btattach                                 libpng-config                      setterm
 bthelper                                 link                               setvtrgb
 btmgmt                                   linux32                            setxkbmap
 btmon                                    linux64                            sftp
 btuart                                   linux-check-removal                sg
 busctl                                   linux-update-symlinks              sha1sum
 bwrap                                    linux-version                      sha224sum
 c++                                      listres                            sha256sum
 c89                                      lnstat                             sha384sum
 c89-gcc                                  loadkeys                           sha512sum
 c99                                      loadunimap                         shasum
 c99-gcc                                  locale                             showconsolefont
 cal                                      localectl                          showkey
 calendar                                 localedef                          showrgb
 captoinfo                                logger                             shred
 catchsegv                                logilab-pytest3                    shuf
 catman                                   logname                            sieve
 cc                                       logresolve                         size
 cec-compliance                           look                               skill
 cec-ctl                                  lorder                             slabtop
 cec-follower                             lsattr                             slogin
 c++filt                                  lsb_release                        snice
 chage                                    lscpu                              soelim
 chardet                                  lsinitramfs                        sort
 chardet3                                 lsipc                              sotruss
 chardetect                               lslocks                            speaker-test
 chardetect3                              lslogins                           splain
 chattr                                   lsmem                              split
 chcon                                    lsns                               splitfont
 checkgid                                 lsof                               sprof
 check-language-support                   lspci                              sqldiff
 chfn                                     lspgpot                            sqlite3
 choom                                    lsusb                              ssh
 chromium-browser                         lua                                ssh-add
 chrt                                     lua5.1                             ssh-agent
 chsh                                     luac                               ssh-argv0
 cifscreds                                luac5.1                            ssh-copy-id
 ciptool                                  luajit                             ssh-import-id
 ckbcomp                                  luit                               ssh-import-id-gh
 cksum                                    lxappearance                       ssh-import-id-lp
 clear                                    lxclipboard                        ssh-keygen
 clear_console                            lxde-logout                        ssh-keyscan
 cmp                                      lxde-pi-shutdown-helper            startlxde
 codepage                                 lxhotkey                           startlxde-pi
 col                                      lxinput                            startx
 colcrt                                   lxpanel                            stat
 colour_to_gtk3                           lxpanelctl                         stdbuf
 colour_to_obconf                         lxpolkit                           strace
 colrm                                    lxrandr                            strace-log-merge
 column                                   lxsession                          strings
 comm                                     lxsession-db                       strip
 compose                                  lxsession-default                  stubgen
 convert-dtsv0                            lxsession-default-terminal         sudo
 corelist                                 lxsession-edit                     sudoedit
 cpan                                     lxsession-logout                   sudoreplay
 cpan5.28-arm-linux-gnueabihf             lxsession-xdg-autostart            sum
 cpp                                      lxtask                             svlc
 cpp-8                                    lxterminal                         symcryptrun
 c_rehash                                 lzcat                              symilar3
 crontab                                  lzcmp                              systemd-analyze
 csplit                                   lzdiff                             systemd-cat
 ctstat                                   lzegrep                            systemd-cgls
 curl                                     lzfgrep                            systemd-cgtop
 cut                                      lzgrep                             systemd-delta
 cvlc                                     lzless                             systemd-detect-virt
 cvt                                      lzma                               systemd-id128
 cvtsudoers                               lzmainfo                           systemd-mount
 cx18-ctl                                 lzmore                             systemd-path
 dbus-cleanup-sockets                     mail                               systemd-resolve
 dbus-daemon                              Mail                               systemd-run
 dbus-launch                              mail.mailutils                     systemd-socket-activate
 dbus-monitor                             mailx                              systemd-stdio-bridge
 dbus-run-session                         make                               systemd-umount
 dbus-send                                make-first-existing-target         tabs
 dbus-update-activation-environment       man                                tac
 dbus-uuidgen                             mandb                              tail
 dc                                       manpath                            tasksel
 ddcmon                                   mapscrn                            taskset
 deallocvt                                mawk                               tbl
 debconf                                  mcookie                            tee
 debconf-apt-progress                     md5sum                             test
 debconf-communicate                      md5sum.textutils                   thonny
 debconf-copydb                           media-ctl                          tic
 debconf-escape                           mesg                               timedatectl
 debconf-getlang                          messages                           timeout
 debconf-get-selections                   messages.mailutils                 tload
 debconf-loadtemplate                     migrate-pubring-from-classic-gpg   toe
 debconf-mergetemplate                    mimeview                           top
 debconf-set-selections                   miniterm                           touch
 debconf-show                             mkfifo                             tput
 debian-reference                         mk_modmap                          tr
 deb-systemd-helper                       mkpasswd                           traceproto
 deb-systemd-invoke                       mousepad                           traceproto.db
 decode-dimms                             movemail                           traceroute
 decode-edid                              movemail.mailutils                 traceroute6
 decode_tm6000                            mpris-proxy                        traceroute6.db
 decode-vaio                              mtrace                             traceroute.db
 delpart                                  mypy                               traceroute-nanog
 desktop-file-edit                        namei                              tree
 desktop-file-install                     nawk                               troff
 desktop-file-validate                    ncal                               truncate
 dh_bash-completion                       ncdu                               tset
 dh_installxmlcatalogs                    neqn                               tsort
 dh_numpy                                 newgrp                             tty
 dh_numpy3                                ngettext                           tvservice
 dh_pypy                                  nice                               tzselect
 dh_python2                               nl                                 ucf
 dh_python3                               nm                                 ucfq
 diff                                     nohup                              ucfr
 diff3                                    nproc                              udisksctl
 dircolors                                nroff                              ul
 dirmngr                                  nsenter                            unexpand
 dirmngr-client                           nstat                              unicode_stop
 dirname                                  ntfsdecrypt                        uniq
 dm-tool                                  numfmt                             unlink
 dmypy                                    nvlc                               unlzma
 dotlock                                  obamenu                            unmkinitramfs
 dotlockfile                              obconf                             unpigz
 dotlock.mailutils                        obexctl                            unshare
 dpkg                                     objcopy                            unxrandr
 dpkg-architecture                        objdump                            unxz
 dpkg-buildflags                          obxprop                            unzip
 dpkg-buildpackage                        od                                 unzipsfx
 dpkg-checkbuilddeps                      omxplayer                          update-alternatives
 dpkg-deb                                 omxplayer.bin                      update-desktop-database
 dpkg-distaddfile                         openbox                            update-mime-database
 dpkg-divert                              openbox-lxde                       uptime
 dpkg-genbuildinfo                        openbox-lxde-pi                    usb-devices
 dpkg-genchanges                          openbox-session                    usbhid-dump
 dpkg-gencontrol                          openssl                            usbreset
 dpkg-gensymbols                          pager                              users
 dpkg-maintscript-helper                  paperconf                          utmpdump
 dpkg-mergechangelogs                     parsechangelog                     uuid
 dpkg-name                                parse-edid                         v4l2-compliance
 dpkg-parsechangelog                      partx                              v4l2-ctl
 dpkg-query                               passwd                             v4l2-sysfs-path
 dpkg-scanpackages                        paste                              vcdbg
 dpkg-scansources                         patch                              vcgencmd
 dpkg-shlibdeps                           pathchk                            vchiq_test
 dpkg-source                              pbr                                vi
 dpkg-split                               pcimodules                         view
 dpkg-statoverride                        pcmanfm                            viewres
 dpkg-trigger                             pdb                                vim.tiny
 dpkg-vendor                              pdb2                               vlc
 dtc                                      pdb2.7                             vlc-wrapper
 dtdiff                                   pdb3                               vmstat
 dtmerge                                  pdb3.7                             vncagent
 dtoverlay                                peekfd                             vncagent-raspi
 dtoverlay-post                           perf                               vncinitconfig
 dtoverlay-pre                            perl                               vnclicense
 dtparam                                  perl5.28.1                         vnclicensehelper
 du                                       perl5.28-arm-linux-gnueabihf       vnclicensewiz
 dumpkeys                                 perlbug                            vncpamhelper
 dwp                                      perldoc                            vncpasswd
 edidparser                               perlivp                            vncpipehelper
 edit                                     perlthanks                         vncserver
 editor                                   pgrep                              vncserverui
 editres                                  pgzrun                             vncserver-virtual
 eject                                    phar                               vncserver-virtuald
 elfedit                                  phar7.3                            vncserver-x11
 enc2xs                                   phar.phar                          vncserver-x11-core
 encguess                                 phar.phar7.3                       vncserver-x11-serviced
 env                                      php                                volname
 envsubst                                 php7.3                             w
 epylint3                                 pic                                wall
 eqn                                      piclone                            watch
 erb                                      pico                               watchgnupg
 erb2.5                                   piconv                             wc
 ex                                       pig2vcd                            wget
 expand                                   pigpiod                            whatis
 expiry                                   pi-gpk-dbus-service                whereis
 expr                                     pi-gpk-install-local-file          which
 f2py                                     pi-gpk-log                         whiptail
 f2py2.7                                  pi-gpk-prefs                       who
 f2py3                                    pi-gpk-update-viewer               whoami
 f2py3.7                                  pigs                               whois
 factor                                   pigz                               word-list-compress
 fail2ban-client                          pinentry                           wpa_passphrase
 fail2ban-python                          pinentry-curses                    w.procps
 fail2ban-regex                           pinky                              write
 fail2ban-server                          pinout                             X
 fail2ban-testcases                       pip                                X11
 faillog                                  pip2                               xarchiver
 faked-sysv                               pip3                               xargs
 faked-tcp                                pi-packages                        xauth
 fakeroot                                 pipanel                            xcmsdb
 fakeroot-sysv                            piwiz                              xcompmgr
 fakeroot-tcp                             pkaction                           xdg-dbus-proxy
 fallocate                                pkcheck                            xdg-desktop-icon
 fc-cache                                 pkexec                             xdg-desktop-menu
 fc-cat                                   pkg-config                         xdg-email
 fc-conflist                              pkill                              xdg-icon-resource
 fcgistarter                              pkttyagent                         xdg-mime
 fc-list                                  pl2pm                              xdg-open
 fc-match                                 pldd                               xdg-screensaver
 fc-pattern                               pmap                               xdg-settings
 fc-query                                 pngfix                             xdg-user-dir
 fc-scan                                  png-fix-itxt                       xdg-user-dirs-update
 fc-validate                              pod2html                           xdpyinfo
 fdtdump                                  pod2man                            xdriinfo
 fdtget                                   pod2text                           xev
 fdtoverlay                               pod2usage                          xfd
 fdtput                                   podchecker                         xfontsel
 ffmpeg                                   podselect                          xgamma
 ffplay                                   pr                                 xhost
 ffprobe                                  precat                             xinit
 file                                     preconv                            xinput
 fincore                                  preunzip                           xkbbell
 find                                     prezip                             xkbcomp
 fio                                      prezip-bin                         xkbevd
 fio2gnuplot                              print                              xkbprint
 fio-btrace2fio                           printenv                           xkbvleds
 fio-dedupe                               printerbanner                      xkbwatch
 fio_generate_plots                       printf                             xkeystone
 fio-genzipf                              prlimit                            xkill
 flask                                    prove                              xlsatoms
 flock                                    proxy                              xlsclients
 fmt                                      prtstat                            xlsfonts
 fold                                     psfaddtable                        xmessage
 free                                     psfgettable                        xmodmap
 frm                                      psfstriptable                      Xorg
 frm.mailutils                            psfxtable                          xprop
 from                                     pslog                              xrandr
 from.mailutils                           pstree                             xrdb
 funzip                                   pstree.x11                         xrefresh
 g++                                      ptar                               xsel
 g++-8                                    ptardiff                           x-session-manager
 galculator                               ptargrep                           xset
 gapplication                             ptx                                xsetmode
 gatttool                                 pwdx                               xsetpointer
 gcc                                      py3clean                           xsetroot
 gcc-8                                    py3compile                         xstdcmap
 gcc-ar                                   py3versions                        xsubpp
 gcc-ar-8                                 pybuild                            x-terminal-emulator
 gcc-nm                                   pyclean                            xvidtune
 gcc-nm-8                                 pycompile                          xvinfo
 gcc-ranlib                               pydoc                              Xvnc
 gcc-ranlib-8                             pydoc2                             Xvnc-core
 gcore                                    pydoc2.7                           x-window-manager
 gcov                                     pydoc3                             xwininfo
 gcov-8                                   pydoc3.7                           x-www-browser
 gcov-dump                                pygettext                          xxd
 gcov-dump-8                              pygettext2                         xz
 gcov-tool                                pygettext2.7                       xzcat
 gcov-tool-8                              pygettext3                         xzcmp
 gdb                                      pygettext3.7                       xzdiff
 gdb-add-index                            pygmentize                         xzegrep
 gdbtui                                   pyjwt                              xzfgrep
 gdbus                                    pyjwt3                             xzgrep
 gdialog                                  pylint3                            xzless
 gdm-control                              pypy                               xzmore
 geany                                    pypyclean                          yes
 gem                                      pypycompile                        zdump
 gem2.5                                   pyreverse3                         zenity
 gencat                                   python                             zip
 genfio                                   python2                            zipcloak
 geqn                                     python2.7                          zipdetails
 getcifsacl                               python2.7-config                   zipgrep
 getconf                                  python2-config                     zipinfo
 get-edid                                 python2-pbr                        zipnote
 getent                                   python3                            zipsplit
 getkeycodes                              python3.7
 getopt                                   python3.7-config
pi@rpiGarageOpener:~/api $ ls /usr/bin/rest*
/usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ cp /usr/bin/rest_server.py .
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ sudo nano rest_server.py
pi@rpiGarageOpener:~/api $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:~/api $ sudo crontab -e
No modification made
pi@rpiGarageOpener:~/api $ cat server_cron.sh
#!/bin/bash

HOME="/user/pi/api"
PIDFILE="$HOME/rest_server.pid"
# echo $PIDFILE

if [ -e "${PIDFILE}" ] && (ps -u $(whoami) -opid= | grep -P "^\s*$(cat ${PIDFILE})$" &> /dev/null); then
  # "rest_server.py is already running."
  # echo "already running"
  exit 99
fi

# echo "starting restserver"
/usr/bin/rest_server.py -msc
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
root      1173  0.0  3.2  21836 14248 ?        S    13:15   0:06 python3 /usr/bin/rest_server.py -msc
pi       10916  0.0  0.4   7336  1956 pts/0    S+   15:44   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo kill 1173
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
pi       10931  0.0  0.4   7336  2032 pts/0    S+   15:44   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/11 15:45:27 - Starting REST server
2020/12/11 15:45:27 - Command line arguments:
2020/12/11 15:45:27 -   Input file  = 
2020/12/11 15:45:27 -   Log file = /home/pi/api/rest_server.log
2020/12/11 15:45:27 -   Port = 9443
2020/12/11 15:45:27 -   Use cert = False
2020/12/11 15:45:27 -   Use HTTPS = False
2020/12/11 15:45:27 -   Use multithreading = False

2020/12/11 15:45:27 - Web Server:
2020/12/11 15:45:27 -   Server name = rpiGarageOpener
2020/12/11 15:45:27 -   Server IP = 127.0.1.1

2020/12/11 15:45:42 - Closing REST server
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^[[A^[[B
^Cpi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/11 15:49:05 - Starting REST server
2020/12/11 15:49:05 - Command line arguments:
2020/12/11 15:49:05 -   Input file  = 
2020/12/11 15:49:05 -   Log file = /home/pi/api/rest_server.log
2020/12/11 15:49:05 -   Port = 9443
2020/12/11 15:49:05 -   Use cert = False
2020/12/11 15:49:05 -   Use HTTPS = False
2020/12/11 15:49:05 -   Use multithreading = False

2020/12/11 15:49:05 - Web Server:
2020/12/11 15:49:05 -   Server name = rpiGarageOpener
2020/12/11 15:49:05 -   Server IP = 127.0.1.1

2020/12/11 15:49:21 - Closing REST server
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/11 15:50:16 - Starting REST server
2020/12/11 15:50:16 - Command line arguments:
2020/12/11 15:50:16 -   Input file  = 
2020/12/11 15:50:16 -   Log file = /home/pi/api/rest_server.log
2020/12/11 15:50:16 -   Port = 9443
2020/12/11 15:50:16 -   Use cert = False
2020/12/11 15:50:16 -   Use HTTPS = False
2020/12/11 15:50:16 -   Use multithreading = False

2020/12/11 15:50:16 - Web Server:
2020/12/11 15:50:16 -   Server name = rpiGarageOpener
2020/12/11 15:50:16 -   Server IP = 127.0.1.1

2020/12/11 15:50:29 - Closing REST server
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -h
Decription: 
  Server-side script for RESTful API sever written in python using json
  There are multiple ways for a client-side server to communicate with this server-side API:
    A client-side script can make HTTP requests (see rest_client.py)
    Open a browser and enter: http://security:9080/api/multi/10/23
    Open a terminal and run: $ curl -X GET http://security:9080/api/multi/10/23

Usage:
  python3 rest_server.py [options...]

Options:
  -h --help           this help
  -c --cert           Use cert, requires use https
  -i --inputfile      input json file
  -l --logfile        write log messages to user specified file
  -m --multithreading use multithreading
  -p --port           User defined port. The default port is9443.
  -s --secure         use https
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ ls navigation
get.json  get.py  get.py~  junk.json
pi@rpiGarageOpener:~/api $ cat navigation/get.py
# returns navigation for API
global Data
global Path

validVerbs  = "get put delete post"
data = '{ "directories" : [ '
# ??? need to remove /navigation
next = False

# excluded_prefixes = ('__', '.')
for paths, dirs, files in os.walk(Path):
    # exclude hidden folders and special files starting with excluded_prefixes
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    dirs[:] = [d for d in dirs if not d.startswith("__")]

    filenames = [f for f in files if not f.startswith(".")]
    filenames[:] = [f for f in files if not f.startswith("__")]

    if next:
        data += ', '

    schema = '"schema" : {}'
    verbs = '"verbs" : ['
    next_verb = False
    for f in filenames:
        if None != re.search('.py', f):
            verb = f[:len(f)-3]
            if validVerbs.find(verb) >= 0:
                if next_verb:
                    verbs += ', '
                file = paths + "/" + verb
                try:
                    # ??? how to get proper indentation
                    schema = '"schema" : { '
                    with open(file + ".json", "r") as read_file:
                        schema += read_file.read()
                        # ??? needs to read line at a time rather than the whole file
                    schema += '}'
                except:
                    schema = '"schema" : {}'

                try:
                    with open(file + ".txt", "r") as read_file:
                        description = read_file.read()
                except:
                    description = ''

                verb = verb.upper()
                verbs += '"' + verb + '"'
                next_verb = True

    verbs += '], '

    data += '{ '
    data += '    "abs" : "' + paths + '", '
    data += '    ' + verbs
    data += '    ' + description + ', '
    data += '    ' + schema
    data += '}'

    next = True

data += '] }'
print("\n\ndata = " +data)

Data = json.loads(data)
pi@rpiGarageOpener:~/api $ python3 rest_server.py -h
Decription: 
  Server-side script for RESTful API sever written in python using json
  There are multiple ways for a client-side server to communicate with this server-side API:
    A client-side script can make HTTP requests (see rest_client.py)
    Open a browser and enter: http://security:9080/api/multi/10/23
    Open a terminal and run: $ curl -X GET http://security:9080/api/multi/10/23

Usage:
  python3 rest_server.py [options...]

Options:
  -h --help           this help
  -c --cert           Use cert, requires use https
  -i --inputfile      input json file
  -l --logfile        write log messages to user specified file
  -m --multithreading use multithreading
  -p --port           User defined port. The default port is9443.
  -s --secure         use https
pi@rpiGarageOpener:~/api $ python3 rest_server.py 
^C
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/11 16:04:41 - Starting REST server
2020/12/11 16:04:41 - Command line arguments:
2020/12/11 16:04:41 -   Input file  = 
2020/12/11 16:04:41 -   Log file = /home/pi/api/rest_server.log
2020/12/11 16:04:41 -   Port = 9443
2020/12/11 16:04:41 -   Use cert = False
2020/12/11 16:04:41 -   Use HTTPS = False
2020/12/11 16:04:41 -   Use multithreading = False

2020/12/11 16:04:41 - Web Server:
2020/12/11 16:04:41 -   Server name = rpiGarageOpener
2020/12/11 16:04:41 -   Server IP = 127.0.1.1

2020/12/11 16:05:50 - Closing REST server
pi@rpiGarageOpener:~/api $ ls ..
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~/api $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ history | grep ssh
   70  ssh pi@security
   71  ssh pi@security.local
   72  ssh pi@security.local
   73  ssh pi@security
   75  ssh pi@security
   76  ssh pi@security
   77  ssh pi@security
   78  ssh pi@security
   79  ssh pi@security
   80  ssh pi@security
   81  ssh pi@security
   82  ssh pi@security
   83  ssh pi@doorbell
   84  ssh pi@raspberrypi
   95  touch ssh
  110  touch ssh
  113  ssh pi@raspberrypi.local
  114  ssh pi@raspberrypi.local
  115  ssh pi@rpiDoorbell.local
  116  ssh pi@rpiDoorbell.local
  117  ssh pi@rpiDoorbell.local
  118  ssh pi@rpiDoorbell.local
  119  ssh pi@rpiDoorbell.local
  120  ssh pi@rpiDoorbell.local
  121  ssh pi@rpiDoorbell.local
  122  ssh pi@rpiDoorbell.local
  124  ssh pi@rpiDoorbell.local
  125  ssh pi@rpiDoorbell.local
  126  ssh pi@rpiDoorbell.local
  127  ssh pi@rpiDoorbell.local
  128  ssh pi@rpiDoorbell.local
  129  ssh pi@rpiDoorbell.local
  130  ssh pi@rpiDoorbell.local
  131  ssh pi@rpiDoorbell.local
  132  ssh pi@rpiDoorbell.local
  133  ssh pi@rpiDoorbell.local
  134  ssh pi@rpiDoorbell.local
  135  ssh pi@rpiDoorbell.local
  136  ssh pi@rpiDoorbell.local
  137  ssh pi@rpiDoorbell.local
  138  ssh pi@rpiDoorbell.local
  140  ssh pi@rpiDoorbell.local
  141  ssh pi@rpiDoorbell.local
  142  ssh pi@rpiDoorbell.local
  143  ssh pi@rpiDoorbell.local
  144  ssh pi@rpiDoorbell.local
  145  ssh pi@rpiDoorbell.local
  146  ssh pi@rpiDoorbell.local
  147  ssh pi@rpiDoorbell.local
  148  ssh pi@rpiDoorbell.local
  149  ssh pi@rpiDoorbell.local
  150  ssh pi@rpiDoorbell.local
  151  ssh pi@rpiDoorbell.local
  153  ssh pi@rpiDoorbell.local
  155  ssh pi@rpiDoorbell.local
  156  ssh pi@rpiDoorbell.local
  157  ssh pi@rpiDoorbell.local
  159  ssh pi@rpiDoorbell.local
  160  ssh pi@rpiDoorbell.local
  161  ssh pi@rpiDoorbell.local
  162  ssh pi@rpiDoorbell.local
  163  ssh pi@rpiDoorbell.local
  164  ssh pi@rpiDoorbell.local
  165  ssh pi@rpiDoorbell.local
  166  ssh pi@rpiDoorbell.local
  167  ssh pi@rpiDoorbell.local
  168  ssh pi@rpiDoorbell.local
  169  ssh pi@rpiDoorbell.local
  170  ssh pi@rpiDoorbell.local
  499  touch ssh
  501  ssh pi@raspberry.local
  502  ssh pi@raspberrypi.local
  508  ssh pi@raspberrypi.local
  509  sudo nano /Users/jeff/.ssh/known_hosts
  510  ssh pi@raspberrypi.local
  511  sudo nano /Users/jeff/.ssh/known_hosts
  512  ssh pi@raspberrypi.local
  513  ssh pi@raspberrypi.local
  514  ssh pi@rpiGarageOpener.local
  515  ssh pi@rpiGarageOpener.local
  516  ssh pi@rpiGarageOpener.local
  518  ssh pi@rpiGarageOpener.local
  519  ssh pi@rpiGarageOpener.local
  520  ssh pi@rpiGarageOpener.local
  521  ssh pi@rpiGarageOpener.local
  522  ssh pi@rpiGarageOpener.local
  523  ssh pi@rpiGarageOpener.local
  524  ssh pi@rpiGarageOpener.local
  525  sudo nano /Users/jeff/.ssh/known_hosts
  526  ssh pi@rpiGarageOpener.local
  527  ssh pi@rpiGarageOpener.local
  528  ssh pi@rpiGarageOpener.local
  529  ssh pi@rpiGarageOpener.local
  531  ssh pi@rpiGarageOpener.local
  532  ssh pi@rpiGarageOpener.local
  533  ssh pi@rpiGarageOpener.local
  534  ssh pi@rpiGarageOpener.local
  535  ssh pi@rpiGarageOpener.local
  536  ssh pi@rpiGarageOpener.local
  538  ssh pi@rpiGarageOpener.local
  539  ssh pi@rpiGarageOpener.local
  541  ssh pi@rpiGarageOpener.local
  542  ssh pi@rpiGarageOpener.local
  545  ssh pi@rpiGarageOpener.local
  546  ssh pi@rpiGarageOpener.local
  547  ssh pi@rpiGarageOpener.local
  548  ssh pi@rpiGarageOpener.local
  549  ssh pi@GarageOpener.local
  550  ssh pi@rpiUnused.local
  551  ssh pi@GarageOpener.local
  552  ssh pi@rpiGarageOpener.local
  553  ssh pi@rpiGarageOpener.local
  555  ssh pi@rpiGarageOpener.local
  556  ssh pi@rpiGarageOpener.local
  557  ssh pi@rpiGarageOpener.local
  558  ssh pi@rpiGarageOpener.local
  559  history | grep ssh
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ history | grep ssh
   70  ssh pi@security
   71  ssh pi@security.local
   72  ssh pi@security.local
   73  ssh pi@security
   75  ssh pi@security
   76  ssh pi@security
   77  ssh pi@security
   78  ssh pi@security
   79  ssh pi@security
   80  ssh pi@security
   81  ssh pi@security
   82  ssh pi@security
   83  ssh pi@doorbell
   84  ssh pi@raspberrypi
   95  touch ssh
  110  touch ssh
  113  ssh pi@raspberrypi.local
  114  ssh pi@raspberrypi.local
  115  ssh pi@rpiDoorbell.local
  116  ssh pi@rpiDoorbell.local
  117  ssh pi@rpiDoorbell.local
  118  ssh pi@rpiDoorbell.local
  119  ssh pi@rpiDoorbell.local
  120  ssh pi@rpiDoorbell.local
  121  ssh pi@rpiDoorbell.local
  122  ssh pi@rpiDoorbell.local
  124  ssh pi@rpiDoorbell.local
  125  ssh pi@rpiDoorbell.local
  126  ssh pi@rpiDoorbell.local
  127  ssh pi@rpiDoorbell.local
  128  ssh pi@rpiDoorbell.local
  129  ssh pi@rpiDoorbell.local
  130  ssh pi@rpiDoorbell.local
  131  ssh pi@rpiDoorbell.local
  132  ssh pi@rpiDoorbell.local
  133  ssh pi@rpiDoorbell.local
  134  ssh pi@rpiDoorbell.local
  135  ssh pi@rpiDoorbell.local
  136  ssh pi@rpiDoorbell.local
  137  ssh pi@rpiDoorbell.local
  138  ssh pi@rpiDoorbell.local
  140  ssh pi@rpiDoorbell.local
  141  ssh pi@rpiDoorbell.local
  142  ssh pi@rpiDoorbell.local
  143  ssh pi@rpiDoorbell.local
  144  ssh pi@rpiDoorbell.local
  145  ssh pi@rpiDoorbell.local
  146  ssh pi@rpiDoorbell.local
  147  ssh pi@rpiDoorbell.local
  148  ssh pi@rpiDoorbell.local
  149  ssh pi@rpiDoorbell.local
  150  ssh pi@rpiDoorbell.local
  151  ssh pi@rpiDoorbell.local
  153  ssh pi@rpiDoorbell.local
  155  ssh pi@rpiDoorbell.local
  156  ssh pi@rpiDoorbell.local
  157  ssh pi@rpiDoorbell.local
  159  ssh pi@rpiDoorbell.local
  160  ssh pi@rpiDoorbell.local
  161  ssh pi@rpiDoorbell.local
  162  ssh pi@rpiDoorbell.local
  163  ssh pi@rpiDoorbell.local
  164  ssh pi@rpiDoorbell.local
  165  ssh pi@rpiDoorbell.local
  166  ssh pi@rpiDoorbell.local
  167  ssh pi@rpiDoorbell.local
  168  ssh pi@rpiDoorbell.local
  169  ssh pi@rpiDoorbell.local
  170  ssh pi@rpiDoorbell.local
  499  touch ssh
  501  ssh pi@raspberry.local
  502  ssh pi@raspberrypi.local
  508  ssh pi@raspberrypi.local
  509  sudo nano /Users/jeff/.ssh/known_hosts
  510  ssh pi@raspberrypi.local
  511  sudo nano /Users/jeff/.ssh/known_hosts
  512  ssh pi@raspberrypi.local
  513  ssh pi@raspberrypi.local
  514  ssh pi@rpiGarageOpener.local
  515  ssh pi@rpiGarageOpener.local
  516  ssh pi@rpiGarageOpener.local
  518  ssh pi@rpiGarageOpener.local
  519  ssh pi@rpiGarageOpener.local
  520  ssh pi@rpiGarageOpener.local
  521  ssh pi@rpiGarageOpener.local
  522  ssh pi@rpiGarageOpener.local
  523  ssh pi@rpiGarageOpener.local
  524  ssh pi@rpiGarageOpener.local
  525  sudo nano /Users/jeff/.ssh/known_hosts
  526  ssh pi@rpiGarageOpener.local
  527  ssh pi@rpiGarageOpener.local
  528  ssh pi@rpiGarageOpener.local
  529  ssh pi@rpiGarageOpener.local
  531  ssh pi@rpiGarageOpener.local
  532  ssh pi@rpiGarageOpener.local
  533  ssh pi@rpiGarageOpener.local
  534  ssh pi@rpiGarageOpener.local
  535  ssh pi@rpiGarageOpener.local
  536  ssh pi@rpiGarageOpener.local
  538  ssh pi@rpiGarageOpener.local
  539  ssh pi@rpiGarageOpener.local
  541  ssh pi@rpiGarageOpener.local
  542  ssh pi@rpiGarageOpener.local
  545  ssh pi@rpiGarageOpener.local
  546  ssh pi@rpiGarageOpener.local
  547  ssh pi@rpiGarageOpener.local
  548  ssh pi@rpiGarageOpener.local
  549  ssh pi@GarageOpener.local
  550  ssh pi@rpiUnused.local
  551  ssh pi@GarageOpener.local
  552  ssh pi@rpiGarageOpener.local
  553  ssh pi@rpiGarageOpener.local
  555  ssh pi@rpiGarageOpener.local
  556  ssh pi@rpiGarageOpener.local
  557  ssh pi@rpiGarageOpener.local
  558  ssh pi@rpiGarageOpener.local
  559  history | grep ssh
  560  history | grep ssh
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec 11 12:55:59 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~ $ ls -l *.py
-rwxr-xr-x 1 root root  686 Dec  6 20:12 emailTry.py
-rw-r--r-- 1 pi   pi    163 Dec  6 11:13 genID.py
-rwxr-xr-x 1 root root  178 Nov 26 16:19 hello.py
-rwxr-xr-x 1 root root  218 Nov 26 12:46 pushGarageRemote.py
-rwxr-xr-x 1 root root 1564 Nov 30 15:16 read.py
-rwxr-xr-x 1 pi   pi   2907 Dec  6 07:17 simple-fan.py
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ cat get.txt
"description" : "returns hostname"
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ python3 -d rest_server.py


^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 -d rest_server.py

^Cpi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/11 20:33:11 - Starting REST server
2020/12/11 20:33:11 - Command line arguments:
2020/12/11 20:33:11 -   Input file  = 
2020/12/11 20:33:11 -   Log file = /home/pi/api/rest_server.log
2020/12/11 20:33:11 -   Port = 9443
2020/12/11 20:33:11 -   Use cert = False
2020/12/11 20:33:11 -   Use HTTPS = False
2020/12/11 20:33:11 -   Use multithreading = False

2020/12/11 20:33:11 - Web Server:
2020/12/11 20:33:11 -   Server name = rpiGarageOpener
2020/12/11 20:33:11 -   Server IP = 127.0.1.1

2020/12/11 20:33:18 - Closing REST server
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 -d rest_server.py
^Cpi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 -d rest_server.py
^Cpi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ python3 -d rest_server.py
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/11 20:40:50 - Starting REST server
2020/12/11 20:40:50 - Command line arguments:
2020/12/11 20:40:50 -   Input file  = 
2020/12/11 20:40:50 -   Log file = /home/pi/api/rest_server.log
2020/12/11 20:40:50 -   Port = 9443
2020/12/11 20:40:50 -   Use cert = False
2020/12/11 20:40:50 -   Use HTTPS = False
2020/12/11 20:40:50 -   Use multithreading = False

2020/12/11 20:40:50 - Web Server:
2020/12/11 20:40:50 -   Server name = rpiGarageOpener
2020/12/11 20:40:50 -   Server IP = 127.0.1.1

2020/12/11 20:40:55 - Closing REST server
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/11 20:43:24 - Starting REST server
2020/12/11 20:43:24 - Command line arguments:
2020/12/11 20:43:24 -   Input file  = 
2020/12/11 20:43:24 -   Log file = /home/pi/api/rest_server.log
2020/12/11 20:43:24 -   Port = 9443
2020/12/11 20:43:24 -   Use cert = False
2020/12/11 20:43:24 -   Use HTTPS = False
2020/12/11 20:43:24 -   Use multithreading = False

2020/12/11 20:43:24 - Web Server:
2020/12/11 20:43:24 -   Server name = rpiGarageOpener
2020/12/11 20:43:25 -   Server IP = 127.0.1.1

^C2020/12/11 20:47:40 - Closing REST server
pi@rpiGarageOpener:~/api $ python3 rest_server.py -ds
2020/12/11 20:47:47 - Starting REST server
2020/12/11 20:47:47 - Command line arguments:
2020/12/11 20:47:47 -   Input file  = 
2020/12/11 20:47:47 -   Log file = /home/pi/api/rest_server.log
2020/12/11 20:47:47 -   Port = 9443
2020/12/11 20:47:47 -   Use cert = False
2020/12/11 20:47:47 -   Use HTTPS = True
2020/12/11 20:47:47 -   Use multithreading = False

2020/12/11 20:47:47 - Web Server:
2020/12/11 20:47:47 -   Server name = rpiGarageOpener
2020/12/11 20:47:47 -   Server IP = 127.0.1.1

^C2020/12/11 20:48:22 - Closing REST server
pi@rpiGarageOpener:~/api $ python3 rest_server.py -dsc
2020/12/11 20:48:28 - Starting REST server
2020/12/11 20:48:28 - Command line arguments:
2020/12/11 20:48:28 -   Input file  = 
2020/12/11 20:48:28 -   Log file = /home/pi/api/rest_server.log
2020/12/11 20:48:28 -   Port = 9443
2020/12/11 20:48:28 -   Use cert = True
2020/12/11 20:48:28 -   Use HTTPS = True
2020/12/11 20:48:28 -   Use multithreading = False

2020/12/11 20:48:28 - Web Server:
2020/12/11 20:48:28 -   Server name = rpiGarageOpener
2020/12/11 20:48:28 -   Server IP = 127.0.1.1




^C2020/12/11 20:50:51 - Closing REST server
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -dsc
2020/12/11 20:56:27 - Starting REST server
2020/12/11 20:56:27 - Command line arguments:
2020/12/11 20:56:27 -   Input file  = 
2020/12/11 20:56:27 -   Log file = /home/pi/api/rest_server.log
2020/12/11 20:56:27 -   Port = 9443
2020/12/11 20:56:27 -   Use cert = True
2020/12/11 20:56:27 -   Use HTTPS = True
2020/12/11 20:56:27 -   Use multithreading = False

2020/12/11 20:56:27 - Web Server:
2020/12/11 20:56:27 -   Server name = rpiGarageOpener
2020/12/11 20:56:27 -   Server IP = 127.0.1.1

^X^C2020/12/11 20:57:00 - Closing REST server
pi@rpiGarageOpener:~/api $ ifconfig
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.227  netmask 255.255.255.0  broadcast 192.168.1.255
        ether b8:27:eb:4f:bd:e9  txqueuelen 1000  (Ethernet)
        RX packets 84987  bytes 12991819 (12.3 MiB)
        RX errors 0  dropped 2  overruns 0  frame 0
        TX packets 14231  bytes 2457652 (2.3 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

pi@rpiGarageOpener:~/api $ hostname -I
192.168.1.227 
pi@rpiGarageOpener:~/api $ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import commands
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'commands'
>>> exit()
pi@rpiGarageOpener:~/api $ ls *.py
get.py  rest_server.py
pi@rpiGarageOpener:~/api $ ls ../*.py
../emailTry.py  ../genID.py  ../hello.py  ../pushGarageRemote.py  ../read.py  ../simple-fan.py
pi@rpiGarageOpener:~/api $ ls ../*.py
../emailTry.py  ../genID.py  ../hello.py  ../pushGarageRemote.py  ../read.py  ../simple-fan.py
pi@rpiGarageOpener:~/api $ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess
>>> subprocess.call('hostname -I')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.7/subprocess.py", line 323, in call
    with Popen(*popenargs, **kwargs) as p:
  File "/usr/lib/python3.7/subprocess.py", line 775, in __init__
    restore_signals, start_new_session)
  File "/usr/lib/python3.7/subprocess.py", line 1522, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'hostname -I': 'hostname -I'
>>> i = subprocess.call('hostname -I', shell=FALSE)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'FALSE' is not defined
>>> i = subprocess.call('hostname -I', shell=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.7/subprocess.py", line 323, in call
    with Popen(*popenargs, **kwargs) as p:
  File "/usr/lib/python3.7/subprocess.py", line 775, in __init__
    restore_signals, start_new_session)
  File "/usr/lib/python3.7/subprocess.py", line 1522, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'hostname -I': 'hostname -I'
>>> exit()
pi@rpiGarageOpener:~/api $ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> import sys
>>> import subprocess
>>> subprocess.call('hostname -I')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.7/subprocess.py", line 323, in call
    with Popen(*popenargs, **kwargs) as p:
  File "/usr/lib/python3.7/subprocess.py", line 775, in __init__
    restore_signals, start_new_session)
  File "/usr/lib/python3.7/subprocess.py", line 1522, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'hostname -I': 'hostname -I'
>>> subprocess.call('hostname -I', shell=True)
192.168.1.227 
0
>>> i = subprocess.call('hostname -I', shell=True)
192.168.1.227 
>>> print (i)
0
>>> ip = i.decode("utf-8"
... )
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'decode'
>>> exit()
pi@rpiGarageOpener:~/api $ python3
Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> import subprocess
>>> subprocess.call('hostname -I', shell=True)
192.168.1.227 
0
>>> import commands
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'commands'
>>> address = subprocess.check_output(['hostname', '-s', '-I']).decode('utf-8')[:-1]
>>> print (address)
192.168.1.227 
>>> exit()
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -dsc
2020/12/11 21:37:37 - Starting REST server
2020/12/11 21:37:37 - Command line arguments:
2020/12/11 21:37:37 -   Input file  = 
2020/12/11 21:37:37 -   Log file = /home/pi/api/rest_server.log
2020/12/11 21:37:37 -   Port = 9443
2020/12/11 21:37:37 -   Use cert = True
2020/12/11 21:37:37 -   Use HTTPS = True
2020/12/11 21:37:37 -   Use multithreading = False

2020/12/11 21:37:37 - Web Server:
2020/12/11 21:37:37 -   Server name = rpiGarageOpener
2020/12/11 21:37:37 -   Server IP = 192.168.1.227 

Traceback (most recent call last):
  File "rest_server.py", line 452, in <module>
    main(sys.argv)
  File "rest_server.py", line 424, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
socket.gaierror: [Errno -2] Name or service not known
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -dsc
2020/12/11 21:40:56 - Starting REST server
2020/12/11 21:40:56 - Command line arguments:
2020/12/11 21:40:56 -   Input file  = 
2020/12/11 21:40:56 -   Log file = /home/pi/api/rest_server.log
2020/12/11 21:40:56 -   Port = 9443
2020/12/11 21:40:56 -   Use cert = True
2020/12/11 21:40:56 -   Use HTTPS = True
2020/12/11 21:40:56 -   Use multithreading = False

2020/12/11 21:40:56 - Web Server:
2020/12/11 21:40:56 -   Server name = rpiGarageOpener
2020/12/11 21:40:56 -   Local Server IP = 127.0.1.1
2020/12/11 21:40:56 -   Server IP = 192.168.1.227 

^C2020/12/11 21:41:05 - Closing REST server
pi@rpiGarageOpener:~/api $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Dec 11 20:20:30 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ httpd -t -c httpd.conf
-bash: httpd: command not found
pi@rpiGarageOpener:~/api $ sudo httpd -t -c httpd.conf
sudo: httpd: command not found
pi@rpiGarageOpener:~/api $ ls /etc/httpd
ls: cannot access '/etc/httpd': No such file or directory
pi@rpiGarageOpener:~/api $ which apache2
/usr/sbin/apache2
pi@rpiGarageOpener:~/api $ ls /usr/sbin
a2disconf              ebtables                     iptables-translate          setvesablank
a2dismod               ebtables-nft                 ispell-autobuildhash        split-logfile
a2dissite              ebtables-nft-restore         ldattach                    sshd
a2enconf               ebtables-nft-save            lightdm                     ssmtp
a2enmod                ebtables-restore             lightdm-gtk-greeter         start-statd
a2ensite               ebtables-save                locale-gen                  tarcat
a2query                fdformat                     logrotate                   tcptraceroute
accessdb               filefrag                     logwatch                    tcptraceroute.db
addgnupghome           flashrom                     maidag                      th-cmd
addgroup               genl                         mailq                       thd
add-shell              gnome-menus-blacklist        make-ssl-cert               traceroute
adduser                groupadd                     mkinitramfs                 tzconfig
alsabat-test           groupdel                     mklost+found                ufw
alsactl                groupmems                    mountstats                  unhide
alsa-info              groupmod                     newaliases                  unhide-linux
apache2                grpck                        newusers                    unhide-posix
apache2ctl             grpconv                      nfnl_osf                    unhide.rb
apachectl              grpunconv                    nfsidmap                    unhide_rb
applygnupgdefaults     httxt2dbm                    nfsiostat                   unhide-tcp
arp                    i2cdetect                    nfsstat                     update-ca-certificates
arpd                   i2cdump                      nologin                     update-catalog
arptables              i2cget                       pam-auth-update             update-default-aspell
arptables-nft          i2cset                       pam_getenv                  update-default-ispell
arptables-nft-restore  i2c-stub-from-dump           pam_timestamp_check         update-default-wordlist
arptables-nft-save     i2ctransfer                  paperconfig                 update-dictcommon-aspell
arptables-restore      iconvconfig                  phpdismod                   update-dictcommon-hunspell
arptables-save         in.identtestd                phpenmod                    update-icon-caches
aspell-autobuildhash   install-sgmlcatalog          phpquery                    update-info-dir
avahi-daemon           invoke-rc.d                  pi-greeter                  update-initramfs
blkmapd                ip6tables                    plymouth-set-default-theme  update-locale
bluetoothd             ip6tables-apply              pwck                        update-mime
check_forensic         ip6tables-legacy             pwconv                      update-passwd
chgpasswd              ip6tables-legacy-restore     pwunconv                    update-pciids
chklastlog             ip6tables-legacy-save        readprofile                 update-rc.d
chkrootkit             ip6tables-nft                remove-default-ispell       update-xmlcatalog
chkwtmp                ip6tables-nft-restore        remove-default-wordlist     usb_modeswitch
chmem                  ip6tables-nft-save           remove-shell                usb_modeswitch_dispatcher
chpasswd               ip6tables-restore            rfkill                      useradd
chroot                 ip6tables-restore-translate  rmt                         userdel
cifs.idmap             ip6tables-save               rmt-tar                     usermod
cifs.upcall            ip6tables-translate          rngd                        v4l2-dbg
cpgr                   iptables                     rpcdebug                    validlocale
cppw                   iptables-apply               rpc.gssd                    vcstime
cron                   iptables-legacy              rpc.idmapd                  vigr
delgroup               iptables-legacy-restore      rpcinfo                     vipw
deluser                iptables-legacy-save         rpc.svcgssd                 visudo
dmidecode              iptables-nft                 rsyslogd                    xtables-legacy-multi
dpkg-preconfigure      iptables-nft-restore         rtcwake                     xtables-monitor
dpkg-reconfigure       iptables-nft-save            select-default-ispell       xtables-nft-multi
e2freefrag             iptables-restore             select-default-wordlist     zic
e4crypt                iptables-restore-translate   sendmail
e4defrag               iptables-save                service
pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py &
[1] 8802
pi@rpiGarageOpener:~/api $ curl -X GET http://localhost:9443/api/cpu
curl: (7) Failed to connect to localhost port 9443: Connection refused

[1]+  Stopped                 sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ sudo kill 8802
pi@rpiGarageOpener:~/api $ sudo nano /etc/apache2/ports.conf
pi@rpiGarageOpener:~/api $ sudo ufw status
Status: inactive
pi@rpiGarageOpener:~/api $ sudo ufw allow 9443
Rules updated
Rules updated (v6)
pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ sudo python3 /usr/bin/rest_server.py &
[2] 9401
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json  memory      README.md    rest_server.log  server_cron.sh  time
client.key  favicon.png  get.py    navigation  reboot       rest_server.py   server.crt      uptime
cpu         get.backup   get.txt   os          restful_api  server           server.key
pi@rpiGarageOpener:~/api $ cat rest_server.log
2020/12/12 08:11:14 - Starting REST server
2020/12/12 08:11:14 - Command line arguments:
2020/12/12 08:11:14 -   Input file  = 
2020/12/12 08:11:14 -   Log file = /home/pi/api/rest_server.log
2020/12/12 08:11:14 -   Port = 9443
2020/12/12 08:11:14 -   Use cert = False
2020/12/12 08:11:14 -   Use HTTPS = False
2020/12/12 08:11:14 -   Use multithreading = False

2020/12/12 08:11:14 - Web Server:
2020/12/12 08:11:14 -   Server name = rpiGarageOpener
2020/12/12 08:11:14 -   Server IP = 127.0.1.1

pi@rpiGarageOpener:~/api $ sudo kill 9401
[2]-  Terminated              sudo python3 /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ ls -l
total 124
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 cpu
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 memory
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 navigation
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   498 Dec 12 08:11 rest_server.log
-rwxr-xr-x 1 pi pi 15430 Dec 11 21:40 rest_server.py
drwxr-xr-x 2 pi pi  4096 Dec  6 09:13 server
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 time
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 uptime
pi@rpiGarageOpener:~/api $ ls -l cpu
total 16
-rw-r--r-- 1 pi pi 183 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi  63 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi 183 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi  45 Dec  6 08:11 get.txt
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ sudo python3 /usr/bin/rest_server.py 
^Cpi@rpiGarageOpener:~/api $ sudo python3 /usr/bin/rest_server.py -d
rest_server.py [options, ...]
rest_server.py -h
pi@rpiGarageOpener:~/api $ sudo python3 /usr/bin/rest_server.py -h
Decription: 
  Server-side script for RESTful API sever written in python using json
  There are multiple ways for a client-side server to communicate with this server-side API:
    A client-side script can make HTTP requests (see rest_client.py)
    Open a browser and enter: http://security:9080/api/multi/10/23
    Open a terminal and run: $ curl -X GET http://security:9080/api/multi/10/23

Usage:
  python3 rest_server.py [options...]

Options:
  -h --help           this help
  -c --cert           Use cert, requires use https
  -i --inputfile      input json file
  -l --logfile        write log messages to user specified file
  -m --multithreading use multithreading
  -p --port           User defined port. The default port is9443.
  -s --secure         use https
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu   favicon.png  get.json  get.txt  navigation  README.md  restful_api      rest_server.py  server_cron.sh  server.key  uptime
client.key  disk  get.backup   get.py    memory   os          reboot     rest_server.log  server          server.crt      time
pi@rpiGarageOpener:~/api $ history | grep rest_server.py
   60  python3 rest_server.py
   64  python3 rest_server.py
   66  python3 rest_server.py
   67  sudo python3 rest_server.py
   68  sudo python rest_server.py
   69  sudo python3 rest_server.py
   72  sudo python3 rest_server.py
   76  nano rest_server.py
   78  nano rest_server.py
   79  sudo python3 rest_server.py -s
   80  sudo python3 rest_server.py 
   86  ls /usr/bin/rest_server.py
   87  ls -l /usr/bin/rest_server.py
   89  sudo nano /usr/bin/rest_server.py
   94  sudo nano /usr/bin/rest_server.py
  101  sudo nano /usr/bin/rest_server.py
  113  sudo nano /usr/bin/rest_server.py &
  119  sudo nano /usr/bin/rest_server.py
  120  sudo python3 /usr/bin/rest_server.py &
  126  nano rest_server.py
  127  sudo python3 /usr/bin/rest_server.py 
  128  sudo python3 /usr/bin/rest_server.py -d
  129  sudo python3 /usr/bin/rest_server.py -h
  131  history | grep rest_server.py
pi@rpiGarageOpener:~/api $ sudo nano /usr/bin/rest_server.py
pi@rpiGarageOpener:~/api $ sudo nano rest_server.py
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py -d
2020/12/12 08:27:17 - Starting REST server
2020/12/12 08:27:17 - Command line arguments:
2020/12/12 08:27:17 -   Input file  = 
2020/12/12 08:27:17 -   Log file = /home/pi/api/rest_server.log
2020/12/12 08:27:17 -   Port = 9443
2020/12/12 08:27:17 -   Use cert = False
2020/12/12 08:27:17 -   Use HTTPS = False
2020/12/12 08:27:17 -   Use multithreading = False

2020/12/12 08:27:17 - Web Server:
2020/12/12 08:27:17 -   Server name = rpiGarageOpener
2020/12/12 08:27:17 -   Local Server IP = 127.0.1.1
2020/12/12 08:27:17 -   Server IP = 192.168.1.227 

2020/12/12 08:27:17 -   No socket is required for HTTP?

^C2020/12/12 08:32:05 - Closing REST server
pi@rpiGarageOpener:~/api $ netstat -l
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 rpiGarageOpener.at:5070 0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:http               [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
udp        0      0 0.0.0.0:mdns            0.0.0.0:*                          
udp        0      0 0.0.0.0:41730           0.0.0.0:*                          
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                          
udp        0      0 0.0.0.0:1900            0.0.0.0:*                          
udp6       0      0 [::]:mdns               [::]:*                             
udp6       0      0 [::]:55497              [::]:*                             
raw6       0      0 [::]:ipv6-icmp          [::]:*                  7          
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     18228    /tmp/ssh-6qVA2F7Zk4I6/agent.701
unix  2      [ ACC ]     STREAM     LISTENING     17786    /tmp/ssh-x3QEpgCXS0pr/agent.583
unix  2      [ ACC ]     STREAM     LISTENING     7455     /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     16526    @/tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     7461     /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     7465     /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     17216    /run/user/1000/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     13638    /var/run/dhcpcd.sock
unix  2      [ ACC ]     STREAM     LISTENING     13640    /var/run/dhcpcd.unpriv.sock
unix  2      [ ACC ]     STREAM     LISTENING     12103    /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     17225    /run/user/1000/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     17228    /run/user/1000/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     16527    /tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     12108    /run/avahi-daemon/socket
unix  2      [ ACC ]     STREAM     LISTENING     17230    /run/user/1000/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     17232    /run/user/1000/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     17234    /run/user/1000/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     17236    /run/user/1000/bus
unix  2      [ ACC ]     STREAM     LISTENING     12123    /run/thd.socket
unix  2      [ ACC ]     STREAM     LISTENING     19308    /run/user/1000/menu-cached-:0
unix  2      [ ACC ]     STREAM     LISTENING     18613    /run/user/1000/pcmanfm-socket--0
unix  2      [ ACC ]     SEQPACKET  LISTENING     7597     /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     17403    /var/run/fail2ban/fail2ban.sock
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py &
[2] 10805
pi@rpiGarageOpener:~/api $ netstat -l
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 rpiGarageOpener.at:5070 0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp        0      0 rpiGarageOpener:9443    0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:http               [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
udp        0      0 0.0.0.0:mdns            0.0.0.0:*                          
udp        0      0 0.0.0.0:41730           0.0.0.0:*                          
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                          
udp        0      0 0.0.0.0:1900            0.0.0.0:*                          
udp6       0      0 [::]:mdns               [::]:*                             
udp6       0      0 [::]:55497              [::]:*                             
raw6       0      0 [::]:ipv6-icmp          [::]:*                  7          
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     18228    /tmp/ssh-6qVA2F7Zk4I6/agent.701
unix  2      [ ACC ]     STREAM     LISTENING     17786    /tmp/ssh-x3QEpgCXS0pr/agent.583
unix  2      [ ACC ]     STREAM     LISTENING     7455     /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     16526    @/tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     7461     /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     7465     /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     17216    /run/user/1000/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     13638    /var/run/dhcpcd.sock
unix  2      [ ACC ]     STREAM     LISTENING     13640    /var/run/dhcpcd.unpriv.sock
unix  2      [ ACC ]     STREAM     LISTENING     12103    /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     17225    /run/user/1000/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     17228    /run/user/1000/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     16527    /tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     12108    /run/avahi-daemon/socket
unix  2      [ ACC ]     STREAM     LISTENING     17230    /run/user/1000/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     17232    /run/user/1000/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     17234    /run/user/1000/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     17236    /run/user/1000/bus
unix  2      [ ACC ]     STREAM     LISTENING     12123    /run/thd.socket
unix  2      [ ACC ]     STREAM     LISTENING     19308    /run/user/1000/menu-cached-:0
unix  2      [ ACC ]     STREAM     LISTENING     18613    /run/user/1000/pcmanfm-socket--0
unix  2      [ ACC ]     SEQPACKET  LISTENING     7597     /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     17403    /var/run/fail2ban/fail2ban.sock
pi@rpiGarageOpener:~/api $ sudo kill 10805
[2]-  Terminated              sudo python3 rest_server.py
pi@rpiGarageOpener:~/api $ nc -zv localhost 8080
nc: connect to localhost port 8080 (tcp) failed: Connection refused
nc: connect to localhost port 8080 (tcp) failed: Cannot assign requested address
pi@rpiGarageOpener:~/api $ nc -zv localhost 443
nc: connect to localhost port 443 (tcp) failed: Connection refused
nc: connect to localhost port 443 (tcp) failed: Cannot assign requested address
pi@rpiGarageOpener:~/api $ nc -zv localhost 5070
nc: connect to localhost port 5070 (tcp) failed: Connection refused
nc: connect to localhost port 5070 (tcp) failed: Cannot assign requested address
pi@rpiGarageOpener:~/api $ nc -z localhost 5070
pi@rpiGarageOpener:~/api $ nc -zv localhost 5070
nc: connect to localhost port 5070 (tcp) failed: Connection refused
nc: connect to localhost port 5070 (tcp) failed: Cannot assign requested address
pi@rpiGarageOpener:~/api $ nc -zv localhost 8888
Connection to localhost 8888 port [tcp/*] succeeded!
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py &
[2] 12215
pi@rpiGarageOpener:~/api $ nc -zv localhost 9443
nc: connect to localhost port 9443 (tcp) failed: Connection refused
nc: connect to localhost port 9443 (tcp) failed: Cannot assign requested address
pi@rpiGarageOpener:~/api $ nc -zv rpiGarageOpener 9443
Connection to rpiGarageOpener 9443 port [tcp/*] succeeded!
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ history | grep nano | grep /
   40  nano /var/www/db/garage.sh
   41  nano /usr/local/bin/garage.sh
   49  sudo nano /etc/ssmtp/ssmtp.conf
   50  sudo nano /etc/ssmtp/revaliases
   82  sudo nano /etc/apache2/apache2.conf
   83  sudo nano /etc/apache2/conf-enabled/*.conf
   84  sudo nano /etc/apache2/sites-enabled/*.conf
   89  sudo nano /usr/bin/rest_server.py
   94  sudo nano /usr/bin/rest_server.py
  101  sudo nano /usr/bin/rest_server.py
  113  sudo nano /usr/bin/rest_server.py &
  116  sudo nano /etc/apache2/ports.conf
  119  sudo nano /usr/bin/rest_server.py
  132  sudo nano /usr/bin/rest_server.py
  148  sudo nano /etc/hosts
  149  history | grep nano | grep /
pi@rpiGarageOpener:~/api $ sudo nano /etc/apache2/ports.conf
pi@rpiGarageOpener:~/api $ sudo nano /etc/ssmtp/revaliases
pi@rpiGarageOpener:~/api $ ls /etc
adduser.conf            fake-hwclock.data  libnl-3         passwd            selinux
aliases                 fb.modes           libpaper.d      passwd-           sensors3.conf
alsa                    fonts              lightdm         paxctld.conf      sensors.d
alternatives            fstab              lighttpd        perl              services
apache2                 fuse.conf          locale.alias    php               sgml
apparmor.d              gai.conf           locale.gen      pip.conf          shadow
apt                     gdb                localtime       plymouth          shadow-
avahi                   ghostscript        logcheck        polkit-1          shells
bash.bashrc             glvnd              login.defs      ppp               skel
bash_completion         gnome              logrotate.conf  profile           ssh
bash_completion.d       groff              logrotate.d     profile.d         ssl
bindresvport.blacklist  group              logwatch        protocols         ssmtp
binfmt.d                group-             machine-id      pulse             subgid
bluetooth               gshadow            magic           python            subuid
ca-certificates         gshadow-           magic.mime      python2.7         sudoers
ca-certificates.conf    gss                mailcap         python3           sudoers.d
calendar                gtk-2.0            mailcap.order   python3.7         sysctl.conf
chkrootkit.conf         gtk-3.0            mailname        rc0.d             sysctl.d
chromium-browser        host.conf          mail.rc         rc1.d             systemd
cifs-utils              hostname           manpath.config  rc2.d             terminfo
console-setup           hosts              menu-methods    rc3.d             timezone
cron.d                  hosts.allow        mime.types      rc4.d             timidity
cron.daily              hosts.deny         mke2fs.conf     rc5.d             tmpfiles.d
cron.hourly             idmapd.conf        modprobe.d      rc6.d             triggerhappy
cron.monthly            ifplugd            modules         rc.local          ucf.conf
crontab                 init               modules-load.d  rcS.d             udev
cron.weekly             init.d             monit           request-key.conf  udisks2
dbus-1                  initramfs-tools    motd            request-key.d     ufw
debconf.conf            inputrc            mtab            resolv.conf       update-motd.d
debian_version          insserv.conf.d     mysql           resolvconf        usb_modeswitch.conf
default                 iproute2           nanorc          resolv.conf.bak   usb_modeswitch.d
deluser.conf            issue              netconfig       resolvconf.conf   vdpau_wrapper.cfg
dhcp                    issue.net          network         rkhunter.conf     vim
dhcpcd.conf             kernel             networks        rmt               vnc
dictionaries-common     ldap               nsswitch.conf   rpc               vulkan
dphys-swapfile          ld.so.cache        openal          rpi-issue         wgetrc
dpkg                    ld.so.conf         opt             rpimonitor        wpa_supplicant
emacs                   ld.so.conf.d       os-release      rsyslog.conf      X11
email-addresses         ld.so.preload      PackageKit      rsyslog.d         xattr.conf
environment             libaudit.conf      pam.conf        RTIMULib.ini      xdg
exim4                   libblockdev        pam.d           securetty         xml
fail2ban                libibverbs.d       papersize       security
pi@rpiGarageOpener:~/api $ sudoo nano /etc/host.conf
-bash: sudoo: command not found
pi@rpiGarageOpener:~/api $ sudo nano /etc/host.conf
pi@rpiGarageOpener:~/api $ sudo nano /etc/host.allow
pi@rpiGarageOpener:~/api $ sudo nano /etc/host.deny
pi@rpiGarageOpener:~/api $ sudo nano /etc/networks
pi@rpiGarageOpener:~/api $ sudo nano /etc/sysctl.conf
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
root      8802  0.0  0.7   9936  3376 pts/0    T    08:03   0:00 sudo nano /usr/bin/rest_server.py
root      8803  0.0  0.7   8096  3436 pts/0    T    08:03   0:00 nano /usr/bin/rest_server.py
root     12215  0.0  0.7   9936  3256 pts/0    S    08:55   0:00 sudo python3 rest_server.py
root     12216  0.2  3.1  21820 13764 pts/0    S    08:55   0:02 python3 rest_server.py
pi       13165  0.0  0.4   7336  2032 pts/0    S+   09:09   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo kill 8802
pi@rpiGarageOpener:~/api $ sudo kill 8803
pi@rpiGarageOpener:~/api $ sudo kill 12215
[2]-  Terminated              sudo python3 rest_server.py
pi@rpiGarageOpener:~/api $ sudo kill 12216
kill: (12216): No such process
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
root      8802  0.0  0.7   9936  3376 pts/0    T    08:03   0:00 sudo nano /usr/bin/rest_server.py
root      8803  0.0  0.7   8096  3436 pts/0    T    08:03   0:00 nano /usr/bin/rest_server.py
pi       13236  0.0  0.4   7336  1956 pts/0    S+   09:10   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo kill 8803
pi@rpiGarageOpener:~/api $ sudo kill 8802
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
root      8802  0.0  0.7   9936  3376 pts/0    T    08:03   0:00 sudo nano /usr/bin/rest_server.py
root      8803  0.0  0.7   8096  3436 pts/0    T    08:03   0:00 nano /usr/bin/rest_server.py
pi       13282  0.0  0.4   7336  1952 pts/0    S+   09:10   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo reboot
pi@rpiGarageOpener:~/api $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sat Dec 12 09:12:04 2020
pi@rpiGarageOpener:~ $ nc -zv rpiGarageOpener 9443
nc: connect to rpiGarageOpener port 9443 (tcp) failed: Connection refused
pi@rpiGarageOpener:~ $ netstat -l
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 rpiGarageOpener.at:5070 0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:http               [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
udp        0      0 0.0.0.0:mdns            0.0.0.0:*                          
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                          
udp        0      0 0.0.0.0:1900            0.0.0.0:*                          
udp        0      0 0.0.0.0:58526           0.0.0.0:*                          
udp6       0      0 [::]:mdns               [::]:*                             
udp6       0      0 [::]:53105              [::]:*                             
raw6       0      0 [::]:ipv6-icmp          [::]:*                  7          
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     17883    /tmp/ssh-0XKSvEPUA0lu/agent.577
unix  2      [ ACC ]     STREAM     LISTENING     19215    /run/user/1000/menu-cached-:0
unix  2      [ ACC ]     STREAM     LISTENING     7455     /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     16619    @/tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     7464     /run/systemd/fsck.progress
unix  2      [ ACC ]     SEQPACKET  LISTENING     7467     /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     18743    /run/user/1000/pcmanfm-socket--0
unix  2      [ ACC ]     STREAM     LISTENING     7484     /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     12104    /run/avahi-daemon/socket
unix  2      [ ACC ]     STREAM     LISTENING     16620    /tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     12877    /var/run/dhcpcd.sock
unix  2      [ ACC ]     STREAM     LISTENING     12879    /var/run/dhcpcd.unpriv.sock
unix  2      [ ACC ]     STREAM     LISTENING     12112    /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     12115    /run/thd.socket
unix  2      [ ACC ]     STREAM     LISTENING     17516    /run/user/1000/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     17260    /run/user/1000/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     17518    /run/user/1000/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     17522    /run/user/1000/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     17524    /run/user/1000/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     17638    /var/run/fail2ban/fail2ban.sock
unix  2      [ ACC ]     STREAM     LISTENING     17383    /run/user/1000/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     17386    /run/user/1000/bus
unix  2      [ ACC ]     STREAM     LISTENING     18356    /tmp/ssh-LdwnQHQdVWBt/agent.683
pi@rpiGarageOpener:~ $ sudo python3 rest_server.py &
[1] 1280
pi@rpiGarageOpener:~ $ python3: can't open file 'rest_server.py': [Errno 2] No such file or directory
sudo kill 1280
kill: (1280): No such process
[1]+  Exit 2                  sudo python3 rest_server.py
pi@rpiGarageOpener:~ $ ps -aux | grep rest_server
pi        1315  0.0  0.4   7336  1948 pts/0    S+   09:16   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py &
[1] 1326
pi@rpiGarageOpener:~/api $ netstat -l
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 rpiGarageOpener.at:5070 0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp        0      0 rpiGarageOpener:9443    0.0.0.0:*               LISTEN     
tcp6       0      0 [::]:http               [::]:*                  LISTEN     
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN     
udp        0      0 0.0.0.0:mdns            0.0.0.0:*                          
udp        0      0 0.0.0.0:bootpc          0.0.0.0:*                          
udp        0      0 0.0.0.0:1900            0.0.0.0:*                          
udp        0      0 0.0.0.0:58526           0.0.0.0:*                          
udp6       0      0 [::]:mdns               [::]:*                             
udp6       0      0 [::]:53105              [::]:*                             
raw6       0      0 [::]:ipv6-icmp          [::]:*                  7          
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  2      [ ACC ]     STREAM     LISTENING     17883    /tmp/ssh-0XKSvEPUA0lu/agent.577
unix  2      [ ACC ]     STREAM     LISTENING     19215    /run/user/1000/menu-cached-:0
unix  2      [ ACC ]     STREAM     LISTENING     7455     /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     16619    @/tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     7464     /run/systemd/fsck.progress
unix  2      [ ACC ]     SEQPACKET  LISTENING     7467     /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     18743    /run/user/1000/pcmanfm-socket--0
unix  2      [ ACC ]     STREAM     LISTENING     7484     /run/systemd/journal/stdout
unix  2      [ ACC ]     STREAM     LISTENING     12104    /run/avahi-daemon/socket
unix  2      [ ACC ]     STREAM     LISTENING     16620    /tmp/.X11-unix/X0
unix  2      [ ACC ]     STREAM     LISTENING     12877    /var/run/dhcpcd.sock
unix  2      [ ACC ]     STREAM     LISTENING     12879    /var/run/dhcpcd.unpriv.sock
unix  2      [ ACC ]     STREAM     LISTENING     12112    /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     12115    /run/thd.socket
unix  2      [ ACC ]     STREAM     LISTENING     17516    /run/user/1000/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     17260    /run/user/1000/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     17518    /run/user/1000/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     17522    /run/user/1000/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     17524    /run/user/1000/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     17638    /var/run/fail2ban/fail2ban.sock
unix  2      [ ACC ]     STREAM     LISTENING     17383    /run/user/1000/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     17386    /run/user/1000/bus
unix  2      [ ACC ]     STREAM     LISTENING     18356    /tmp/ssh-LdwnQHQdVWBt/agent.683
pi@rpiGarageOpener:~/api $ nc -zv rpiGarageOpener 9443
Connection to rpiGarageOpener 9443 port [tcp/*] succeeded!
pi@rpiGarageOpener:~/api $ cat < /dev/null > /dev/tcp/rpiGarageOpener:9443; echo $?
-bash: /dev/tcp/rpiGarageOpener:9443: No such file or directory
1
pi@rpiGarageOpener:~/api $ cat < /dev/null > /dev/tcp/rpiGarageOpener/9443; echo $?
0
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
root      1326  0.0  0.7   9936  3200 pts/0    S    09:16   0:00 sudo python3 rest_server.py
root      1327  0.8  3.1  21820 13708 pts/0    S    09:16   0:01 python3 rest_server.py
pi        1555  0.0  0.4   7336  1952 pts/0    S+   09:19   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ history
    1  which php
    2  sudo apt install --dry-run php7.4
    3  sudo apt install  php7.3
    4  sudo apt install --dry-run php7.4-sqlite3
    5  sudo apt install --dry-run php7.3-sqlite3
    6  sudo apt install  php7.3 php7.3-sqlite3
    7  nano createDB.sh
    8  sudo bash createDB.sh
    9  nano createDB.sh
   10  sudo bash createDB.sh
   11  nano createDB.sh
   12  sudo bash createDB.sh
   13  nano createDB.sh
   14  sudo bash createDB.sh
   15  nano createDB.sh
   16  sudo bash createDB.sh
   17  nano createDB.sh
   18  sudo bash createDB.sh
   19  nano createDB.sh
   20  sudo bash createDB.sh
   21  nano createDB.sh
   22  sudo bash createDB.sh
   23  nano createDB.sh
   24  sqlite3 /var/www/db/garagedoor.db
   25  nano createDB.sh
   26  ls
   27  nano push_garage_opener.py
   28  mv push_garage_opener.py pushGarageRemote.py
   29  nano createDB.sh
   30  wget "https://raw.githubusercontent.com/dumbo25/garageDoorOpener2/main/garage.sh"
   31  ls -l
   32  ls /usr/local/bin
   33  chmod UG+x garage.sh
   34  chmod ug+x garage.sh
   35  ls -l
   36  mv garage.sh /usr/local/bin/garage.sh
   37  sudo mv garage.sh /usr/local/bin/garage.sh
   38  ls /usr/local/bin
   39  ls -l /usr/local/bin
   40  nano /var/www/db/garage.sh
   41  nano /usr/local/bin/garage.sh
   42  ls
   43  gpio read 17
   44  which which gpio
   45  /usr/bin/gpio read 17
   46  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   47  sudo apt-get update -y
   48  sudo apt-get upgrade -y
   49  sudo nano /etc/ssmtp/ssmtp.conf
   50  sudo nano /etc/ssmtp/revaliases
   51  sudo chmod og+x /etc/ssmtp/ssmtp.conf
   52  nano emailTry.py
   53  python emailTry.py
   54  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   55  sudo ufw show added
   56  sudo ufw allow 9080
   57  sudo ufw show added
   58  history | grep rest
   59  history | grep server
   60  python3 rest_server.py
   61  ls
   62  cd api
   63  ls
   64  python3 rest_server.py
   65  pwd
   66  python3 rest_server.py
   67  sudo python3 rest_server.py
   68  sudo python rest_server.py
   69  sudo python3 rest_server.py
   70  history |grep distro
   71  sudo pip3 install distro
   72  sudo python3 rest_server.py
   73  ls
   74  ls multi
   75  ls os
   76  nano rest_server.py
   77  ls
   78  nano rest_server.py
   79  sudo python3 rest_server.py -s
   80  sudo python3 rest_server.py 
   81  cat /etc/hosts
   82  sudo nano /etc/apache2/apache2.conf
   83  sudo nano /etc/apache2/conf-enabled/*.conf
   84  sudo nano /etc/apache2/sites-enabled/*.conf
   85  ls /usr/bin
   86  ls /usr/bin/rest_server.py
   87  ls -l /usr/bin/rest_server.py
   88  ps -aux | grep rest
   89  sudo nano /usr/bin/rest_server.py
   90  ls
   91  ls -l
   92  cat rest_server.log
   93  ls ../*.log
   94  sudo nano /usr/bin/rest_server.py
   95  pwd
   96  ls -l
   97  ps -aux | grep rest
   98  netstat -lptn
   99  netstat --tcp --listening --programs --numeric
  100  sudo ufw status
  101  sudo nano /usr/bin/rest_server.py
  102  cat /home/pi/api/server_cron.sh
  103  ls *.pid
  104  ls
  105  cat rest_server.log
  106  ls
  107  cd api
  108  httpd -t -c httpd.conf
  109  sudo httpd -t -c httpd.conf
  110  ls /etc/httpd
  111  which apache2
  112  ls /usr/sbin
  113  sudo nano /usr/bin/rest_server.py &
  114  curl -X GET http://localhost:9443/api/cpu
  115  sudo kill 8802
  116  sudo nano /etc/apache2/ports.conf
  117  sudo ufw status
  118  sudo ufw allow 9443
  119  sudo nano /usr/bin/rest_server.py
  120  sudo python3 /usr/bin/rest_server.py &
  121  ls
  122  cat rest_server.log
  123  sudo kill 9401
  124  ls -l
  125  ls -l cpu
  126  nano rest_server.py
  127  sudo python3 /usr/bin/rest_server.py 
  128  sudo python3 /usr/bin/rest_server.py -d
  129  sudo python3 /usr/bin/rest_server.py -h
  130  ls
  131  history | grep rest_server.py
  132  sudo nano /usr/bin/rest_server.py
  133  sudo nano rest_server.py
  134  sudo python3 rest_server.py -d
  135  netstat -l
  136  sudo python3 rest_server.py &
  137  netstat -l
  138  sudo kill 10805
  139  nc -zv localhost 8080
  140  nc -zv localhost 443
  141  nc -zv localhost 5070
  142  nc -z localhost 5070
  143  nc -zv localhost 5070
  144  nc -zv localhost 8888
  145  sudo python3 rest_server.py &
  146  nc -zv localhost 9443
  147  nc -zv rpiGarageOpener 9443
  148  sudo nano /etc/hosts
  149  history | grep nano | grep /
  150  sudo nano /etc/apache2/ports.conf
  151  sudo nano /etc/ssmtp/revaliases
  152  ls /etc
  153  sudoo nano /etc/host.conf
  154  sudo nano /etc/host.conf
  155  sudo nano /etc/host.allow
  156  sudo nano /etc/host.deny
  157  sudo nano /etc/networks
  158  sudo nano /etc/sysctl.conf
  159  ps -aux | grep rest_server
  160  sudo kill 8802
  161  sudo kill 8803
  162  sudo kill 12215
  163  sudo kill 12216
  164  ps -aux | grep rest_server
  165  sudo kill 8803
  166  sudo kill 8802
  167  ps -aux | grep rest_server
  168  sudo reboot
  169  nc -zv rpiGarageOpener 9443
  170  netstat -l
  171  sudo python3 rest_server.py &
  172  sudo kill 1280
  173  ps -aux | grep rest_server
  174  cd api
  175  sudo python3 rest_server.py &
  176  netstat -l
  177  nc -zv rpiGarageOpener 9443
  178  cat < /dev/null > /dev/tcp/rpiGarageOpener:9443; echo $?
  179  cat < /dev/null > /dev/tcp/rpiGarageOpener/9443; echo $?
  180  ps -aux | grep rest_server
  181  history
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
root      1326  0.0  0.7   9936  3200 pts/0    S    09:16   0:00 sudo python3 rest_server.py
root      1327  0.7  3.1  21820 13708 pts/0    S    09:16   0:01 python3 rest_server.py
pi        1597  0.0  0.4   7336  2020 pts/0    S+   09:20   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo kill 1327
[1]+  Terminated              sudo python3 rest_server.py
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
pi        1611  0.0  0.4   7336  1944 pts/0    S+   09:20   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ python3 rest_server.py &
[1] 1652
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
pi        1652 58.0  3.1  21820 13720 pts/0    S    09:21   0:01 python3 rest_server.py
pi        1655  0.0  0.4   7336  2036 pts/0    S+   09:21   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo kill 1652
pi@rpiGarageOpener:~/api $ python3 rest_server.py -p5070 &
[2] 1698
[1]   Terminated              python3 rest_server.py
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
pi        1698 24.7  3.1  21820 13716 pts/0    S    09:21   0:01 python3 rest_server.py -p5070
pi        1711  0.0  0.4   7336  2028 pts/0    S+   09:22   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo kill 1698
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py -p5070 &
[3] 1763
[2]   Terminated              python3 rest_server.py -p5070
pi@rpiGarageOpener:~/api $ sudo kill 1763
pi@rpiGarageOpener:~/api $ sudo netstat -anp | grep ':80 '

tcp6       0      0 :::80                   :::*                    LISTEN      499/apache2         
[3]+  Terminated              sudo python3 rest_server.py -p5070
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ sudo netstat -anp | grep ':9443 '
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py &
[1] 1898
pi@rpiGarageOpener:~/api $ sudo netstat -anp | grep ':9443 '
tcp        0      0 127.0.1.1:9443          0.0.0.0:*               LISTEN      1899/python3        
pi@rpiGarageOpener:~/api $ hotsname -L
-bash: hotsname: command not found
pi@rpiGarageOpener:~/api $ hotsname -I
-bash: hotsname: command not found
pi@rpiGarageOpener:~/api $ hostname -I
192.168.1.227 
pi@rpiGarageOpener:~/api $ sudo netstat -tnlp | grep :9443
tcp        0      0 127.0.1.1:9443          0.0.0.0:*               LISTEN      1899/python3        
pi@rpiGarageOpener:~/api $ sudo tcpdump -n icmp
sudo: tcpdump: command not found
pi@rpiGarageOpener:~/api $ sudo service ssh status
● ssh.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
   Active: active (running) since Sat 2020-12-12 09:11:54 CST; 25min ago
     Docs: man:sshd(8)
           man:sshd_config(5)
  Process: 402 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
 Main PID: 418 (sshd)
    Tasks: 1 (limit: 881)
   CGroup: /system.slice/ssh.service
           └─418 /usr/sbin/sshd -D

Dec 12 09:11:50 rpiGarageOpener systemd[1]: Starting OpenBSD Secure Shell server...
Dec 12 09:11:53 rpiGarageOpener sshd[418]: Server listening on 0.0.0.0 port 22.
Dec 12 09:11:53 rpiGarageOpener sshd[418]: Server listening on :: port 22.
Dec 12 09:11:54 rpiGarageOpener systemd[1]: Started OpenBSD Secure Shell server.
Dec 12 09:14:16 rpiGarageOpener sshd[1167]: Accepted password for pi from 192.168.1.118 port 58526 ssh2
Dec 12 09:14:16 rpiGarageOpener sshd[1167]: pam_unix(sshd:session): session opened for user pi by (uid=0)
pi@rpiGarageOpener:~/api $ netstat -an | grep "LISTEN "
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.1.1:9443          0.0.0.0:*               LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ sudo netstat -tnlp | grep :5070
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN      949/python          
pi@rpiGarageOpener:~/api $ ps -aux 
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.4  1.8  32780  8236 ?        Ss   09:11   0:08 /sbin/init splash
root         2  0.0  0.0      0     0 ?        S    09:11   0:00 [kthreadd]
root         6  0.0  0.0      0     0 ?        I<   09:11   0:00 [mm_percpu_wq]
root         7  0.1  0.0      0     0 ?        S    09:11   0:02 [ksoftirqd/0]
root         8  0.0  0.0      0     0 ?        S    09:11   0:00 [kdevtmpfs]
root         9  0.0  0.0      0     0 ?        I<   09:11   0:00 [netns]
root        11  0.0  0.0      0     0 ?        S    09:11   0:00 [kauditd]
root        12  0.0  0.0      0     0 ?        S    09:11   0:00 [khungtaskd]
root        13  0.0  0.0      0     0 ?        S    09:11   0:00 [oom_reaper]
root        14  0.0  0.0      0     0 ?        I<   09:11   0:00 [writeback]
root        15  0.0  0.0      0     0 ?        S    09:11   0:00 [kcompactd0]
root        30  0.0  0.0      0     0 ?        I<   09:11   0:00 [kblockd]
root        31  0.0  0.0      0     0 ?        I<   09:11   0:00 [blkcg_punt_bio]
root        32  0.0  0.0      0     0 ?        S    09:11   0:00 [watchdogd]
root        33  0.0  0.0      0     0 ?        I<   09:11   0:00 [rpciod]
root        34  0.0  0.0      0     0 ?        I<   09:11   0:00 [kworker/u3:0-hci0]
root        35  0.0  0.0      0     0 ?        I<   09:11   0:00 [xprtiod]
root        36  0.0  0.0      0     0 ?        S    09:11   0:00 [kswapd0]
root        37  0.0  0.0      0     0 ?        I<   09:11   0:00 [nfsiod]
root        38  0.0  0.0      0     0 ?        I<   09:11   0:00 [iscsi_eh]
root        39  0.0  0.0      0     0 ?        I<   09:11   0:00 [dwc_otg]
root        40  0.0  0.0      0     0 ?        I<   09:11   0:00 [DWC Notificatio]
root        42  0.0  0.0      0     0 ?        S<   09:11   0:00 [vchiq-slot/0]
root        43  0.0  0.0      0     0 ?        S<   09:11   0:00 [vchiq-recy/0]
root        44  0.0  0.0      0     0 ?        S<   09:11   0:00 [vchiq-sync/0]
root        45  0.0  0.0      0     0 ?        S    09:11   0:00 [vchiq-keep/0]
root        46  0.0  0.0      0     0 ?        S<   09:11   0:00 [SMIO]
root        48  0.0  0.0      0     0 ?        I<   09:11   0:00 [mmc_complete]
root        49  0.1  0.0      0     0 ?        I<   09:11   0:02 [kworker/0:1H-kblockd]
root        50  0.0  0.0      0     0 ?        S    09:11   0:00 [jbd2/mmcblk0p2-]
root        51  0.0  0.0      0     0 ?        I<   09:11   0:00 [ext4-rsv-conver]
root        53  0.0  0.0      0     0 ?        I<   09:11   0:00 [ipv6_addrconf]
root        88  0.1  1.4  15932  6624 ?        Ss   09:11   0:02 /lib/systemd/systemd-journald
root       109  0.0  0.8  18364  3820 ?        Ss   09:11   0:01 /lib/systemd/systemd-udevd
root       123  0.0  0.0      0     0 ?        S<   09:11   0:00 [SMIO]
root       127  0.0  0.0      0     0 ?        I<   09:11   0:00 [mmal-vchiq]
root       133  0.0  0.0      0     0 ?        I<   09:11   0:00 [mmal-vchiq]
root       134  0.0  0.0      0     0 ?        I<   09:11   0:00 [mmal-vchiq]
root       135  0.0  0.0      0     0 ?        I<   09:11   0:00 [mmal-vchiq]
root       164  0.0  0.0      0     0 ?        I<   09:11   0:00 [cfg80211]
root       166  0.0  0.0      0     0 ?        I<   09:11   0:00 [brcmf_wq/mmc1:0]
root       167  0.0  0.0      0     0 ?        S    09:11   0:01 [brcmf_wdog/mmc1]
systemd+   216  0.0  1.2  22396  5548 ?        Ssl  09:11   0:00 /lib/systemd/systemd-timesyncd
root       254  0.0  1.2  12028  5580 ?        Ss   09:11   0:00 /usr/bin/python /home/pi/simple-fan.py
avahi      256  0.0  0.6   5888  2996 ?        Ss   09:11   0:00 avahi-daemon: running [rpiGarageOpener.local
root       264  0.0  0.5   7964  2344 ?        Ss   09:11   0:00 /usr/sbin/cron -f
root       271  0.0  1.3  13024  5912 ?        Ss   09:11   0:00 /lib/systemd/systemd-logind
avahi      276  0.0  0.3   5756  1588 ?        S    09:11   0:00 avahi-daemon: chroot helper
message+   284  0.0  0.8   6712  3688 ?        Ss   09:11   0:01 /usr/bin/dbus-daemon --system --address=syst
root       299  0.0  1.0  10724  4700 ?        Ss   09:11   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_suppl
nobody     304  0.0  0.4   4304  2064 ?        Ss   09:11   0:00 /usr/sbin/thd --triggers /etc/triggerhappy/t
root       305  0.0  0.4   2816  1780 ?        Ss   09:11   0:00 /sbin/dhcpcd -q -b
root       307  0.0  0.4   3676  2056 ?        SNs  09:11   0:00 /usr/sbin/alsactl -E HOME=/run/alsa -s -n 19
root       332  0.0  2.4  62156 10740 ?        Ssl  09:11   0:01 /usr/lib/udisks2/udisksd
root       339  0.0  0.3  27640  1364 ?        SLsl 09:11   0:00 /usr/sbin/rngd -r /dev/hwrng
root       344  0.0  0.8  24736  3684 ?        Ssl  09:11   0:00 /usr/sbin/rsyslogd -n -iNONE
root       363  0.0  1.7  39504  7536 ?        Ssl  09:12   0:00 /usr/lib/policykit-1/polkitd --no-debug
root       366  0.0  0.0      0     0 ?        I<   09:12   0:00 [kworker/u3:1-hci0]
root       367  0.0  0.1   2124   600 ?        S    09:12   0:00 /usr/bin/hciattach /dev/serial1 bcm43xx 3000
root       372  0.0  0.9  11108  4292 ?        Ss   09:12   0:00 wpa_supplicant -B -c/etc/wpa_supplicant/wpa_
root       396  0.0  1.0   9792  4728 ?        Ss   09:12   0:00 /usr/lib/bluetooth/bluetoothd
root       417  0.4  3.5  50508 15548 ?        Ssl  09:12   0:08 /usr/bin/python3 /usr/bin/fail2ban-server -x
root       418  0.0  1.2  10708  5740 ?        Ss   09:12   0:00 /usr/sbin/sshd -D
root       434  0.0  1.0  26692  4544 ?        Ssl  09:12   0:00 /usr/bin/bluealsa
root       451  0.0  1.6  39096  7340 ?        Ssl  09:12   0:00 /usr/sbin/lightdm
root       454  0.0  0.0      0     0 ?        S<   09:12   0:00 [krfcommd]
root       491  0.0  8.1 114896 36076 tty7     Ssl+ 09:12   0:01 /usr/lib/xorg/Xorg :0 -seat seat0 -auth /var
root       495  0.0  0.6   5604  2788 tty1     Ss   09:12   0:00 /bin/login -f
root       499  0.0  3.7 196136 16564 ?        Ss   09:12   0:00 /usr/sbin/apache2 -k start
www-data   510  0.0  2.1 197680  9436 ?        S    09:12   0:00 /usr/sbin/apache2 -k start
www-data   511  0.0  2.1 197680  9440 ?        S    09:12   0:00 /usr/sbin/apache2 -k start
www-data   512  0.0  2.1 197680  9440 ?        S    09:12   0:00 /usr/sbin/apache2 -k start
www-data   513  0.0  2.1 197680  9408 ?        S    09:12   0:00 /usr/sbin/apache2 -k start
www-data   514  0.0  2.1 197680  9440 ?        S    09:12   0:00 /usr/sbin/apache2 -k start
pi         529  0.0  1.6  14712  7308 ?        Ss   09:12   0:00 /lib/systemd/systemd --user
pi         534  0.0  0.8  16824  3624 ?        S    09:12   0:00 (sd-pam)
root       550  0.0  1.7  32392  7896 ?        Sl   09:12   0:00 lightdm --session-child 14 17
root       557  0.0  2.3  58280 10492 ?        SNs  09:12   0:00 /usr/bin/perl /usr/bin/rpimonitord -b /var/r
pi         569  0.0  2.4  58416 10928 ?        SN   09:12   0:00 /usr/bin/perl /usr/bin/rpimonitord -b /var/r
root       570  1.2  2.5  58280 11140 ?        SN   09:12   0:25 /usr/bin/perl /usr/bin/rpimonitord -b /var/r
pi         577  0.0  2.8  55304 12800 ?        Ssl  09:12   0:00 /usr/bin/lxsession -s LXDE-pi -e LXDE
pi         582  0.0  0.8   8472  3656 tty1     S+   09:12   0:00 -bash
pi         588  0.0  0.7   6524  3532 ?        Ss   09:12   0:00 /usr/bin/dbus-daemon --session --address=sys
pi         630  0.0  0.3   4504  1340 ?        Ss   09:12   0:00 /usr/bin/ssh-agent x-session-manager
pi         650  0.0  1.4  42384  6224 ?        Ssl  09:12   0:00 /usr/lib/gvfs/gvfsd
pi         657  0.0  1.5  53808  6840 ?        Sl   09:12   0:00 /usr/lib/gvfs/gvfsd-fuse /run/user/1000/gvfs
pi         673  0.0  3.2  62068 14576 ?        S    09:12   0:00 openbox --config-file /home/pi/.config/openb
pi         674  0.0  2.3  47120 10568 ?        Sl   09:12   0:00 lxpolkit
pi         675  0.3  6.4 144172 28588 ?        Sl   09:12   0:07 lxpanel --profile LXDE-pi
pi         676  0.1  4.9  71972 21708 ?        Sl   09:12   0:03 pcmanfm --desktop --profile LXDE-pi
pi         692  0.0  0.2   4504  1308 ?        Ss   09:12   0:00 /usr/bin/ssh-agent -s
root       695  0.0  0.7   9936  3368 ?        S    09:12   0:00 sudo piwiz
root       717  0.0  3.7  30436 16652 ?        S    09:12   0:01 piwiz
pi         844  0.0  2.3  78424 10608 ?        Ssl  09:12   0:00 /usr/lib/gvfs/gvfs-udisks2-volume-monitor
pi         850  0.0  1.4  28688  6632 ?        Sl   09:12   0:00 /usr/lib/menu-cache/menu-cached /run/user/10
pi         855  0.0  1.5  53968  7008 ?        Ssl  09:12   0:00 /usr/lib/gvfs/gvfs-afc-volume-monitor
pi         861  0.0  1.2  39068  5328 ?        Ssl  09:12   0:00 /usr/lib/gvfs/gvfs-goa-volume-monitor
pi         865  0.0  1.2  39084  5540 ?        Ssl  09:12   0:00 /usr/lib/gvfs/gvfs-mtp-volume-monitor
pi         870  0.0  1.3  40660  5772 ?        Ssl  09:12   0:00 /usr/lib/gvfs/gvfs-gphoto2-volume-monitor
pi         928  0.0  1.8  53060  8348 ?        Sl   09:12   0:00 /usr/lib/gvfs/gvfsd-trash --spawner :1.4 /or
root       949  0.3  4.1  25268 18312 ?        Ss   09:12   0:06 /usr/bin/python /usr/local/bin/rpi-echo.py
root      1167  0.0  1.4  12220  6336 ?        Ss   09:14   0:00 sshd: pi [priv]
pi        1173  0.0  0.9  12220  4024 ?        S    09:14   0:00 sshd: pi@pts/0
pi        1174  0.0  0.8   8608  3748 pts/0    Ss   09:14   0:01 -bash
root      1458  0.0  0.0      0     0 ?        I    09:18   0:01 [kworker/u2:0-brcmf_wq/mmc1:0001:1]
root      1898  0.0  0.7   9936  3336 pts/0    S    09:24   0:00 sudo python3 rest_server.py
root      1899  0.1  3.0  21820 13704 pts/0    S    09:24   0:02 python3 rest_server.py
root      2443  0.1  0.0      0     0 ?        I    09:33   0:01 [kworker/0:1-events]
root      2684  0.1  0.0      0     0 ?        I    09:37   0:00 [kworker/u2:2-brcmf_wq/mmc1:0001:1]
root      2749  0.0  0.0      0     0 ?        I<   09:38   0:00 [kworker/0:0H]
root      2780  0.0  0.0      0     0 ?        I    09:38   0:00 [kworker/0:0-events]
root      3125  0.0  0.0      0     0 ?        I<   09:43   0:00 [kworker/0:2H]
root      3126  0.1  0.0      0     0 ?        I    09:43   0:00 [kworker/u2:1-brcmf_wq/mmc1:0001:1]
root      3159  0.2  0.0      0     0 ?        I    09:44   0:00 [kworker/0:2-events]
pi        3285  0.0  0.5   9776  2496 pts/0    R+   09:46   0:00 ps -aux
pi@rpiGarageOpener:~/api $ ps -aux | grep 5070
pi        3307  0.0  0.4   7336  1956 pts/0    S+   09:46   0:00 grep --color=auto 5070
pi@rpiGarageOpener:~/api $ ps -aux | grep python
root       254  0.0  1.2  12028  5580 ?        Ss   09:11   0:00 /usr/bin/python /home/pi/simple-fan.py
root       417  0.4  3.5  50508 15548 ?        Ssl  09:12   0:08 /usr/bin/python3 /usr/bin/fail2ban-server -xf start
root       949  0.3  4.1  25268 18312 ?        Ss   09:12   0:06 /usr/bin/python /usr/local/bin/rpi-echo.py
root      1898  0.0  0.7   9936  3336 pts/0    S    09:24   0:00 sudo python3 rest_server.py
root      1899  0.1  3.0  21820 13704 pts/0    S    09:24   0:02 python3 rest_server.py
pi        3322  2.0  0.4   7336  1960 pts/0    S+   09:46   0:00 grep --color=auto python
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/rpi-echo.py
pi@rpiGarageOpener:~/api $ sudo netstat -tnlp | grep :5070
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN      949/python          
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/rpi-echo.py
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
root      1898  0.0  0.7   9936  3336 pts/0    S    09:24   0:00 sudo python3 rest_server.py
root      1899  0.1  3.0  21820 13704 pts/0    S    09:24   0:02 python3 rest_server.py
pi        3714  0.0  0.4   7336  2032 pts/0    S+   09:52   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ sudo kill 1898
[1]+  Terminated              sudo python3 rest_server.py
pi@rpiGarageOpener:~/api $ ps -aux | grep rest_server
pi        3728  0.0  0.4   7336  1952 pts/0    S+   09:53   0:00 grep --color=auto rest_server
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 09:55:56 - Starting REST server
2020/12/12 09:55:56 - Command line arguments:
2020/12/12 09:55:56 -   Input file  = 
2020/12/12 09:55:56 -   Log file = /home/pi/api/rest_server.log
2020/12/12 09:55:56 -   Port = 9443
2020/12/12 09:55:56 -   Use cert = False
2020/12/12 09:55:56 -   Use HTTPS = False
2020/12/12 09:55:56 -   Use multithreading = False

2020/12/12 09:55:56 - Web Server:
2020/12/12 09:55:56 -   Server name = rpiGarageOpener
2020/12/12 09:55:56 -   Local Server IP = 127.0.1.1
2020/12/12 09:55:56 -   Server IP = 192.168.1.227 

2020/12/12 09:55:56 -   No socket is required for HTTP?
^C2020/12/12 09:56:58 - Closing REST server
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 09:58:16 - Starting REST server
2020/12/12 09:58:16 - Command line arguments:
2020/12/12 09:58:16 -   Input file  = 
2020/12/12 09:58:16 -   Log file = /home/pi/api/rest_server.log
2020/12/12 09:58:16 -   Port = 9443
2020/12/12 09:58:16 -   Use cert = False
2020/12/12 09:58:16 -   Use HTTPS = False
2020/12/12 09:58:16 -   Use multithreading = False

2020/12/12 09:58:16 - Web Server:
2020/12/12 09:58:16 -   Server name = rpiGarageOpener
2020/12/12 09:58:16 -   Local Server IP = 127.0.1.1
2020/12/12 09:58:16 -   Server IP = 192.168.1.227 

Traceback (most recent call last):
  File "rest_server.py", line 463, in <module>
    main(sys.argv)
  File "rest_server.py", line 430, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
socket.gaierror: [Errno -2] Name or service not known
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 10:01:37 - Starting REST server
2020/12/12 10:01:37 - Command line arguments:
2020/12/12 10:01:37 -   Input file  = 
2020/12/12 10:01:37 -   Log file = /home/pi/api/rest_server.log
2020/12/12 10:01:37 -   Port = 9443
2020/12/12 10:01:37 -   Use cert = False
2020/12/12 10:01:37 -   Use HTTPS = False
2020/12/12 10:01:37 -   Use multithreading = False

2020/12/12 10:01:37 - Web Server:
2020/12/12 10:01:37 -   Server name = rpiGarageOpener
Traceback (most recent call last):
  File "rest_server.py", line 464, in <module>
    main(sys.argv)
  File "rest_server.py", line 416, in main
    printMsg("  Local Server IP = " + local_host_ip)
NameError: name 'local_host_ip' is not defined
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 10:02:32 - Starting REST server
2020/12/12 10:02:32 - Command line arguments:
2020/12/12 10:02:32 -   Input file  = 
2020/12/12 10:02:32 -   Log file = /home/pi/api/rest_server.log
2020/12/12 10:02:32 -   Port = 9443
2020/12/12 10:02:32 -   Use cert = False
2020/12/12 10:02:32 -   Use HTTPS = False
2020/12/12 10:02:32 -   Use multithreading = False

2020/12/12 10:02:32 - Web Server:
2020/12/12 10:02:32 -   Server name = rpiGarageOpener
2020/12/12 10:02:32 -   Local Server IP = 0:0:0:0
2020/12/12 10:02:32 -   Server IP = 192.168.1.227 

Traceback (most recent call last):
  File "rest_server.py", line 464, in <module>
    main(sys.argv)
  File "rest_server.py", line 431, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
socket.gaierror: [Errno -2] Name or service not known
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls /cat
ls: cannot access '/cat': No such file or directory
pi@rpiGarageOpener:~/api $ ls /etc
adduser.conf            fake-hwclock.data  libnl-3         passwd            selinux
aliases                 fb.modes           libpaper.d      passwd-           sensors3.conf
alsa                    fonts              lightdm         paxctld.conf      sensors.d
alternatives            fstab              lighttpd        perl              services
apache2                 fuse.conf          locale.alias    php               sgml
apparmor.d              gai.conf           locale.gen      pip.conf          shadow
apt                     gdb                localtime       plymouth          shadow-
avahi                   ghostscript        logcheck        polkit-1          shells
bash.bashrc             glvnd              login.defs      ppp               skel
bash_completion         gnome              logrotate.conf  profile           ssh
bash_completion.d       groff              logrotate.d     profile.d         ssl
bindresvport.blacklist  group              logwatch        protocols         ssmtp
binfmt.d                group-             machine-id      pulse             subgid
bluetooth               gshadow            magic           python            subuid
ca-certificates         gshadow-           magic.mime      python2.7         sudoers
ca-certificates.conf    gss                mailcap         python3           sudoers.d
calendar                gtk-2.0            mailcap.order   python3.7         sysctl.conf
chkrootkit.conf         gtk-3.0            mailname        rc0.d             sysctl.d
chromium-browser        host.conf          mail.rc         rc1.d             systemd
cifs-utils              hostname           manpath.config  rc2.d             terminfo
console-setup           hosts              menu-methods    rc3.d             timezone
cron.d                  hosts.allow        mime.types      rc4.d             timidity
cron.daily              hosts.deny         mke2fs.conf     rc5.d             tmpfiles.d
cron.hourly             idmapd.conf        modprobe.d      rc6.d             triggerhappy
cron.monthly            ifplugd            modules         rc.local          ucf.conf
crontab                 init               modules-load.d  rcS.d             udev
cron.weekly             init.d             monit           request-key.conf  udisks2
dbus-1                  initramfs-tools    motd            request-key.d     ufw
debconf.conf            inputrc            mtab            resolv.conf       update-motd.d
debian_version          insserv.conf.d     mysql           resolvconf        usb_modeswitch.conf
default                 iproute2           nanorc          resolv.conf.bak   usb_modeswitch.d
deluser.conf            issue              netconfig       resolvconf.conf   vdpau_wrapper.cfg
dhcp                    issue.net          network         rkhunter.conf     vim
dhcpcd.conf             kernel             networks        rmt               vnc
dictionaries-common     ldap               nsswitch.conf   rpc               vulkan
dphys-swapfile          ld.so.cache        openal          rpi-issue         wgetrc
dpkg                    ld.so.conf         opt             rpimonitor        wpa_supplicant
emacs                   ld.so.conf.d       os-release      rsyslog.conf      X11
email-addresses         ld.so.preload      PackageKit      rsyslog.d         xattr.conf
environment             libaudit.conf      pam.conf        RTIMULib.ini      xdg
exim4                   libblockdev        pam.d           securetty         xml
fail2ban                libibverbs.d       papersize       security
pi@rpiGarageOpener:~/api $ ls /etc/.hosts
ls: cannot access '/etc/.hosts': No such file or directory
pi@rpiGarageOpener:~/api $ cat /etc/hosts
127.0.0.1	localhost
::1		localhost ip6-localhost ip6-loopback
ff02::1		ip6-allnodes
ff02::2		ip6-allrouters

127.0.1.1	rpiGarageOpener
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ sudo reboot
Connection to rpigarageopener.local closed by remote host.
Connection to rpigarageopener.local closed.
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sat Dec 12 10:10:15 2020
pi@rpiGarageOpener:~ $ python3 rest_server.py -d
python3: can't open file 'rest_server.py': [Errno 2] No such file or directory
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 10:17:42 - Starting REST server
2020/12/12 10:17:42 - Command line arguments:
2020/12/12 10:17:42 -   Input file  = 
2020/12/12 10:17:42 -   Log file = /home/pi/api/rest_server.log
2020/12/12 10:17:42 -   Port = 9443
2020/12/12 10:17:42 -   Use cert = False
2020/12/12 10:17:42 -   Use HTTPS = False
2020/12/12 10:17:42 -   Use multithreading = False

2020/12/12 10:17:42 - Web Server:
2020/12/12 10:17:42 -   Server name = rpiGarageOpener
2020/12/12 10:17:42 -   Local Server IP = 0:0:0:0
2020/12/12 10:17:42 -   Server IP = 192.168.1.227 

Traceback (most recent call last):
  File "rest_server.py", line 464, in <module>
    main(sys.argv)
  File "rest_server.py", line 431, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
socket.gaierror: [Errno -2] Name or service not known
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 10:18:27 - Starting REST server
2020/12/12 10:18:27 - Command line arguments:
2020/12/12 10:18:27 -   Input file  = 
2020/12/12 10:18:27 -   Log file = /home/pi/api/rest_server.log
2020/12/12 10:18:27 -   Port = 9443
2020/12/12 10:18:27 -   Use cert = False
2020/12/12 10:18:27 -   Use HTTPS = False
2020/12/12 10:18:27 -   Use multithreading = False

2020/12/12 10:18:27 - Web Server:
2020/12/12 10:18:27 -   Server name = rpiGarageOpener
2020/12/12 10:18:27 -   Local Server IP = 0.0.0.0
2020/12/12 10:18:27 -   Server IP = 192.168.1.227 

2020/12/12 10:18:27 -   No socket is required for HTTP?
2020/12/12 10:19:20 - GET /api/cpu HTTP/1.1
2020/12/12 10:19:20 - Client is: 192.168.1.139 39658
2020/12/12 10:19:20 - 192.168.1.139 39658
----------------------------------------
Exception happened during processing of request from ('192.168.1.139', 39658)
Traceback (most recent call last):
  File "/usr/lib/python3.7/socketserver.py", line 316, in _handle_request_noblock
    self.process_request(request, client_address)
  File "/usr/lib/python3.7/socketserver.py", line 347, in process_request
    self.finish_request(request, client_address)
  File "/usr/lib/python3.7/socketserver.py", line 360, in finish_request
    self.RequestHandlerClass(request, client_address, self)
  File "/usr/lib/python3.7/socketserver.py", line 720, in __init__
    self.handle()
  File "/usr/lib/python3.7/http/server.py", line 426, in handle
    self.handle_one_request()
  File "/usr/lib/python3.7/http/server.py", line 414, in handle_one_request
    method()
  File "rest_server.py", line 248, in do_GET
    if self.isClientIpInvalid():
  File "rest_server.py", line 203, in isClientIpInvalid
    printMsg('Client IP is valid: ' + client)
TypeError: can only concatenate str (not "IPv4Address") to str
----------------------------------------
^C2020/12/12 10:22:11 - Closing REST server
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 10:22:53 - Starting REST server
2020/12/12 10:22:53 - Command line arguments:
2020/12/12 10:22:53 -   Input file  = 
2020/12/12 10:22:53 -   Log file = /home/pi/api/rest_server.log
2020/12/12 10:22:53 -   Port = 9443
2020/12/12 10:22:53 -   Use cert = False
2020/12/12 10:22:53 -   Use HTTPS = False
2020/12/12 10:22:53 -   Use multithreading = False

2020/12/12 10:22:53 - Web Server:
2020/12/12 10:22:53 -   Server name = rpiGarageOpener
2020/12/12 10:22:53 -   Local Server IP = 0.0.0.0
2020/12/12 10:22:53 -   Server IP = 192.168.1.227 

2020/12/12 10:22:53 -   No socket is required for HTTP?
2020/12/12 10:22:55 - GET /api/cpu HTTP/1.1
2020/12/12 10:22:55 - Client is: 192.168.1.139 39660
2020/12/12 10:22:55 - 192.168.1.139 39660
2020/12/12 10:22:55 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 10:22:55] "GET /api/cpu HTTP/1.1" 200 -
2020/12/12 10:22:55 - Execute command: /home/pi/api/cpu/get.py
^C2020/12/12 10:34:51 - Closing REST server
pi@rpiGarageOpener:~/api $ netstat -an | grep "LISTEN "
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
pi@rpiGarageOpener:~/api $ python3 rest_server.py &
[1] 2442
pi@rpiGarageOpener:~/api $ netstat -an | grep "LISTEN "
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:9443            0.0.0.0:*               LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
pi@rpiGarageOpener:~/api $ sudo kill 2442
[1]+  Terminated              python3 rest_server.py
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ python3 rest_server.py &
[1] 2520
pi@rpiGarageOpener:~/api $ netstat -an | grep "LISTEN "
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.1.1:9443          0.0.0.0:*               LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
tcp6       0      0 :::22                   :::*                    LISTEN     
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ nc -zv rpiGarageOpener 9443
nc: connect to rpiGarageOpener port 9443 (tcp) failed: Connection refused
pi@rpiGarageOpener:~/api $ sudo kill 2520
[1]+  Terminated              python3 rest_server.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py &
[1] 3560
pi@rpiGarageOpener:~/api $ nc -zv rpiGarageOpener 9443
Connection to rpiGarageOpener 9443 port [tcp/*] succeeded!
pi@rpiGarageOpener:~/api $ python3 rest_server.py &
[2] 3858
pi@rpiGarageOpener:~/api $ Traceback (most recent call last):
  File "rest_server.py", line 464, in <module>
    main(sys.argv)
  File "rest_server.py", line 431, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
^C
[2]+  Exit 1                  python3 rest_server.py
pi@rpiGarageOpener:~/api $ ps -aux | grep reset_server
pi        3892  0.0  0.4   7336  1888 pts/0    S+   10:57   0:00 grep --color=auto reset_server
pi@rpiGarageOpener:~/api $ python3 rest_server.py &
[2] 3913
pi@rpiGarageOpener:~/api $ Traceback (most recent call last):
  File "rest_server.py", line 464, in <module>
    main(sys.argv)
  File "rest_server.py", line 431, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
^C
[2]+  Exit 1                  python3 rest_server.py
pi@rpiGarageOpener:~/api $ sudo nano /etc/hosts
pi@rpiGarageOpener:~/api $ python3 rest_server.py 
Traceback (most recent call last):
  File "rest_server.py", line 464, in <module>
    main(sys.argv)
  File "rest_server.py", line 431, in main
    httpd = HTTPServer(rest_server, customHandler)
  File "/usr/lib/python3.7/socketserver.py", line 452, in __init__
    self.server_bind()
  File "/usr/lib/python3.7/http/server.py", line 137, in server_bind
    socketserver.TCPServer.server_bind(self)
  File "/usr/lib/python3.7/socketserver.py", line 466, in server_bind
    self.socket.bind(self.server_address)
OSError: [Errno 98] Address already in use
pi@rpiGarageOpener:~/api $ sudo reboot
pi@rpiGarageOpener:~/api $ Connection to rpigarageopener.local closed by remote host.
Connection to rpigarageopener.local closed.
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sat Dec 12 11:00:19 2020
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 11:01:59 - Starting REST server
2020/12/12 11:01:59 - Command line arguments:
2020/12/12 11:01:59 -   Input file  = 
2020/12/12 11:01:59 -   Log file = /home/pi/api/rest_server.log
2020/12/12 11:01:59 -   Port = 9443
2020/12/12 11:01:59 -   Use cert = False
2020/12/12 11:01:59 -   Use HTTPS = False
2020/12/12 11:01:59 -   Use multithreading = False

2020/12/12 11:01:59 - Web Server:
2020/12/12 11:01:59 -   Server name = rpiGarageOpener
2020/12/12 11:01:59 -   Local Server IP = 0.0.0.0
2020/12/12 11:01:59 -   Server IP = 192.168.1.227 

2020/12/12 11:01:59 -   No socket is required for HTTP?
2020/12/12 11:03:04 - GET /api/cpu HTTP/1.1
2020/12/12 11:03:04 - Client is: 192.168.1.139 39672
2020/12/12 11:03:04 - 192.168.1.139 39672
2020/12/12 11:03:04 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 11:03:04] "GET /api/cpu HTTP/1.1" 200 -
2020/12/12 11:03:04 - Execute command: /home/pi/api/cpu/get.py
^C2020/12/12 11:26:25 - Closing REST server
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
pi@rpiGarageOpener:~/api $ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
22/tcp                     LIMIT       Anywhere                  
443/tcp                    ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
Anywhere                   ALLOW       192.168.0.0/24            
9080                       ALLOW       Anywhere                  
9443                       ALLOW       Anywhere                  
22/tcp (v6)                LIMIT       Anywhere (v6)             
443/tcp (v6)               ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
9080 (v6)                  ALLOW       Anywhere (v6)             
9443 (v6)                  ALLOW       Anywhere (v6)             

pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 11:59:12 - Starting REST server
2020/12/12 11:59:12 - Command line arguments:
2020/12/12 11:59:12 -   Input file  = 
2020/12/12 11:59:12 -   Log file = /home/pi/api/rest_server.log
2020/12/12 11:59:12 -   Port = 9443
2020/12/12 11:59:12 -   Use cert = False
2020/12/12 11:59:12 -   Use HTTPS = False
2020/12/12 11:59:12 -   Use multithreading = False

2020/12/12 11:59:12 - Web Server:
2020/12/12 11:59:12 -   Server name = rpiGarageOpener
2020/12/12 11:59:12 -   Local Server IP = 0.0.0.0
2020/12/12 11:59:12 -   Server IP = 192.168.1.227 

2020/12/12 11:59:12 -   No socket is required for HTTP?
2020/12/12 11:59:18 - GET /api/cpu HTTP/1.1
2020/12/12 11:59:18 - Client is: 192.168.1.139 39674
2020/12/12 11:59:18 - 192.168.1.139 39674
2020/12/12 11:59:18 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 11:59:18] "GET /api/cpu HTTP/1.1" 200 -
2020/12/12 11:59:18 - Execute command: /home/pi/api/cpu/get.py
^C2020/12/12 12:13:26 - Closing REST server
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ $ netstat -lptn
-bash: $: command not found
pi@rpiGarageOpener:~/api $ netstat -lptn
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 192.168.1.227:5070      0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8888            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
pi@rpiGarageOpener:~/api $ ls ..
api                dead.letter  genID.py        Music                read.py           Templates
Bookshelf          Desktop      getScripts2.sh  myID.txt             rpi-echo.log      tls2.sh
b.sh               Documents    getScripts.sh   Pictures             rpi-echo.service  tls.sh
check_apache.html  Downloads    getWebsite.sh   Public               simple-fan.py     unused_rpi.sh
createDB.sh        emailTry.py  hello.py        pushGarageRemote.py  simple-fan.py.1   Videos
pi@rpiGarageOpener:~/api $ cp ../getScripts.sh .
pi@rpiGarageOpener:~/api $ nano getServer.sh
pi@rpiGarageOpener:~/api $ mv getScripts.sh getServer.sh
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ nano getServer.sh
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.json      get.txt     os         restful_api      server          server.key
client.key  favicon.png  get.py        memory      README.md  rest_server.log  server_cron.sh  time
cpu         get.backup   getServer.sh  navigation  reboot     rest_server.py   server.crt      uptime
pi@rpiGarageOpener:~/api $ cat get.text
cat: get.text: No such file or directory
pi@rpiGarageOpener:~/api $ cat get.txt
"description" : "returns hostname"
pi@rpiGarageOpener:~/api $ nano getServer.sh
pi@rpiGarageOpener:~/api $ mkdir test
pi@rpiGarageOpener:~/api $ nano getServer.sh
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ cd ..
pi@rpiGarageOpener:~ $  wget https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/getAPI.sh
--2020-12-12 14:22:22--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/getAPI.sh
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.128.133, 151.101.192.133, 151.101.0.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.128.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1770 (1.7K) [text/plain]
Saving to: ‘getAPI.sh’

getAPI.sh                   100%[========================================>]   1.73K  --.-KB/s    in 0.002s  

2020-12-12 14:22:22 (1.04 MB/s) - ‘getAPI.sh’ saved [1770/1770]

pi@rpiGarageOpener:~ $ bash getAPI.sh
--2020-12-12 14:22:31--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/open/get.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 100 [text/plain]
Saving to: ‘get.py’

get.py                      100%[========================================>]     100  --.-KB/s    in 0.003s  

2020-12-12 14:22:31 (33.1 KB/s) - ‘get.py’ saved [100/100]

--2020-12-12 14:22:31--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/open/get.json
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1 [text/plain]
Saving to: ‘get.json’

get.json                    100%[========================================>]       1  --.-KB/s    in 0s      

2020-12-12 14:22:32 (3.45 KB/s) - ‘get.json’ saved [1/1]

--2020-12-12 14:22:32--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/open/get.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 35 [text/plain]
Saving to: ‘get.txt’

get.txt                     100%[========================================>]      35  --.-KB/s    in 0.001s  

2020-12-12 14:22:32 (35.6 KB/s) - ‘get.txt’ saved [35/35]

--2020-12-12 14:22:32--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/open/get.backup.sh
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 100 [text/plain]
Saving to: ‘get.backup.sh’

get.backup.sh               100%[========================================>]     100  --.-KB/s    in 0s      

2020-12-12 14:22:33 (312 KB/s) - ‘get.backup.sh’ saved [100/100]

--2020-12-12 14:22:33--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/close/get.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 102 [text/plain]
Saving to: ‘get.py’

get.py                      100%[========================================>]     102  --.-KB/s    in 0s      

2020-12-12 14:22:33 (318 KB/s) - ‘get.py’ saved [102/102]

--2020-12-12 14:22:33--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/close/get.json
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1 [text/plain]
Saving to: ‘get.json’

get.json                    100%[========================================>]       1  --.-KB/s    in 0s      

2020-12-12 14:22:34 (3.71 KB/s) - ‘get.json’ saved [1/1]

--2020-12-12 14:22:34--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/close/get.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 36 [text/plain]
Saving to: ‘get.txt’

get.txt                     100%[========================================>]      36  --.-KB/s    in 0s      

2020-12-12 14:22:34 (112 KB/s) - ‘get.txt’ saved [36/36]

--2020-12-12 14:22:34--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/close/get.backup.sh
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 102 [text/plain]
Saving to: ‘get.backup.sh’

get.backup.sh               100%[========================================>]     102  --.-KB/s    in 0s      

2020-12-12 14:22:34 (320 KB/s) - ‘get.backup.sh’ saved [102/102]

--2020-12-12 14:22:34--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/toggle/get.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.0.133, 151.101.128.133, 151.101.192.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.0.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 169 [text/plain]
Saving to: ‘get.py’

get.py                      100%[========================================>]     169  --.-KB/s    in 0.002s  

2020-12-12 14:22:35 (93.1 KB/s) - ‘get.py’ saved [169/169]

--2020-12-12 14:22:35--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/toggle/get.json
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1 [text/plain]
Saving to: ‘get.json’

get.json                    100%[========================================>]       1  --.-KB/s    in 0s      

2020-12-12 14:22:35 (3.44 KB/s) - ‘get.json’ saved [1/1]

--2020-12-12 14:22:35--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/toggle/get.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.128.133, 151.101.64.133, 151.101.0.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.128.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 38 [text/plain]
Saving to: ‘get.txt’

get.txt                     100%[========================================>]      38  --.-KB/s    in 0s      

2020-12-12 14:22:36 (132 KB/s) - ‘get.txt’ saved [38/38]

--2020-12-12 14:22:36--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/toggle/get.backup.sh
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 169 [text/plain]
Saving to: ‘get.backup.sh’

get.backup.sh               100%[========================================>]     169  --.-KB/s    in 0s      

2020-12-12 14:22:36 (548 KB/s) - ‘get.backup.sh’ saved [169/169]

--2020-12-12 14:22:36--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/state/get.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 129 [text/plain]
Saving to: ‘get.py’

get.py                      100%[========================================>]     129  --.-KB/s    in 0s      

2020-12-12 14:22:37 (409 KB/s) - ‘get.py’ saved [129/129]

--2020-12-12 14:22:37--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/state/get.json
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1 [text/plain]
Saving to: ‘get.json’

get.json                    100%[========================================>]       1  --.-KB/s    in 0s      

2020-12-12 14:22:37 (3.38 KB/s) - ‘get.json’ saved [1/1]

--2020-12-12 14:22:37--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/state/get.txt
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 199.232.8.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|199.232.8.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 36 [text/plain]
Saving to: ‘get.txt’

get.txt                     100%[========================================>]      36  --.-KB/s    in 0s      

2020-12-12 14:22:38 (119 KB/s) - ‘get.txt’ saved [36/36]

--2020-12-12 14:22:38--  https://raw.githubusercontent.com/dumbo25/garage-door/main/home/pi/api/state/get.backup.sh
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.0.133, 151.101.192.133, 151.101.64.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.0.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 129 [text/plain]
Saving to: ‘get.backup.sh’

get.backup.sh               100%[========================================>]     129  --.-KB/s    in 0s      

2020-12-12 14:22:38 (395 KB/s) - ‘get.backup.sh’ saved [129/129]

pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        hello.py  pushGarageRemote.py  simple-fan.py.1  Videos
Bookshelf          Desktop      getAPI.sh       Music     read.py              Templates
b.sh               Documents    getScripts2.sh  myID.txt  rpi-echo.log         tls2.sh
check_apache.html  Downloads    getScripts.sh   Pictures  rpi-echo.service     tls.sh
createDB.sh        emailTry.py  getWebsite.sh   Public    simple-fan.py        unused_rpi.sh
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.py        navigation  reboot           server          state   uptime
client.key  favicon.png  getServer.sh  open        restful_api      server_cron.sh  test
close       get.backup   get.txt       os          rest_server.log  server.crt      time
cpu         get.json     memory        README.md   rest_server.py   server.key      toggle
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 14:24:10 - Starting REST server
2020/12/12 14:24:10 - Command line arguments:
2020/12/12 14:24:10 -   Input file  = 
2020/12/12 14:24:10 -   Log file = /home/pi/api/rest_server.log
2020/12/12 14:24:10 -   Port = 9443
2020/12/12 14:24:10 -   Use cert = False
2020/12/12 14:24:10 -   Use HTTPS = False
2020/12/12 14:24:10 -   Use multithreading = False

2020/12/12 14:24:10 - Web Server:
2020/12/12 14:24:10 -   Server name = rpiGarageOpener
2020/12/12 14:24:10 -   Local Server IP = 0.0.0.0
2020/12/12 14:24:10 -   Server IP = 192.168.1.227 

2020/12/12 14:24:10 -   No socket is required for HTTP?
2020/12/12 14:24:14 - GET /api/open HTTP/1.1
2020/12/12 14:24:14 - Client is: 192.168.1.139 39680
2020/12/12 14:24:14 - 192.168.1.139 39680
2020/12/12 14:24:14 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 14:24:15] "GET /api/open HTTP/1.1" 200 -
2020/12/12 14:24:15 - Execute command: /home/pi/api/open/get.py
^C2020/12/12 14:24:53 - Closing REST server
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 14:29:17 - Starting REST server
2020/12/12 14:29:17 - Command line arguments:
2020/12/12 14:29:17 -   Input file  = 
2020/12/12 14:29:17 -   Log file = /home/pi/api/rest_server.log
2020/12/12 14:29:17 -   Port = 9443
2020/12/12 14:29:17 -   Use cert = False
2020/12/12 14:29:17 -   Use HTTPS = False
2020/12/12 14:29:17 -   Use multithreading = False

2020/12/12 14:29:17 - Web Server:
2020/12/12 14:29:17 -   Server name = rpiGarageOpener
2020/12/12 14:29:17 -   Local Server IP = 0.0.0.0
2020/12/12 14:29:17 -   Server IP = 192.168.1.227 

2020/12/12 14:29:17 -   No socket is required for HTTP?
2020/12/12 14:30:58 - GET /api/close HTTP/1.1
2020/12/12 14:30:58 - Client is: 192.168.1.139 39682
2020/12/12 14:30:58 - 192.168.1.139 39682
2020/12/12 14:30:58 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 14:31:01] "GET /api/close HTTP/1.1" 200 -
2020/12/12 14:31:01 - Execute command: /home/pi/api/close/get.py
2020/12/12 17:00:37 - GET /api/state HTTP/1.1
2020/12/12 17:00:37 - Client is: 192.168.1.139 39684
2020/12/12 17:00:37 - 192.168.1.139 39684
2020/12/12 17:00:37 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 17:00:38] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:00:38 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 17:01:13 - Closing REST server
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ cat state/get.py
global Data
# returns whether garage door is open or closed
cmd = 'sudo python /usr/local/bin/close.py'
os.system(cmd)
Data = {}
pi@rpiGarageOpener:~/api $ ls ..
api                dead.letter  genID.py        hello.py  pushGarageRemote.py  simple-fan.py.1  Videos
Bookshelf          Desktop      getAPI.sh       Music     read.py              Templates
b.sh               Documents    getScripts2.sh  myID.txt  rpi-echo.log         tls2.sh
check_apache.html  Downloads    getScripts.sh   Pictures  rpi-echo.service     tls.sh
createDB.sh        emailTry.py  getWebsite.sh   Public    simple-fan.py        unused_rpi.sh
pi@rpiGarageOpener:~/api $ ls /usr/local/bin
close.py   distro     fauxmo.pyc  mylog.py   open.py      sleep.py
disarm.py  fauxmo.py  garage.sh   mylog.pyc  rpi-echo.py  toggle.py
pi@rpiGarageOpener:~/api $ cat /usr/lcaol/bin/garage.sh
cat: /usr/lcaol/bin/garage.sh: No such file or directory
pi@rpiGarageOpener:~/api $ cat /usr/local/bin/garage.sh
#!/bin/bash
# check if the garage door is open.
# enter a  crontab: */5 * * * * sudo /usr/local/bin/garage.sh
# If open send an alert and write to syslog
up=0
gmail='cartwright25@gmail.com'
id='SL9ZXP'

sensor=5
gpio -g mode $sensor down
sleep 1

door=$(gpio read $sensor)

# get current time
currTime=`date +%k%M`


# get whether or not on vacation
# I get emails when SQLITE_BUSY occurs. So, changed timeout from 1000 to 20000. Seems like recommended solution.
vacation=$(sqlite3 -init <(echo .timeout 20000) /var/www/db/garagedoor.db "SELECT value FROM status WHERE name = \"vacation\"";)


# # if on vacation
if [ "$vacation" == "yes" ]
then
	# and door is up
	if [ "$door" -eq "$up" ]; then
		logger rpiGarageOpener: Garage Door Open
		subj = id + " Garage: open while vacationing"
		echo "close the garage door" | mail -s $subj $gmail
        fi
# if not on vacation and time is between 10pm and midnight
elif [ "$vacation" == "no" ]
then
        if [ $currTime -gt 2200 -a $currTime -lt 2400 ]
        then
                if [ "$door" -eq "$up" ]
	        then
                        logger rpiGarageOpener: Garage Door Open
	                subj = id + " Garage: open too late"
        	        echo "close the garage door" | mail -s $subj $gmail
                fi
        # or, if time is less then 7:00am
        elif [ $currTime -gt 0 -a $currTime -lt 700 ]
        then
                if [ "$door" -eq "$up" ]
        	then
                        logger rpiGarageOpener: Garage Door Open
	                subj = id + " Garage: open too early"
        	        echo "close the garage door" | mail -s $subj $gmail
                fi
        fi
fi

# some debug outputs
# echo "up = $up"
# echo "door = $door"
# echo "vacation = #vacation"
# echo "time = $currtIme"
exit 0
pi@rpiGarageOpener:~/api $ gpio -g mode 5 down
pi@rpiGarageOpener:~/api $ gpio -g read 5
0
pi@rpiGarageOpener:~/api $ gpio -g mode 5 down; gpio -g read 5
0
pi@rpiGarageOpener:~/api $ cd state
pi@rpiGarageOpener:~/api/state $ ls
get.backup.sh  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api/state $ nano get.py
pi@rpiGarageOpener:~/api/state $ cd ..
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.py        navigation  reboot           server          state   uptime
client.key  favicon.png  getServer.sh  open        restful_api      server_cron.sh  test
close       get.backup   get.txt       os          rest_server.log  server.crt      time
cpu         get.json     memory        README.md   rest_server.py   server.key      toggle
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 17:06:37 - Starting REST server
2020/12/12 17:06:37 - Command line arguments:
2020/12/12 17:06:37 -   Input file  = 
2020/12/12 17:06:37 -   Log file = /home/pi/api/rest_server.log
2020/12/12 17:06:37 -   Port = 9443
2020/12/12 17:06:37 -   Use cert = False
2020/12/12 17:06:37 -   Use HTTPS = False
2020/12/12 17:06:37 -   Use multithreading = False

2020/12/12 17:06:37 - Web Server:
2020/12/12 17:06:37 -   Server name = rpiGarageOpener
2020/12/12 17:06:37 -   Local Server IP = 0.0.0.0
2020/12/12 17:06:37 -   Server IP = 192.168.1.227 

2020/12/12 17:06:37 -   No socket is required for HTTP?
2020/12/12 17:07:46 - GET /api/state HTTP/1.1
2020/12/12 17:07:46 - Client is: 192.168.1.139 39686
2020/12/12 17:07:46 - 192.168.1.139 39686
2020/12/12 17:07:46 - Client IP is valid: 192.168.1.139
0
192.168.1.139 - - [12/Dec/2020 17:07:46] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:07:46 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 17:08:04 - Closing REST server
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls state
get.backup.sh  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ cat state/get.txt
"description" : "close garage door"
pi@rpiGarageOpener:~/api $ nano state/get.txt
pi@rpiGarageOpener:~/api $ nano state/get.json
pi@rpiGarageOpener:~/api $ cat state/get.backup.sh
global Data
# returns whether garage door is open or closed
cmd = 'sudo python /usr/local/bin/close.py'
os.system(cmd)
Data = {}
pi@rpiGarageOpener:~/api $ nano state/get.backup.sh
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.py        navigation  reboot           server          state   uptime
client.key  favicon.png  getServer.sh  open        restful_api      server_cron.sh  test
close       get.backup   get.txt       os          rest_server.log  server.crt      time
cpu         get.json     memory        README.md   rest_server.py   server.key      toggle
pi@rpiGarageOpener:~/api $ ls os
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ cat os/get.py
global Data
# returns operating system data
Data = {"distro": distro.linux_distribution()}

pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ nano state/get.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 17:13:33 - Starting REST server
2020/12/12 17:13:33 - Command line arguments:
2020/12/12 17:13:33 -   Input file  = 
2020/12/12 17:13:33 -   Log file = /home/pi/api/rest_server.log
2020/12/12 17:13:33 -   Port = 9443
2020/12/12 17:13:33 -   Use cert = False
2020/12/12 17:13:33 -   Use HTTPS = False
2020/12/12 17:13:33 -   Use multithreading = False

2020/12/12 17:13:33 - Web Server:
2020/12/12 17:13:33 -   Server name = rpiGarageOpener
2020/12/12 17:13:33 -   Local Server IP = 0.0.0.0
2020/12/12 17:13:33 -   Server IP = 192.168.1.227 

2020/12/12 17:13:33 -   No socket is required for HTTP?
2020/12/12 17:13:38 - GET /api/state HTTP/1.1
2020/12/12 17:13:38 - Client is: 192.168.1.139 39688
2020/12/12 17:13:38 - 192.168.1.139 39688
2020/12/12 17:13:38 - Client IP is valid: 192.168.1.139
0
192.168.1.139 - - [12/Dec/2020 17:13:38] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:13:38 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:13:51 - GET /api/open HTTP/1.1
2020/12/12 17:13:51 - Client is: 192.168.1.139 39690
2020/12/12 17:13:51 - 192.168.1.139 39690
2020/12/12 17:13:51 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 17:13:54] "GET /api/open HTTP/1.1" 200 -
2020/12/12 17:13:54 - Execute command: /home/pi/api/open/get.py
2020/12/12 17:14:00 - GET /api/state HTTP/1.1
2020/12/12 17:14:00 - Client is: 192.168.1.139 39692
2020/12/12 17:14:00 - 192.168.1.139 39692
2020/12/12 17:14:00 - Client IP is valid: 192.168.1.139
0
192.168.1.139 - - [12/Dec/2020 17:14:00] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:14:00 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:14:08 - GET /api/state HTTP/1.1
2020/12/12 17:14:08 - Client is: 192.168.1.139 39694
2020/12/12 17:14:08 - 192.168.1.139 39694
2020/12/12 17:14:08 - Client IP is valid: 192.168.1.139
0
192.168.1.139 - - [12/Dec/2020 17:14:08] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:14:08 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:14:18 - GET /api/state HTTP/1.1
2020/12/12 17:14:18 - Client is: 192.168.1.139 39696
2020/12/12 17:14:18 - 192.168.1.139 39696
2020/12/12 17:14:18 - Client IP is valid: 192.168.1.139
0
192.168.1.139 - - [12/Dec/2020 17:14:18] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:14:18 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:14:29 - GET /api/state HTTP/1.1
2020/12/12 17:14:29 - Client is: 192.168.1.139 39698
2020/12/12 17:14:29 - 192.168.1.139 39698
2020/12/12 17:14:29 - Client IP is valid: 192.168.1.139
0
192.168.1.139 - - [12/Dec/2020 17:14:29] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:14:29 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:15:35 - GET /api/state HTTP/1.1
2020/12/12 17:15:35 - Client is: 192.168.1.139 39700
2020/12/12 17:15:35 - 192.168.1.139 39700
2020/12/12 17:15:35 - Client IP is valid: 192.168.1.139
0
192.168.1.139 - - [12/Dec/2020 17:15:35] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:15:35 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 17:15:47 - Closing REST server
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls ../..
pi
pi@rpiGarageOpener:~/api $ ls ..
api                dead.letter  genID.py        hello.py  pushGarageRemote.py  simple-fan.py.1  Videos
Bookshelf          Desktop      getAPI.sh       Music     read.py              Templates
b.sh               Documents    getScripts2.sh  myID.txt  rpi-echo.log         tls2.sh
check_apache.html  Downloads    getScripts.sh   Pictures  rpi-echo.service     tls.sh
createDB.sh        emailTry.py  getWebsite.sh   Public    simple-fan.py        unused_rpi.sh
pi@rpiGarageOpener:~/api $ cat open/close.py
cat: open/close.py: No such file or directory
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.py        navigation  reboot           server          state   uptime
client.key  favicon.png  getServer.sh  open        restful_api      server_cron.sh  test
close       get.backup   get.txt       os          rest_server.log  server.crt      time
cpu         get.json     memory        README.md   rest_server.py   server.key      toggle
pi@rpiGarageOpener:~/api $ ls close
get.backup.sh  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ cat /usr/local/bin/close.py
#!/susr/bin/python

#########################
#
# closes.py closes a garage door by electronically closing a push button on
# a universla remote
#
# if the garage door is already closed then no action is taken
#
# The complete project is described here:
#  https://sites.google.com/site/cartwrightraspberrypiprojects/home/home-automation-categories/access-control/garage-door-opener
#
# close.py is used in conjunction with fauxmo and Amazon Echo to control
# the garage door.
#
# The system requires a remote control, relay and a sensor
#
# close.py was tested on a Raspberry Pi Zero WH running Raspberry Pi OS
#
# The connections are as shown below:
#   RPi0 GND (physical pin 6) to Relay GND
#   RPi0 BCM GPIO 23 (physical pin 16, Wiring Pi pin 4) to Relay IN2
#   RPi0 5v (pin 2 or 4) to Relay VCC
#   Relay NO to Header Pin on Remote
#   Relay Power to 12V+ on Remote
#   RPi0 3.3v (physical pin1) to Sensor GND
#   RPi0 BCM GPIO 24 (physical pin 18, Wiring Pi pin 5) to Sensor output
#
# close.py is called rpi-echo.py
# rpi-echo.py starts automatically using systemd
#
#########################

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

PRESS = 23
SENSOR = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(PRESS, GPIO.OUT)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# wait for sensor pin to reach steady state before reading
sleep(1)

open = GPIO.input(SENSOR)
# print ("open = " + str(open))
if open == 0:
    GPIO.output(PRESS, GPIO.LOW)
    sleep(1)
    GPIO.output(PRESS, GPIO.HIGH)
    sleep(1)

GPIO.cleanup()

pi@rpiGarageOpener:~/api $ sudo cp /usr/local/bin/close.py /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ sudo python /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ sudo python /usr/local/bin/state.py
closed
pi@rpiGarageOpener:~/api $ sudo python /usr/local/bin/state.py
closed
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ sudo python /usr/local/bin/state.py
open
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ nano state/get.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 17:25:19 - Starting REST server
2020/12/12 17:25:19 - Command line arguments:
2020/12/12 17:25:19 -   Input file  = 
2020/12/12 17:25:19 -   Log file = /home/pi/api/rest_server.log
2020/12/12 17:25:19 -   Port = 9443
2020/12/12 17:25:19 -   Use cert = False
2020/12/12 17:25:19 -   Use HTTPS = False
2020/12/12 17:25:19 -   Use multithreading = False

2020/12/12 17:25:19 - Web Server:
2020/12/12 17:25:19 -   Server name = rpiGarageOpener
2020/12/12 17:25:19 -   Local Server IP = 0.0.0.0
2020/12/12 17:25:19 -   Server IP = 192.168.1.227 

2020/12/12 17:25:19 -   No socket is required for HTTP?
2020/12/12 17:25:27 - GET /api/state HTTP/1.1
2020/12/12 17:25:27 - Client is: 192.168.1.139 39702
2020/12/12 17:25:27 - 192.168.1.139 39702
2020/12/12 17:25:27 - Client IP is valid: 192.168.1.139
open
192.168.1.139 - - [12/Dec/2020 17:25:28] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:25:28 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 17:28:00 - Closing REST server
pi@rpiGarageOpener:~/api $ sudo python /usr/local/bin/state.py
open
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 17:29:07 - Starting REST server
2020/12/12 17:29:07 - Command line arguments:
2020/12/12 17:29:07 -   Input file  = 
2020/12/12 17:29:07 -   Log file = /home/pi/api/rest_server.log
2020/12/12 17:29:07 -   Port = 9443
2020/12/12 17:29:07 -   Use cert = False
2020/12/12 17:29:07 -   Use HTTPS = False
2020/12/12 17:29:07 -   Use multithreading = False

2020/12/12 17:29:07 - Web Server:
2020/12/12 17:29:07 -   Server name = rpiGarageOpener
2020/12/12 17:29:07 -   Local Server IP = 0.0.0.0
2020/12/12 17:29:07 -   Server IP = 192.168.1.227 

2020/12/12 17:29:07 -   No socket is required for HTTP?
2020/12/12 17:29:14 - GET /api/state HTTP/1.1
2020/12/12 17:29:14 - Client is: 192.168.1.139 39704
2020/12/12 17:29:14 - 192.168.1.139 39704
2020/12/12 17:29:14 - Client IP is valid: 192.168.1.139
open
192.168.1.139 - - [12/Dec/2020 17:29:15] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:29:15 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 17:29:50 - Closing REST server
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 17:30:29 - Starting REST server
2020/12/12 17:30:29 - Command line arguments:
2020/12/12 17:30:29 -   Input file  = 
2020/12/12 17:30:29 -   Log file = /home/pi/api/rest_server.log
2020/12/12 17:30:29 -   Port = 9443
2020/12/12 17:30:29 -   Use cert = False
2020/12/12 17:30:29 -   Use HTTPS = False
2020/12/12 17:30:29 -   Use multithreading = False

2020/12/12 17:30:29 - Web Server:
2020/12/12 17:30:29 -   Server name = rpiGarageOpener
2020/12/12 17:30:29 -   Local Server IP = 0.0.0.0
2020/12/12 17:30:29 -   Server IP = 192.168.1.227 

2020/12/12 17:30:29 -   No socket is required for HTTP?
2020/12/12 17:30:34 - GET /api/state HTTP/1.1
2020/12/12 17:30:34 - Client is: 192.168.1.139 39706
2020/12/12 17:30:34 - 192.168.1.139 39706
2020/12/12 17:30:34 - Client IP is valid: 192.168.1.139
  File "/usr/local/bin/state.py", line 48
    sys.exit0)
             ^
SyntaxError: invalid syntax
192.168.1.139 - - [12/Dec/2020 17:30:34] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:30:34 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 17:30:43 - Closing REST server
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 17:31:01 - Starting REST server
2020/12/12 17:31:01 - Command line arguments:
2020/12/12 17:31:01 -   Input file  = 
2020/12/12 17:31:01 -   Log file = /home/pi/api/rest_server.log
2020/12/12 17:31:01 -   Port = 9443
2020/12/12 17:31:01 -   Use cert = False
2020/12/12 17:31:01 -   Use HTTPS = False
2020/12/12 17:31:01 -   Use multithreading = False

2020/12/12 17:31:01 - Web Server:
2020/12/12 17:31:01 -   Server name = rpiGarageOpener
2020/12/12 17:31:01 -   Local Server IP = 0.0.0.0
2020/12/12 17:31:01 -   Server IP = 192.168.1.227 

2020/12/12 17:31:01 -   No socket is required for HTTP?
2020/12/12 17:31:06 - GET /api/state HTTP/1.1
2020/12/12 17:31:06 - Client is: 192.168.1.139 39708
2020/12/12 17:31:06 - 192.168.1.139 39708
2020/12/12 17:31:06 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 17:31:07] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:31:07 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:31:25 - GET /api/close HTTP/1.1
2020/12/12 17:31:25 - Client is: 192.168.1.139 39710
2020/12/12 17:31:25 - 192.168.1.139 39710
2020/12/12 17:31:25 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 17:31:28] "GET /api/close HTTP/1.1" 200 -
2020/12/12 17:31:28 - Execute command: /home/pi/api/close/get.py
2020/12/12 17:31:53 - GET /api/state HTTP/1.1
2020/12/12 17:31:53 - Client is: 192.168.1.139 39712
2020/12/12 17:31:53 - 192.168.1.139 39712
2020/12/12 17:31:53 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 17:31:54] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:31:54 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:32:02 - GET /api/state HTTP/1.1
2020/12/12 17:32:02 - Client is: 192.168.1.139 39714
2020/12/12 17:32:02 - 192.168.1.139 39714
2020/12/12 17:32:02 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 17:32:03] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:32:03 - Execute command: /home/pi/api/state/get.py
2020/12/12 17:54:11 - GET /api/state HTTP/1.1
2020/12/12 17:54:11 - Client is: 192.168.1.139 39716
2020/12/12 17:54:11 - 192.168.1.139 39716
2020/12/12 17:54:11 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 17:54:13] "GET /api/state HTTP/1.1" 200 -
2020/12/12 17:54:13 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 17:54:39 - Closing REST server
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ nano close/get.py
pi@rpiGarageOpener:~/api $ nano state/get.py
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/state.py
pi@rpiGarageOpener:~/api $ nano state/get.py
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/12 19:41:39 - Starting REST server
2020/12/12 19:41:39 - Command line arguments:
2020/12/12 19:41:39 -   Input file  = 
2020/12/12 19:41:39 -   Log file = /home/pi/api/rest_server.log
2020/12/12 19:41:39 -   Port = 9443
2020/12/12 19:41:39 -   Use cert = False
2020/12/12 19:41:39 -   Use HTTPS = False
2020/12/12 19:41:39 -   Use multithreading = False

2020/12/12 19:41:39 - Web Server:
2020/12/12 19:41:39 -   Server name = rpiGarageOpener
2020/12/12 19:41:39 -   Local Server IP = 0.0.0.0
2020/12/12 19:41:39 -   Server IP = 192.168.1.227 

2020/12/12 19:41:39 -   No socket is required for HTTP?
2020/12/12 19:41:46 - GET /api/state HTTP/1.1
2020/12/12 19:41:46 - Client is: 192.168.1.139 39718
2020/12/12 19:41:46 - 192.168.1.139 39718
2020/12/12 19:41:46 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 19:41:47] "GET /api/state HTTP/1.1" 200 -
2020/12/12 19:41:47 - Execute command: /home/pi/api/state/get.py
2020/12/12 19:42:26 - GET /api/open HTTP/1.1
2020/12/12 19:42:26 - Client is: 192.168.1.139 39720
2020/12/12 19:42:26 - 192.168.1.139 39720
2020/12/12 19:42:26 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 19:42:29] "GET /api/open HTTP/1.1" 200 -
2020/12/12 19:42:29 - Execute command: /home/pi/api/open/get.py
2020/12/12 19:43:08 - GET /api/state HTTP/1.1
2020/12/12 19:43:08 - Client is: 192.168.1.139 39722
2020/12/12 19:43:08 - 192.168.1.139 39722
2020/12/12 19:43:08 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 19:43:09] "GET /api/state HTTP/1.1" 200 -
2020/12/12 19:43:09 - Execute command: /home/pi/api/state/get.py
2020/12/12 19:43:18 - GET /api/close HTTP/1.1
2020/12/12 19:43:18 - Client is: 192.168.1.139 39724
2020/12/12 19:43:18 - 192.168.1.139 39724
2020/12/12 19:43:18 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 19:43:21] "GET /api/close HTTP/1.1" 200 -
2020/12/12 19:43:21 - Execute command: /home/pi/api/close/get.py
2020/12/12 19:44:06 - GET /api/state HTTP/1.1
2020/12/12 19:44:06 - Client is: 192.168.1.139 39726
2020/12/12 19:44:06 - 192.168.1.139 39726
2020/12/12 19:44:06 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [12/Dec/2020 19:44:07] "GET /api/state HTTP/1.1" 200 -
2020/12/12 19:44:07 - Execute command: /home/pi/api/state/get.py
^C2020/12/12 19:45:24 - Closing REST server
pi@rpiGarageOpener:~/api $ nano state/get.py
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ sudo crontab -e
No modification made
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/garage.sh
pi@rpiGarageOpener:~/api $ sudo cp /usr/local/bin/garage.sh /usr/local/bin/weekly.sh
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/weekly.sh
pi@rpiGarageOpener:~/api $ sudo crontab -e
No modification made
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/weekly.sh
pi@rpiGarageOpener:~/api $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/weekly.sh
pi@rpiGarageOpener:~/api $ sudo bash /usr/local/bin/weekly.sh
/usr/local/bin/weekly.sh: line 19: subj: command not found
mail: You must specify to-addr recipients when using -s, -c, -b, or -r
pi@rpiGarageOpener:~/api $ sudo nano /usr/local/bin/weekly.sh
pi@rpiGarageOpener:~/api $ man mail
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ mkdir junk
pi@rpiGarageOpener:~/api $ cd junk
pi@rpiGarageOpener:~/api/junk $ wget https://raw.githubusercontent.com/dumbo25/send-text-message/main/sendTextMessage.py
--2020-12-12 20:13:37--  https://raw.githubusercontent.com/dumbo25/send-text-message/main/sendTextMessage.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.128.133, 151.101.64.133, 151.101.192.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.128.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 799 [text/plain]
Saving to: ‘sendTextMessage.py’

sendTextMessage.py                      100%[=============================================================================>]     799  --.-KB/s    in 0s      

2020-12-12 20:13:37 (1.79 MB/s) - ‘sendTextMessage.py’ saved [799/799]

pi@rpiGarageOpener:~/api/junk $ ls
sendTextMessage.py
pi@rpiGarageOpener:~/api/junk $ nano sendTextMessage.py
pi@rpiGarageOpener:~/api/junk $ cd /usr/local/bin
pi@rpiGarageOpener:/usr/local/bin $ ls
close.py  disarm.py  distro  fauxmo.py  fauxmo.pyc  garage.sh  mylog.py  mylog.pyc  open.py  rpi-echo.py  sleep.py  state.py  toggle.py  weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 84
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ sudo nano weekly.py
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 88
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rw-r--r-- 1 root root   662 Dec 12 20:18 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ sudo chmod +x weekly.py
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 88
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   662 Dec 12 20:18 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials t5sm3106133oth.16 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo nano weekly.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano weekly.py
pi@rpiGarageOpener:/usr/local/bin $ python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials g5sm3101506otq.43 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials g21sm3108281otj.77 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo nano weekly.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials e12sm3099955otp.25 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo nano weekly.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials d20sm2295123otl.64 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials i16sm3144171otc.61 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials c6sm3105581oif.48 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials i82sm3123128oia.2 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python3.7/smtplib.py", line 730, in login
    raise last_exception
  File "/usr/lib/python3.7/smtplib.py", line 721, in login
    initial_response_ok=initial_response_ok)
  File "/usr/lib/python3.7/smtplib.py", line 642, in auth
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials 9sm3145327otl.52 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ sudo nano weekly.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python weekly.py
Traceback (most recent call last):
  File "weekly.py", line 21, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python2.7/smtplib.py", line 623, in login
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, '5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials k63sm3126036oif.12 - gsmtp')
pi@rpiGarageOpener:/usr/local/bin $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sat Dec 12 11:01:30 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ sudo nano /etc/ssmtp/ssmtp.conf
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ sudo nano /etc/ssmtp/revaliases
pi@rpiGarageOpener:~ $ sudo chmod og+x /etc/ssmtp/ssmtp.conf
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ pwd
/home/pi
pi@rpiGarageOpener:~ $ python3 genID.py
VR89FD
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        hello.py  pushGarageRemote.py  simple-fan.py.1  Videos
Bookshelf          Desktop      getAPI.sh       Music     read.py              Templates
b.sh               Documents    getScripts2.sh  myID.txt  rpi-echo.log         tls2.sh
check_apache.html  Downloads    getScripts.sh   Pictures  rpi-echo.service     tls.sh
createDB.sh        emailTry.py  getWebsite.sh   Public    simple-fan.py        unused_rpi.sh
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  disk         get.py        memory      README.md        rest_server.py  server.key  toggle
client.key  favicon.png  getServer.sh  navigation  reboot           server          state       uptime
close       get.backup   get.txt       open        restful_api      server_cron.sh  test
cpu         get.json     junk          os          rest_server.log  server.crt      time
pi@rpiGarageOpener:~/api $ cd junk
pi@rpiGarageOpener:~/api/junk $ $ wget https://raw.githubusercontent.com/dumbo25/send-text-message/main/sendTextMessage.py
-bash: $: command not found
pi@rpiGarageOpener:~/api/junk $ wget https://raw.githubusercontent.com/dumbo25/send-text-message/main/sendTextMessage.py
--2020-12-13 10:50:00--  https://raw.githubusercontent.com/dumbo25/send-text-message/main/sendTextMessage.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 151.101.180.133
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|151.101.180.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 799 [text/plain]
Saving to: ‘sendTextMessage.py.1’

sendTextMessage.py.1       100%[=====================================>]     799  --.-KB/s    in 0s      

2020-12-13 10:50:00 (1.80 MB/s) - ‘sendTextMessage.py.1’ saved [799/799]

pi@rpiGarageOpener:~/api/junk $ ls
sendTextMessage.py  sendTextMessage.py.1
pi@rpiGarageOpener:~/api/junk $ rm *.1
pi@rpiGarageOpener:~/api/junk $ ls
sendTextMessage.py
pi@rpiGarageOpener:~/api/junk $ cat sendTextMessage.py
#! /usr/bin/env python
#
# run using python3 sendTextMessage.py

import smtplib

# CHANGE THE ITEMS BELOW - DO NOT PUBLISH
#  Change the items enclosed by angle brackets and delete the angle barckets
gmail_password = '<your-throw-away-gmail-account-password>'
gmail_address = '<your-throw-away-gmail-account>@gmail.com'
ID = '<6-digit-ID>' # This is the ID gmail forwards to your smart phone
#
# CHANGE THE ITEMS ABOVE - DO NOT PUBLISH

subject = ID + " Project: Garage door open"
message = 'Subject: %s' % (subject)
# 587 uses TLS
# 465 uses SSL - not supported see edits to /etc/ssmtp/ssmtp.conf
mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()
mail.login(gmail_address, gmail_password)
mail.sendmail("cell", gmail_address, message)
mail.close()

print ('text message sent')
pi@rpiGarageOpener:~/api/junk $ nano sendTextMessage.py
pi@rpiGarageOpener:~/api/junk $ python sendTextMessage.py
text message sent
pi@rpiGarageOpener:~/api/junk $ cd ../..
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        hello.py  pushGarageRemote.py  simple-fan.py.1  Videos
Bookshelf          Desktop      getAPI.sh       Music     read.py              Templates
b.sh               Documents    getScripts2.sh  myID.txt  rpi-echo.log         tls2.sh
check_apache.html  Downloads    getScripts.sh   Pictures  rpi-echo.service     tls.sh
createDB.sh        emailTry.py  getWebsite.sh   Public    simple-fan.py        unused_rpi.sh
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  genID.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ sudo nano emailTry.py
pi@rpiGarageOpener:~ $ python emailTry.py
text message sent
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        hello.py  pushGarageRemote.py  simple-fan.py.1  Videos
Bookshelf          Desktop      getAPI.sh       Music     read.py              Templates
b.sh               Documents    getScripts2.sh  myID.txt  rpi-echo.log         tls2.sh
check_apache.html  Downloads    getScripts.sh   Pictures  rpi-echo.service     tls.sh
createDB.sh        emailTry.py  getWebsite.sh   Public    simple-fan.py        unused_rpi.sh
pi@rpiGarageOpener:~ $ ls *.py
emailTry.py  genID.py  hello.py  pushGarageRemote.py  read.py  simple-fan.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/weekly.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/weekly.py
pi@rpiGarageOpener:~ $ python pi@rpiGarageOpener:~ $ sudo nano 
python: can't open file 'pi@rpiGarageOpener:~': [Errno 2] No such file or directory
pi@rpiGarageOpener:~ $ python /usr/local/bin/weekly.py
Traceback (most recent call last):
  File "/usr/local/bin/weekly.py", line 22, in <module>
    mail.login(gmail_address, gmail_password)
  File "/usr/lib/python2.7/smtplib.py", line 623, in login
    raise SMTPAuthenticationError(code, resp)
smtplib.SMTPAuthenticationError: (535, '5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials n9sm12219718qti.75 - gsmtp')
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/weekly.py
pi@rpiGarageOpener:~ $ ls
api                dead.letter  genID.py        hello.py  pushGarageRemote.py  simple-fan.py.1  Videos
Bookshelf          Desktop      getAPI.sh       Music     read.py              Templates
b.sh               Documents    getScripts2.sh  myID.txt  rpi-echo.log         tls2.sh
check_apache.html  Downloads    getScripts.sh   Pictures  rpi-echo.service     tls.sh
createDB.sh        emailTry.py  getWebsite.sh   Public    simple-fan.py        unused_rpi.sh
pi@rpiGarageOpener:~ $ nano emailTry.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/weekly.py
pi@rpiGarageOpener:~ $ python /usr/local/bin/weekly.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/weekly.py
pi@rpiGarageOpener:~ $ python /usr/local/bin/weekly.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/weekly.py
pi@rpiGarageOpener:~ $ ls /usr/local/bin
close.py   distro     fauxmo.pyc  mylog.py   open.py      sleep.py  toggle.py  weekly.sh
disarm.py  fauxmo.py  garage.sh   mylog.pyc  rpi-echo.py  state.py  weekly.py
pi@rpiGarageOpener:~ $ ls -l /usr/local/bin
total 88
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   707 Dec 13 11:15 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:~ $ sudo chown root:root weekly.py
chown: cannot access 'weekly.py': No such file or directory
pi@rpiGarageOpener:~ $ cd /usr/local/bin
pi@rpiGarageOpener:/usr/local/bin $ sudo chown root:root weekly.py
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 88
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   707 Dec 13 11:15 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ sudo chmod og+x weekly.py
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 88
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   707 Dec 13 11:15 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ sudo chmod o+x weekly.py
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 88
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   707 Dec 13 11:15 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 88
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 pi   pi    1787 Dec  6 15:00 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   707 Dec 13 11:15 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ nano garage.sh
pi@rpiGarageOpener:/usr/local/bin $ cp garage.sh garage.cp
cp: cannot create regular file 'garage.cp': Permission denied
pi@rpiGarageOpener:/usr/local/bin $ sudo cp garage.sh garage.cp
pi@rpiGarageOpener:/usr/local/bin $ ls -l
total 92
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root   208 Dec  8 15:26 distro
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rw-r--r-- 1 root root 13714 Nov 29 19:33 fauxmo.pyc
-rwxr-xr-- 1 root root  2047 Dec 13 11:58 garage.cp
-rwxr-xr-- 1 pi   pi    2047 Dec 13 11:58 garage.sh
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rw-r--r-- 1 root root  1744 Nov 29 19:33 mylog.pyc
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   707 Dec 13 11:15 weekly.py
-rwxr-xr-- 1 root root   431 Dec 12 20:07 weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ sudo nano weekly.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo cp garage.sh garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo rm garage.cp
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano close.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ cat close.py | grep sqlite
pi@rpiGarageOpener:/usr/local/bin $ cat open.py | grep sqlite
pi@rpiGarageOpener:/usr/local/bin $ cat rpi-echo.py | grep sqlite
pi@rpiGarageOpener:/usr/local/bin $ sudo nano rpi-echo.py
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ ls -l *.py
-rwxr-xr-x 1 root root  1569 Nov 30 15:28 close.py
-rwxr-xr-x 1 root root   575 Nov 29 19:09 disarm.py
-rwxr-xr-x 1 root root 15029 Nov 29 19:09 fauxmo.py
-rwxr-xr-- 1 root root  2775 Dec 13 12:12 garage.py
-rwxr-xr-x 1 root root  1340 Nov 29 19:09 mylog.py
-rwxr-xr-x 1 root root  1561 Nov 30 15:19 open.py
-rwxr-xr-x 1 root root  5291 Nov 30 14:49 rpi-echo.py
-rwxr-xr-x 1 root root   601 Nov 29 19:09 sleep.py
-rwxr-xr-x 1 root root  1341 Dec 12 17:30 state.py
-rwxr-xr-x 1 root root  1072 Nov 30 14:05 toggle.py
-rwxr-xr-x 1 root root   707 Dec 13 11:15 weekly.py
pi@rpiGarageOpener:/usr/local/bin $ cat disarm.py | grep sqlite
import sqlite3
		self.db_con = sqlite3.connect(self.db_file)
pi@rpiGarageOpener:/usr/local/bin $ sudo nano disarm.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ history
    1  which php
    2  sudo apt install --dry-run php7.4
    3  sudo apt install  php7.3
    4  sudo apt install --dry-run php7.4-sqlite3
    5  sudo apt install --dry-run php7.3-sqlite3
    6  sudo apt install  php7.3 php7.3-sqlite3
    7  nano createDB.sh
    8  sudo bash createDB.sh
    9  nano createDB.sh
   10  sudo bash createDB.sh
   11  nano createDB.sh
   12  sudo bash createDB.sh
   13  nano createDB.sh
   14  sudo bash createDB.sh
   15  nano createDB.sh
   16  sudo bash createDB.sh
   17  nano createDB.sh
   18  sudo bash createDB.sh
   19  nano createDB.sh
   20  sudo bash createDB.sh
   21  nano createDB.sh
   22  sudo bash createDB.sh
   23  nano createDB.sh
   24  sqlite3 /var/www/db/garagedoor.db
   25  nano createDB.sh
   26  ls
   27  nano push_garage_opener.py
   28  mv push_garage_opener.py pushGarageRemote.py
   29  nano createDB.sh
   30  wget "https://raw.githubusercontent.com/dumbo25/garageDoorOpener2/main/garage.sh"
   31  ls -l
   32  ls /usr/local/bin
   33  chmod UG+x garage.sh
   34  chmod ug+x garage.sh
   35  ls -l
   36  mv garage.sh /usr/local/bin/garage.sh
   37  sudo mv garage.sh /usr/local/bin/garage.sh
   38  ls /usr/local/bin
   39  ls -l /usr/local/bin
   40  nano /var/www/db/garage.sh
   41  nano /usr/local/bin/garage.sh
   42  ls
   43  gpio read 17
   44  which which gpio
   45  /usr/bin/gpio read 17
   46  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   47  sudo apt-get update -y
   48  sudo apt-get upgrade -y
   49  sudo nano /etc/ssmtp/ssmtp.conf
   50  sudo nano /etc/ssmtp/revaliases
   51  sudo chmod og+x /etc/ssmtp/ssmtp.conf
   52  nano emailTry.py
   53  python emailTry.py
   54  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   55  sudo ufw show added
   56  sudo ufw allow 9080
   57  sudo ufw show added
   58  history | grep rest
   59  history | grep server
   60  python3 rest_server.py
   61  ls
   62  cd api
   63  ls
   64  python3 rest_server.py
   65  pwd
   66  python3 rest_server.py
   67  sudo python3 rest_server.py
   68  sudo python rest_server.py
   69  sudo python3 rest_server.py
   70  history |grep distro
   71  sudo pip3 install distro
   72  sudo python3 rest_server.py
   73  ls
   74  ls multi
   75  ls os
   76  nano rest_server.py
   77  ls
   78  nano rest_server.py
   79  sudo python3 rest_server.py -s
   80  sudo python3 rest_server.py 
   81  cat /etc/hosts
   82  sudo nano /etc/apache2/apache2.conf
   83  sudo nano /etc/apache2/conf-enabled/*.conf
   84  sudo nano /etc/apache2/sites-enabled/*.conf
   85  ls /usr/bin
   86  ls /usr/bin/rest_server.py
   87  ls -l /usr/bin/rest_server.py
   88  ps -aux | grep rest
   89  sudo nano /usr/bin/rest_server.py
   90  ls
   91  ls -l
   92  cat rest_server.log
   93  ls ../*.log
   94  sudo nano /usr/bin/rest_server.py
   95  pwd
   96  ls -l
   97  ps -aux | grep rest
   98  netstat -lptn
   99  netstat --tcp --listening --programs --numeric
  100  sudo ufw status
  101  sudo nano /usr/bin/rest_server.py
  102  cat /home/pi/api/server_cron.sh
  103  ls *.pid
  104  ls
  105  cat rest_server.log
  106  ls
  107  cd api
  108  httpd -t -c httpd.conf
  109  sudo httpd -t -c httpd.conf
  110  ls /etc/httpd
  111  which apache2
  112  ls /usr/sbin
  113  sudo nano /usr/bin/rest_server.py &
  114  curl -X GET http://localhost:9443/api/cpu
  115  sudo kill 8802
  116  sudo nano /etc/apache2/ports.conf
  117  sudo ufw status
  118  sudo ufw allow 9443
  119  sudo nano /usr/bin/rest_server.py
  120  sudo python3 /usr/bin/rest_server.py &
  121  ls
  122  cat rest_server.log
  123  sudo kill 9401
  124  ls -l
  125  ls -l cpu
  126  nano rest_server.py
  127  sudo python3 /usr/bin/rest_server.py 
  128  sudo python3 /usr/bin/rest_server.py -d
  129  sudo python3 /usr/bin/rest_server.py -h
  130  ls
  131  history | grep rest_server.py
  132  sudo nano /usr/bin/rest_server.py
  133  sudo nano rest_server.py
  134  sudo python3 rest_server.py -d
  135  netstat -l
  136  sudo python3 rest_server.py &
  137  netstat -l
  138  sudo kill 10805
  139  nc -zv localhost 8080
  140  nc -zv localhost 443
  141  nc -zv localhost 5070
  142  nc -z localhost 5070
  143  nc -zv localhost 5070
  144  nc -zv localhost 8888
  145  sudo python3 rest_server.py &
  146  nc -zv localhost 9443
  147  nc -zv rpiGarageOpener 9443
  148  sudo nano /etc/hosts
  149  history | grep nano | grep /
  150  sudo nano /etc/apache2/ports.conf
  151  sudo nano /etc/ssmtp/revaliases
  152  ls /etc
  153  sudoo nano /etc/host.conf
  154  sudo nano /etc/host.conf
  155  sudo nano /etc/host.allow
  156  sudo nano /etc/host.deny
  157  sudo nano /etc/networks
  158  sudo nano /etc/sysctl.conf
  159  ps -aux | grep rest_server
  160  sudo kill 8802
  161  sudo kill 8803
  162  sudo kill 12215
  163  sudo kill 12216
  164  ps -aux | grep rest_server
  165  sudo kill 8803
  166  sudo kill 8802
  167  ps -aux | grep rest_server
  168  sudo reboot
  169  nc -zv rpiGarageOpener 9443
  170  netstat -l
  171  sudo python3 rest_server.py &
  172  sudo kill 1280
  173  ps -aux | grep rest_server
  174  cd api
  175  sudo python3 rest_server.py &
  176  netstat -l
  177  nc -zv rpiGarageOpener 9443
  178  cat < /dev/null > /dev/tcp/rpiGarageOpener:9443; echo $?
  179  cat < /dev/null > /dev/tcp/rpiGarageOpener/9443; echo $?
  180  ps -aux | grep rest_server
  181  history
  182  ps -aux | grep rest_server
  183  sudo kill 1327
  184  ps -aux | grep rest_server
  185  python3 rest_server.py &
  186  ps -aux | grep rest_server
  187  sudo kill 1652
  188  python3 rest_server.py -p5070 &
  189  ps -aux | grep rest_server
  190  sudo kill 1698
  191  sudo python3 rest_server.py -p5070 &
  192  sudo kill 1763
  193  sudo netstat -anp | grep ':80 '
  194  sudo netstat -anp | grep ':9443 '
  195  sudo python3 rest_server.py &
  196  sudo netstat -anp | grep ':9443 '
  197  hotsname -L
  198  hotsname -I
  199  hostname -I
  200  sudo netstat -tnlp | grep :9443
  201  sudo tcpdump -n icmp
  202  sudo service ssh status
  203  netstat -an | grep "LISTEN "
  204  sudo nano /etc/hosts
  205  sudo netstat -tnlp | grep :5070
  206  ps -aux 
  207  ps -aux | grep 5070
  208  ps -aux | grep python
  209  sudo nano /usr/local/bin/rpi-echo.py
  210  sudo netstat -tnlp | grep :5070
  211  sudo nano /usr/local/bin/rpi-echo.py
  212  ps -aux | grep rest_server
  213  sudo kill 1898
  214  ps -aux | grep rest_server
  215  nano rest_server.py
  216  python3 rest_server.py
  217  python3 rest_server.py -d
  218  nano rest_server.py
  219  python3 rest_server.py -d
  220  nano rest_server.py
  221  python3 rest_server.py -d
  222  nano rest_server.py
  223  python3 rest_server.py -d
  224  ls /cat
  225  ls /etc
  226  ls /etc/.hosts
  227  cat /etc/hosts
  228  sudo nano /etc/hosts
  229  sudo reboot
  230  sudo nano /etc/ssmtp/ssmtp.conf
  231  sudo nano /etc/ssmtp/revaliases
  232  sudo chmod og+x /etc/ssmtp/ssmtp.conf
  233  pwd
  234  python3 genID.py
  235  ls
  236  cd api
  237  ls
  238  cd junk
  239  $ wget https://raw.githubusercontent.com/dumbo25/send-text-message/main/sendTextMessage.py
  240  wget https://raw.githubusercontent.com/dumbo25/send-text-message/main/sendTextMessage.py
  241  ls
  242  rm *.1
  243  ls
  244  cat sendTextMessage.py
  245  nano sendTextMessage.py
  246  python sendTextMessage.py
  247  cd ../..
  248  ls
  249  ls *.py
  250  sudo nano emailTry.py
  251  python emailTry.py
  252  ls
  253  ls *.py
  254  sudo nano /usr/local/weekly.py
  255  sudo nano /usr/local/bin/weekly.py
  256  python pi@rpiGarageOpener:~ $ sudo nano 
  257  python /usr/local/bin/weekly.py
  258  sudo nano /usr/local/bin/weekly.py
  259  ls
  260  nano emailTry.py
  261  sudo nano /usr/local/bin/weekly.py
  262  python /usr/local/bin/weekly.py
  263  sudo nano /usr/local/bin/weekly.py
  264  python /usr/local/bin/weekly.py
  265  sudo nano /usr/local/bin/weekly.py
  266  ls /usr/local/bin
  267  ls -l /usr/local/bin
  268  sudo chown root:root weekly.py
  269  cd /usr/local/bin
  270  sudo chown root:root weekly.py
  271  ls -l
  272  sudo chmod og+x weekly.py
  273  ls -l
  274  sudo chmod o+x weekly.py
  275  ls -l
  276  sudo crontab -e
  277  ls -l
  278  nano garage.sh
  279  cp garage.sh garage.cp
  280  sudo cp garage.sh garage.cp
  281  ls -l
  282  sudo nano weekly.py
  283  sudo nano garage.py
  284  sudo cp garage.sh garage.py
  285  sudo rm garage.cp
  286  sudo nano garage.py
  287  sudo nano close.py
  288  sudo nano garage.py
  289  cat close.py | grep sqlite
  290  cat open.py | grep sqlite
  291  cat rpi-echo.py | grep sqlite
  292  sudo nano rpi-echo.py
  293  ls -l *.py
  294  cat disarm.py | grep sqlite
  295  sudo nano disarm.py
  296  sudo nano garage.py
  297  history
pi@rpiGarageOpener:/usr/local/bin $ sudo nano rpi-echo.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ ls /var/www
db  html
pi@rpiGarageOpener:/usr/local/bin $ ls /var/www/db
garage.db  garagedoor.db
pi@rpiGarageOpener:/usr/local/bin $ ls -l /var/www/db
total 12
-rw-r--r-- 1 root root     0 Nov 30 15:25 garage.db
-rw-rw-rw- 1 pi   pi   12288 Nov 29 14:14 garagedoor.db
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ ls
close.py   distro     fauxmo.pyc  garage.sh  mylog.pyc  rpi-echo.py  state.py   weekly.py
disarm.py  fauxmo.py  garage.py   mylog.py   open.py    sleep.py     toggle.py  weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ nano rpi-echo.py
pi@rpiGarageOpener:/usr/local/bin $ nano mylog.py
pi@rpiGarageOpener:/usr/local/bin $ nano sleep.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ cat close.py
#!/susr/bin/python

#########################
#
# closes.py closes a garage door by electronically closing a push button on
# a universla remote
#
# if the garage door is already closed then no action is taken
#
# The complete project is described here:
#  https://sites.google.com/site/cartwrightraspberrypiprojects/home/home-automation-categories/access-control/garage-door-opener
#
# close.py is used in conjunction with fauxmo and Amazon Echo to control
# the garage door.
#
# The system requires a remote control, relay and a sensor
#
# close.py was tested on a Raspberry Pi Zero WH running Raspberry Pi OS
#
# The connections are as shown below:
#   RPi0 GND (physical pin 6) to Relay GND
#   RPi0 BCM GPIO 23 (physical pin 16, Wiring Pi pin 4) to Relay IN2
#   RPi0 5v (pin 2 or 4) to Relay VCC
#   Relay NO to Header Pin on Remote
#   Relay Power to 12V+ on Remote
#   RPi0 3.3v (physical pin1) to Sensor GND
#   RPi0 BCM GPIO 24 (physical pin 18, Wiring Pi pin 5) to Sensor output
#
# close.py is called rpi-echo.py
# rpi-echo.py starts automatically using systemd
#
#########################

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

PRESS = 23
SENSOR = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(PRESS, GPIO.OUT)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# wait for sensor pin to reach steady state before reading
sleep(1)

open = GPIO.input(SENSOR)
# print ("open = " + str(open))
if open == 0:
    GPIO.output(PRESS, GPIO.LOW)
    sleep(1)
    GPIO.output(PRESS, GPIO.HIGH)
    sleep(1)

GPIO.cleanup()

pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ ls /var/www/db
garage.db  garagedoor.db
pi@rpiGarageOpener:/usr/local/bin $ sqlite3 /var/www/db/garagedoor.db
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
sqlite> .tables
schedule  status  
sqlite> . schema schedule
CREATE TABLE schedule (tdate DATE, ttime TIME, day TEXT, arm TIME, disarm TIME);
sqlite> .quit
pi@rpiGarageOpener:/usr/local/bin $ ls
close.py   distro     fauxmo.pyc  garage.sh  mylog.pyc  rpi-echo.py  state.py   weekly.py
disarm.py  fauxmo.py  garage.py   mylog.py   open.py    sleep.py     toggle.py  weekly.sh
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
  File "garage.py", line 80
    elif vacation" == "no":
                      ^
SyntaxError: invalid syntax
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ cat close.py
#!/susr/bin/python

#########################
#
# closes.py closes a garage door by electronically closing a push button on
# a universla remote
#
# if the garage door is already closed then no action is taken
#
# The complete project is described here:
#  https://sites.google.com/site/cartwrightraspberrypiprojects/home/home-automation-categories/access-control/garage-door-opener
#
# close.py is used in conjunction with fauxmo and Amazon Echo to control
# the garage door.
#
# The system requires a remote control, relay and a sensor
#
# close.py was tested on a Raspberry Pi Zero WH running Raspberry Pi OS
#
# The connections are as shown below:
#   RPi0 GND (physical pin 6) to Relay GND
#   RPi0 BCM GPIO 23 (physical pin 16, Wiring Pi pin 4) to Relay IN2
#   RPi0 5v (pin 2 or 4) to Relay VCC
#   Relay NO to Header Pin on Remote
#   Relay Power to 12V+ on Remote
#   RPi0 3.3v (physical pin1) to Sensor GND
#   RPi0 BCM GPIO 24 (physical pin 18, Wiring Pi pin 5) to Sensor output
#
# close.py is called rpi-echo.py
# rpi-echo.py starts automatically using systemd
#
#########################

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

PRESS = 23
SENSOR = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(PRESS, GPIO.OUT)
GPIO.setup(SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# wait for sensor pin to reach steady state before reading
sleep(1)

open = GPIO.input(SENSOR)
# print ("open = " + str(open))
if open == 0:
    GPIO.output(PRESS, GPIO.LOW)
    sleep(1)
    GPIO.output(PRESS, GPIO.HIGH)
    sleep(1)

GPIO.cleanup()

pi@rpiGarageOpener:/usr/local/bin $ ls *.py
close.py  disarm.py  fauxmo.py  garage.py  mylog.py  open.py  rpi-echo.py  sleep.py  state.py  toggle.py  weekly.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano rpi-echo.py
pi@rpiGarageOpener:/usr/local/bin $ ls *.py
close.py  disarm.py  fauxmo.py  garage.py  mylog.py  open.py  rpi-echo.py  sleep.py  state.py  toggle.py  weekly.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano mylog.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
  File "garage.py", line 141
    
    ^
SyntaxError: unexpected EOF while parsing
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
  File "garage.py", line 142
    
    ^
SyntaxError: unexpected EOF while parsing
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
Traceback (most recent call last):
  File "garage.py", line 66, in <module>
    GPIO.setup(PRESS, GPIO.OUT)
NameError: name 'PRESS' is not defined
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
Traceback (most recent call last):
  File "garage.py", line 72, in <module>
    printMsg("Door 0 = open: " + door)
TypeError: can only concatenate str (not "int") to str
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
Traceback (most recent call last):
  File "garage.py", line 72, in <module>
    printMsg("Door 0 = open: " + str(door))
  File "garage.py", line 48, in printMsg
    print(self.timeStamp() + s)
NameError: name 'self' is not defined
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
2020/12/13 17:17:06 - Door 0 = open: 1
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
  File "garage.py", line 37
    DOOR = {0 : 'Open', 1 : 'Closed', 2}
                                       ^
SyntaxError: invalid syntax
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
Traceback (most recent call last):
  File "garage.py", line 73, in <module>
    printMsg("Door: " + DOOR[d])
NameError: name 'd' is not defined
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
2020/12/13 17:20:20 - Door: Closed
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
2020/12/13 18:02:20 - Door: Closed
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ 
pi@rpiGarageOpener:/usr/local/bin $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sun Dec 13 10:34:14 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Sun Dec 13 23:44:47 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ ls os
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ps -aux | grep garage
pi       32504  0.0  0.4   7336  2016 pts/0    S+   07:36   0:00 grep --color=auto garage
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls /usr/local/bin
close.py   distro     fauxmo.pyc  garage.sh  mylog.pyc  rpi-echo.py  state.py   weekly.py
disarm.py  fauxmo.py  garage.py   mylog.py   open.py    sleep.py     toggle.py  weekly.sh
pi@rpiGarageOpener:~/api $ sudo rm /usr/local/bin/garage.sh
pi@rpiGarageOpener:~/api $ ls /usr/local/bin
close.py   distro     fauxmo.pyc  mylog.py   open.py      sleep.py  toggle.py  weekly.sh
disarm.py  fauxmo.py  garage.py   mylog.pyc  rpi-echo.py  state.py  weekly.py
pi@rpiGarageOpener:~/api $ cat /usr/local/bin*.py | grep cartwright25
cat: '/usr/local/bin*.py': No such file or directory
pi@rpiGarageOpener:~/api $ cat /usr/local/bin/*.py | grep cartwright25
pi@rpiGarageOpener:~/api $ cat /usr/local/bin/*.py | grep 310
gmail_address = '310glenhollow@gmail.com'
gmail_address = '310glenhollow@gmail.com'
pi@rpiGarageOpener:~/api $ ls ..
api                createDB.sh  Downloads    getScripts2.sh  Music     pushGarageRemote.py  simple-fan.py    tls.sh
Bookshelf          dead.letter  emailTry.py  getScripts.sh   myID.txt  read.py              simple-fan.py.1  unused_rpi.sh
b.sh               Desktop      genID.py     getWebsite.sh   Pictures  rpi-echo.log         Templates        Videos
check_apache.html  Documents    getAPI.sh    hello.py        Public    rpi-echo.service     tls2.sh
pi@rpiGarageOpener:~/api $ ls ../*.py
../emailTry.py  ../genID.py  ../hello.py  ../pushGarageRemote.py  ../read.py  ../simple-fan.py
pi@rpiGarageOpener:~/api $ cat ../*.py | grep cartwright
#  https://sites.google.com/site/cartwrightraspberrypiprojects/home/home-automation-categories/access-control/garage-door-opener
pi@rpiGarageOpener:~/api $ cat ../*.py | grep 310
gmail_address = '310glenhollow@gmail.com'
pi@rpiGarageOpener:~/api $ cd /usr/local/bin
pi@rpiGarageOpener:/usr/local/bin $ ls
close.py   distro     fauxmo.pyc  mylog.py   open.py      sleep.py  toggle.py  weekly.sh
disarm.py  fauxmo.py  garage.py   mylog.pyc  rpi-echo.py  state.py  weekly.py
pi@rpiGarageOpener:/usr/local/bin $ ls /var/www/db
garage.db  garagedoor.db
pi@rpiGarageOpener:/usr/local/bin $ ls -l /var/www/db
total 12
-rw-r--r-- 1 root root     0 Nov 30 15:25 garage.db
-rw-rw-rw- 1 pi   pi   12288 Nov 29 14:14 garagedoor.db
pi@rpiGarageOpener:/usr/local/bin $ sudo rm /var/www/db/garage.db
pi@rpiGarageOpener:/usr/local/bin $ cat *.py | grep garage.db
pi@rpiGarageOpener:/usr/local/bin $ cat /home/pi/*.py | grep garage.db
pi@rpiGarageOpener:/usr/local/bin $ cat /home/pi/*.py | grep garagedoor.db
pi@rpiGarageOpener:/usr/local/bin $ cat *.py | grep garagedoor.db
db_file = '/var/www/db/garagedoor.db'
pi@rpiGarageOpener:/usr/local/bin $ sqlite3 /var/www/db/garagedoor.db
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
sqlite> .tables
schedule  status  
sqlite> .schema status
CREATE TABLE status (tdate DATE, ttime TIME, name TEXT, value TEXT);
sqlite> .schema schedule
CREATE TABLE schedule (tdate DATE, ttime TIME, day TEXT, arm TIME, disarm TIME);
sqlite> select * from statue where name is vacation
   ...> ;
Error: no such table: statue
sqlite> select * from status where name is vacation;
Error: no such column: vacation
sqlite> select * from status 
   ...> ;
2020-11-29|13:24:29|vacation|yes
2020-11-29|13:24:29|schedule|on
2020-11-29|13:24:29|command|vacation
2020-11-29|13:24:29|monitor|on
sqlite> select * from status where name = 'vacation';
2020-11-29|13:24:29|vacation|yes
sqlite> .quit
pi@rpiGarageOpener:/usr/local/bin $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo crontab -e
crontab: installing new crontab
pi@rpiGarageOpener:/usr/local/bin $ sudo nano garage.py
pi@rpiGarageOpener:/usr/local/bin $ sudo python3 garage.py
2020/12/14 07:50:47 - Door: Closed
pi@rpiGarageOpener:/usr/local/bin $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Mon Dec 14 07:24:13 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Downloads    getScripts2.sh  Music     pushGarageRemote.py  simple-fan.py    tls.sh
Bookshelf          dead.letter  emailTry.py  getScripts.sh   myID.txt  read.py              simple-fan.py.1  unused_rpi.sh
b.sh               Desktop      genID.py     getWebsite.sh   Pictures  rpi-echo.log         Templates        Videos
check_apache.html  Documents    getAPI.sh    hello.py        Public    rpi-echo.service     tls2.sh
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ ls cpu
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls navigation
get.json  get.py  get.py~  junk.json
pi@rpiGarageOpener:~/api $ cd navigation
pi@rpiGarageOpener:~/api/navigation $ cat get.py
# returns navigation for API
global Data
global Path

validVerbs  = "get put delete post"
data = '{ "directories" : [ '
# ??? need to remove /navigation
next = False

# excluded_prefixes = ('__', '.')
for paths, dirs, files in os.walk(Path):
    # exclude hidden folders and special files starting with excluded_prefixes
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    dirs[:] = [d for d in dirs if not d.startswith("__")]

    filenames = [f for f in files if not f.startswith(".")]
    filenames[:] = [f for f in files if not f.startswith("__")]

    if next:
        data += ', '

    schema = '"schema" : {}'
    verbs = '"verbs" : ['
    next_verb = False
    for f in filenames:
        if None != re.search('.py', f):
            verb = f[:len(f)-3]
            if validVerbs.find(verb) >= 0:
                if next_verb:
                    verbs += ', '
                file = paths + "/" + verb
                try:
                    # ??? how to get proper indentation
                    schema = '"schema" : { '
                    with open(file + ".json", "r") as read_file:
                        schema += read_file.read()
                        # ??? needs to read line at a time rather than the whole file
                    schema += '}'
                except:
                    schema = '"schema" : {}'

                try:
                    with open(file + ".txt", "r") as read_file:
                        description = read_file.read()
                except:
                    description = ''

                verb = verb.upper()
                verbs += '"' + verb + '"'
                next_verb = True

    verbs += '], '

    data += '{ '
    data += '    "abs" : "' + paths + '", '
    data += '    ' + verbs
    data += '    ' + description + ', '
    data += '    ' + schema
    data += '}'

    next = True

data += '] }'
print("\n\ndata = " +data)

Data = json.loads(data)
pi@rpiGarageOpener:~/api/navigation $ ls
get.json  get.py  get.py~  junk.json
pi@rpiGarageOpener:~/api/navigation $ cd ..
pi@rpiGarageOpener:~/api $ cat get.py
global Data
# returns hostanme of server
Data = {"hostname" : socket.gethostname()}
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py


data = { "directories" : [ {     "abs" : "/home/pi/api",     "verbs" : ["GET"],     "description" : "returns hostname"
,     "schema" : { "hostname" : "string"
}}, {     "abs" : "/home/pi/api/test",     "verbs" : [],     "description" : "returns hostname"
,     "schema" : {}}, {     "abs" : "/home/pi/api/open",     "verbs" : ["GET"],     "description" : "open garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/time",     "verbs" : ["GET"],     "description" : "returns server date and time"

,     "schema" : { "date" : "string",
"time" : "string"

}}, {     "abs" : "/home/pi/api/uptime",     "verbs" : ["GET"],     "description" : "returns server uptime"
,     "schema" : { "days" : "string",
"hours" : "string",
"minutes" : "string",
"seconds" : "string"
}}, {     "abs" : "/home/pi/api/os",     "verbs" : ["GET"],     "description" : "returns operating system details"

,     "schema" : { "distro" : "string"

}}, {     "abs" : "/home/pi/api/restful_api",     "verbs" : [],     "description" : "returns operating system details"

,     "schema" : {}}, {     "abs" : "/home/pi/api/junk",     "verbs" : [],     "description" : "returns operating system details"

,     "schema" : {}}, {     "abs" : "/home/pi/api/disk",     "verbs" : ["GET"],     "description" : "returns disk stats"
,     "schema" : { "total" : "string",
"used" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/server",     "verbs" : [],     "description" : "returns disk stats"
,     "schema" : {}}, {     "abs" : "/home/pi/api/reboot",     "verbs" : ["GET"],     "description" : "reboots server"

,     "schema" : { 
}}, {     "abs" : "/home/pi/api/toggle",     "verbs" : ["GET"],     "description" : "toggles garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/navigation",     "verbs" : ["GET"],     ,     "schema" : { "abs" : "string",
"verbs" : "list",
"description" : "string",
"schema" : "dictionary"

}}, {     "abs" : "/home/pi/api/cpu",     "verbs" : ["GET"],     "description" : "returns server cpu details"
,     "schema" : { "cores" : "string",
"frequency" : "string",
"used" : "string"

}}, {     "abs" : "/home/pi/api/close",     "verbs" : ["GET"],     "description" : "close garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/memory",     "verbs" : ["GET"],     "description" : "returns memory stats"
,     "schema" : { "total" : "string",
"used" : "string",
"available" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/state",     "verbs" : ["GET"],     "description" : "garage door state"
,     "schema" : {  }}] }
192.168.1.139 - - [14/Dec/2020 14:57:28] code 404, message Invalid resource requested
192.168.1.139 - - [14/Dec/2020 14:57:28] "GET /api/navigation HTTP/1.1" 404 -
^Cpi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ sudo crontab -e
No modification made
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ cat rest_server.py
#!/usr/bin/env python3

#########################
#
# Server-side script for RESTful API sever written in python using json
#
# The directory structure essentially defines the API. Each directory requires the following files:
#   verb = get, put, post, delete
#   <verb>.py performs the actions of the verb. For a get, it builds a JSON Data structure returned
#   <verb>.txt describes the API
#   <verb>.json defines the JSON schema
#
# Both client-side and server-side scripts are required for the API to work
#
#########################


#########################
#
# To run the script:
#   $ python3 rest_server.py
#
# There are multiple ways for a client-side to communicate with the Server-side API (see Help)
#
# This script requires the following:
#   Two raspberry pis: one running the server-side script and the other running the client-side script
#
#   Add the requests and distro modules:
#      $ pip install requests
#      $ sudo pip3 install distro
#
# Improvements
#   ??? how does importing this as a module work? or will it work
#   ??? renewing the cert should be part of the API, as long as the request is secure
#       certs should have their own directory within api
#   ??? add post, put and delete - but this can wait for actual usage example
#
# Each resource has one or more python script verbs (get.py, put.py)
# Sample directory Structure:
#    api
#       get.py
#       get.json
#       get.txt
#       server
#          get.py
#          get.json
#          get.txt
#          os
#             get.py
#             get.json
#             get.txt
#          memory
#             get.py
#             get.json
#             get.txt
#
# HTTP status codes:
#   1xx informational - not used
#   2xx success
#       200 OK for Get
#       201 Resource created for Post
#   3xx redirection - not used
#   4xx client error
#       400 Bad Request
#       401 Unauthorized: server not on LAN or bad HTTPS cert
#       404 Not Found
#   5xx web server error
#
# My understanding of Hypermedia as the Engine of Application State(HATEAOS),
# which guided implementation:
#   Client-Sever model: the rest and client scripts
#   Stateless: the web server is stateless.
#      If necessary, the client maintains state
#   Cacheable: resources are identified by the webserver as cacheable by the client
#   Uniform interface
#      Resource-Based: resources are identified in requests using URIs
#      Modification: resources are manipulated through API verbs (POST, PUT, GET, DELETE)
#      Self-descriptive client messages: a message contains sufficient information to describe
#         how a client can process a message
#         For example, a resource that allows POST, must support GET, which returns schema
#      Client can use API with no a priori knowledge, except base URI of API (i.e., discoverable)
#         So, versioning is not required
#         The entry URI provides a navigation resource (i.e., an object of all other URIs)
#            Navaigation includes allowed verbs (get, post, put, delete) on the URI and
#            whether or not the resource is cacheable (i.e., values in object are constant)
#         Other URIs: return the resource, which includes
#            resource object, its schema (how to the client can interpret the object) and/or
#            a status code
#   Layered system: client cannot tell if it is connected to end system or intermediary
#   Code on demand (optional)
#      For my applications, an SQL query can be passed to the web server
#   Idempotency: same object returned for the same call (values within object may change)
#      POST is NOT idempotent.
#      GET, PUT and DELETE are idempotent (e.g., delete should return same return code if
#      resource does not exist)
#
# HTTP Verbs:
#   GET: Provides read-only access to a resource
#   POST: Create a resource
#   DELETE: Delete a resource
#   PUT: Modify an existing resource (POST is use for creating a resource)
#
# Multithreading
#   I doubt my home systems will be transferring large files or have such a large volume of
#   API requests that multithreading would be required. In the course of putting together this
#   script, I ran across several instances of multithreaded http and https servers. Perhaps,
#   multithreading is a requirement and I am not in a position to see it yet. So, I'll add it.
#   g10guang's post 27JUL2018 in stackoverflow seems to be the most straight forward.
#
# HTTP and HTTPS support
#   In general, only servers that are authorized to use the API should be allowed, which
#   requires opening an SSL socket using a cert.
#
#   Run these commands on the server (use defaults and for FQDN use hostanme.local):
#
#      $ openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365
#      $ openssl req -x509 -newkey rsa:4096 -nodes -out client.crt -keyout client.key -days 365
#
#   copy the server.crt, client.key and client.crt to the rest_client server
#
#########################


#########################
# import needed libraries
import time
import datetime
import distro
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
import socket
import re
import os
import subprocess
import sys
import getopt
import ipaddress
import ssl
import json
import socket
import psutil


#########################
# use all CAPs for constants
MY_LAN = '192.168.1.0/24'


#########################
# use first CAP for global variables
#
# use high numbered port (90xx) indicating it is using http (port 80) and 9443 for https
Port = 9443
InputFile = ''
OutputFile = ''
Path = '/home/pi/api'
LogFile = Path + '/rest_server.log'
Use_HTTPS = False
Use_cert = False
Use_multithreading = False
ServerKeyFile = Path + '/server.key'
ServerCertFile = Path + '/server.crt'
ClientCertFile = Path + '/client.crt'
Debug = False

#########################
# Log messages should be time stamped
def timeStamp():
    t = time.time()
    s = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S - ')
    return s

# Write messages in a standard format
def printMsg(s):
    if s == '':
        LogFileObject.write("\n")
        if Debug:
            print('')
    else:
        LogFileObject.write(timeStamp() + s + "\n")
        if Debug:
            print(timeStamp() + s)

    LogFileObject.flush()

#########################

class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass

class customHandler(BaseHTTPRequestHandler):
    def getClient(self):
        c = str(self.client_address[0]) + " " + str(self.client_address[1])
        printMsg('Client is: ' + c)
        return(c)

    # only allow the API to be used by other servers on my LAN
    def isClientIpInvalid(self):
        network= ipaddress.ip_network(MY_LAN)
        client = ipaddress.ip_address(self.client_address[0])
        if (client in ipaddress.ip_network(MY_LAN)):
            printMsg('Client IP is valid: ' + str(client))
            return(False)
        printMsg('Client IP is invalid')
        self.sendInvalid('Client IP address is invalid')
        return(True)

    def sendIcon(self):
        # returns icon for the webserver
        self.send_response(200)
        self.send_header('Content-type','image/png')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        with open(Path + "/favicon.png", "rb") as fout:
            self.wfile.write(fout.read())
        return

    def sendHeaders(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        return

    def sendInvalid(self, s):
        printMsg(s + '\n')
        self.send_error(404, message=s)
        self.send_header('Content-type','text/html')
        self.end_headers()
        return

    def do_GET(self):
        # GET provides read-only access to the server's resources
        global Data

        pc = Path.split("/")
        l = len(pc) - 1
        no_api_path = ""
        for i in range(l):
            if pc[i] != "":
                no_api_path += "/" + pc[i]

        printMsg(self.requestline)
        printMsg(self.getClient())
        if Use_multithreading:
            printMsg('Thread: ' + str(threading.currentThread().getName()) + ' ' + str(threading.active_count()))

        if self.isClientIpInvalid():
            return

        if None != re.search('/api', self.path):
            data = {}
            try:
                exec(open(no_api_path + self.path + "/" + "get.py").read())
                data = Data
                self.sendHeaders()
                self.wfile.write(bytes(json.dumps(data), 'utf-8'))
                printMsg("Execute command: " + no_api_path + self.path + "/" + "get.py")
                return
            except:
                # unhandled resource
                self.sendInvalid('Invalid resource requested')
                printMsg('Invalid resource requested' + '\n')
                printMsg('')
                return
        elif None != re.search('/favicon.ico', self.path):
            # This is not part of the API, but browsers may request a favicon.ico to display in the tab
            self.sendIcon()
            printMsg('')
            return
        else:
            self.sendInvalid('Invalid request')
            printMsg('Invalid request' + '\n')
            printMsg('')
            return

    def do_POST(self):
        # POST allows client to add a new resource on the server
        # ??? needs work should follow get
        # successful request returns a 201
        printMsg(self.path)
        printMsg(self.getClient())
        # dummy code
        self.sendHeaders()
        self.wfile.write("POST Request", "utf8")
        printMsg('')
        return

    def do_DELETE(self):
        # DELETE allows a client to remove a server's resources
        # ??? needs work should follow get
        printMsg(self.path)
        printMsg(self.getClient())
        # dummy code
        self.sendHeaders()
        self.wfile.write("DELETE Request")
        printMsg('')
        return

    def do_PUT(self):
        # PUT alllows client to update an existing resource
        # ??? needs work should follow get
        printMsg(self.path)
        printMsg(self.getClient())
        # dummy code
        self.sendHeaders()
        self.wfile.write("PUT Request")
        printMsg('')
        return

    def handle_http(self):
        printMsg("http")
        printMsg('')
        return

    def respond(self):
        printMsg("respond")
        printMsg('')
        return

def cmdLine(argv):
    global InputFile
    global OutputFile
    global Port
    global LogFile
    global Use_HTTPS
    global Use_cert
    global Debug
    global Use_multithreading

    port_set = False
    try:
        # new options must be added here:
        validOpts = "hcdi:l:mp:s"
        opts, args = getopt.getopt(argv,validOpts,["help=", "cert", "debug", "inputfile=", "logfile=", "multithreading", "port=", "secure"])
    except getopt.GetoptError:
        print('rest_server.py [options, ...]' )
        print('rest_server.py -h' )
        sys.exit(2)

    for opt, arg in opts:
        # help option goes first and exits, regardless of other options
        if opt in ('-h', "--help"):
            print('Decription: ')
            print('  Server-side script for RESTful API sever written in python using json')
            print('  There are multiple ways for a client-side server to communicate with this server-side API:')
            print('    A client-side script can make HTTP requests (see rest_client.py)')
            print('    Open a browser and enter: http://<hostname>:<port>/api/cpu')
            print('    Open a terminal and run: $ curl -X GET http://<hostname>:<port>/api/cpu')
            print('')
            print('Usage:')
            print('  python3 rest_server.py [options...]')
            print('')
            print('Options:')
            print('  -h --help           this help')
            print('  -c --cert           Use cert, requires use https')
            print('  -d --debug          debug mode')
            print('  -i --inputfile      input json file')
            print('  -l --logfile        write log messages to user specified file')
            print('  -m --multithreading use multithreading')
            print('  -p --port           User defined port. The default port is ' + str(Port) + '.')
            print('  -s --secure         use https')
            sys.exit()
        elif opt in ("-c", "--cert"):
            Use_cert = True
        elif opt in ("-d", "--debug"):
            Debug = True
        elif opt in ("-i", "--inputfile"):
            InputFile = arg
        elif opt in ("-l", "--logfile"):
            LogFile = arg
        elif opt in ("-m", "--multithreading"):
            Use_multithreading = True
        elif opt in ("-p", "--port"):
            Port = int(arg)
            port_set = True
        elif opt in ("-s", "--secure"):
            Use_HTTPS = True
            if port_set:
                pass
            else:
                Port = 9443
    return

def printCmdLine():
    printMsg('Command line arguments:')
    printMsg('  Input file  = ' + InputFile)
    printMsg('  Log file = ' + LogFile)
    printMsg('  Port = ' + str(Port))
    printMsg('  Use cert = ' + str(Use_cert))
    printMsg('  Use HTTPS = ' + str(Use_HTTPS))
    printMsg('  Use multithreading = ' + str(Use_multithreading))
    printMsg('')
    return

#########################
def main(sysargv):
    global LogFileObject
    global Port

    # process command line arguments
    cmdLine(sysargv[1:])

    # open a log file. printMsg writes to the log file
    LogFileObject = open(LogFile, 'w+')

    printMsg("Starting REST server")
    printCmdLine()

    # get info about server-side host
    hostname = socket.gethostname()
    printMsg('Web Server:')
    printMsg("  Server name = " + hostname)
    local_host_ip = socket.gethostbyname(hostname)
    # local_host_ip = '0:0:0:0'
    printMsg("  Local Server IP = " + local_host_ip)

    host_ip = subprocess.check_output(['hostname', '-s', '-I']).decode('utf-8')[:-1]
    printMsg("  Server IP = " + host_ip)
    printMsg('')

    # create a handle for the server-side using the host information
    rest_server = (local_host_ip, Port)
    # rest_server = (host_ip, Port)

    if Use_multithreading:
        # threaded server
        httpd = ThreadingSimpleServer(rest_server, customHandler)
    else:
        # non-threaded server
        httpd = HTTPServer(rest_server, customHandler)

    if Use_HTTPS and Use_cert:
        printMsg("  Using HTTPS and cert")
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_cert_chain(certfile=ServerCertFile, keyfile=ServerKeyFile)
        context.load_verify_locations(cafile=ClientCertFile)

    # The server will run forever unless interrupted by CTRL-c
    try:
        if Use_HTTPS:
             if Use_cert:
                 httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
                 printMsg("  Got socket for HTTPS and cert")
             else:
                 httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=ServerKeyFile, certfile=ServerCertFile, server_side=True)
                 printMsg("  Got socket for HTTPS with no cert")
        else:
             printMsg("  No socket is required for HTTP?")

        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    # close server and files
    httpd.server_close()
    printMsg("Closing REST server")
    exit()

#########################
if __name__ == '__main__':
    # run as a script from command line
    main(sys.argv)
else:
    # ??? could allow import to another module; needs work
    pass
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ history
    1  which php
    2  sudo apt install --dry-run php7.4
    3  sudo apt install  php7.3
    4  sudo apt install --dry-run php7.4-sqlite3
    5  sudo apt install --dry-run php7.3-sqlite3
    6  sudo apt install  php7.3 php7.3-sqlite3
    7  nano createDB.sh
    8  sudo bash createDB.sh
    9  nano createDB.sh
   10  sudo bash createDB.sh
   11  nano createDB.sh
   12  sudo bash createDB.sh
   13  nano createDB.sh
   14  sudo bash createDB.sh
   15  nano createDB.sh
   16  sudo bash createDB.sh
   17  nano createDB.sh
   18  sudo bash createDB.sh
   19  nano createDB.sh
   20  sudo bash createDB.sh
   21  nano createDB.sh
   22  sudo bash createDB.sh
   23  nano createDB.sh
   24  sqlite3 /var/www/db/garagedoor.db
   25  nano createDB.sh
   26  ls
   27  nano push_garage_opener.py
   28  mv push_garage_opener.py pushGarageRemote.py
   29  nano createDB.sh
   30  wget "https://raw.githubusercontent.com/dumbo25/garageDoorOpener2/main/garage.sh"
   31  ls -l
   32  ls /usr/local/bin
   33  chmod UG+x garage.sh
   34  chmod ug+x garage.sh
   35  ls -l
   36  mv garage.sh /usr/local/bin/garage.sh
   37  sudo mv garage.sh /usr/local/bin/garage.sh
   38  ls /usr/local/bin
   39  ls -l /usr/local/bin
   40  nano /var/www/db/garage.sh
   41  nano /usr/local/bin/garage.sh
   42  ls
   43  gpio read 17
   44  which which gpio
   45  /usr/bin/gpio read 17
   46  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   47  sudo apt-get update -y
   48  sudo apt-get upgrade -y
   49  sudo nano /etc/ssmtp/ssmtp.conf
   50  sudo nano /etc/ssmtp/revaliases
   51  sudo chmod og+x /etc/ssmtp/ssmtp.conf
   52  nano emailTry.py
   53  python emailTry.py
   54  echo "close the garage door" | mail -s "Garage Door Open" 5127139980@txt.att.net
   55  sudo ufw show added
   56  sudo ufw allow 9080
   57  sudo ufw show added
   58  history | grep rest
   59  history | grep server
   60  python3 rest_server.py
   61  ls
   62  cd api
   63  ls
   64  python3 rest_server.py
   65  pwd
   66  python3 rest_server.py
   67  sudo python3 rest_server.py
   68  sudo python rest_server.py
   69  sudo python3 rest_server.py
   70  history |grep distro
   71  sudo pip3 install distro
   72  sudo python3 rest_server.py
   73  ls
   74  ls multi
   75  ls os
   76  nano rest_server.py
   77  ls
   78  nano rest_server.py
   79  sudo python3 rest_server.py -s
   80  sudo python3 rest_server.py 
   81  cat /etc/hosts
   82  sudo nano /etc/apache2/apache2.conf
   83  sudo nano /etc/apache2/conf-enabled/*.conf
   84  sudo nano /etc/apache2/sites-enabled/*.conf
   85  ls /usr/bin
   86  ls /usr/bin/rest_server.py
   87  ls -l /usr/bin/rest_server.py
   88  ps -aux | grep rest
   89  sudo nano /usr/bin/rest_server.py
   90  ls
   91  ls -l
   92  cat rest_server.log
   93  ls ../*.log
   94  sudo nano /usr/bin/rest_server.py
   95  pwd
   96  ls -l
   97  ps -aux | grep rest
   98  netstat -lptn
   99  netstat --tcp --listening --programs --numeric
  100  sudo ufw status
  101  sudo nano /usr/bin/rest_server.py
  102  cat /home/pi/api/server_cron.sh
  103  ls *.pid
  104  ls
  105  cat rest_server.log
  106  ls
  107  cd api
  108  httpd -t -c httpd.conf
  109  sudo httpd -t -c httpd.conf
  110  ls /etc/httpd
  111  which apache2
  112  ls /usr/sbin
  113  sudo nano /usr/bin/rest_server.py &
  114  curl -X GET http://localhost:9443/api/cpu
  115  sudo kill 8802
  116  sudo nano /etc/apache2/ports.conf
  117  sudo ufw status
  118  sudo ufw allow 9443
  119  sudo nano /usr/bin/rest_server.py
  120  sudo python3 /usr/bin/rest_server.py &
  121  ls
  122  cat rest_server.log
  123  sudo kill 9401
  124  ls -l
  125  ls -l cpu
  126  nano rest_server.py
  127  sudo python3 /usr/bin/rest_server.py 
  128  sudo python3 /usr/bin/rest_server.py -d
  129  sudo python3 /usr/bin/rest_server.py -h
  130  ls
  131  history | grep rest_server.py
  132  sudo nano /usr/bin/rest_server.py
  133  sudo nano rest_server.py
  134  sudo python3 rest_server.py -d
  135  netstat -l
  136  sudo python3 rest_server.py &
  137  netstat -l
  138  sudo kill 10805
  139  nc -zv localhost 8080
  140  nc -zv localhost 443
  141  nc -zv localhost 5070
  142  nc -z localhost 5070
  143  nc -zv localhost 5070
  144  nc -zv localhost 8888
  145  sudo python3 rest_server.py &
  146  nc -zv localhost 9443
  147  nc -zv rpiGarageOpener 9443
  148  sudo nano /etc/hosts
  149  history | grep nano | grep /
  150  sudo nano /etc/apache2/ports.conf
  151  sudo nano /etc/ssmtp/revaliases
  152  ls /etc
  153  sudoo nano /etc/host.conf
  154  sudo nano /etc/host.conf
  155  sudo nano /etc/host.allow
  156  sudo nano /etc/host.deny
  157  sudo nano /etc/networks
  158  sudo nano /etc/sysctl.conf
  159  ps -aux | grep rest_server
  160  sudo kill 8802
  161  sudo kill 8803
  162  sudo kill 12215
  163  sudo kill 12216
  164  ps -aux | grep rest_server
  165  sudo kill 8803
  166  sudo kill 8802
  167  ps -aux | grep rest_server
  168  sudo reboot
  169  nc -zv rpiGarageOpener 9443
  170  netstat -l
  171  sudo python3 rest_server.py &
  172  sudo kill 1280
  173  ps -aux | grep rest_server
  174  cd api
  175  sudo python3 rest_server.py &
  176  netstat -l
  177  nc -zv rpiGarageOpener 9443
  178  cat < /dev/null > /dev/tcp/rpiGarageOpener:9443; echo $?
  179  cat < /dev/null > /dev/tcp/rpiGarageOpener/9443; echo $?
  180  ps -aux | grep rest_server
  181  history
  182  ps -aux | grep rest_server
  183  sudo kill 1327
  184  ps -aux | grep rest_server
  185  python3 rest_server.py &
  186  ps -aux | grep rest_server
  187  sudo kill 1652
  188  python3 rest_server.py -p5070 &
  189  ps -aux | grep rest_server
  190  sudo kill 1698
  191  sudo python3 rest_server.py -p5070 &
  192  sudo kill 1763
  193  sudo netstat -anp | grep ':80 '
  194  sudo netstat -anp | grep ':9443 '
  195  sudo python3 rest_server.py &
  196  sudo netstat -anp | grep ':9443 '
  197  hotsname -L
  198  hotsname -I
  199  hostname -I
  200  sudo netstat -tnlp | grep :9443
  201  sudo tcpdump -n icmp
  202  sudo service ssh status
  203  netstat -an | grep "LISTEN "
  204  sudo nano /etc/hosts
  205  sudo netstat -tnlp | grep :5070
  206  ps -aux 
  207  ps -aux | grep 5070
  208  ps -aux | grep python
  209  sudo nano /usr/local/bin/rpi-echo.py
  210  sudo netstat -tnlp | grep :5070
  211  sudo nano /usr/local/bin/rpi-echo.py
  212  ps -aux | grep rest_server
  213  sudo kill 1898
  214  ps -aux | grep rest_server
  215  nano rest_server.py
  216  python3 rest_server.py
  217  python3 rest_server.py -d
  218  nano rest_server.py
  219  python3 rest_server.py -d
  220  nano rest_server.py
  221  python3 rest_server.py -d
  222  nano rest_server.py
  223  python3 rest_server.py -d
  224  ls /cat
  225  ls /etc
  226  ls /etc/.hosts
  227  cat /etc/hosts
  228  sudo nano /etc/hosts
  229  sudo reboot
  230  ls
  231  cd api
  232  ls
  233  ls cpu
  234  ls
  235  nano rest_server.py
  236  ls navigation
  237  cd navigation
  238  cat get.py
  239  ls
  240  cd ..
  241  cat get.py
  242  ls
  243  sudo python3 rest_server.py
  244  sudo crontab -e
  245  ls
  246  cat rest_server.py
  247  nano rest_server.py
  248  history
pi@rpiGarageOpener:~/api $ cd ..
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py
  File "/usr/local/bin/garage.py", line 80
    opts, args = getopt.getopt(argv,validOpts,["help=", "cert", "debug", "inputfile=", "logfile=", "multithreading", "por$
                                                                                                                         ^
SyntaxError: EOL while scanning string literal
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py
  File "/usr/local/bin/garage.py", line 80
    opts, args = getopt.getopt(argv,validOpts,["help=", "Debug", "database=", "logfile=")
                                                                                        ^
SyntaxError: invalid syntax
pi@rpiGarageOpener:~ $ nano rest_server.py
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ cd ..
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py
Traceback (most recent call last):
  File "/usr/local/bin/garage.py", line 133, in <module>
    cmdLine(sysargv[1:])
NameError: name 'sysargv' is not defined
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py
Traceback (most recent call last):
  File "/usr/local/bin/garage.py", line 133, in <module>
    cmdLine(sysargv[1:])
NameError: name 'sysargv' is not defined
pi@rpiGarageOpener:~ $ nano api/rest_server.py
pi@rpiGarageOpener:~ $ nano api/rest_server.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py
pi@rpiGarageOpener:~ $ ls
api                createDB.sh  Downloads    getScripts2.sh  Music     pushGarageRemote.py  rpi-echo.service  tls2.sh
Bookshelf          dead.letter  emailTry.py  getScripts.sh   myID.txt  read.py              simple-fan.py     tls.sh
b.sh               Desktop      genID.py     getWebsite.sh   Pictures  rest_server.log      simple-fan.py.1   unused_rpi.sh
check_apache.html  Documents    getAPI.sh    hello.py        Public    rpi-echo.log         Templates         Videos
pi@rpiGarageOpener:~ $ cat garage.log
cat: garage.log: No such file or directory
pi@rpiGarageOpener:~ $ ls *.log
rest_server.log  rpi-echo.log
pi@rpiGarageOpener:~ $ cat rest_server.log
2020/12/14 17:35:29 - Starting REST server
2020/12/14 17:35:29 - Command line arguments:
2020/12/14 17:35:29 -   Log file = /home/pi/rest_server.log

2020/12/14 17:35:30 - Door: Closed
2020/12/14 17:35:30 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 17:40:22 - Starting garage.py
2020/12/14 17:40:22 - Command line arguments:
2020/12/14 17:40:22 -   Log file = /home/pi/garage.log

2020/12/14 17:40:23 - Door: Closed
2020/12/14 17:40:23 - Opening database = /var/www/db/garagedoor.db
2020/12/14 17:40:23 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 17:42:29 - Starting garage.py
2020/12/14 17:42:29 - Command line arguments:
2020/12/14 17:42:29 -   Log file = /home/pi/garage.log

2020/12/14 17:42:30 - Door: Closed
Traceback (most recent call last):
  File "/usr/local/bin/garage.py", line 224, in <module>
    main(sys.argv)
  File "/usr/local/bin/garage.py", line 215, in main
    db_con.close()
UnboundLocalError: local variable 'db_con' referenced before assignment
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 17:44:44 - Starting garage.py
2020/12/14 17:44:44 - Command line arguments:
2020/12/14 17:44:44 -   Log file = /home/pi/garage.log

2020/12/14 17:44:45 - Door: Closed
2020/12/14 17:44:45 - Closing garage.py
pi@rpiGarageOpener:~ $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Mon Dec 14 17:07:53 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.sh -D
python3: can't open file '/usr/local/bin/garage.sh': [Errno 2] No such file or directory
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:05:40 - Starting garage.py
2020/12/14 20:05:40 - Command line arguments:
2020/12/14 20:05:40 -   Log file = /home/pi/garage.log

2020/12/14 20:05:41 - Door: Open
2020/12/14 20:05:41 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:05:41 - Vacation: yes
2020/12/14 20:05:44 - Closing garage.py
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ sqlite3 /var/www/db/garagedoor.db
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
sqlite> .tables
schedule  status  
sqlite> .schema status
CREATE TABLE status (tdate DATE, ttime TIME, name TEXT, value TEXT);
sqlite> select * from status
   ...> ;
2020-11-29|13:24:29|vacation|yes
2020-11-29|13:24:29|schedule|on
2020-11-29|13:24:29|command|vacation
2020-11-29|13:24:29|monitor|on
sqlite> select * from schedule;
2020-11-29|13:24:28|Sunday|00:00:00|05:00:00
2020-11-29|13:24:28|Monday|00:00:00|05:00:00
2020-11-29|13:24:28|Tuesday|00:00:00|05:00:00
2020-11-29|13:24:29|Wednesday|00:00:00|05:00:00
2020-11-29|13:24:29|Thursday|00:00:00|05:00:00
2020-11-29|13:24:29|Friday|00:00:00|05:00:00
2020-11-29|13:24:29|Saturday|00:00:00|05:00:00
sqlite> .schema schedule
CREATE TABLE schedule (tdate DATE, ttime TIME, day TEXT, arm TIME, disarm TIME);
sqlite> update schedule set arm = '20:00:00', disarm = '06:00:00' where day = 'Monday";
   ...> ;
   ...> ^C''
   ...> "
   ...> '
   ...> ;
sqlite> select * from schedule;
2020-11-29|13:24:28|Sunday|00:00:00|05:00:00
2020-11-29|13:24:28|Monday|00:00:00|05:00:00
2020-11-29|13:24:28|Tuesday|00:00:00|05:00:00
2020-11-29|13:24:29|Wednesday|00:00:00|05:00:00
2020-11-29|13:24:29|Thursday|00:00:00|05:00:00
2020-11-29|13:24:29|Friday|00:00:00|05:00:00
2020-11-29|13:24:29|Saturday|00:00:00|05:00:00
sqlite> update schedule set arm = '20:00:00', disarm = '06:00:00' where day = 'Monday';
sqlite> select * from schedule;
2020-11-29|13:24:28|Sunday|00:00:00|05:00:00
2020-11-29|13:24:28|Monday|20:00:00|06:00:00
2020-11-29|13:24:28|Tuesday|00:00:00|05:00:00
2020-11-29|13:24:29|Wednesday|00:00:00|05:00:00
2020-11-29|13:24:29|Thursday|00:00:00|05:00:00
2020-11-29|13:24:29|Friday|00:00:00|05:00:00
2020-11-29|13:24:29|Saturday|00:00:00|05:00:00
sqlite> .quit
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:17:09 - Starting garage.py
2020/12/14 20:17:09 - Command line arguments:
2020/12/14 20:17:09 -   Log file = /home/pi/garage.log

2020/12/14 20:17:10 - Door: Open
2020/12/14 20:17:10 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:17:10 - Vacation: yes
2020/12/14 20:17:12 - Closing garage.py
pi@rpiGarageOpener:~ $ sqlite3 /var/www/db/garagedoor.db
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
sqlite> update status value = 'no' where name = 'vacation';
Error: near "value": syntax error
sqlite> update status set value = 'no' where name = 'vacation';
sqlite> select * from status;
2020-11-29|13:24:29|vacation|no
2020-11-29|13:24:29|schedule|on
2020-11-29|13:24:29|command|vacation
2020-11-29|13:24:29|monitor|on
sqlite> .quit
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:19:06 - Starting garage.py
2020/12/14 20:19:06 - Command line arguments:
2020/12/14 20:19:06 -   Log file = /home/pi/garage.log

2020/12/14 20:19:07 - Door: Open
2020/12/14 20:19:07 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:19:07 - Vacation: no
2020/12/14 20:19:07 - Schedule: on
2020/12/14 20:19:07 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:21:42 - Starting garage.py
2020/12/14 20:21:42 - Command line arguments:
2020/12/14 20:21:42 -   Log file = /home/pi/garage.log

2020/12/14 20:21:43 - Door: Open
2020/12/14 20:21:43 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:21:43 - Vacation: no
2020/12/14 20:21:43 - Schedule: on
2020/12/14 20:21:43 - Closing garage.py
pi@rpiGarageOpener:~ $ sqlite3 /var/www/db/garagedoor.db
SQLite version 3.27.2 2019-02-25 16:06:06
Enter ".help" for usage hints.
sqlite> update status value = 'yes' where name = 'schedule';
Error: near "value": syntax error
sqlite> update status set value = 'yes' where name = 'schedule';
sqlite> .quit
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:24:05 - Starting garage.py
2020/12/14 20:24:05 - Command line arguments:
2020/12/14 20:24:05 -   Log file = /home/pi/garage.log

2020/12/14 20:24:06 - Door: Open
2020/12/14 20:24:06 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:24:06 - Vacation: no
2020/12/14 20:24:06 - Schedule: yes
2020/12/14 20:24:06 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:28:47 - Starting garage.py
2020/12/14 20:28:47 - Command line arguments:
2020/12/14 20:28:47 -   Log file = /home/pi/garage.log

2020/12/14 20:28:48 - Door: Open
2020/12/14 20:28:48 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:28:48 - Vacation: no
2020/12/14 20:28:48 - Schedule: yes
2020/12/14 20:28:48 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:29:13 - Starting garage.py
2020/12/14 20:29:13 - Command line arguments:
2020/12/14 20:29:13 -   Log file = /home/pi/garage.log

2020/12/14 20:29:14 - Door: Open
2020/12/14 20:29:14 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:29:14 - Vacation: no
2020/12/14 20:29:14 - Schedule: yes
2020/12/14 20:29:14 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo nano /usr/local/bin/garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
  File "/usr/local/bin/garage.py", line 188
    printMsg("Day of week = ' + day)
                                   ^
SyntaxError: EOL while scanning string literal
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:34:33 - Starting garage.py
2020/12/14 20:34:33 - Command line arguments:
2020/12/14 20:34:33 -   Log file = /home/pi/garage.log

2020/12/14 20:34:34 - Door: Open
2020/12/14 20:34:34 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:34:34 - Vacation: no
2020/12/14 20:34:34 - Schedule: yes
2020/12/14 20:34:34 - Day of week = Monday
2020/12/14 20:34:34 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:36:09 - Starting garage.py
2020/12/14 20:36:09 - Command line arguments:
2020/12/14 20:36:09 -   Log file = /home/pi/garage.log

2020/12/14 20:36:10 - Door: Open
2020/12/14 20:36:10 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:36:10 - Vacation: no
2020/12/14 20:36:10 - Schedule: yes
2020/12/14 20:36:10 - Day of week = Monday
2020/12/14 20:36:10 - arm time = 20:00:00
2020/12/14 20:36:10 - disarm time = 06:00:00
2020/12/14 20:36:10 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:37:22 - Starting garage.py
2020/12/14 20:37:22 - Command line arguments:
2020/12/14 20:37:22 -   Log file = /home/pi/garage.log

2020/12/14 20:37:23 - Door: Open
2020/12/14 20:37:23 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:37:23 - Vacation: no
2020/12/14 20:37:23 - Schedule: yes
2020/12/14 20:37:23 - Day of week = Monday
2020/12/14 20:37:23 - arm time = 20:00:00
2020/12/14 20:37:23 - disarm time = 06:00:00
2020/12/14 20:37:23 - Current time = time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=20, tm_min=37, tm_sec=23, tm_wday=0, tm_yday=1, tm_isdst=-1)
2020/12/14 20:37:24 - Garage: open late at night
2020/12/14 20:37:24 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:41:42 - Starting garage.py
2020/12/14 20:41:42 - Command line arguments:
2020/12/14 20:41:42 -   Log file = /home/pi/garage.log

2020/12/14 20:41:43 - Door: Open
2020/12/14 20:41:43 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:41:43 - Vacation: no
2020/12/14 20:41:43 - Schedule: yes
2020/12/14 20:41:43 - Day of week = Monday
2020/12/14 20:41:43 - arm time = 20:00:00
2020/12/14 20:41:43 - disarm time = 06:00:00
2020/12/14 20:41:44 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:42:35 - Starting garage.py
2020/12/14 20:42:35 - Command line arguments:
2020/12/14 20:42:35 -   Log file = /home/pi/garage.log

2020/12/14 20:42:36 - Door: Open
2020/12/14 20:42:36 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:42:36 - Vacation: no
2020/12/14 20:42:36 - Schedule: yes
2020/12/14 20:42:36 - Day of week = Monday
2020/12/14 20:42:36 - arm time = 20:00:00
2020/12/14 20:42:36 - disarm time = 06:00:00
2020/12/14 20:42:36 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:43:29 - Starting garage.py
2020/12/14 20:43:29 - Command line arguments:
2020/12/14 20:43:29 -   Log file = /home/pi/garage.log

2020/12/14 20:43:30 - Door: Open
2020/12/14 20:43:30 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:43:30 - Vacation: no
2020/12/14 20:43:30 - Schedule: yes
2020/12/14 20:43:30 - Day of week = Monday
2020/12/14 20:43:30 - arm time = 20:00:00
2020/12/14 20:43:30 - disarm time = 06:00:00
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=20, tm_min=43, tm_sec=30, tm_wday=0, tm_yday=1, tm_isdst=-1)
2020/12/14 20:43:32 - Garage: open late at night
2020/12/14 20:43:32 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:49:01 - Starting garage.py
2020/12/14 20:49:01 - Command line arguments:
2020/12/14 20:49:01 -   Log file = /home/pi/garage.log

2020/12/14 20:49:02 - Door: Open
2020/12/14 20:49:02 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:49:02 - Vacation: no
2020/12/14 20:49:02 - Schedule: yes
2020/12/14 20:49:02 - Day of week = Monday
2020/12/14 20:49:02 - arm time = 20:00:00
2020/12/14 20:49:02 - disarm time = 06:00:00
2020/12/14 20:49:02 - Closing garage.py
pi@rpiGarageOpener:~ $ sudo python3 /usr/local/bin/garage.py -D
2020/12/14 20:49:48 - Starting garage.py
2020/12/14 20:49:48 - Command line arguments:
2020/12/14 20:49:48 -   Log file = /home/pi/garage.log

2020/12/14 20:49:49 - Door: Open
2020/12/14 20:49:49 - Opening database = /var/www/db/garagedoor.db
2020/12/14 20:49:49 - Vacation: no
2020/12/14 20:49:49 - Schedule: yes
2020/12/14 20:49:49 - Day of week = Monday
2020/12/14 20:49:49 - arm time = 20:00:00
2020/12/14 20:49:49 - disarm time = 06:00:00
2020/12/14 20:49:49 - Current time = 20:49:49
2020/12/14 20:49:51 - Garage: open late at night
2020/12/14 20:49:51 - Closing garage.py
pi@rpiGarageOpener:~ $ ls
api                dead.letter  garage.log      getWebsite.sh  Public               rpi-echo.service  tls.sh
Bookshelf          Desktop      genID.py        hello.py       pushGarageRemote.py  simple-fan.py     unused_rpi.sh
b.sh               Documents    getAPI.sh       Music          read.py              simple-fan.py.1   Videos
check_apache.html  Downloads    getScripts2.sh  myID.txt       rest_server.log      Templates
createDB.sh        emailTry.py  getScripts.sh   Pictures       rpi-echo.log         tls2.sh
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ history | grep rest_server
   60  python3 rest_server.py
   64  python3 rest_server.py
   66  python3 rest_server.py
   67  sudo python3 rest_server.py
   68  sudo python rest_server.py
   69  sudo python3 rest_server.py
   72  sudo python3 rest_server.py
   76  nano rest_server.py
   78  nano rest_server.py
   79  sudo python3 rest_server.py -s
   80  sudo python3 rest_server.py 
   86  ls /usr/bin/rest_server.py
   87  ls -l /usr/bin/rest_server.py
   89  sudo nano /usr/bin/rest_server.py
   92  cat rest_server.log
   94  sudo nano /usr/bin/rest_server.py
  101  sudo nano /usr/bin/rest_server.py
  105  cat rest_server.log
  113  sudo nano /usr/bin/rest_server.py &
  119  sudo nano /usr/bin/rest_server.py
  120  sudo python3 /usr/bin/rest_server.py &
  122  cat rest_server.log
  126  nano rest_server.py
  127  sudo python3 /usr/bin/rest_server.py 
  128  sudo python3 /usr/bin/rest_server.py -d
  129  sudo python3 /usr/bin/rest_server.py -h
  131  history | grep rest_server.py
  132  sudo nano /usr/bin/rest_server.py
  133  sudo nano rest_server.py
  134  sudo python3 rest_server.py -d
  136  sudo python3 rest_server.py &
  145  sudo python3 rest_server.py &
  159  ps -aux | grep rest_server
  164  ps -aux | grep rest_server
  167  ps -aux | grep rest_server
  171  sudo python3 rest_server.py &
  173  ps -aux | grep rest_server
  175  sudo python3 rest_server.py &
  180  ps -aux | grep rest_server
  182  ps -aux | grep rest_server
  184  ps -aux | grep rest_server
  185  python3 rest_server.py &
  186  ps -aux | grep rest_server
  188  python3 rest_server.py -p5070 &
  189  ps -aux | grep rest_server
  191  sudo python3 rest_server.py -p5070 &
  195  sudo python3 rest_server.py &
  212  ps -aux | grep rest_server
  214  ps -aux | grep rest_server
  215  nano rest_server.py
  216  python3 rest_server.py
  217  python3 rest_server.py -d
  218  nano rest_server.py
  219  python3 rest_server.py -d
  220  nano rest_server.py
  221  python3 rest_server.py -d
  222  nano rest_server.py
  223  python3 rest_server.py -d
  243  history | grep rest_server
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ nano rest_server.py
pi@rpiGarageOpener:~/api $ cd navigation
pi@rpiGarageOpener:~/api/navigation $ ls
get.json  get.py  get.py~  junk.json
pi@rpiGarageOpener:~/api/navigation $ cat get.py~
# returns navigation for API
global Data
global Path
data = ""

# ??? need to remove /navigation
next = False

# excluded_prefixes = ('__', '.')
for paths, dirs, files in os.walk(Path):
    # exclude hidden folders and special files starting with excluded_prefixes
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    dirs[:] = [d for d in dirs if not d.startswith("__")]

    filenames = [f for f in files if not f.startswith(".")]
    filenames[:] = [f for f in files if not f.startswith("__")]

    if next:
        data += ", "

    schema = "'schema' : {''}"
    verbs = "'verbs' : ["
    next_verb = False
    for f in filenames:
        if None != re.search('.py', f):

            if next_verb:
                verbs += ", "
            verb = f[:len(f)-3]
            file = paths + "/" + verb
            try:
                # ??? how to get proper indentation
                schema = "'schema' : { "
                with open(file + ".json", "r") as read_file:
                    schema += read_file.read()
                    # ??? needs to read line at a time rather than the whole file
                schema += "}"
            except:
                schema = "'schema' : {''}"
            verb = verb.upper()
            verbs += "'" + verb + "'"
            next_verb = True
    if next_verb:
        verbs += "], "
    else:
        verbs += "''], "

    data += "{ "
    data += "    'abs' : '" + paths + "', "
    data += "    " + verbs
    data += "    'description' : 'returns server date and time', "
    data += "    " + schema
    data += " }"

    next = True
    print("\n\ndata = " +data)

Data = json.loads(data)
pi@rpiGarageOpener:~/api/navigation $ ls
get.json  get.py  get.py~  junk.json
pi@rpiGarageOpener:~/api/navigation $ cat ../get.py
global Data
# returns hostanme of server
Data = {"hostname" : socket.gethostname()}
pi@rpiGarageOpener:~/api/navigation $ cd ..
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py
^Cpi@rpiGarageOpener:~/api $ sudo python3 rest_server.py -d
2020/12/14 21:27:08 - Starting REST server
2020/12/14 21:27:08 - Command line arguments:
2020/12/14 21:27:08 -   Input file  = 
2020/12/14 21:27:08 -   Log file = /home/pi/api/rest_server.log
2020/12/14 21:27:08 -   Port = 9443
2020/12/14 21:27:08 -   Use cert = False
2020/12/14 21:27:08 -   Use HTTPS = False
2020/12/14 21:27:08 -   Use multithreading = False

2020/12/14 21:27:08 - Web Server:
2020/12/14 21:27:08 -   Server name = rpiGarageOpener
2020/12/14 21:27:09 -   Local Server IP = 0.0.0.0
2020/12/14 21:27:09 -   Server IP = 192.168.1.227 

2020/12/14 21:27:09 -   No socket is required for HTTP?
2020/12/14 21:27:22 - GET /api/cpu HTTP/1.1
2020/12/14 21:27:22 - Client is: 192.168.1.139 39734
2020/12/14 21:27:22 - 192.168.1.139 39734
2020/12/14 21:27:22 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [14/Dec/2020 21:27:22] "GET /api/cpu HTTP/1.1" 200 -
2020/12/14 21:27:22 - Execute command: /home/pi/api/cpu/get.py
2020/12/14 21:27:34 - GET /api HTTP/1.1
2020/12/14 21:27:34 - Client is: 192.168.1.139 39736
2020/12/14 21:27:34 - 192.168.1.139 39736
2020/12/14 21:27:34 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [14/Dec/2020 21:27:34] "GET /api HTTP/1.1" 200 -
2020/12/14 21:27:34 - Execute command: /home/pi/api/get.py
2020/12/14 21:27:47 - GET /api/navigation HTTP/1.1
2020/12/14 21:27:47 - Client is: 192.168.1.139 39738
2020/12/14 21:27:47 - 192.168.1.139 39738
2020/12/14 21:27:47 - Client IP is valid: 192.168.1.139


data = { "directories" : [ {     "abs" : "/home/pi/api",     "verbs" : ["GET"],     "description" : "returns hostname"
,     "schema" : { "hostname" : "string"
}}, {     "abs" : "/home/pi/api/test",     "verbs" : [],     "description" : "returns hostname"
,     "schema" : {}}, {     "abs" : "/home/pi/api/open",     "verbs" : ["GET"],     "description" : "open garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/time",     "verbs" : ["GET"],     "description" : "returns server date and time"

,     "schema" : { "date" : "string",
"time" : "string"

}}, {     "abs" : "/home/pi/api/uptime",     "verbs" : ["GET"],     "description" : "returns server uptime"
,     "schema" : { "days" : "string",
"hours" : "string",
"minutes" : "string",
"seconds" : "string"
}}, {     "abs" : "/home/pi/api/os",     "verbs" : ["GET"],     "description" : "returns operating system details"

,     "schema" : { "distro" : "string"

}}, {     "abs" : "/home/pi/api/restful_api",     "verbs" : [],     "description" : "returns operating system details"

,     "schema" : {}}, {     "abs" : "/home/pi/api/junk",     "verbs" : [],     "description" : "returns operating system details"

,     "schema" : {}}, {     "abs" : "/home/pi/api/disk",     "verbs" : ["GET"],     "description" : "returns disk stats"
,     "schema" : { "total" : "string",
"used" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/server",     "verbs" : [],     "description" : "returns disk stats"
,     "schema" : {}}, {     "abs" : "/home/pi/api/reboot",     "verbs" : ["GET"],     "description" : "reboots server"

,     "schema" : { 
}}, {     "abs" : "/home/pi/api/toggle",     "verbs" : ["GET"],     "description" : "toggles garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/navigation",     "verbs" : ["GET"],     ,     "schema" : { "abs" : "string",
"verbs" : "list",
"description" : "string",
"schema" : "dictionary"

}}, {     "abs" : "/home/pi/api/cpu",     "verbs" : ["GET"],     "description" : "returns server cpu details"
,     "schema" : { "cores" : "string",
"frequency" : "string",
"used" : "string"

}}, {     "abs" : "/home/pi/api/close",     "verbs" : ["GET"],     "description" : "close garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/memory",     "verbs" : ["GET"],     "description" : "returns memory stats"
,     "schema" : { "total" : "string",
"used" : "string",
"available" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/state",     "verbs" : ["GET"],     "description" : "garage door state"
,     "schema" : {  }}] }
2020/12/14 21:27:47 - Invalid resource requested

192.168.1.139 - - [14/Dec/2020 21:27:47] code 404, message Invalid resource requested
192.168.1.139 - - [14/Dec/2020 21:27:47] "GET /api/navigation HTTP/1.1" 404 -
2020/12/14 21:27:47 - Invalid resource requested


^C2020/12/14 21:28:36 - Closing REST server
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ nano navigation/get.py
pi@rpiGarageOpener:~/api $ cat close/get.py
global Data
# closes garage door
cmd = 'sudo python /usr/local/bin/close.py'
os.system(cmd)
Data = {}
pi@rpiGarageOpener:~/api $ nano navigation/get.py
pi@rpiGarageOpener:~/api $ sudo python3 rest_server.py -d
2020/12/14 21:34:59 - Starting REST server
2020/12/14 21:34:59 - Command line arguments:
2020/12/14 21:34:59 -   Input file  = 
2020/12/14 21:34:59 -   Log file = /home/pi/api/rest_server.log
2020/12/14 21:34:59 -   Port = 9443
2020/12/14 21:34:59 -   Use cert = False
2020/12/14 21:34:59 -   Use HTTPS = False
2020/12/14 21:34:59 -   Use multithreading = False

2020/12/14 21:34:59 - Web Server:
2020/12/14 21:34:59 -   Server name = rpiGarageOpener
2020/12/14 21:34:59 -   Local Server IP = 0.0.0.0
2020/12/14 21:34:59 -   Server IP = 192.168.1.227 

2020/12/14 21:34:59 -   No socket is required for HTTP?
2020/12/14 21:35:03 - GET /api/navigation HTTP/1.1
2020/12/14 21:35:03 - Client is: 192.168.1.139 39740
2020/12/14 21:35:03 - 192.168.1.139 39740
2020/12/14 21:35:03 - Client IP is valid: 192.168.1.139


data = { "directories" : [ {     "abs" : "/home/pi/api",     "verbs" : ["GET"],     "description" : "returns hostname"
,     "schema" : { "hostname" : "string"
}}, {     "abs" : "/home/pi/api/test",     "verbs" : [],     "description" : "returns hostname"
,     "schema" : {}}, {     "abs" : "/home/pi/api/open",     "verbs" : ["GET"],     "description" : "open garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/time",     "verbs" : ["GET"],     "description" : "returns server date and time"

,     "schema" : { "date" : "string",
"time" : "string"

}}, {     "abs" : "/home/pi/api/uptime",     "verbs" : ["GET"],     "description" : "returns server uptime"
,     "schema" : { "days" : "string",
"hours" : "string",
"minutes" : "string",
"seconds" : "string"
}}, {     "abs" : "/home/pi/api/os",     "verbs" : ["GET"],     "description" : "returns operating system details"

,     "schema" : { "distro" : "string"

}}, {     "abs" : "/home/pi/api/restful_api",     "verbs" : [],     "description" : "returns operating system details"

,     "schema" : {}}, {     "abs" : "/home/pi/api/junk",     "verbs" : [],     "description" : "returns operating system details"

,     "schema" : {}}, {     "abs" : "/home/pi/api/disk",     "verbs" : ["GET"],     "description" : "returns disk stats"
,     "schema" : { "total" : "string",
"used" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/server",     "verbs" : [],     "description" : "returns disk stats"
,     "schema" : {}}, {     "abs" : "/home/pi/api/reboot",     "verbs" : ["GET"],     "description" : "reboots server"

,     "schema" : { 
}}, {     "abs" : "/home/pi/api/toggle",     "verbs" : ["GET"],     "description" : "toggles garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/navigation",     "verbs" : ["GET"],     ,     "schema" : { "abs" : "string",
"verbs" : "list",
"description" : "string",
"schema" : "dictionary"

}}, {     "abs" : "/home/pi/api/cpu",     "verbs" : ["GET"],     "description" : "returns server cpu details"
,     "schema" : { "cores" : "string",
"frequency" : "string",
"used" : "string"

}}, {     "abs" : "/home/pi/api/close",     "verbs" : ["GET"],     "description" : "close garage door"
,     "schema" : {  }}, {     "abs" : "/home/pi/api/memory",     "verbs" : ["GET"],     "description" : "returns memory stats"
,     "schema" : { "total" : "string",
"used" : "string",
"available" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/state",     "verbs" : ["GET"],     "description" : "garage door state"
,     "schema" : {  }}] }
2020/12/14 21:35:03 - Invalid resource requested

192.168.1.139 - - [14/Dec/2020 21:35:03] code 404, message Invalid resource requested
192.168.1.139 - - [14/Dec/2020 21:35:03] "GET /api/navigation HTTP/1.1" 404 -
2020/12/14 21:35:03 - Invalid resource requested


^C2020/12/14 21:35:58 - Closing REST server
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
  [Restored Dec 15, 2020 at 7:44:42 AM]
Last login: Tue Dec 15 07:44:42 on ttys004
Restored session: Tue Dec 15 07:33:43 CST 2020

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
pi@rpigarageopener.local's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Mon Dec 14 20:04:56 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ 
pi@rpiGarageOpener:~ $ ls
api                dead.letter  garage.log      getWebsite.sh  Public               rpi-echo.service  tls.sh
Bookshelf          Desktop      genID.py        hello.py       pushGarageRemote.py  simple-fan.py     unused_rpi.sh
b.sh               Documents    getAPI.sh       Music          read.py              simple-fan.py.1   Videos
check_apache.html  Downloads    getScripts2.sh  myID.txt       rest_server.log      Templates
createDB.sh        emailTry.py  getScripts.sh   Pictures       rpi-echo.log         tls2.sh
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ ls -l os
total 16
-rw-r--r-- 1 pi pi 92 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi 21 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi 92 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi 52 Dec  6 08:11 get.txt
pi@rpiGarageOpener:~/api $ ls -l close
total 16
-rw-r--r-- 1 pi pi 102 Dec 12 14:22 get.backup.sh
-rw-r--r-- 1 pi pi   1 Dec 12 14:22 get.json
-rw-r--r-- 1 pi pi 102 Dec 12 14:22 get.py
-rw-r--r-- 1 pi pi  36 Dec 12 14:22 get.txt
pi@rpiGarageOpener:~/api $ cat os/get.txt
"description" : "returns operating system details"

pi@rpiGarageOpener:~/api $ cat close/get.txt
"description" : "close garage door"
pi@rpiGarageOpener:~/api $ cat os/get.json
"distro" : "string"

pi@rpiGarageOpener:~/api $ cat close/get.json
 pi@rpiGarageOpener:~/api $ nano close/get.json
pi@rpiGarageOpener:~/api $ cat close/get.json
"Close" : "Close garage door" 
pi@rpiGarageOpener:~/api $ cat os/get.json
"distro" : "string"

pi@rpiGarageOpener:~/api $ nano close/get.json
pi@rpiGarageOpener:~/api $ nano open/get.json
pi@rpiGarageOpener:~/api $ nano toggle/get.json
pi@rpiGarageOpener:~/api $ nano state/get.json
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  memory      os         restful_api      server          server.key  time
client.key  disk         get.json    get.txt       navigation  README.md  rest_server.log  server_cron.sh  state       toggle
close       favicon.png  get.py      junk          open        reboot     rest_server.py   server.crt      test        uptime
pi@rpiGarageOpener:~/api $ rm -r junk
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  navigation  README.md    rest_server.log  server_cron.sh  state  toggle
client.key  disk         get.json    get.txt       open        reboot       rest_server.py   server.crt      test   uptime
close       favicon.png  get.py      memory        os          restful_api  server           server.key      time
pi@rpiGarageOpener:~/api $ cat get.txt
"description" : "returns hostname"
pi@rpiGarageOpener:~/api $ cat get.backup
global Data
# returns hostanme of server
Data = {"hostname" : socket.gethostname()}
pi@rpiGarageOpener:~/api $ client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
ssh: connect to host rpigarageopener.local port 22: Connection refused
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener.local
ssh: connect to host rpigarageopener.local port 22: Connection refused
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ 
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener
pi@rpigarageopener's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Tue Dec 15 13:41:51 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  navigation  README.md    rest_server.log  server_cron.sh  state  toggle
client.key  disk         get.json    get.txt       open        reboot       rest_server.py   server.crt      test   uptime
close       favicon.png  get.py      memory        os          restful_api  server           server.key      time
pi@rpiGarageOpener:~/api $ ls cpu/
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ cat cpu/get.backup
global Data
# returns CPU stats
Data = {"cores" : str(psutil.cpu_count()), "frequency" : str(round(psutil.cpu_freq().max/1000,2)) + "GHz", "used" : str(psutil.cpu_percent()) + "%" }

pi@rpiGarageOpener:~/api $ rm cpu/get.backup
pi@rpiGarageOpener:~/api $ rm state/get.backup
rm: cannot remove 'state/get.backup': No such file or directory
pi@rpiGarageOpener:~/api $ ls state/
get.backup.sh  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ rm state/get.backup.sh
pi@rpiGarageOpener:~/api $ ls -l
total 148
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 close
drwxr-xr-x 2 pi pi  4096 Dec 15 18:06 cpu
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi  3119 Dec 12 12:44 getServer.sh
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 memory
drwxr-xr-x 2 pi pi  4096 Dec 14 21:34 navigation
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 open
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   954 Dec 14 21:35 rest_server.log
-rwxr-xr-x 1 pi pi 15852 Dec 12 11:58 rest_server.py
drwxr-xr-x 2 pi pi  4096 Dec  6 09:13 server
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 state
drwxr-xr-x 2 pi pi  4096 Dec 12 12:44 test
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 time
drwxr-xr-x 2 pi pi  4096 Dec 15 13:45 toggle
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 uptime
pi@rpiGarageOpener:~/api $ ls disk/
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ 
pi@rpiGarageOpener:~/api $ rm disk/get.backup
pi@rpiGarageOpener:~/api $ rm disk/memory.backup
rm: cannot remove 'disk/memory.backup': No such file or directory
pi@rpiGarageOpener:~/api $ rm memory/get.backup
pi@rpiGarageOpener:~/api $ rm navigation/get.backup
rm: cannot remove 'navigation/get.backup': No such file or directory
pi@rpiGarageOpener:~/api $ ls navigation
get.json  get.py  get.py~  junk.json
pi@rpiGarageOpener:~/api $ rm navigation/junk.json
pi@rpiGarageOpener:~/api $ ls -l
total 148
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 close
drwxr-xr-x 2 pi pi  4096 Dec 15 18:06 cpu
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi  3119 Dec 12 12:44 getServer.sh
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 memory
drwxr-xr-x 2 pi pi  4096 Dec 15 18:08 navigation
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 open
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   954 Dec 14 21:35 rest_server.log
-rwxr-xr-x 1 pi pi 15852 Dec 12 11:58 rest_server.py
drwxr-xr-x 2 pi pi  4096 Dec  6 09:13 server
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 state
drwxr-xr-x 2 pi pi  4096 Dec 12 12:44 test
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 time
drwxr-xr-x 2 pi pi  4096 Dec 15 13:45 toggle
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 uptime
pi@rpiGarageOpener:~/api $ rm open/get.backup
rm: cannot remove 'open/get.backup': No such file or directory
pi@rpiGarageOpener:~/api $ rm open/get.backup.sh
pi@rpiGarageOpener:~/api $ rm os/get.backup
pi@rpiGarageOpener:~/api $ rm reboot/get.backup
pi@rpiGarageOpener:~/api $ rm server/get.backup
rm: cannot remove 'server/get.backup': No such file or directory
pi@rpiGarageOpener:~/api $ rm state/get.backup
rm: cannot remove 'state/get.backup': No such file or directory
pi@rpiGarageOpener:~/api $ rm state/get.backup.sh
rm: cannot remove 'state/get.backup.sh': No such file or directory
pi@rpiGarageOpener:~/api $ ls server/
pi@rpiGarageOpener:~/api $ rmdir server
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  navigation  README.md    rest_server.log  server.crt  test    uptime
client.key  disk         get.json    get.txt       open        reboot       rest_server.py   server.key  time
close       favicon.png  get.py      memory        os          restful_api  server_cron.sh   state       toggle
pi@rpiGarageOpener:~/api $ ls -l
total 144
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 close
drwxr-xr-x 2 pi pi  4096 Dec 15 18:06 cpu
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi  3119 Dec 12 12:44 getServer.sh
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 memory
drwxr-xr-x 2 pi pi  4096 Dec 15 18:08 navigation
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 open
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   954 Dec 14 21:35 rest_server.log
-rwxr-xr-x 1 pi pi 15852 Dec 12 11:58 rest_server.py
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 state
drwxr-xr-x 2 pi pi  4096 Dec 12 12:44 test
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 time
drwxr-xr-x 2 pi pi  4096 Dec 15 13:45 toggle
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 uptime
pi@rpiGarageOpener:~/api $ ls state/
get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ ls test/
pi@rpiGarageOpener:~/api $ rmdir test
pi@rpiGarageOpener:~/api $ ls time/
get.backup  get.json  get.py  get.txt
pi@rpiGarageOpener:~/api $ rm time/get.backup
pi@rpiGarageOpener:~/api $ ls -l
total 140
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 close
drwxr-xr-x 2 pi pi  4096 Dec 15 18:06 cpu
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi  3119 Dec 12 12:44 getServer.sh
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 memory
drwxr-xr-x 2 pi pi  4096 Dec 15 18:08 navigation
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 open
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   954 Dec 14 21:35 rest_server.log
-rwxr-xr-x 1 pi pi 15852 Dec 12 11:58 rest_server.py
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 state
drwxr-xr-x 2 pi pi  4096 Dec 15 18:10 time
drwxr-xr-x 2 pi pi  4096 Dec 15 13:45 toggle
drwxr-xr-x 2 pi pi  4096 Dec  6 08:11 uptime
pi@rpiGarageOpener:~/api $ rm toggle/get.backup
rm: cannot remove 'toggle/get.backup': No such file or directory
pi@rpiGarageOpener:~/api $ rm toggle/get.backup.sh
pi@rpiGarageOpener:~/api $ rm uptime/get.backup
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.backup  getServer.sh  navigation  README.md    rest_server.log  server.crt  time
client.key  disk         get.json    get.txt       open        reboot       rest_server.py   server.key  toggle
close       favicon.png  get.py      memory        os          restful_api  server_cron.sh   state       uptime
pi@rpiGarageOpener:~/api $ ls -l
total 140
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 close
drwxr-xr-x 2 pi pi  4096 Dec 15 18:06 cpu
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.backup
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi  3119 Dec 12 12:44 getServer.sh
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 memory
drwxr-xr-x 2 pi pi  4096 Dec 15 18:08 navigation
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 open
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   954 Dec 14 21:35 rest_server.log
-rwxr-xr-x 1 pi pi 15852 Dec 12 11:58 rest_server.py
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 state
drwxr-xr-x 2 pi pi  4096 Dec 15 18:10 time
drwxr-xr-x 2 pi pi  4096 Dec 15 18:11 toggle
drwxr-xr-x 2 pi pi  4096 Dec 15 18:11 uptime
pi@rpiGarageOpener:~/api $ rm get.backup
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.json      get.txt     open       reboot           rest_server.py  server.key  toggle
client.key  disk         get.py        memory      os         restful_api      server_cron.sh  state       uptime
close       favicon.png  getServer.sh  navigation  README.md  rest_server.log  server.crt      time
pi@rpiGarageOpener:~/api $ ls -l
total 136
-rw-r--r-- 1 pi pi  2025 Dec  6 08:46 client.crt
-rw------- 1 pi pi  3272 Dec  6 08:45 client.key
drwxr-xr-x 2 pi pi  4096 Dec 15 13:44 close
drwxr-xr-x 2 pi pi  4096 Dec 15 18:06 cpu
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 disk
-rw-r--r-- 1 pi pi 23666 Dec  6 08:11 favicon.png
-rw-r--r-- 1 pi pi    22 Dec  6 08:11 get.json
-rw-r--r-- 1 pi pi    84 Dec  6 08:11 get.py
-rw-r--r-- 1 pi pi  3119 Dec 12 12:44 getServer.sh
-rw-r--r-- 1 pi pi    35 Dec  6 08:11 get.txt
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 memory
drwxr-xr-x 2 pi pi  4096 Dec 15 18:08 navigation
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 open
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 os
-rw-r--r-- 1 pi pi   272 Dec  6 08:11 README.md
drwxr-xr-x 2 pi pi  4096 Dec 15 18:09 reboot
drwxr-xr-x 3 pi pi  4096 Dec  6 09:12 restful_api
-rw-r--r-- 1 pi pi   954 Dec 14 21:35 rest_server.log
-rwxr-xr-x 1 pi pi 15852 Dec 12 11:58 rest_server.py
-rw-r--r-- 1 pi pi   327 Dec  6 08:11 server_cron.sh
-rw-r--r-- 1 pi pi  2025 Dec  6 08:43 server.crt
-rw------- 1 pi pi  3272 Dec  6 08:42 server.key
drwxr-xr-x 2 pi pi  4096 Dec 15 18:07 state
drwxr-xr-x 2 pi pi  4096 Dec 15 18:10 time
drwxr-xr-x 2 pi pi  4096 Dec 15 18:11 toggle
drwxr-xr-x 2 pi pi  4096 Dec 15 18:11 uptime
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.json      get.txt     open       reboot           rest_server.py  server.key  toggle
client.key  disk         get.py        memory      os         restful_api      server_cron.sh  state       uptime
close       favicon.png  getServer.sh  navigation  README.md  rest_server.log  server.crt      time
pi@rpiGarageOpener:~/api $ cd navigation
pi@rpiGarageOpener:~/api/navigation $ nano get.py
pi@rpiGarageOpener:~/api/navigation $ history | grep server
   59  history | grep server
   60  python3 rest_server.py
   64  python3 rest_server.py
   66  python3 rest_server.py
   67  sudo python3 rest_server.py
   68  sudo python rest_server.py
   69  sudo python3 rest_server.py
   72  sudo python3 rest_server.py
   76  nano rest_server.py
   78  nano rest_server.py
   79  sudo python3 rest_server.py -s
   80  sudo python3 rest_server.py 
   86  ls /usr/bin/rest_server.py
   87  ls -l /usr/bin/rest_server.py
   89  sudo nano /usr/bin/rest_server.py
   92  cat rest_server.log
   94  sudo nano /usr/bin/rest_server.py
  101  sudo nano /usr/bin/rest_server.py
  102  cat /home/pi/api/server_cron.sh
  105  cat rest_server.log
  113  sudo nano /usr/bin/rest_server.py &
  119  sudo nano /usr/bin/rest_server.py
  120  sudo python3 /usr/bin/rest_server.py &
  122  cat rest_server.log
  126  nano rest_server.py
  127  sudo python3 /usr/bin/rest_server.py 
  128  sudo python3 /usr/bin/rest_server.py -d
  129  sudo python3 /usr/bin/rest_server.py -h
  131  history | grep rest_server.py
  132  sudo nano /usr/bin/rest_server.py
  133  sudo nano rest_server.py
  134  sudo python3 rest_server.py -d
  136  sudo python3 rest_server.py &
  145  sudo python3 rest_server.py &
  159  ps -aux | grep rest_server
  164  ps -aux | grep rest_server
  167  ps -aux | grep rest_server
  171  sudo python3 rest_server.py &
  173  ps -aux | grep rest_server
  175  sudo python3 rest_server.py &
  180  ps -aux | grep rest_server
  182  ps -aux | grep rest_server
  184  ps -aux | grep rest_server
  185  python3 rest_server.py &
  186  ps -aux | grep rest_server
  188  python3 rest_server.py -p5070 &
  189  ps -aux | grep rest_server
  191  sudo python3 rest_server.py -p5070 &
  195  sudo python3 rest_server.py &
  212  ps -aux | grep rest_server
  214  ps -aux | grep rest_server
  215  nano rest_server.py
  216  python3 rest_server.py
  217  python3 rest_server.py -d
  218  nano rest_server.py
  219  python3 rest_server.py -d
  220  nano rest_server.py
  221  python3 rest_server.py -d
  222  nano rest_server.py
  223  python3 rest_server.py -d
  251  rm server/get.backup
  254  ls server/
  255  rmdir server
  275  history | grep server
pi@rpiGarageOpener:~/api/navigation $   217  
-bash: 217: command not found
pi@rpiGarageOpener:~/api/navigation $ python3 rest_server.py -d
python3: can't open file 'rest_server.py': [Errno 2] No such file or directory
pi@rpiGarageOpener:~/api/navigation $ cd..
-bash: cd..: command not found
pi@rpiGarageOpener:~/api/navigation $ cd ..
pi@rpiGarageOpener:~/api $ python3 rest_server.py -d
2020/12/15 18:38:52 - Starting REST server
2020/12/15 18:38:52 - Command line arguments:
2020/12/15 18:38:52 -   Input file  = 
2020/12/15 18:38:52 -   Log file = /home/pi/api/rest_server.log
2020/12/15 18:38:52 -   Port = 9443
2020/12/15 18:38:52 -   Use cert = False
2020/12/15 18:38:52 -   Use HTTPS = False
2020/12/15 18:38:52 -   Use multithreading = False

2020/12/15 18:38:52 - Web Server:
2020/12/15 18:38:52 -   Server name = rpiGarageOpener
2020/12/15 18:38:52 -   Local Server IP = 0.0.0.0
2020/12/15 18:38:52 -   Server IP = 192.168.1.227 

2020/12/15 18:38:52 -   No socket is required for HTTP?
2020/12/15 18:39:09 - GET /api/cpu HTTP/1.1
2020/12/15 18:39:09 - Client is: 192.168.1.139 39744
2020/12/15 18:39:09 - 192.168.1.139 39744
2020/12/15 18:39:09 - Client IP is valid: 192.168.1.139
192.168.1.139 - - [15/Dec/2020 18:39:09] "GET /api/cpu HTTP/1.1" 200 -
2020/12/15 18:39:09 - Execute command: /home/pi/api/cpu/get.py
2020/12/15 18:39:22 - GET /api/navigation HTTP/1.1
2020/12/15 18:39:22 - Client is: 192.168.1.139 39746
2020/12/15 18:39:22 - 192.168.1.139 39746
2020/12/15 18:39:22 - Client IP is valid: 192.168.1.139


data = { "directories" : [ {     "abs" : "/home/pi/api",     "verbs" : ["GET"],     "description" : "returns hostname"
,     "schema" : { "hostname" : "string"
}}, {     "abs" : "/home/pi/api/open",     "verbs" : ["GET"],     "description" : "open garage door"
,     "schema" : { "open" : "Open garage door" 
 
}}, {     "abs" : "/home/pi/api/time",     "verbs" : ["GET"],     "description" : "returns server date and time"

,     "schema" : { "date" : "string",
"time" : "string"

}}, {     "abs" : "/home/pi/api/uptime",     "verbs" : ["GET"],     "description" : "returns server uptime"
,     "schema" : { "days" : "string",
"hours" : "string",
"minutes" : "string",
"seconds" : "string"
}}, {     "abs" : "/home/pi/api/os",     "verbs" : ["GET"],     "description" : "returns operating system details"

,     "schema" : { "distro" : "string"

}}, {     "abs" : "/home/pi/api/restful_api",     "verbs" : [],     "description" : "returns operating system details"

,     "schema" : {}}, {     "abs" : "/home/pi/api/disk",     "verbs" : ["GET"],     "description" : "returns disk stats"
,     "schema" : { "total" : "string",
"used" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/reboot",     "verbs" : ["GET"],     "description" : "reboots server"

,     "schema" : { 
}}, {     "abs" : "/home/pi/api/toggle",     "verbs" : ["GET"],     "description" : "toggles garage door"
,     "schema" : { "toggle" : "Presses garage door remote" 
 
}}, {     "abs" : "/home/pi/api/navigation",     "verbs" : ["GET"],     ,     "schema" : { "abs" : "string",
"verbs" : "list",
"description" : "string",
"schema" : "dictionary"

}}, {     "abs" : "/home/pi/api/cpu",     "verbs" : ["GET"],     "description" : "returns server cpu details"
,     "schema" : { "cores" : "string",
"frequency" : "string",
"used" : "string"

}}, {     "abs" : "/home/pi/api/close",     "verbs" : ["GET"],     "description" : "close garage door"
,     "schema" : { "close" : "Close garage door"

}}, {     "abs" : "/home/pi/api/memory",     "verbs" : ["GET"],     "description" : "returns memory stats"
,     "schema" : { "total" : "string",
"used" : "string",
"available" : "string",
"free" : "string"
}}, {     "abs" : "/home/pi/api/state",     "verbs" : ["GET"],     "description" : "garage door state"
,     "schema" : { "state" : "Returns if garage door is opened or closed" 
 
}}] }
192.168.1.139 - - [15/Dec/2020 18:39:22] "GET /api/navigation HTTP/1.1" 200 -
2020/12/15 18:39:22 - Execute command: /home/pi/api/navigation/get.py
client_loop: send disconnect: Broken pipe
Jeffs-MBP:~ jeff$ ssh pi@rpiGarageOpener
pi@rpigarageopener's password: 
Linux rpiGarageOpener 5.4.72+ #1356 Thu Oct 22 13:56:00 BST 2020 armv6l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Tue Dec 15 18:05:34 2020 from 192.168.1.118
pi@rpiGarageOpener:~ $ cd api
pi@rpiGarageOpener:~/api $ ls
client.crt  cpu          get.json      get.txt     open       reboot           rest_server.py  server.key  toggle
client.key  disk         get.py        memory      os         restful_api      server_cron.sh  state       uptime
close       favicon.png  getServer.sh  navigation  README.md  rest_server.log  server.crt      time
pi@rpiGarageOpener:~/api $ cd navigration
-bash: cd: navigration: No such file or directory
pi@rpiGarageOpener:~/api $ cd navigation
pi@rpiGarageOpener:~/api/navigation $ nano get.py

  GNU nano 3.2                                                get.py                                                          

# returns navigation for API
global Data
global Path

validVerbs  = "get put delete post"
data = '{ "directories" : [ '
# ??? need to remove /navigation
next = False

# excluded_prefixes = ('__', '.')
for paths, dirs, files in os.walk(Path):
    # exclude hidden folders and special files starting with excluded_prefixes
    dirs[:] = [d for d in dirs if not d.startswith(".")]
    dirs[:] = [d for d in dirs if not d.startswith("__")]

    filenames = [f for f in files if not f.startswith(".")]
    filenames[:] = [f for f in files if not f.startswith("__")]

    if next:
        data += ', '

    schema = '"schema" : {}'
    verbs = '"verbs" : ['
    next_verb = False
    for f in filenames:
        if None != re.search('.py', f):
            verb = f[:len(f)-3]
            if validVerbs.find(verb) >= 0:
                if next_verb:
                    verbs += ', '
                file = paths + "/" + verb
                try:
                    # ??? how to get proper indentation
                    schema = '"schema" : { '
                    with open(file + ".json", "r") as read_file:
                        schema += read_file.read()
                        # ??? needs to read line at a time rather than the whole file
                    schema += '}'
                except:
                    schema = '"schema" : {}'

                try:
                    with open(file + ".txt", "r") as read_file:
                        description = read_file.read()
                except:
                    description = ''

                verb = verb.upper()
                verbs += '"' + verb + '"'
                next_verb = True

    verbs += '], '

    data += '{ '
    data += '    "abs" : "' + paths + '", '
    data += '    ' + verbs
    data += '    ' + description + ', '
    data += '    ' + schema
    data += '}'

    next = True

data += '] }'
print("\n\ndata = " + data)

Data = data
# Data = json.loads(data)

  
