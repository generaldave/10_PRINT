################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# App class: App initializer                                                   #
#                                                                              #
# Created on 2016-12-29                                                        #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   .Constants  import *            # Constants file
from   .processing import Processing   # Processing style package
import pygame                          # For GUI
import random

################################################################################
#                                                                              #
#                                   APP CLASS                                  #
#                                                                              #
################################################################################

class App(object):

    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, appDirectory: str) -> None:
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Run app
        self.runApp()

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Mehtod sets up GUI
    def setupGUI(self) -> None:
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.processing = Processing(self.screen)

    # Method runs app
    def runApp(self) -> None:
        x = 0
        y = 0
        spacing = 20
        running = True
        while running:
            for event in pygame.event.get():
                
                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

                # Handle keyboard input
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_F5:
                        self.screen.fill(black)
                        x = 0
                        y = 0

            # 10 print stuff
            self.processing.stroke(white)
            if y < screen_resolution.height:
                if random.random() < fifty_percent:
                    self.processing.line(x, y, x + spacing, y + spacing)
                else:
                    self.processing.line(x, y + spacing, x + spacing, y)
                x = x + spacing
                if x >= screen_resolution.width:
                    x = 0
                    y = y + spacing

            # Update Screen
            pygame.display.update()
            self.clock.tick(fps)            

        # Close app cleanly
        pygame.quit()
