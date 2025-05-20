[app]
# (str) Title of your application
title = Android Evolutivo

# (str) Package name
package.name = androidevolutivo

# (str) Package domain (unique, reverse-DNS style)
package.domain = org.eduartoba

# (str) Source code directory ('.' if your main.py is in root)
source.dir = .

# (str) Application versioning
version = 0.1

# (str) Application entry point
entrypoint = main.py

# (list) Permissions
android.permissions = INTERNET

# (list) Requirements (libraries used)
requirements = python3,kivy

# (str) Application icon (optional)
# icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash (optional)
# presplash.filename = %(source.dir)s/data/presplash.png

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
orientation = portrait
fullscreen = 1
android.arch = armeabi-v7a

# (bool) Enable android logcat during build
android.logcat = 1

# (bool) Enable debug
android.debug = 1

# (str) Python version to use
android.python3 = True
