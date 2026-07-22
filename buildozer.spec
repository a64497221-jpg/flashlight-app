[app]

# (str) Title of your application
title = Flashlight App

# (str) Package name
package.name = flashlightapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it point to current directory)
source.dir = .

# (list) Source files to exclude (let it empty)
source.exclude_exts = spec

# (list) List of inclusions using glob patterns
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add kivy and other dependencies your app needs here
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = CAMERA

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android and python lib to use
android.ndk_api = 21

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a
