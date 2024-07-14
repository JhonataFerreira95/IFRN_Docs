import pygame
pygame.init()

pygame.mixer.init

pygame.mixer.music.load("race.mp3")
pygame.mixer.music.play()

x = input("Digite algo para parar: ")

pygame.mixer.music.stop()


