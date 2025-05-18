import tkinter as tk
from tkinter import ttk
from logic.ship import SHIPS
from logic.board import Board

class Window:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self._show_rules()
        self._build_components()
        self.render()
        self.root.mainloop()
    
    def _show_rules(self):
        rules = tk.Toplevel(self.root)
        rules.title('Game Rules')

        rules_text = (
            "Welcome to Battleship!\n\n"
            "1. There are two players: you and the bot.\n"
            "2. Each player has a 10x10 board.\n"
            "3. You will place your ships on the board first.\n"
            "4. Ships cannot overlap and must fit within the board.\n"
            "5. The players will take turns shooting at each other's boards.\n"
            "6. A hit is marked in red, a miss in blue.\n"
            "7. A hit, allows you to continue shooting until you miss.\n"
            "8. The first player to sink all the opponent's ships wins.\n"
        )

        tk.Label(rules, text=rules_text, justify=tk.LEFT, padx=10, pady=10).pack()
        tk.Button(rules, text="Ok", command=rules.destroy).pack(pady=(0,10))
        rules.grab_set()
        self.root.wait_window(rules)

    def _build_components(self):
        self.bot_frame = tk.Frame(self.root)
        self.bot_frame.grid(row=0, column=0, columnspan=2)
        self.spacer = tk.Frame(self.root, height=20)
        self.spacer.grid(row=1)
        self.player_frame = tk.Frame(self.root)
        self.player_frame.grid(row=2, column=0, columnspan=2)

        self.bot_buttons = self._make_grid(self.bot_frame, self.handle_bot_click)
        self.player_buttons = self._make_grid(self.player_frame, self.handle_player_click)

        self.status = tk.Label(self.root, text='')
        self.status.grid(row=3, column=0, columnspan=2)
        
        self.orientation_variable = tk.StringVar(self.root)
        self.orientation_menu = tk.OptionMenu(self.root, self.orientation_variable, *SHIPS[0][2])
        self.orientation_menu.grid(row=4, column=0, columnspan=2, pady=5)

    def _make_grid(self, frame, command):
        buttons = []
        for row in range(self.game.size):
            button_row = []
            for col in range(self.game.size):
                button = tk.Button(frame, width=2, command=lambda R=row, C=col: command(R, C))
                button.grid(row=row, column=col)
                button_row.append(button)
            buttons.append(button_row)
        return buttons

    def handle_player_click(self, row, col):
        # if the game is not in playing state, exit
        if self.game.state != 'placing':
            return

        orientation = self.orientation_variable.get()
        if self.game.player_place_ship(row, col, orientation):
            self.render()
            if self.game.state == 'playing':
                self.orientation_menu.grid_remove()
                self.status.config(text='Take your shot!')

    def handle_bot_click(self, row, col):
        # if the game is not in playing state, exit
        if self.game.state != 'playing' or not self.game.player_turn:
            return

        # take a shot, handle the result
        shot_result = self.game.player_shot(row, col)

        if shot_result == 'hit':
            self.status.config(text='Hit! Shoot again')
        elif shot_result == 'miss':
            self.status.config(text='Miss! Bot is shooting')
            self.root.after(500, self._bot_turn)
        elif shot_result == 'win':
            self.status.config(text='Winner! great job!')
            self._end_game()
        self.render()
    
    def _bot_turn(self):
        # take a shot, handle the result
        shot_result = self.game.bot_shot()

        if shot_result == 'hit':
            self.status.config(text='Hit! Bot is shooting')
            self.root.after(500, self._bot_turn)
            return
        elif shot_result == 'miss':
            self.status.config(text='Take your shot!')
        elif shot_result == 'lose':
            self.status.config(text='Game Over! the bot won')
            self._end_game()
        self.render()

    def _end_game(self):
        # disable all buttons at the end of the game
        for button in sum(self.bot_buttons, []) + sum(self.player_buttons, []):
            button.config(state=tk.DISABLED)

    def render(self):
        # update the ui based on game state
        for row in range(self.game.size):
            for col in range(self.game.size):
                state = self.game.bot_board.grid[row][col]
                button = self.bot_buttons[row][col]

                if state == Board.HIT:
                    button.config(bg='red')
                elif state == Board.MISS:
                    button.config(bg='blue')
                else:
                    button.config(bg='lightgrey')

        for row in range(self.game.size):
            for col in range(self.game.size):
                state = self.game.player_board.grid[row][col]
                button = self.player_buttons[row][col]

                if state == Board.HIT:
                    button.config(bg='red')
                elif state == Board.MISS:
                    button.config(bg='blue')
                elif state == Board.SHIP:
                    button.config(bg='grey')
                else:
                    button.config(bg='lightgrey')

        if self.game.state == 'placing':
            name, _, directions = SHIPS[self.game.ship_index]
            self.status.config(text=f"Place {name}")
            menu = self.orientation_menu['menu']
            menu.delete(0, 'end')
            for direction in directions:
                menu.add_command(label=direction, command=lambda v=direction: self.orientation_variable.set(v))
            self.orientation_variable.set(directions[0])



