# Rotary-Crystallizer

A Modern Holden style Rotary Crystallizer, using off the shelf parts (apart from PCB), capable of growing large optically clear crystals of Potassium DiHydrogen Phosphate (KDP) in just 7 days!
![screenshot](media/xtal.png)

## Theory

Quanitities and Graphs
![screenshot](graphs/sol1.PNG)

Above is solubility data derived from data at https://www.sigmaaldrich.com/GB/en/support/calculators-and-apps/solubility-table-compounds-water-temperature


![screenshot](graphs/sol2.PNG)

Above: Solubilty curve assuming 450ml of solvent.

![screenshot](graphs/sol3.PNG)

Above: Projected crystal mass for a 10C temperature drop.

![screenshot](graphs/sol4.PNG)

Initial start temperature of 47C. This is 0.9C below the saturation point, giving an intitial supersaturation of 1.5%

![screenshot](graphs/sol5.PNG)

At 44.5C the projected supersaturation is about 7%. This does not take into account crystal growth in this period, and is likely closer to 6% during a growth cycle. This puts the supersaturation level in te fast growth regime.

![screenshot](graphs/updated-curve.png)

## Hardware

BOM 

### LightBurn Files

![screenshot](lightburn/lightburn.png)

## PCB Design

![screenshot](pcb/pcbimg.png)

TODO:
0.96" OLED SSD1306
The hole spacing for the OLED needs attending to! Seemingly different manufacturers have different hole spacings, mechanical drawings are thin on the ground CHECK the measurements for your OLED and edit the PCB to suit before sending files off for Manufacture!!!
Future versions will simply omit the holes. Honestly you might be better off mouting with double sided foam pads and soldering direct to the board.
I2C breakout is planned in version 2 for TMP117 sensors and expandability.


![screenshot](pcb/3dpcbimg.png)

## Arduino code

## Python Data Processing

![screenshot](graphs/example-run.png)
![screenshot](graphs/example-oscillation.png)
![screenshot](graphs/example-error.png)




