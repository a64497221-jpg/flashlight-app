[app]

# (str) Title of your application
title = Flashlight App

# (str) Package name
package.name = flashlightapp

# (str) Package domain (needed for android packaging)
package.domain = org.flashlight

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# تأكد من إضافة الحزم التي يحتاجها تطبيقك مثل plyer
requirements = python3,kivy,plyer

# (str) Supported orientations
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
