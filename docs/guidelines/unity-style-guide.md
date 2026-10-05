---
sidebar_position: 1
---

# Unity Development Style Guide

:::info
**Document Creation:** 4 October, 2026. **Last Edited:** 4 October, 2026. **Authors:** VR Team.
<br></br> **Document Code:** DOC-VR-GUI-001. **Effective Date:** 4 October, 2026. **Expiry Date:** 4 October, 2027.
:::

## 1. Overview

This guide outlines the standard conventions for C# coding, asset naming, and project structure within the Redback SmartBike VR Unity project. Adhering to these guidelines ensures maintainability, readability, and consistency across the codebase.

- **Target Environment:** Unity 2022.3.22 (URP), Meta Quest 2/3

## 2. Project Structure & Asset Locations

To keep the project clean, all assets must be placed in their respective folders under the `Assets/` directory. If a feature has great complexity, create a sub-folder within these main directories.

- **Animations:** Unity-based animations linked to models (excluding those embedded in FBX/OBJ).
- **Audio:** Music or sound effects.
- **Materials:** Imported or created materials. (Ensure they are URP-based to prevent pink rendering).
- **Models:** Imported geometry (FBX/OBJ) rendered in the virtual world.
- **Packages:** Large packages that come as single units.
- **Prefabs:** Reusable game objects containing embedded scripts, materials, and models.
- **Renderer:** URP-based assets for base configuration.
- **Scenes:** Main levels or environments.
- **Scripts:** All C# scripts. Editor-specific scripts must go in `Scripts/Editor`.
- **Shaders:** Custom URP shaders.
- **Terrain:** Terrain data folders named after their respective scenes.
- **Textures:** Image assets applied to 3D models.
- **UI:** Image assets used strictly for user interfaces.
- **XR / XRI:** Assets for the Unity XR system (currently Oculus XR).

## 3. Asset Naming Conventions

To easily identify assets in the Project window and search functions, use the following prefixes:

| Asset Type | Prefix | Example |
| :--- | :--- | :--- |
| **Prefabs** | `PF_` | `PF_SmartBike`, `PF_CollectibleBox` |
| **Materials** | `M_` | `M_RoadSurface`, `M_PlayerHands` |
| **Textures** | `T_` | `T_Skybox`, `T_ConcreteAlbedo` |
| **Audio** | `A_` | `A_BrakeSound`, `A_MissionComplete` |
| **Scenes** | `*Scene` (Suffix) | `CityScene`, `GarageScene` |

*Note: Use `PascalCase` (no spaces) for the core asset name after the prefix.*

## 4. C# Coding Guidelines

All C# scripts must follow standard Unity coding conventions to maintain a readable and predictable codebase.

### Naming Rules
- **Classes & Structs:** `PascalCase` (e.g., `MissionManager`, `BikeController`)
- **Public Variables:** `PascalCase` (e.g., `public float MaxSpeed;`)
- **Private/Protected Variables:** `camelCase` with an underscore prefix (e.g., `private float _currentSpeed;`)
- **Methods/Functions:** `PascalCase` (e.g., `CalculateSpeed()`, `Update()`)
- **Method Parameters:** `camelCase` (e.g., `public void SetSpeed(float targetSpeed)`)

### Best Practices
- **RequireComponent:** Use `[RequireComponent(typeof(ClassName))]` for scripts that depend on specific components (e.g., Rigidbody).
- **Serialization:** Use `[SerializeField]` to expose private variables to the Unity Editor instead of making them public, preserving encapsulation.
- **Namespaces:** Wrap scripts in appropriate namespaces (e.g., `namespace Redback.SmartBike.Missions`) to avoid class name collisions.
