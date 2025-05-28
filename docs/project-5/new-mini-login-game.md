---
sidebar_position: 12
---
# New Mini Login Game

## Gamehub

The GameHub screen acts as the central hub of the game platform. It presents users with a selection of games they can choose from. Each game is represented as a card with a logo, name, and a "Play" button. When a user selects a game by clicking the "Play" button, a verification process begins. This process includes:

1. Displaying a reCAPTCHA modal to confirm the user is human.
2. If reCAPTCHA is passed, a mini CAPTCHA game (like selecting specific emojis) is shown.
3. Upon successfully completing both steps, the user is navigated to the selected game.

This ensures that only verified users can access the games, preventing bots from interacting with the platform.

## HumanCheckModal

The HumanCheckModal component is a modal popup that appears when a user attempts to play a game from the GameHub. It serves as the first layer of human verification using Google reCAPTCHA.

**Features:**
- Displays a message prompting the user to verify they're human.
- Integrates Google reCAPTCHA (v2 or v3) for human verification.
- Has "Continue" and "Cancel" buttons.
- Only enables the "Continue" button after successful reCAPTCHA verification.
- On successful verification, it triggers the next step in the verification process.

## CaptchaGridGame

The CaptchaGridGame component is a custom CAPTCHA game designed to further verify the user's humanity. It's shown after the user passes the reCAPTCHA in the HumanCheckModal.

**Features:**
- Displays a 3x3 grid of emojis.
- Prompts the user to select all emojis of a specific type (e.g., all "cat" emojis).
- Randomizes the emojis in the grid each time.
- Ensures at least one correct emoji is present.
- Provides feedback ("Try again") if the user selects incorrectly.
- On correct selection, proceeds to the game.

This adds an engaging layer of human verification beyond standard CAPTCHA.

## MathMatch Game

The MathMatch game is an interactive math quiz game with a robot character (RoboMatch) guiding the user.

**Features:**
- Animated robot character walks in and then stands idle.
- Displays a welcome message from the robot.
- Offers 3 difficulty levels: Level 1 (basic), Level 2 (intermediate), Level 3 (advanced).
- Randomly selects a question from a pool based on selected difficulty.
- Displays the question and multiple choice answers.
- On correct answer:
  - Shows a congratulatory message.
  - Triggers a confetti animation.
- On incorrect answer:
  - Prompts the user to try again.
- After answering, asks if the user wants another question or to finish.

This game helps users practice math skills in a fun and engaging way.

## Technology Stack

**Frontend:**
- React (functional components and hooks)
- CSS Modules for component styling
- React Router for navigation
- Google reCAPTCHA (via react-google-recaptcha)
- Confetti animation (via react-confetti)
- @react-hook/window-size for responsive confetti

**Project Setup:**
- Node.js and npm for package management
- Local development server via `npm start`

**Version Control:**
- Git for source control
- GitHub for remote repository management

**Development Tools:**
- Visual Studio Code (VS Code) for code editing
- Browser for testing (Chrome)
- Terminal for running npm commands
