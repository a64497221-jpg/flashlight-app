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
# إزالة أو تعديل حسب الحاجة
# source.exclude_exts = spec

# (list) List of inclusions using glob patterns
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# أنصح بتحديد نسخة Kivy المناسبة إذا تظهر أخطاء
requirements = python3,kivy==2.1.0

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

# (str) Android NDK version to use (تأكد من دعم هذه النسخة في بيئتك)
android.ndk = 25b

# (str) Android and python lib to use
android.ndk_api = 21

# (str) The Android arch to build for (مفصولة بفاصلة بدون فراغات)
android.archs = armeabi-v7a

# (bool) Automatically accept SDK license
android.accept_sdk_license = True

# (int) مستوى السجل للتشخيص
log_level = 2
