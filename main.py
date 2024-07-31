def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_art = """ ▄████▄   ██▓███   ███▄ ▄███▓▓█████  █     █░ ▄▄▄       ███▄    █ 
▒██▀ ▀█  ▓██░  ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓█░ █ ░█░▒████▄     ██ ▀█   █ 
▒▓█    ▄ ▓██░ ██▓▒▓██    ▓██░▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓██  ▀█ ██▒
▒▓▓▄ ▄██▒▒██▄█▓▒ ▒▒██    ▒██ ▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
▒ ▓███▀ ░▒██▒ ░  ░▒██▒   ░██▒░▒████▒░░██▒██▓  ▓█   ▓██▒▒██░   ▓██░
░ ░▒ ▒  ░▒▓▒░ ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
  ░  ▒   ░▒ ░     ░  ░      ░ ░ ░  ░  ▒ ░ ░    ▒   ▒▒ ░░ ░░   ░ ▒░
░        ░░       ░      ░      ░     ░   ░    ░   ▒      ░   ░ ░ 
░ ░                      ░      ░  ░    ░          ░  ░         ░ 
░                                                                 """
    start_color = Color.parse("#28e99a")
    end_color = Color.parse("#cbd31a")
    start_rgb = np.array(start_color.triplet)
    end_rgb = np.array(end_color.triplet)
    lines = ascii_art.split("\n")
    max_len = max(len(line) for line in lines)
    num_lines = len(lines)
    gradient_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char.strip():
                position = (y / num_lines + x / max_len) / 2
                color_rgb = start_rgb + position * (end_rgb - start_rgb)
                color_hex = '#{:02x}{:02x}{:02x}'.format(int(color_rgb[0]), int(color_rgb[1]), int(color_rgb[2]))
                gradient_text.append(char, style=color_hex)
            else:
                gradient_text.append(char)
                
        gradient_text.append("\n")
        
    console.print(gradient_text)
    
    console.print("[bold][red]==================================================================[/red][/bold]")
    
    console.print("\t   𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋")
    
    console.print("   [bold][red]  𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃[/bold][red]")
    
    console.print("[bold][red]==================================================================[/red][/bold]")
