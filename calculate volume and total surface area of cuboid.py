L,B,H = map(int,input().split())
total_surface_area = 2 * ((L * B) + (B * H) + (H * L))
volume = L * B * H
print(total_surface_area,end = " ")
print(volume)
