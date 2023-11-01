# Guess a Number Game with Vite + React

## Introduction

In this assignment, you will create a "Guess a Number" game using the Vite + React.js development environment. The goal of this project is to build a simple interactive game where players guess a randomly generated number within a specified range. This assignment will help you apply your knowledge of React.js, state management, and user interactions to create an engaging game.

## Assignment Tasks

### Task 1: Setup Your Development Environment

1. Set up your development environment with Vite and React. Install Vite and create a new React project using the following commands:

   ```bash
   npm create-vite
   ```

2. Navigate to your project directory and ensure that your development environment is ready to start building the game.

### Task 2: Create the User Interface

1. Design the user interface for the "Guess a Number" game. Create a React component that displays the following elements:

   - A title or heading that introduces the game.
   - An input field where players can enter their guess.
   - A "Submit" button to submit the guess.
   - A message area to display feedback to the player (e.g., "Too high," "Too low," "You guessed it!").
   - A section to display the number of attempts made by the player.

2. Style the user interface with appropriate visuals and layout to make the game engaging and user-friendly.

### Task 3: Generate a Random Number

1. Implement a function to generate a random number between a specified range (e.g., 1 to 100). This number will be the target for the player to guess.

2. Store the randomly generated number in the state of your React component to track the target number.

### Task 4: Handle User Input

1. Implement a function that listens to user input in the input field.

2. Validate the user's input to ensure it's a valid number within the specified range.

3. Update the state to store the player's guess.

### Task 5: Compare Guess to the Target

1. Compare the player's guess to the randomly generated target number.

2. Provide feedback to the player based on their guess (e.g., "Too high," "Too low," "You guessed it!").

3. Keep track of the number of attempts made by the player, and display this information on the screen.

### Task 6: Reset the Game

1. Implement a "Play Again" button that allows the player to start a new game.

2. When the player clicks the "Play Again" button, reset the game by generating a new random number and resetting the number of attempts.

## Additional Tips

- You can use CSS or a CSS framework of your choice to style the game.
- Make sure to provide clear and friendly feedback to the player to keep the game engaging.

This assignment will help you apply your knowledge of React.js, state management, and user interactions to create an interactive and fun "Guess a Number" game. Enjoy building your game, and good luck!
