# Blinky McBlinkster

A project to drive ws2811 LED strings with python and raspberry PI

Notes:
- following instructions found [here](https://learn.adafruit.com/neopixels-on-raspberry-pi/overview)
- don't forget to turn the audio off as mentioned [here](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage). 


```
Sound must be disabled to use GPIO18. This can be done in /boot/config.txt by changing "dtparam=audio=on" to "dtparam=audio=off" and rebooting. Failing to do so can result in a segmentation fault.
```

Hardware:
- [Raspberry Pi Zero W](https://www.amazon.com/gp/product/B06XFZC3BX/ref=ppx_yo_dt_b_asin_title_o05_s01?ie=UTF8&psc=1)
- [connectors](https://www.amazon.com/gp/product/B083GQPM3G/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
- [the string lights](https://www.amazon.com/gp/product/B06XSFT1VK/ref=ppx_yo_dt_b_asin_image_o06_s00?ie=UTF8&psc=1)
- [a power supply](https://www.amazon.com/gp/product/B06XJVYDDW/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)

# PI run on boot

```bash
sudo su
cp blinky.service /etc/systemd/system/
sudo systemctl start blinky
sudo systemctl stop blinky
sudo systemctl enable blinky
```
