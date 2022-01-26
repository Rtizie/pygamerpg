from os import walk
import pygame

def import_folder(path):
	surface_list = []

	for _,__,img_files in walk(path):
		for image in sorted(img_files):
			full_path = path + '/' + image
			image_surf = pygame.image.load(full_path)
			surface_list.append(image_surf)
			print(image)

	return surface_list