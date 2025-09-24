---
sidebar_position: 1
---

# Next-Gen Dotty Research

Where to next for BugBox

:::info
**Document Creation:** 28 July, 2024. **Last Edited:** 28 July, 2024. **Author:** Kaleb Bowen.
:::

## The Current Bot

In the existing configuration of the “Dotty” robot, the bot is powered by an Arduino Nano V3.0, supported by a custom PCB. This PCB enhances the user experience by embedding the motor drives directly and re-routing the pins of the board to logical spaces.

The grunt force behind the bot is two TT motors, running a dual shaft gearbox, and variable voltage up to 12 volts.
In terms of capabilities, the bot recovers code through a command line interface connected via Micro USB to the bot, powered by Amazon EC2 which is fed from the BugBox Playground learning environment.

Present expandability functions are rather limited both by the PCB layout and by the functionality of the Arduino Nano board. Beyond the core platform, the bot has the ability to expand to contain two ultrasonic sensors and two infrared sensors. These two sensors will be continuing into the thought process of the new model, and thus not discussed in the proposed new components.

## The Desired Outcome

Looking into the long-term, the ideal outcome for the bot is to have an established base bot that can be effortlessly modified using pre-defined “modules” that are integrated both with the physical bot and through the Playground environment. A refreshed Dotty will provide more opportunities for students to learn, across a larger number of auxiliary accessories to the device. In upgrading the device in this manner, so too will the price become modular, with schools being able to customise their purchasing to suit the current needs of the students, only buying what the accessories necessary to them. Expanding on this platform provides further growth in the BugBox curriculum, with the opportunity to grow challenges and tasks based off the functionality of extra modules. Building a solid foundation will also ensure that BugBox is sustainable into the future, with a modular build allowing for upgrading components with less waste when inevitable future iterations occur.

## Proposed Modules

### Sound Module

Combining a small form factor microphone and speaker, Dotty would gain an enormous amount of functionality at a relatively low-cost and size. This dynamic duo would engage students through the following abilities:

-	Function to program sound effects to play back on the device, such as when running into objects and being responsive to objects through the two sensor modules.
-	Using a combination of the microphone and quick swivel movements to recognise the location of where sound comes from.
-	In a more advanced option, the implementation of basic voice commands could be added.

### Button Module

Adding a small panel of tactile buttons to the top of the bot will add physical controls to the device. This addition could relay with the Playground to act as a trigger of sorts, with each button assigned to a group of blocks created by the user. Use cases could include:

-	Buttons to control the direction and speed of Dotty.
-	A soundboard.
-	Quick switching between different scripts.

### Light / Display Module

Another responsive and useful addition would be through various types of light and display modules, which could be used through progression, moving up complexity of the module, such as:

-	Single LCDs
-	LCD panel
-	OLED display
-	Touch-screen display
-	E-ink display

These affordable options add another versatile learning experience, through the ability to program different light sequences and light displays. The more complex displays could be turned into fun displays such as a programmable “face” for the Dotty bot, which could be programmed by students to respond to events, potentially through gathered events of other sensors. A touch screen sensor could add even more reactivity to this, creating an interactive screen option, or working like the button module to deliver responsive feedback guided movements.

### Inertia Module

Likely suited for the older side of BugBox’s demographic, an inertia module would provide useful statistics to the user. An inertia module would allow the bot to detect its speed, direction, and rotation status. This data could in-turn be used to provide feedback for other sensors, or simply returned to the user in order to complete assigned tasks.

### Battery Module

Albeit not an upgrade for the users, one upgrade to the bot itself that would improve overall functionality would be the addition of a LiPo battery pack. The full functionality of this addition would be enabled through either sourcing or creating a separate component that is capable of transmitting power to the battery pack, and data to the device, all though one single connection. Given the small battery usage of the device, it is likely that the short time Dotty is connected to the computer to get code would be enough to recharge any drained battery. LiPo batteries are also relatively cheap and have a greater capacity over alkaline batteries.

## Standard Connection / Ease-Of-Use

In order to fully utilise this new modular design, the bot will need the implementation of several standardised connections that work with all modules. To ensure cheap manufacturing and easy use for students, the easiest implementation of this of this may be through having several “patches” of either female or male pins in several key locations on the board, that has the minimal number of pins required to sufficiently run all the components. This would likely need research in trimester three by someone with PCB and IoT knowledge to fully maximise the design.

## Board Improvements

The current board, an Arduino Nano, is likely not able to power or handle the data flow of several of these new modules. In researching this topic, many non-Arduino boards appear to be the best options. This however may not be the best option, as the current Playground environment has the avrgirl-arduino package as an integral part of the program, handling all code deployments to Dotty. By switching to a non-Arduino board, this would also require a full rebuild of the backend, potentially meaning BugBox would have to develop their own solution to meet the needs of the particular board.

So considering this, the Arduino Mega may be the best option going forward. It offers significantly more memory (30kB vs 248kB when removing bootloader usage) which is likely needed for the display and sound modules, nearly three times as many pins, and four serial ports which could be used for the modules. 

The Mega does come with a substantial price increase over the Nano, however for the longevity of the device, this price could be justified. The older Nano and PCBs could still be used in basic classes to avoid waste. 

