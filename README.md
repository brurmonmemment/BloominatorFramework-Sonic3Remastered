# bloominator framework

a custom game engine im building for retro 16-bit games. (still getting started, so dont expect... anything!)

--- **engine details**
-- basic info
- **language:** python (sorry)
- **rendering:** sdl3 (via pysdl3)
- **physics:** retro engine-like
- **resolution:** base of 424x240 with up to 5x pixel-perfect upscaling in windowed mode, plus 
custom ratio support (e.g. 16:9, 4:3, 17-21:9 n more)
- **input:** keyboard & gamepad
- **system:** scene-based
- **scene system:** binaries that have information as to how big its going to be, what kind of sprites will it use, the whole 9 yards

-- **TODO**
- Finish structuring the scene
- Update the scene system to work with the new scene
- Have a fully working scene with code execution
- TBC

**the REQUIREMENTS**
1. python
2. a computer
3. pysdl3 package
4. patience, like a LOT

# sonic 3 & knuckles in bloominator framework

im working on an open-source, easy-to-mod version of sonic 3 — no unmodifiable hardcoded parts or renderhooking required (looking at YOU S3AIR)!

-- **planned features**
- **multiple gameplay modes:** full support for widescreen, ultrawide & 4:3
  - accommodations for widescreen (like moving the fire breath boss and adjusting the data select screen & other stuff)
- **ost:** high-quality direct vgm rips and restorations (still vgm rips but with new hi-hats and source DAC samples, selected by default)
-- big thanks to sengin31 on YouTube for the sample pack I used + the hi hats
- **smooth 60+ fps gameplay:**  
  - possibly with interpolation for extra smoothness  
  - interpolated, smooth moving objects like aiz's monkey dude, swings
- **features i definetly dont and wont know how to add but if anybody wants it then i might add it:**  
  - a classic mode (game in 4:3)  
  - an original mode (using integrated blastem with a user-supplied sonic 3k rom)

i basically havent made any progress on either of these so if someone can help me out it would be greatly appreciated!!!!
