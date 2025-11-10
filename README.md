# General TODOs
- Build on subsystem abstraction layer
- Extra code for stuff like inputs and audio tests
- (POTENTIALLY) Start working on the stage system again

# Hedge Engine
A robust 2D sprite-based engine, designed for ease of use and mod-ability.

## Engine Details
### Basic Info
- **Programming Language:** Python (sorry)
- **Backend(s):** SDL3 (PySDL3), managed via abstraction layer & allows for new backends
- **Resolution:** 424x240 base with custom scaling 

  Custom ratio support (e.g. 16:9, 16:10, 4:3, 17:9, etc.)

  Allows for custom W/H scaling (e.g. you can have a scale of 2W/3H)
- **Supported Inputs:** Keyboards & Controllers
- **Style:** Stage-based

  Stages are the separate screens/rooms that are usually shown in-order but can jump to other ones regardless of order.
- **Stage system:** A stage in this context is usually made up of:
  - Title
  - Stage logic
  - Spritesheets
  - Object definitions in binaries (background parallax features, other objects, etc.)
  - Editable with a custom, open-source stage editor.
    - not in python lmao

### Prerequisites
1. Python 3.10 (preferably later)
2. Desktop OS (Windows/macOS/Linux)
3. PySDL3

# Project Echidna in Hedge Engine (TBD)
An open source Sonic 3 & Knuckles remaster in Hedge Engine that will be developed alongside this engine.

Proper development will not start until the engine is in a state where it can actually perform basic to somewhat advanced functions.
### Le Planned Features
- **Viewport res support:** Widescreen, ultrawide & 4:3
  - Depending on the screen resolution, there will be accommodations.
- **OST:** Having the option between:
  - Unchanged SMPS rips
  - "Restorations" (Source instruments + PSG3 -> Hi hats)
    - Big thanks to Sengin31 on YouTube for the sample pack I used + the hi hats
    - SVG 360 (supervideogamer3607) for the MJ beatboxing vox (S3 Credits Theme)
  - Full-on remasters (restoration + other enhancements) (PROBABLY WON'T EXIST DON'T GET YOUR HOPES UP)
- **Consistent 60 FPS+ gameplay:**  
  - (maybe with interpolation?)
  - Smoother objects like Monkey Dude & gumball machine crank (movements are more perpetuated by math rather than prearranged frames)
### Potential Features? (I don't know if I could add these)
- A "Throwback mode" (4:3 with additional tweaks) 
- An original mode (embed of an emulator like BlastEm with a Sonic 3K ROM supplied by the user)