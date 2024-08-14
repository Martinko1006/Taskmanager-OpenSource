import pygame, psutil, os

pygame.init()

window = pygame.display.set_mode(flags=pygame.FULLSCREEN,vsync=1)
pygame.display.set_caption("Taskmanager Gold")
pygame.display.set_icon(pygame.image.load("programIcon.png"))

process_location = 0
process_location_vert = 0

font = pygame.font.SysFont("segoe ui", 20)

def text(text, dest):
    img = font.render(text, True, (0,0,0))
    window.blit(img, dest)

processes = []
seen_paths = set()

for process in psutil.process_iter():
    try:
        exe_path = process.exe()
        if not exe_path.startswith("C:\\Windows") and not process.name() == "System" and not process.name() == "MemCompression" and not process.name() == "Registry" and not process.name() == "":
            if not exe_path in seen_paths:
                print(process.exe())
                seen_paths.add(exe_path)
                processes.append(process)
    except:
        pass

program_input = pygame.Rect(window.get_size()[0]-400,window.get_size()[1]-30,400,30)
program_input_in = pygame.Rect(window.get_size()[0]-400,window.get_size()[1]-30,400,30)

input_process = ""

run = True
while run:
    process_location = 0
    process_location_vert = 0
    pygame.time.Clock().tick(60)
    window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_BACKSPACE:
                input_process = input_process[:-1]
            elif event.key == pygame.K_DELETE:
                pass
            elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                if input_process == "refresh":
                    processes = []
                    seen_paths = set()

                    for process in psutil.process_iter():
                        try:
                            exe_path = process.exe()
                            if not exe_path.startswith("C:\\Windows") and not process.name() == "System" and not process.name() == "MemCompression" and not process.name() == "Registry" and not process.name() == "":
                                if not exe_path in seen_paths:
                                    print(process.exe())
                                    seen_paths.add(exe_path)
                                    processes.append(process)
                        except:
                            pass
                elif input_process == "exit":
                    run = False
                else:
                    os.system(f"taskkill /f /im {input_process}.exe")
                input_process = ""
            else:
                input_process = input_process + event.unicode
    for process in processes:
        text(process.name(), (process_location_vert,process_location))
        pygame.draw.rect(window, "gray", program_input_in)
        pygame.draw.rect(window, "red", program_input, 2)
        text(input_process, (window.get_size()[0]-400,window.get_size()[1]-30))
        process_location += 30
        if process_location >= window.get_size()[1]-30:
            process_location_vert += 400
            process_location = 0
    pygame.display.update()