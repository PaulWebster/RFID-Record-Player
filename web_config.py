from pathlib import Path
import warnings


_PORT_FILE = Path(__file__).with_name("web_port.conf")
_DEFAULT_WEB_PORT = 8080

try:
    WEB_PORT = int(_PORT_FILE.read_text(encoding="ascii").strip())
    if not 1 <= WEB_PORT <= 65535:
        raise ValueError("port must be between 1 and 65535")
except (OSError, ValueError) as e:
    warnings.warn(
        f"Unable to read a valid web port from {_PORT_FILE}: {e}; using {_DEFAULT_WEB_PORT}",
        RuntimeWarning,
        stacklevel=2,
    )
    WEB_PORT = _DEFAULT_WEB_PORT
