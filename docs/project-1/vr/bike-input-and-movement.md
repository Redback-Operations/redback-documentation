---
sidebar_position: 8
---

#  Unity Bike Movement System


| Script Name               | Responsibility                                                          |
| ------------------------- | ----------------------------------------------------------------------- |
| `PlayerController`        | Entry point that assigns input and movement handlers to the active bike |
| `IBikeMover`              | Interface to abstract bike movement logic                               |
| `IPlayerInput`            | Interface to abstract input source (Axis, XR, MQTT)                     |
| `SimpleBikeController`    | Arcade-style simplified bike movement                                   |
| `RealisticBikeController` | Physics-based realistic bike movement and balance                       |
| `AxisInput`               | Uses Unity Input (keyboard/controller)                                  |
| `MQTTInput`               | Uses MQTT topics to get steering and speed                              |
| `XRInput`                 | Uses XR controller joystick axis for input                              |

###  `PlayerController`

* Selects and initializes the appropriate movement controller (`IBikeMover`)
* Dynamically chooses the input handler (`IPlayerInput`) based on:

  * MQTT connection
  * XR controller detection
  * Fallback to keyboard
* Passes input values to the active `IBikeMover` in `FixedUpdate()`
* Handles score collection through `OnTriggerEnter`
* Exposes `SetSpeed()` and `GetSpeed()` for runtime tuning

---

###  `IBikeMover` Interface

Defines the API for movement components:

```csharp
float Speed { get; set; }
void Init(GameObject controller);
void HanldeInput(Vector2 direction);
```

###  `IPlayerInput` Interface

Defines how directional input is gathered. All implementations return a `Vector2`:

* `x`: Horizontal steering
* `y`: Forward/backward movement

---

###  `SimpleBikeController`

Arcade-style bike movement:

* No physics (rigidbody is kinematic)
* Manual rotation and translation based on direction
* Rotates wheels visually
* Aligns bike to terrain normal for realism

Best for: simple mobile control, joystick or keyboard input.

---

###  `RealisticBikeController`
Physics-based bike system:

* Controls motor torque, braking, and steering via `WheelColliders`
* Computes steering angle reduction at higher speeds
* Uses `AnimationCurve` to simulate self-balancing (torque applied against tilt)
* Leaning is computed and visualized
* Syncs visual wheel rotation with physics colliders

Best for: immersive VR, realistic terrain, and learning physics principles.

---

###  `AxisInput`

* Uses Unity's built-in `Input.GetAxis("Horizontal"/"Vertical")`
* Best for development/testing or traditional control schemes

---

###  `MQTTInput`

* Subscribes to MQTT topics for:

  * Speed control
  * Left/right turns
* Parses JSON-encoded speed data
* Designed for hardware integration or IoT-enabled exercise bikes

---

###  `XRInput`

* Uses `XR.InputDevices` to read joystick direction from hand-held controllers
* Ideal for VR motion controllers

---

##  Data Flow Summary

### Initialization

1. `PlayerController` checks input method and selects `IPlayerInput`.
2. Retrieves or overrides the movement handler (`IBikeMover`) based on preferences.
3. Calls `Init()` to link the movement handler with the current bike model.

### Runtime Loop

* `FixedUpdate()`:

  * Gets input via `IPlayerInput.GetDirection()`
  * Passes input to `IBikeMover.HanldeInput()`
  * Movement logic is executed (e.g., wheel torque, transform rotation)
