# Candy Crush Game Automation Project

## Project Overview

This repository contains my ongoing work on a Candy Crush game automation and board analysis project.

So far, I have mainly focused on the initial image-processing and board extraction stage, which is the foundation required before implementing move detection and automated gameplay logic.

The current progress is centered around identifying the game grid from screenshots and preparing the board matrix for further analysis.



## Progress So Far

### 1. Screenshot Capture and Board Extraction

The first milestone completed is extracting the game board area from a screenshot.

At this stage, I have:

* captured the Candy Crush game screen
* identified the board region using pixel coordinates
* cropped the exact matrix area from the screenshot
* saved the cropped board image for further processing

This gives me a clean input image that can later be used for candy recognition.



### 2. Manual Coordinate Selection Tool

I have developed a Python script that helps me manually select the game board coordinates.

Using this tool, I can:

* click on the top-left corner of the grid
* click on the bottom-right corner
* verify the selected region visually
* preview the cropped output

This step helps in accurately defining the playable matrix.



### 3. Fixed Grid Crop Script

I have also created a script that performs direct cropping using predefined coordinates.

This script currently:

* reads the game screenshot
* crops the board matrix
* stores the output as an image file

This is useful for repeated testing with the same screen resolution.

![Game UI](game.jpg)


## Current Status

At present, the project has successfully reached the image preprocessing stage.

The board extraction workflow is working, and the next phase will be focused on:

* identifying individual candy blocks
* detecting colors / shapes
* converting the board into a matrix format
* implementing move suggestion logic



## Next Planned Work

The next development stages are:

* tile segmentation – split the board into equal cells
* candy recognition – identify each candy type
* pattern detection – detect possible matches
* best move solver – suggest optimal moves
* automation – perform moves automatically



## Tech Stack

* Python
* Tkinter
* Pillow (PIL)

