# if event.type == pygame.KEYDOWN:
#     input_history.append({event.key})
#     if event.key == pygame.K_DOWN:
#         print("sij")
#         down_press = True
# if event.type == pygame.KEYUP:
#     if event.key == pygame.K_DOWN:
#         print("no")
#         down_press = False
#     if event.key == pygame.K_RIGHT and down_press:
#         print("asfju")

# if event.type == pygame.KEYDOWN:
#     # if event.key == pygame.K_a or event.key == pygame.K_ESCAPE:  # <--- or
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_DOWN]:
#         input_history.append("down")
#     if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
#         input_history.append("down_right")
#     if keys[pygame.K_RIGHT] and not keys[pygame.K_DOWN]:
#         input_history.append("right")
#
#     print(input_history)
#
#     if input_history == ["down", "down_right", "right"]:
#         print("hadooooken")