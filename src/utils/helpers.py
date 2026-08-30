import string
import secrets
import subprocess
from typing import Optional, Callable

def generate_password(length: int = 16, use_upper: bool = True, use_digits: bool = True, 
                      use_symbols: bool = True, exclude_ambiguous: bool = False) -> str:
    """
    Generates a cryptographically secure random password using secrets.
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if exclude_ambiguous:
        # Exclude characters: l, 1, I, o, 0, O, |, etc.
        lowercase = "".join(c for c in lowercase if c not in "lo")
        uppercase = "".join(c for c in uppercase if c not in "IO")
        digits = "".join(c for c in digits if c not in "01")
        symbols = "".join(c for c in symbols if c not in "|`'\",.")

    chars = lowercase
    # Keep track of required charsets to ensure representation
    required_sets = [lowercase]
    
    if use_upper:
        chars += uppercase
        required_sets.append(uppercase)
    if use_digits:
        chars += digits
        required_sets.append(digits)
    if use_symbols:
        chars += symbols
        required_sets.append(symbols)

    # Generate characters
    password = []
    # Guarantee at least one char from each requested set
    for char_set in required_sets:
        password.append(secrets.choice(char_set))

    # Fill up the rest of the password
    for _ in range(length - len(password)):
        password.append(secrets.choice(chars))

    # Shuffle the password list using CSPRNG to mix up the guaranteed chars
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

def _set_clipboard(text: str, app=None):
    """Copies text using pyperclip, pbcopy (macOS), or Tkinter clipboard."""
    # 1. Try pyperclip if installed
    try:
        import pyperclip
        pyperclip.copy(text)
        return
    except Exception:
        pass

    # 2. Try macOS pbcopy
    try:
        p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        p.communicate(input=str(text).encode('utf-8'))
        return
    except Exception:
        pass

    # 3. Try Tkinter clipboard fallback
    if app:
        try:
            app.clipboard_clear()
            app.clipboard_append(text)
            app.update()
        except Exception:
            pass

def _get_clipboard(app=None) -> str:
    """Reads clipboard text using pyperclip, pbpaste (macOS), or Tkinter clipboard."""
    try:
        import pyperclip
        return pyperclip.paste()
    except Exception:
        pass

    try:
        p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
        out, _ = p.communicate()
        return out.decode('utf-8')
    except Exception:
        pass

    if app:
        try:
            return app.clipboard_get()
        except Exception:
            pass
    return ""

def copy_to_clipboard(text: str, app, on_clear_callback: Optional[Callable[[], None]] = None):
    """
    Copies text to clipboard and schedules it to clear in 30 seconds
    if the clipboard content hasn't changed.
    """
    _set_clipboard(text, app)
    
    def clear_clipboard():
        try:
            current_clipboard = _get_clipboard(app)
            # Only clear if the user hasn't copied anything else in the meantime
            if current_clipboard == text:
                _set_clipboard("", app)
                if on_clear_callback:
                    on_clear_callback()
        except Exception as e:
            print(f"Failed to clear clipboard: {e}")

    # Schedule clearing in 30,000 milliseconds (30 seconds)
    if hasattr(app, 'after'):
        app.after(30000, clear_clipboard)
