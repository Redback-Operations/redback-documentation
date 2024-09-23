---
sidebar_position: 2
---
# Software Requirements Specification

## 1. Introduction

The SmartBike VR project aims for gamification exercise at the comfort of one’s home with a prepared built-in bicycle and a VR headset ready for the user to explore around many scenes one cannot otherwise see or experience as someone who might prefer the indoors over the outdoors. It is a combination of VR and IoT mixing virtual reality and hardware added to the physical bike for a fun filled adventure for the sake of exercise to a physically fit body.

The purposes of the project would be for students to work on both VR and IoT aspects of the bike, be it Unity for making gamified exercises through fun missions, design by Blender to create wondrous scenes into the Unity project that people can see real time by a VR headset and working on the bike itself to connect the Unity project to the physical bike so gamified exercise on screen can be felt through the body.

Students interested in Unity, with good understanding of C# coding by various units such as SIT232 can start upskilling and start making wondrous missions and gimmicks for the bike and scenes to motivate users for exercise.

## 2. Intended Audience

The intended audience for SmartBike VR is diverse, catering to a range of demographics and interests. At its core, the game appeals to fitness enthusiasts and cycling fans who are looking for a fun, interactive way to stay active, regardless of weather conditions. The platform provides an alternative for those who may face outdoor challenges, such as older individuals who find it difficult to go outside or those who are unable to exercise due to environmental limitations.

The game also targets people who struggle with motivation, offering an engaging experience through gamified fitness, multiplayer interactions, and real-time progress tracking. Social riders who enjoy community-based fitness can benefit from the cooperative challenges and group rides, while gamers are drawn in by the competitive elements, smooth multiplayer gameplay, and immersive VR experience.

In addition, companies looking for innovative wellness activities can adopt the game to promote employee fitness, teamwork, and social interaction. Tech enthusiasts, drawn by the integration of VR, real-time multiplayer capabilities, and advanced fitness tracking, will also find appeal in the game's cutting-edge features. With a broad target audience ranging from ages 13 and up, the game creates opportunities for players of different backgrounds to participate in a unique and engaging fitness experience.

## 3. Intended Use

SmartBike VR is designed with versatility and broad appeal in mind, offering numerous practical applications. One of its primary uses is to promote physical activity, particularly for individuals who may struggle with motivation or face other barriers to regular exercise. Additionally, the game serves as a tool for rehabilitation and therapy, providing patients with a safe and engaging way to regain strength and mobility through guided cycling routines.

Beyond its fitness benefits, the game offers entertainment and leisure for casual users and competitive gaming opportunities for those who enjoy the challenge of head-to-head races or virtual events. Virtual tourism allows players to explore new environments and landscapes, making cycling a visually enriching experience. It also supports training and skill development, allowing users to enhance their cycling performance or technique in a controlled, virtual setting.

To ensure accessibility, the game is designed to function on most VR headsets, making it available to a wide audience. The multiplayer feature enables users to connect and ride with friends, fostering social interaction. Player scores and preferences are tied to accounts, allowing seamless transitions between systems. For those who may find wearing a VR headset for long periods fatiguing, a non-VR mode ensures that the game remains accessible and enjoyable without the need for virtual reality.

## 4. Competitors

There are several competitors to SmartBike VR, each offering different approaches to virtual cycling, fitness, and gaming experiences. Here’s a list of some key competitors:

1. **Zwift**  
    Zwift is one of the most popular virtual cycling platforms, combining video game elements with structured workouts and live races. Riders can cycle through virtual worlds, train, and compete with others globally.
2. **Rouvy**  
    Rouvy focuses on augmented reality cycling, where real-world routes are overlaid with virtual elements. It provides realistic road simulations, allowing cyclists to experience global routes from home.
3. **Bkool**  
    Bkool offers a range of virtual cycling experiences, including real-world video simulations and 3D virtual routes. It also features a social aspect with multiplayer races and group rides.
4. **Wahoo RGT (Road Grand Tours)**  
    Wahoo RGT offers virtual cycling with an emphasis on real-world physics and competitive group riding. It provides structured training plans, simulated races, and group rides with realistic terrains and dynamics.
5. **FulGaz**  
    FulGaz delivers high-quality, real-world video footage of famous cycling routes. The app adjusts difficulty based on actual terrain and user power, offering a realistic training experience.
6. **Peloton (Digital App)**  
    While primarily known for its indoor bike and fitness classes, Peloton offers virtual cycling workouts and live classes via their app, focusing on guided workouts, motivation, and community interaction.
7. **VZfit**  
    VZfit uses the Oculus VR platform to provide immersive cycling experiences. Users can ride through various environments and fitness challenges using VR, offering both exercise and entertainment.
8. **Expresso Bike**  
    Expresso offers interactive virtual cycling through stationary bikes equipped with screens. Riders can choose different courses and compete against others in live competitions.
9. **TrainerRoad**  
    TrainerRoad focuses on structured cycling workouts and performance improvement through data-driven training plans, though it lacks the more immersive virtual worlds of other platforms.
10. **Kinomap**  
    Kinomap uses real-world video routes where users can ride along virtually while cycling on a stationary trainer. It also includes multiplayer challenges, competitions, and real-time performance tracking.

These competitors each offer unique features, from competitive racing environments to guided workouts, making the virtual cycling and fitness space highly dynamic and varied.

## 5. Scope

This trimester we will endeavor to work on the missions in VR Unity project, fixing up a mission board using MissionActivator code left in the previous trimester to store mission code and select on missions for user to play smoothly. New missions have been created, making sure they are gamified as the focus of the SmartBike project is to exercise and not to play games focused on the city scene as the only scene ready and working currently in the VR project.

Next trimester, the company intends to move missions to new scenes such as the terrain scene or work on missions that are required in scenes other than the city scene such as ‘Escape The Flood’ mission. Leftover missions in the Planner board, left at ongoing, could be updated once new terrains are made for more suitable places. However, thanks to the latest overhaul in the Unity project as nice as it is to have a loading screen and spawning points, the missions can no longer access the UI and print out any statuses or objectives which should be analyzed and fixed immediately before contuining onto other missions.

## 6. Overall Description

### 6.1. User Needs

The following users we need to cater for the Smart Bike project would be VR enthusiasts with concerns for physical fitness and desire more motivation to become fit even though they do not like going out to exercise and prefer to stay at home.

Cycling enthusiasts do not always have time for long bike rides due to work responsibilities so they would want to cycle at home while collecting health data and exercise while hopping off when needed, ideally with a timed settable workout where user can set the amount of time they wish to ride.

Medical students might be interested in the bike project as users who want to keep a record of their own workout data to have a wholistic record of themselves when adding it to their health/medical records.

Game developers might be interested in the VR part of the smart bike project through branching out into more interesting experiences concerning games and gamified experiences that the smart bike provides through its mission and may contribute something more life changing to end users than just a recreational game. Developers would like to educate, train, motivate and encourage improvement of life through their skillset.

For the smart bike, users who wear glasses and get motion sickness would like to be able to experience the wonders of the project without falling sick so a headset off mode would be ideal especially as they would prefer to be immersed as possible with sound effects and background music / ambiance and interactions as examples.

Users would like to stay log in for the project instead of re-login manually every time the mobile app version of the project is reopened. For non-technical users, they want to be able to plug and play the bike without having to configure anything or setup the Wifi.

### 6.2. Assumptions / Dependencies

Development and design require the following applications:

- Windows / Mac / Linux PC
- Unity LTS v2022.3.22 (for VR application)
- Blender 4.2 / Autodesk 3ds Max / Autodesk Maya (for 3D modelling)
- Visual Studio / VSCode / JetBrains Rider / MonoDevelop

To play the game, the following requirements must be met:

- Windows PC and/or Meta Quest 2/3 headset
- Wahoo KICKR Core
- Raspberry Pi device with MQTT system installed

A completed build will be created at the end of each trimester of work through the Unity project:

- Build an Android APK, named SmartBike-VR-YEAR-T#-Meta-Quest.apk
- Build a Windows build, zip the file and name is SmartBike-VR-YEAR-T#-Windows.zip

### 6.3. UI/UX considerations

#### 6.3.1. User Interface Design Guidelines for Mobile

TODO  

#### 6.3.2. User Interface Design Guidelines for Unity

##### 6.3.2.1. Immersive Interaction Design

Natural Input Methods

Utilize VR-specific input methods, such as motion controllers and gaze-based interactions. Design UI elements that respond intuitively to hand gestures, pointing, and controller inputs to enhance immersion.

Haptic Feedback

Incorporate haptic feedback for interactive elements to provide physical sensations, reinforcing user actions and enhancing engagement. Use vibrations or tactile responses to confirm selections or interactions.

##### 6.3.2.2. Spatial UI Layout

3D Spatial Arrangement3D

Position UI elements in 3D space rather than on a flat plane. Use floating panels or contextual menus that the user can reach easily without breaking immersion. Ensure that UI is always within the user's field of view.

Depth and Scaling

Adjust the size and depth of UI elements according to their importance. Make frequently used elements larger and within easy reach, while less critical elements can be smaller or placed farther away.

##### 6.3.2.3. Visual Clarity and Readability

High Contrast Text

Use high-contrast colors between text and backgrounds to improve readability in various lighting conditions. Ensure that font sizes are large enough to be easily readable from a distance.

Simple and Bold Fonts

Opt for clear, bold typography that is legible in 3D space. Avoid overly stylized fonts that may hinder readability, especially in fast-paced environments.

##### 6.3.2.4. Consistent Visual Language

Unified Design Elements

Maintain a consistent visual style throughout the UI, including colors, shapes, and iconography. This helps users quickly understand interactions and navigate the interface.

Feedback and States

Provide visual feedback for different states (hover, selected, disabled) through color changes, animations, or outlines. This informs users about the current state of UI elements.

##### 6.3.2.5. User-Centric Navigation

Intuitive Navigation Patterns

Design navigation to feel intuitive and natural. Use gaze-based selections or raycasting to allow users to easily select and interact with UI elements without complicated gestures.

Guided Tutorials

Implement onboarding tutorials that guide users through the interface and controls. Use visual cues and prompts to help users learn interactions without overwhelming them.

##### 6.3.2.6. Contextual UI

Dynamic UI Elements

Create context-sensitive UI that adapts based on user actions or environmental changes. For example, show inventory items when a user reaches for their backpack or display relevant information when looking at an object.

Minimize Clutter

Keep the UI minimal and relevant. Avoid overwhelming users with too much information at once; prioritize essential functions and hide less important elements until needed.

#### 6.3.3. User Experience Guidelines for Blender Navigation

##### 6.3.3.1. Consistent Navigation Controls

Maintain consistency with navigation controls across different modes (Object Mode, Edit Mode, Sculpt Mode) so users don’t have to relearn movements or shortcuts. Know how to navigate through Blender’s 3D viewport, outliner, Properties panel and understand the different workplaces (Modelling, Sculpting, UV Editing, etc.)

- Optimal Viewport Shading: For a better visualization of objects, inform users about different viewport shading modes (Wireframe, Solid, Material Preview, Rendered) and how each is used for specific tasks.
- Performance Considerations: Users should know how to toggle off unnecessary layers, objects, or heavy textures when performance slows down, especially in complex scenes.
- Intuitive Camera Controls: Ensure that camera angles and positions are easy to adjust. Teaching users about hotkeys like "Shift + Middle Mouse Button" for panning and "Scroll Wheel" for zooming can significantly improve navigation in the 3D viewport.
- Custom Layouts: Blender allows custom workspace layouts for different stages of the project (e.g., modeling, texturing, animation). UI/UX contributors should create or suggest layouts that make navigation and tool access easier depending on the task at hand.
- Orthographic vs. Perspective Views: Guiding users to switch between orthographic and perspective views ("NumPad 5" key) helps with precision when modeling or aligning objects. Default setups should make this accessible.

##### 6.3.3.2. Snapping and Precision Tools

- Snapping Options: Snapping tools ("Shift + Tab" to toggle snapping) are crucial for precise alignment, especially when working with grids or when multiple objects need to align perfectly.
- Transform Constraints: Users should be encouraged to use axis constraints (press "X", "Y", or "Z" after a transformation command like grab, scale, or rotate) for more precise movement along one axis.
- Measurement Tools: Teaching users how to access the ruler tool ("N" key for the side panel to toggle) or to enable edge lengths for more accurate modeling is helpful for UI/UX clarity.

##### 6.3.3.3. Shortcut Hints

Familiarity with shortcut hints for key actions in pop up menus and on hover tooltips will promote efficient workflow

- Hotkey Familiarity: Ensure that users are familiar with common Blender shortcuts like "G" for Grab, "R" for Rotate, and "S" for Scale. Well-documented hotkeys save time and improve workflow.
- Custom Key Mapping: If a user prefers different shortcuts or workflows, Blender allows custom key maps. Ensure there’s documentation on how to modify these settings for a more personalized user experience.

##### 6.3.3.4. Undo System

Ensure a robust undo/redo system is in place for all object and mesh modifications. Users should have back up folders, so they are able to navigate their modeling history without losing progress.

##### 6.3.3.5. Efficient Use of the Outliner

- Outliner Navigation: The outliner is a vital tool for tracking all objects in the scene. Educate users on grouping objects and managing visibility via the outliner, making it easier to organize large scenes.
- Colour Coding and Layer Management: Encourage using Blender's color tagging feature for collections or objects, allowing users to visually organize their projects more efficiently.

##### 6.3.3.6. Organized Naming Conventions and Hierarchies

- Objects: All objects in the scene should be given clear and descriptive names (e.g., "Table_Leg" instead of "Cube.001"). This improves both the user experience and collaboration, especially on larger projects.
- Materials: Proper naming of materials (e.g., "Wood_Texture" instead of "Material.001") helps users easily identify and apply the correct textures.

##### 6.3.3.7. Folders and Collections

Organizing objects into Collections (Blender’s way of grouping objects) and naming them appropriately ensures that the scene is easy to navigate. For example, a collection named "Furniture" could group all furniture objects, making it easier for users to hide, show, or edit entire groups of assets quickly.

- Consistency: Consistent naming schemes across the entire project help users quickly understand how assets are structured, which is key for efficient workflows.

## 7. System Features and Requirements

### 7.1. Functional Requirements

For the SmartBike Project, students focusing on the VR Unity project must abide by the guideline while creating and pushing the code into GitHub:

- Before uploading anything into the project, make sure that the latest project is pulled from the GitHub before adding, committing and finally pushing anything into the GitHub to be contributed.
- As long as there is progress, run through it with the leader and project tutor to make sure it is fine to push the work into the project as it can be better to push what has already been done immediately than finishing it and pushing a bulk into the project that might be too much for a push.
- When creating mission code, create an empty object and place the code inside. For the mission to activate, place the empty object in Objectives>Missions (seen in CityScene) where there is MissionActivator script to add missions in a list as empty objects.
- Do not add mission code on bike even for testing purposes, as it will interfere with other missions and mission code needs to be tested within mission activator to know it will work there.

For the Smartbike mobile app project, students must abide to following guidelines:

- Make sure to always update your IDEs (android studio, Xcode, etc.) to the latest version before working.
- Make sure the fork your work from main repository and synchronize it with main mobile repository before working on any new tasks.
- Make sure to format code changes correctly. If your IDE (Likely VS Code) has its own formatting that is altering unchanged file, make sure to only commit files that you worked on.
- If making changes to the API, make sure that the changes do not break anything. If the changes must be made, update the readme, and inform team members of breaking changes.
- The VR workout is integrated to MQTT protocol to send data from bike. To run it properly, the server must send necessary data with correct connection information. This is not readily available so you might need to adjust the connection information yourself to test during development (Hive MQ is a common tool we use). Most of the necessary test codes are already present in the application.
- The user should be able to login, signup, edit profile and add workout stats in the application.

### 7.2. External Interface Requirements

The spectator or non-VR mode uses a Windows PC with a full screen application that uses a 16:9 resolution. This is based on the standard Full High-Definition (FHD) resolution of 1920x1080. The screen needs to be connected to the PC on display port 1, or the primary display and will allow the player to experience the game on a TV or computer screen, such as a laptop device, or when in simultaneous viewing the player in a VR headset allowing spectators to see the world that the player is exploring.

### 7.3. System Features

The virtual cycling game offers a wide range of system features designed to provide a comprehensive and engaging user experience:

- **Real-time Multiplayer:**  
    Powered by Photon Fusion, the game ensures smooth, low-latency multiplayer interactions, allowing players to join virtual events, races, or group rides.
- **Synchronized Views:**  
    Players in VR experience immersive first-person perspectives, while external monitors display alternative views, cycling stats, and race progress, making it suitable for spectators.
- **Performance Tracking:**  
    The game tracks detailed metrics like time, distance, speed, calories burned, and player positions, providing real-time feedback and rankings.
- **Cooperative Challenges:**  
    Players can participate in team-based activities like endurance rides or obstacle courses, promoting teamwork and social interaction.
- **Cross-platform Compatibility:**  
    The game is designed to run on most VR headsets, ensuring broad accessibility, and includes a non-VR mode for those who prefer traditional gaming without wearing a headset.
- **Account Syncing:**  
    Player scores, progress, and preferences are tied to user accounts, allowing seamless transitions between devices and preserving personal settings.
- **Virtual Tourism:**  
    Players can explore virtual landscapes and real-world routes, offering an immersive experience beyond typical fitness apps.
- **Competitive and Casual Modes:**  
    The system caters to both competitive gaming through races and leaderboards, as well as casual riders seeking leisure or structured fitness sessions.
- **Rehabilitation and Therapy Support:**  
    The game can be used as a tool for physical rehabilitation, providing controlled cycling exercises to aid recovery.

These features combine to create a dynamic system that appeals to fitness enthusiasts, social gamers, and anyone looking for a fun and interactive way to exercise.

## 8. Non-Functional Requirements

1. **Visual Aesthetic:**  
    The game must adhere to an art style that is 80% realism and 20% cartoon, creating a visually appealing yet approachable experience. All assets and images must reflect this aesthetic balance. For reference, developers and designers should consult the Asset Handbook (URL HERE). This ensures that the look and feel of the game is consistent across all environments, characters, and objects.
2. **Documentation and Educational Materials:**  
    Comprehensive "how-to-build" documentation must be provided for the development process, aimed at future developers, particularly students. This documentation should include detailed steps, screenshots, and/or video explanations, enabling others to recreate the game from scratch. The materials should be clear, beginner-friendly, and outline the process in a structured manner, allowing learners to build their own custom games. The guides should emphasize the development of similar 2D or 3D games using the provided assets, with instructions designed for users with minimal programming experience.
3. **Asset and Documentation Accessibility:**  
    All visual assets and reference documents, including the Asset Handbook and development guides, must be easily accessible through the company’s internal documentation system. This ensures that future developers have quick access to necessary resources when expanding or customizing the game.
4. **Compatibility and Scalability:**  
    The game must be scalable to work on a wide range of VR headsets while maintaining performance. The non-VR version must also ensure compatibility with a variety of screen sizes and input devices, without compromising the core aesthetic or functionality.

## 9. Definitions and Acronyms

- PR = pull request
- QA = Quality Assurance
- SRS = Software Requirements Specification
- 2D = Two Dimensional
- RPi = Raspberry pi
- API = Application Programming Interface
- VR = Virtual Reality