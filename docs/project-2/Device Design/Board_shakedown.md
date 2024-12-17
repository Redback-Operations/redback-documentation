---
sidebar-position: 3
---

# Board Validation Testing

The Custom PCB was received from the factory at the end of Week 11 T2-24
Unfortunately this means that the Senior that designed the board had graduated from the project by the time it was being worked upon and he could not learn from the mistakes made on it. 

Here is an overview of the *quirks* of the device.

## 1. It will literally burn you 

In each example provided in [the datasheet of the TMP36](https://www.analog.com/media/en/technical-documentation/data-sheets/TMP35_36_37.pdf) a 100nF capacitor is placed in front of the V<sub>in</sub> pin.
![An extract of the sensor datasheet explaining why a capacitor is needed on the V in pin](./img/TMP36Cap_DS.png)

This was omitted from the PCB design
![The board schematic showing a the leads of the pin and no capacitor](./img/TMP36Schem.png)

I believe this is why after about 10 seconds of being plugged in, the sensor becomes untouchably hot. 
This may also be compounding some of the other issues below

## 2. No power over USB
The board is only able to receive power via the LiPo JST connectors. Therefore when attempting to verify that my bootloader burn worked I was a bit confused as to why after seemingly successfully completing it according to the terminal output, I saw no communication between Lachesis and my computer. After some time of steam coming out of my ears pop-eye style I remembered that in T2 I noticed that the board didn't have a charging circuit included for the LiPos to be able to charge over USB. We bought some tiny usb LiPo mediator chips from Core-Electronics to bodge it and I spent a considerable amount of time trying to hack it in but to no avail. 

Therefore, if you want to program the board, you need to be draining the battery. Or at least you would if it weren't for...

## 3. Serial Communications dies after roughly 3 minutes
I dont understand why but after performing the ritual to interface with the board, I found that I kept losing the COM port.
I did a few tests and found that it pretty consistently turns off after around 2 minutes and 45 seconds and if you do it in quick succession, the time before comms are lost is lessened. This leads me to believe that the heat from the temperature sensor (which is located next to the USB socket by the by) is increasing the resistance of the traces to the point where not enough current is available to maintain the connection. 

## 4. The processor is too weak and too expensive
It can barely run the display by itself. It will probably struggle trying to run both at the same time but when I went to test it I cracked the screen because it turns out the displays dont have caps at the end of the threads either. (I ordered replacements)

## Design Flaws.
These aren't necessarily deal breakers but they are still gripes
1. The wearable looks more like a house arrest ankle monitor than a smart watch
2. In an effort to minimise the ankle monitor vibe, I was trying to keep the case as compact as possible. However some layout decisions made that a fools errand, namely internal interfaces (the JST plugs to the batteries) share a wall with the small hardware switch which must be accessible to turn the board on. This means that unless the case sticks out a bit to provide a channel for the power cable to run through, the cables have to stick out the side and feed back into the watch. The edge with the push button and USB plug has the EXACT same issue. I tried to leave it with the librarian because I was working late to get it ready for innofes and didn't think I'd be able to wake up early enough to hand it to Manan and the librarian / security flat out refused because it "Looks sketchy as hell"


## Advice
If the opportunity for another hardware revision exists, use an off the shelf display + mcu. There are plenty of ESP32s with embedded displays and GPIO that will work fine, obviously the more powerful the processor the better considering there's a goal of putting AI into it. 
Custom PCB work should be limited to essentially making sensor 'shields' or even a couple of PCBS. This should also be done at the same time as the Case design so that one aspect can inform the other. 

And finally, get it checked by someone with experience manufacturing custom PCBs. The mechatronics course has a PCB Fab Lab which so far as I can tell doesn't have the capability to do custom SMT level boards but at least they'll be able to tell you if you've made an obvious mistake.


:::info
**Document Creation:** 15 December 2024. **Last Edited:** 15 December 2024. **Authors:** Lachlan Costigan
:::
