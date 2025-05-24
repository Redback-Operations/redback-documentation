---
sidebar_position: 2
---

# 3D Solar System Planet Match Game

:::info
By **Parami Liyanage**
:::

The Planet Match Game challenges players to drag and drop planet names onto the correct planet in the 3D solar system. When a planet is labeled to the right planet, the label disappears, and the planet name appears on the planet. Once all labels are correctly matched, a success message is displayed and the planets begin orbiting the Sun.

![3d-solar-system](img\3d-solar-system.png) 

--- 

## Features

- **Interactive 3D View:**
    -  Pinch or scroll to zoom and click-and-drag to pan around the system.
- **3D visualization of the full solar system with:**
  - The Sun and all 8 planets
  - Orbit rings with animation
  - Planetary textures
  - Ambient stars and lighting
- **Drag and Drop:** Matching Drag-and-drop labels to match planet names
- **Visual feedback**
    - Pop up error modal for incorrect matches
    - Pop up modal when game complete
- **Animations**
    - Planetary motion (orbits) after game is completed
    - Twinkling starfield
- **Reset and navigation options**



## Packages & Libraries 

- **@react-three/fiber** for 3D rendering
- **@react-three/drei** (for controls, stars, environment, HTML overlays)
- **react-dnd** (for drag-and-drop interaction)
- **react-spring** (for smooth animations)
- **bootstrap**	(UI library)
- **react-router-dom**	(Page navigation)


## Game Components

- Planet: 3D mesh of a textured sphere with a drop zone
- DraggableLabel: React DnD label for dragging planet names
- OrbitRing: Visual animated orbit ring for each planet
- OrbitingPlanet: Animates orbiting planets on win
- Sun: Glowing sphere with optional light
- Stars, Lights: Background effects and global illumination



## 🎮 How to Play

1. Drag a label planet name from the top UI bar.
2. Drop it onto the correct planet in the solar system.
3. If correct, the label locks in planet.
4. If incorrect, an error modal pops up.
5. Once all planets are matched correctly:
   - A success message overlay is shown.
   - Planets begin orbiting the sun.
   - Playground navigation button appears.

:::note
Game can be accessed through `/planet-match-game` as mini login game is set as default currently. To use this game as the default login game, change in `Router.tsx`
::::

| Incorrect Match | Correct Match | Game complete |
| ---- | ---- | ---- |
| ![error_message](img\error_message.png)  | ![game_complete_message](img\game_complete_message.png)  | ![complete](img\complete.png) |


## Notes
#### Further improvements

- Lighting: Add backlighting and adjustable light angles to reduce shadows and better showcase planet textures on all sides.
- Textures: Improve visual by including higher-quality or generated mesh textures. The Sun is rendered as a non-light-emitting object but this can be adjusted by swapping textures.
- Adjust camera angles



After completing the game, to login to playground make sure bugbox backend app is running as well.
:::danger[Important:]
For future development if drag and drop functionality is needed using **react-dnd**, we can just simply add this element as a child in the router.
**see `Router.tsx` in Playground repository**
:::

