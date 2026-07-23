[app]

# (str) Title of your application
title = Flashlight App

# (str) Package name
package.name = flashlightapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it point to current directory)
source.dir = .


# (list) Source files to exclude
source.exclude_exts = spec

# (list) List of inclusions using glob patterns
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = CAMERA

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android and python lib to use
android.ndk_api = 21

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Automatically accept SDK license
android.accept_sdk_license = True
