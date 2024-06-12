import platform

from utils.opener import open_urls_for_macos, open_urls_for_windows

OS_HANDLERS = {
    "Darwin": open_urls_for_macos,
    "Windows": open_urls_for_windows
}


def open_urls():
    current_os = platform.system()
    handler = OS_HANDLERS.get(current_os, lambda: print(f"Unknown operating system: {current_os}"))
    handler()  # Call the handler function
