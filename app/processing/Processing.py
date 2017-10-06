################################################################################
#                                                                              #
# David Fuller                                                                 #
#                                                                              #
# Processing class: Java-Processing type class                                 #
#                                                                              #
# Created on 2017-4-27                                                         #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                              IMPORT STATEMENTS                               #
#                                                                              #
################################################################################

from   .Constants import *   # Constants file
import pygame                # For GUI

################################################################################
#                                                                              #
#                              PROCESSING CLASS                                #
#                                                                              #
################################################################################

class Processing(object):
    ############################################################################
    #                                                                          #
    #                               CONSTRUCTOR                                #
    #                                                                          #
    ############################################################################
    
    def __init__(self, screen):
        self.screen = screen
        self.boolStroke = True
        self.strokecolour = black
        self.boolFill = True
        self.fillcolour = black
        self.strokeweight = 1

    ############################################################################
    #                                                                          #
    #                                 METHODS                                  #
    #                                                                          #
    ############################################################################

    # Method sets strokeweight
    def strokeWeight(self, weight : int) -> None:
        self.strokeweight = weight

    # Method sets stroke to false
    def noStroke(self) -> None:
        self.boolStroke = False

    # Method sets stroke to true and the colour for stroke
    def stroke(self, colour : color) -> None:
        self.boolStroke = True
        self.strokecolour = colour

    # Method sets fill to false
    def noFill(self) -> None:
        self.boolFill = False

    # Method sets fill to true and the colour for fill
    def fill(self, colour : color) -> None:
        self.boolFill = True
        self.fillcolour = colour

    # Method draws a line to and from the given points
    def line(self, sx : int, sy : int, ex : int, ey : int) -> None:
        if self.boolStroke:
            start = (sx, sy)
            end = (ex, ey)
            pygame.draw.line(self.screen, \
                             self.strokecolour, \
                             start, end, self.strokeweight)

    # Method draws a rectangle according to the given x, y, and width
    def rect(self, x : int, y : int, width : int, height: int) -> None:
        rectangle = (x, y, width, height)

        # Fill and Stroke
        if self.boolFill and self.boolStroke:
            # Stroke
            stroke_rectangle = (x - self.strokeweight, \
                                y - self.strokeweight, \
                                width + self.strokeweight * 2, \
                                height + self.strokeweight * 2)
            pygame.draw.rect(self.screen, \
                               self.strokecolour, \
                               stroke_rectangle, \
                               fill)
            
            # Fill
            pygame.draw.rect(self.screen, \
                             self.fillcolour, \
                             rectangle, \
                             fill)

        # Fill, no Stroke
        elif self.boolFill and not self.boolStroke:
            pygame.draw.rect(self.screen, \
                             self.fillcolour, \
                             rectangle, \
                             fill)

        # Stroke, no Fill
        elif not self.boolFill and self.boolStroke:
            pygame.draw.rect(self.screen, \
                             self.strokecolour, \
                             rectangle, \
                             self.strokeweight)

        # no Stroke, no Fill does nothing

	# Method draws a rectangle according to the given x, y, and width
    def ellipse(self, x : int, y : int, width : int, height: int) -> None:
        rectangle = (x, y, width, height)

        # Fill and Stroke
        if self.boolFill and self.boolStroke:
            # Stroke
            stroke_rectangle = (x - self.strokeweight, \
                                y - self.strokeweight, \
                                width + self.strokeweight * 2, \
                                height + self.strokeweight * 2)
            pygame.draw.ellipse(self.screen, \
                               self.strokecolour, \
                               stroke_rectangle, \
                               fill)
            
            # Fill
            pygame.draw.ellipse(self.screen, \
                               self.fillcolour, \
                               rectangle, \
                               fill)            

        # Fill, no Stroke
        elif self.boolFill and not self.boolStroke:
            pygame.draw.ellipse(self.screen, \
                               self.fillcolour, \
                               rectangle, \
                               fill)

        # Stroke, no Fill
        elif not self.boolFill and self.boolStroke:
            pygame.draw.ellipse(self.screen, \
                                self.strokecolour, \
                                rectangle, \
                                self.strokeweight)

        # no Stroke, no Fill does nothing
        
