import os
import time
from random import randint, sample

def main():
    # Prompt user to choose game type
    type = None
    while type not in ['1', '2', '3']:   

        # Title
        print '            ______ _______ ______ ______    _______ ______  ______ __  __'
        print '           / __  //__  __// __  // __  /   /__  __// __  / / ____// / / /'
        print '          / / /_/   / /  / /_/ // /_/ /      / /  / /_/ / / /__  / //`/`'
        print '          _\ \     / /  / __  //   __/      / /  /   __/ / __ / /  `/`'
        print '        / /_/ /   / /  / / / // /\ \       / /  / /\ \  / /___ / /\ \\'
        print '       /_____/   /_/  /_/ /_//_/  \_\     /_/  /_/  \_\/_____//_/  \_\\'
        print '               ____        _   _   _           _     _       _ '
        print '              |  _ \      | | | | | |         | |   (_)     | |'
        print '              | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __ | |'
        print '              |  _ < / _` | __| __| |/ _ \/ __| `_ \| | `_ \| |'
        print '              | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |_|'
        print '              |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/(_)'
        print '                                                      | |      '
        print '                                                      |_|      v0.1 beta'
        print ''
        print '                                _____..---========+*+==========---.._____'
        print '   ______________________ __,-=`=====____  =================== _____=====`='
        print '  (._____________________I__) - _-=_/    `---------=+=--------`'
        print '      /      /__...---====`---+---_`'
        print '     `------`---.___ -  _ =   _.-`'
        print '                    `--------`'
        print '                       +-----------------------------+'
        print '                       |     Game Types:             |'
        print '                       |     1. Single-Player        |'
        print '                       |     2. Two-Player           |'
        print '                       |     3. AI vs AI (*beta)     |'
        print '                       +-----------------------------+'
        print

        # User input
        type = raw_input('Choose Game Type (Enter 1, 2 or 3): ')
        os.system('cls')

    # Define game parameters
    BOARD_SIZE = 10
    SHIP_COUNT = 5
    SHIP_LENGTH = 3

    # Define boards
    p1_board = []
    p2_board = []

    p1_radar = []
    p2_radar = []

    # Define ships
    p1_ships = []
    p2_ships = []

    # Define name lists
    ship_names = ['USS Adelphi', 'USS Agamemnon', 'USS Ahwahnee', 'USS Ajax', 'USS Akagi', 'USS Al-Batani', 'USS Albert Einstein', 'USS Aleo', 'USS Alka-Selsior', 'USS Antares', 'USS Antares', 'USS Apollo', 'USS Appalachia', 'USS Archer', 'USS Ariel', 'USS Aries', 'USS Armstrong', 'USS Atlantis', 'USS Baton Rouge', 'USS Bellerophon', 'USS Berlin', 'USS Biddeford', 'USS Biko', 'USS Billings', 'USS Bonaventure', 'USS Bonchune', 'USS Bozeman', 'USS Bradbury', 'USS Brattain', 'USS Budapest', 'USS Buran', 'USS Cairo', 'USS Callisto', 'USS Carolina', 'USS Centaur', 'USS Challenger', 'USS Charleston', 'USS Chekov', 'USS Chicago', 'USS Clavyn', 'USS Clayton', 'USS Clement', 'USS Cochrane', 'USS Columbia', 'USS Concord', 'USS Constantinople', 'USS Constellation', 'USS Copernicus', 'USS Cortez', 'USS Crazy Horse', 'USS Crockett', 'USS Curry', 'USS Da-Teplan', 'USS Defiant', 'USS Denver', 'USS Destiny', 'USS D\'hjty', 'USS Discovery', 'USS Donovan', 'USS Drake', 'USS Eagle', 'USS Elkins', 'USS Elmer Fudd', 'USS Emden', 'USS Endeavour', 'USS Entente', 'USS Enterprise', 'USS Equicon', 'USS Equinox', 'USS Essex', 'USS Excalibur', 'USS Excelsior', 'USS Exeter', 'USS Farouk El-Baz', 'USS Farragut', 'USS Fearless', 'USS Firebrand', 'USS Fleming', 'USS Fredrickson', 'USS Galaxy', 'USS Gallico', 'USS Gander', 'USS Gandhi', 'USS Ganges', 'USS Ganymede', 'USS Gettysburg', 'USS G\'Mat', 'USS Goddard', 'USS Gorkon', 'USS Gremlin', 'USS Grissom', 'USS Hathaway', 'USS Havana', 'USS Heart of Gold', 'USS Helin', 'USS Hera', 'USS Hermes', 'USS Hispaniola', 'USS Hokule\'a', 'USS Honshu', 'USS Hood', 'USS Horatio', 'USS Horizon', 'USS Hornet', 'USS Huron', 'USS Intrepid', 'USS James Fennimore Cooper', 'USS Jenolan', 'USS John F. Kennedy', 'USS John Muir', 'USS Kearsarge', 'USS Kelvin', 'USS K\'Marco', 'USS Kongo', 'USS Korolev', 'USS Kyushu', 'USS Lakota', 'USS Lalo', 'USS Lantree', 'USS LaSalle', 'USS Leeds', 'USS Lexington', 'USS Liberator', 'USS Livingston', 'USS Madison', 'USS Malone', 'USS Mare Tranquillitatis',
                  'USS Maryland', 'USS Matte Fringe', 'USS Max Plank', 'USS Mayflower', 'USS Mekong', 'USS Melbourne', 'USS Merrimac', 'USS Minnow', 'USS Min\'ow', 'USS Monitor', 'USS Musashi', 'USS Mustang', 'USS Nash', 'USS Nautilus', 'USS Neil Armstrong', 'USS Newton', 'USS Niels Bohr', 'USS Nightwing', 'USS Nobel', 'USS Noble', 'USS Non Sequitur', 'USS Northridge', 'USS Nova', 'USS Oberth', 'USS Odele', 'USS Odyssey', 'USS Okinawa', 'USS Olympia', 'USS Omaha Nebraska', 'USS Orinoco', 'USS Pasteur', 'USS Pegasus', 'USS Peterson', 'USS Philadelphia', 'USS Phoenix', 'USS Portland', 'USS Potemkin', 'USS Princeton', 'USS Prokofiev', 'USS Prometheus', 'USS Proxima', 'USS Pueblo', 'USS Puget Sound', 'USS Raging Queen', 'USS Raman', 'USS Relativity', 'USS Reliant', 'USS Renegade', 'USS Republic', 'USS Repulse', 'USS Revere', 'USS Rhode Island', 'USS Rio Grande', 'USS Robert Louis Stevenson', 'USS Roosevelt', 'USS Rubicon', 'USS Rutledge', 'USS Sarajevo', 'USS Saratoga', 'USS Sarek', 'USS Scovill', 'USS Seaquest', 'USS Seaview', 'USS Sentinel', 'USS Shenandoah', 'USS Shepard', 'USS Sherlock Holmes', 'USS ShirKahr', 'USS Silversides', 'USS Sitak', 'USS Springfield', 'USS Stargazer', 'USS Strata', 'USS Suleiman', 'USS Sutherland', 'USS Syracuse', 'USS Tecumseh', 'USS Thomas Paine', 'USS Thunderchild', 'USS Tian An Men', 'USS Ticonderoga', 'USS Titan', 'USS T\'Kumbra', 'USS Tolstoy', 'USS Tombaugh', 'USS Tranquillity Base', 'USS Trial', 'USS Trieste', 'USS Tripoli', 'USS Truman', 'USS Tsiolkovsky', 'USS Tycho', 'USS Ulysses', 'USS Umibozu', 'USS Unicorn', 'USS Valdemar', 'USS Valiant', 'USS Valley Forge', 'USS Vengeance', 'USS Venture', 'USS Veracruz', 'USS Vico', 'USS Victory', 'USS Volga', 'USS Voyager', 'USS Wellington', 'USS White Sands', 'USS Whorfin', 'USS Woden', 'USS Wolcott', 'USS Wyoming', 'USS Yamaguchi', 'USS Yamato', 'USS Yangtzee Kiang', 'USS Yeager', 'USS Yellowstone', 'USS Yorkshire', 'USS Yorktown', 'USS Yosemite', 'USS Yukon', 'USS Yuri Gagarin', 'USS Zapata', 'USS Zhukov']
    
    ai_names = ['Jonathan Archer', 'Ayala', 'Azan', 'Reginald Barclay', 'Bareil Antos', 'Julian Bashir', 'B\'Etor', 'The Borg Queen', 'Phillip Boyce', 'Brunt', 'Joseph Carey', 'Chakotay', 'Chell', 'Christine Chapel', 'Pavel Chekov', 'J. M. Colt', 'Kimara Cretak', 'Beverly Crusher', 'Wesley Crusher', 'Jal Culluh', 'Elizabeth Cutler', 'Leonardo da Vinci', 'Damar', 'Daniels', 'Data', 'Ezri Dax', 'Jadzia Dax', 'Degra', 'The Doctor', 'Dolim', 'Dukat', 'Evek', 'Michael Eddington', 'Female Changeling', 'Vic Fontaine', 'Maxwell Forrest', 'Elim Garak', 'Garrison', 'Sonya Gomez', 'Gowron', 'Amanda Grayson', 'Guinan', 'J. Hayes', 'Erika Hernandez', 'Hogan', 'Mr. Homn', 'Hugh of Borg', 'Icheb', 'Ishka', 'Kathryn Janeway', 'Jannar', 'Michael Jonas', 'K\'Ehleyr', 'Kes', 'Harry Kim', 'Kira Nerys', 'James T. Kirk', 'Kor', 'Kurn', 'Geordi La Forge', 'Leeta', 'Robin Lefler', 'Li Nalas', 'Lore', 'Lursa', 'Maihar\'du', 'Mallora', 'Carol Marcus', 'Martok', 'Travis Mayweather', 'Leonard McCoy', 'Mezoti', 'Mila', 'Mora Pol', 'Morn', 'Mot', 'Neelix', 'Susan Nicoletti', 'Nog', 'Kashimuro Nozawa', 'Number One', 'Keiko O\'Brien', 'Miles O\'Brien', 'Molly O\'Brien', 'Odo', 'Alyssa Ogawa', 'Opaka Sulan', 'Owen Paris', 'Tom Paris', 'Phlox', 'Jean-Luc Picard', 'Christopher Pike', 'Katherine Pulaski', 'Q', 'Quark', 'Janice Rand', 'Rebi', 'Malcolm Reed', 'William Riker', 'Ro Laren', 'Rom', 'William Ross', 'Michael Rostov', 'Alexander Rozhenko', 'Saavik', 'Sarek', 'Hoshi Sato', 'Montgomery Scott', 'Sela', 'Seska', 'Seven of Nine', 'Shakaar Edon', 'Thy\'lek Shran', 'Silik', 'Benjamin Sisko', 'Jake Sisko', 'Jennifer Sisko', 'Joseph Sisko', 'Sarah Sisko', 'Luther Sloan', 'Soval', 'Spock', 'Lon Suder', 'Hikaru Sulu', 'Enabran Tain', 'Tal Celes', 'Tomalak', 'Tora Ziyal', 'B\'Elanna Torres', 'T\'Pol', 'The Traveler', 'Deanna Troi', 'Lwaxana Troi', 'Charles Tucker', 'Tuvok', 'Jose Tyler', 'Nyota Uhura', 'Vash', 'Vorik', 'Weyoun', 'Naomi Wildman', 'Samantha Wildman', 'Winn Adami', 'Worf', 'Tasha Yar', 'Kasidy Yates', 'Zek']

    # Initialize the boards
    for _ in range(BOARD_SIZE):
        row = []
        for _ in range(BOARD_SIZE):
            row.append('-')

        p1_board.append(row[:])
        p2_board.append(row[:])
        p1_radar.append(row[:])
        p2_radar.append(row[:])

    # Define alpha header (MAX 26)
    header = list(map(chr, range(65, 65 + BOARD_SIZE)))

    p1_name = None
    p2_name = None

    p1_ai = None
    p1_ai = None

    # Enter ships
    os.system('cls')

    # Pick random ship names
    rand_ship_names =  sample(set(ship_names), SHIP_COUNT * 2)
    rand_player_names = sample(set(ai_names), 2)

    # Setup different game types
    if type == '1':
        p1_name = raw_input('Player 1, enter your name: ')
        p2_name = rand_player_names[0]
        p1_ai = False
        p2_ai = True
    if type == '2':
        p1_name = raw_input('Player 1, enter your name: ')
        p2_name = raw_input('Player 2, enter your name: ')
        p1_ai = False
        p2_ai = False
    if type == '3':
        p1_name = rand_player_names[0]
        p2_name = rand_player_names[1]
        p1_ai = True
        p2_ai = True

    os.system('cls')

    # Place ships

    # If PvP, clear board between player turns
    ship_entry(p1_name, BOARD_SIZE, SHIP_COUNT, SHIP_LENGTH, header,
        p1_ships, p1_board, rand_ship_names[:SHIP_COUNT], ai=p1_ai)

    if type == '2':
        raw_input('Press ENTER to continue to ' + p2_name + '\'s turn...')
        os.system('cls')

    ship_entry(p2_name, BOARD_SIZE, SHIP_COUNT, SHIP_LENGTH, header,
        p2_ships, p2_board[:], rand_ship_names[SHIP_COUNT:], ai=p2_ai)

    if type == '2':
        raw_input('Press ENTER to start ' + p1_name +'\'s turn...')
        os.system('cls')

    # Start game
    print 'Starting game...'
    time.sleep(1)
    os.system('cls')

    # Game loop
    game_on = True
    turn_ctr = 0  # Player 1 moves on even, player 2 on odd

    while game_on:
        if turn_ctr % 2 == 0:
            # Player 1
            game_on = fire_weapon(p1_name, BOARD_SIZE, SHIP_LENGTH, 
                header, p1_ships, p1_board, p1_radar, p2_ships, p2_board,
                p2_radar, turn_ctr, ai=p1_ai)
            # If PvP, clear board between player turns
            if game_on and type == '2':
                print '             SWITCH SIDES'
                print '                ______'
                print '              _-` .   .`-_'
                print '          |/ /  .. . `   .\ `\|'
                print '         |/ /            ..\` \|'
                print '       \|/ |: .   ._|_ .. . `| \|/'
                print '        \/ |   _|_ .| . .:  `| \/'
                print '       \ / |.   |  .  .    .`| \ /'
                print '        \||| .  . .  _|_   .`|||/'
                print '       \__| \  . :.  .|.  ./` |__/'
                print '         __| \_  .    .. _/ `|__'
                print '          __|  `-______-`  |`__'
                print '             -,____  ____,-'
                print '               ---`  `---'
                raw_input(p2_name + ', press ENTER to start your turn...')
                os.system('cls')

        else:
            # Player 2            
            game_on = fire_weapon(p2_name, BOARD_SIZE, SHIP_LENGTH, 
                header, p2_ships, p2_board, p2_radar, p1_ships, p1_board,
                p1_radar, turn_ctr, ai=p2_ai)
            if game_on and type == '2':
                print '             SWITCH SIDES'
                print '                   |'
                print '                   |'
                print '                   |'
                print '                  ` `'
                print '                  | |'
                print '                  | |'
                print '                 `   `'
                print '              .-`|   |`-.'
                print '             /  /     \  \\'
                print '            |__,\     /   |'
                print '           -`   \\   //\_ |'
                print '        ,-`   ___\\.//   `-__'
                print '       /__,--`       `--.____--'
                print '              `-._____.-`'
                raw_input(p2_name + ', press ENTER to start your turn...')
                os.system('cls')

        turn_ctr += 1

    # End Game
    print '   ______                        ____                 '
    print '  / ____/___ _____ ___  ___     / __ \_   _____  _____'
    print ' / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/'
    print '/ /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /    '
    print '\____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/     '
    print
    print 'Congratulations',

    if turn_ctr % 2 == 0:
        print p1_name,', you won!'
    else:
        print p2_name,', you won!'

def ship_entry(player_name, BOARD_SIZE, SHIP_COUNT, SHIP_LENGTH, header,
        ships, board, ship_names, ai=False):
    if ai:
        print
        print player_name, '(AI) placing ships...'
        time.sleep(1)

    # Place each ship
    for ship in range(1, SHIP_COUNT+1):
        # Create new ship
        ships.append({
            'location': [],
            'name': ''
        })

        # Define coordinates
        coord_x = coord_y = None
        error = ''

        # Place one piece at a time
        for piece in range(1, SHIP_LENGTH+1):
            # Only place if space is valid
            # Valid means:
            # 1) space not occupied by another piece
            # 2) have enough surrounding free spaces to finish placing
            #   entire ship
            # 3) space must be adjacent to another piece from the same ship
            #   (unless first piece)

            valid = False
            status_msg = ''

            # Loop until user enters a valid space
            while not valid:
                if not ai:                
                    # Ship entry display
                    # Title
                    print 'Prepare for Battle!'
                    print '-' * 52
                    print player_name, 'place your ships...'
                    print

                    # Print main display
                    display = ship_entry_display(player_name, BOARD_SIZE, header, board, ships)
                    
                    for d in display:
                        print d

                    # Print status message
                    print status_msg

                    # Reset status message
                    status_msg = ''

                if not ai:
                    # User input coordinates
                    coord = raw_input('Enter coordinates for ship #' + str(ship) +
                        ' (' + str(piece) + '/' + str(SHIP_LENGTH) + '): ')

                    # Convert entered coordinates to grid indices
                    try:
                        # Convert x-axis letter to int
                        coord_x = ord(coord[0].upper()) - 65
                    except IndexError:
                        coord_x = -1
                    try:
                        # Subtract 1 from y-axis number
                        coord_y = int(coord[1:]) - 1
                    except ValueError:
                        coord_y = -1
                else:
                    # Randomly generated coordinates
                    coord_x = randint(0, BOARD_SIZE)
                    coord_y = randint(0, BOARD_SIZE)

                # Check if space entered is valid

                # Check if coordinates are inside board
                if not ((coord_x >= 0 and coord_x < BOARD_SIZE) and 
                        (coord_y >= 0 and coord_y < BOARD_SIZE)):
                    status_msg = 'Invalid coordinates'
                else:
                    # Check if spot is free
                    if board[coord_y][coord_x] != '-':
                        status_msg = 'That spot is already taken'
                    else:
                        # Check if there is space avail for remaining pieces
                        rem_pieces = SHIP_LENGTH - piece
                        free_y = adj_y = free_x = adj_x = 0

                        # Check all 4 directions 
                        for i in range(1, SHIP_LENGTH):
                            # Up
                            if coord_y-i >= 0:
                                if (rem_pieces > 0 and 
                                        board[coord_y-i][coord_x] == '-'):
                                    free_y += 1
                                if board[coord_y-i][coord_x] == str(ship):
                                    adj_y += 1
                            # Down
                            if coord_y+i < BOARD_SIZE:
                                if (rem_pieces > 0 and
                                        board[coord_y+i][coord_x] == '-'):
                                    free_y += 1
                                if board[coord_y+i][coord_x] == str(ship):
                                    adj_y += 1
                            # Left
                            if coord_x-i >= 0:
                                if (rem_pieces > 0 and 
                                        board[coord_y][coord_x-i] == '-'):
                                    free_x += 1
                                if board[coord_y][coord_x-i] == str(ship):
                                    adj_x += 1
                            # Right
                            if coord_x+i < BOARD_SIZE:
                                if (rem_pieces > 0 and 
                                        board[coord_y][coord_x+i] == '-'):
                                    free_x += 1
                                if board[coord_y][coord_x+i] == str(ship):
                                    adj_x += 1

                        # Determine if valid
                        if free_y >= rem_pieces or free_x >= rem_pieces:
                            if adj_y >= piece-1 or adj_x >= piece-1:
                                valid = True
                            else:
                                status_msg = ('Pieces must be placed next '
                                    'to each other')
                        else:
                            status_msg = ('There is not enough space '
                                'to complete to ship')

                if not ai:
                    os.system('cls')

            # Valid entry
            # Update ship location
            ships[-1]['location'].append([coord_x, coord_y])
            # Update board
            board[coord_y][coord_x] = str(ship)

        # Ship added, assign name
        ships[-1]['name'] = ship_names[ship-1]

    # All ships added
    if not ai:
        # Print display
        print player_name + '\'s', 'ships placed...'
        print '-' * 52
        print

        # Print main display
        display = ship_entry_display(player_name, BOARD_SIZE, header, board, ships)
        
        for d in display:
            print d

def ship_entry_display(player_name, BOARD_SIZE, header, board, ships):
    # First column
    display = []
    # Header
    display.append(' '.join([str(x) for x in header]).
        rjust(BOARD_SIZE * 2 + 2))
    # Board
    for row in range(BOARD_SIZE):
        display.append(str(row+1).rjust(2) + ' '.join(board[row]).
            rjust(BOARD_SIZE * 2))

    # Second column
    # Status board
    display[0] += ' ' * 10 + player_name + '\'s' + ' Ships'
    display[1] += ' ' * 10 + '-' * 20

    for row in range(len(ships)):
        display[row+2] += (' ' * 10 + str(row+1) + '. '
            + ships[row]['name'])

    return display  

def fire_weapon(player_name, BOARD_SIZE, SHIP_LENGTH, header,
        ships, board, radar, enemy_ships, enemy_board, enemy_radar, turn_ctr, 
        ai=False):

    game_on = True

    # Loop until user enters a valid space
    valid = False
    status_msg = ''

    while not valid:
        if not ai:
            # Ship entry display
            # Title
            print 'In Battle, Round #' + str(turn_ctr / 2 + 1)
            print '-' * 52
            print player_name + '\'s turn...'
            print

            # Print main display
            display = fire_weapon_display(BOARD_SIZE, SHIP_LENGTH, header, board,
                radar, ships, enemy_ships)

            for d in display:
                print d

            print status_msg

        # Reset status message
        status_msg = ''

        if not ai:
            # User input coordinates
            coord = raw_input('Enter target coordinates: ')

            # Convert entered coordinates to grid indices
            try:
                # Convert x-axis letter to int
                coord_x = ord(coord[0].upper()) - 65
            except IndexError:
                coord_x = -1
            try:
                # Subtract 1 from y-axis number
                coord_y = int(coord[1:]) - 1
            except ValueError:
                coord_y = -1
        else:
            # Randomly generated coordinates
            coord_x = randint(0, BOARD_SIZE)
            coord_y = randint(0, BOARD_SIZE)

        # Check if coordinates are inside board
        if not ((coord_x >= 0 and coord_x < BOARD_SIZE) and 
                (coord_y >= 0 and coord_y < BOARD_SIZE)):
            status_msg = 'Invalid coordinates'
        else:
            # Check if spot is free
            if radar[coord_y][coord_x] != '-':
                status_msg = 'You\'ve already tried that spot'
            else:
                valid = True

        if not ai:
            os.system('cls')

    # Valid move
    # Check if hit or miss
    hit = False
    for i in enemy_ships:
        if [coord_x, coord_y] in i['location']:
            # Hit
            hit = True
            status_msg = 'Hit'
            # Remove piece from location array
            i['location'].remove([coord_x, coord_y])
            # Mark radar
            radar[coord_y][coord_x] = 'x'
            enemy_board[coord_y][coord_x] = 'x'
            # If all pieces removed, ship is sunk
            if not i['location']:
                status_msg = i['name'] + ' has sunk!'
            break

    if not hit:
        # Miss
        status_msg = 'Miss'
        #Mark radar
        radar[coord_y][coord_x] = 'o'
        enemy_board[coord_y][coord_x] = 'o'

    # At end of turn, check score
    rem_hits = 0
    for i in enemy_ships:
        rem_hits += len(i['location'])
    
    if rem_hits == 0:
        # No enemy ships left, game over
        game_on = False

    if not ai:
        print 'In Battle, Round #' + str(turn_ctr / 2 + 1)
        print '-' * 52
        print player_name + '\'s turn...'
        print

        # Print main display
        display = fire_weapon_display(BOARD_SIZE, SHIP_LENGTH, header, board,
            radar, ships, enemy_ships)
    
        for d in display:
            print d

    # Print status message
    if ai:
        # Title
        print 'In Battle, Round #' + str(turn_ctr / 2 + 1)
        print '-' * 52
        print player_name + '\'s turn...'
        print        
        print '---------------------------------------=----------------------------------------'
        print '--------------------------------------===---------------------------------------'
        print '-------------------------------------=====--------------------------------------'
        print '------------------------------------=======-------------------------------------'
        print '------------------------------====-=========-===--------------------------------'
        print '-------------------------=====----==========----====----------------------------'
        print '-----------------------==--------============-------==--------------------------'
        print '---------------------==---------==============--------==------------------------'
        print '--------------------=-----------==============----------=-----------------------'
        print '---------------------=---------=========-======--------==-----------------------'
        print '----------------------==------=======------====------==-------------------------'
        print '------------------------===---====----------====---==---------------------------'
        print '---------------------------=====--------------=====-----------------------------'
        print '------------------------+-----------------------------+-------------------------'
        print '------------------------|      ' + player_name + ' FIRING!...     |' + '-' * (24 - (len(player_name) - 8))
        print '------------------------+-----------------------------+-------------------------'
        print '--------------------------------------------------------------------------------'    

        time.sleep(1)

        status_msg = 'Computer Move: ' + chr(coord_x + 65).upper() + str(coord_y+1) + ' ' + status_msg
    else:
        status_msg = 'Your Move: ' + chr(coord_x + 65).upper() + str(coord_y+1) + ' ' + status_msg
        print

    
    print status_msg

    time.sleep(1.5)
    os.system('cls')

    return game_on

def fire_weapon_display(BOARD_SIZE, SHIP_LENGTH, header, board, radar, ships,
        enemy_ships):
    # First column
    display = []
    # Header
    display.append('   ' + 'Map' + '  ' * BOARD_SIZE + '     ' + 'Radar')
    display.append(
        ' '.join([str(x) for x in header]).rjust(BOARD_SIZE * 2 + 2) +
        '  ||  ' +
        ' '.join([str(x) for x in header]).rjust(BOARD_SIZE * 2 + 2)
    )
    # Board
    for row in range(BOARD_SIZE):
        display.append(
            str(row+1).rjust(2) + ' '.join(board[row]).rjust(BOARD_SIZE * 2) +
            '  ||  ' +
            str(row+1).rjust(2) + ' '.join(radar[row]).rjust(BOARD_SIZE * 2)
        )

    # Second column
    # Status board
    disp_ctr = 1
    display[disp_ctr] += ' ' * 5 + 'Your Ships'
    disp_ctr += 1
    display[disp_ctr] += ' ' * 5 + '-' * 20
    offset = len(display[disp_ctr])

    for row in range(len(ships)):
        disp_ctr += 1
        label = (' [' + str(len(ships[row]['location'])) + '/' + 
            str(SHIP_LENGTH) + ']')
        if len(ships[row]['location']) == 0:
            label = ' [SUNK]'

        display[disp_ctr] += (' ' * 5 + str(row+1) + '. ' +
            ships[row]['name'] + label)

    # Third column
    disp_ctr = 1
    display[disp_ctr] += ' ' * 25 + 'Enemy Ships'
    disp_ctr += 1
    display[disp_ctr] += ' ' * 15 + '-' * 20

    for row in range(len(enemy_ships)):
        disp_ctr += 1
        label = (' [' + str(len(enemy_ships[row]['location'])) + '/' + 
            str(SHIP_LENGTH) + ']')
        if len(enemy_ships[row]['location']) == 0:
            label = ' [SUNK]'

        spacing = (offset + 15) - len(display[disp_ctr])
            
        display[disp_ctr] += (' ' * spacing + str(row+1) + '. ' +
            enemy_ships[row]['name'] + label)

    return display

if __name__ == '__main__':
    main()
