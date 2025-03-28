# Copyright (c) 2022-2024 José Manuel Barroso Galindo <theypsilon@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# You can download the latest version of this tool from:
# https://github.com/theypsilon/Update_All_MiSTer

# Default SSL option
from enum import unique, Enum

# From patreon.com/theypsilon
supporter_plus_patrons = ('Alex Frégeau', 'Luca Fiandri', "The Sentinel's Playground Team", 'Thomas Williams', 'Wayne Booker')

# Default options
DEFAULT_CURL_SSL_OPTIONS = '--cacert /etc/ssl/certs/cacert.pem'
DEFAULT_COMMIT = 'unknown'
DEFAULT_LOCATION_STR = 'MiSTer'
DEFAULT_DEBUG = 'false'
DEFAULT_KEY_IGNORE_TIME = '0.1'
DEFAULT_TRANSITION_SERVICE_ONLY = 'false'

MISTER_ENVIRONMENT = 'mister'
STANDARD_UI_THEME = 'Blue Installer'

# Downloader files
FILE_update_all_pyz = 'Scripts/.config/update_all/update_all.pyz'
FILE_update_all_zipped_storage = 'Scripts/.config/update_all/update_all.json.zip'
FILE_update_all_storage = 'Scripts/.config/update_all/update_all.json'
FILE_update_all_log = 'Scripts/.config/update_all/update_all.log'
FILE_update_all_ini = 'Scripts/update_all.ini'
FILE_update_jtcores_ini = 'Scripts/update_jtcores.ini'
FILE_update_jtcores_sh = 'Scripts/update_jtcores.sh'
FILE_update_names_txt_ini = 'Scripts/update_names-txt.ini'
FILE_update_names_txt_sh = 'Scripts/update_names-txt.sh'
FILE_MiSTer = 'MiSTer'
FILE_MiSTer_delme = '.MiSTer.delme'
FILE_MiSTer_ini = 'MiSTer.ini'
FOLDER_scripts = 'Scripts'
FOLDER_scripts_config_lc = 'scripts/.config'
FILE_downloader_temp_ini = '/tmp/downloader_temp.ini'

# Reboot files
FILE_downloader_needs_reboot_after_linux_update = '/tmp/downloader_needs_reboot_after_linux_update'
FILE_mister_downloader_needs_reboot = '/tmp/MiSTer_downloader_needs_reboot'

MEDIA_FAT = '/media/fat'

# Dictionary Keys:

# Config
K_BASE_PATH = 'base_path'
K_BASE_SYSTEM_PATH = 'base_system_path'
K_STORAGE_PRIORITY = 'storage_priority'
K_DATABASES = 'databases'
K_ALLOW_DELETE = 'allow_delete'
K_ALLOW_REBOOT = 'allow_reboot'
K_UPDATE_LINUX = 'update_linux'
K_PARALLEL_UPDATE = 'parallel_update'
K_DOWNLOADER_SIZE_MB_LIMIT = 'downloader_size_mb_limit'
K_DOWNLOADER_PROCESS_LIMIT = 'downloader_process_limit'
K_DOWNLOADER_TIMEOUT = 'downloader_timeout'
K_DOWNLOADER_RETRIES = 'downloader_retries'
K_ZIP_FILE_COUNT_THRESHOLD = 'zip_file_count_threshold'
K_ZIP_ACCUMULATED_MB_THRESHOLD = 'zip_accumulated_mb_threshold'
K_FILTER = 'filter'
K_VERBOSE = 'verbose'
K_CONFIG_PATH = 'config_path'
K_USER_DEFINED_OPTIONS = 'user_defined_options'
K_CURL_SSL = 'curl_ssl'
K_DB_URL = 'db_url'
K_SECTION = 'section'
K_OPTIONS = 'options'
K_DEBUG = 'debug'
K_FAIL_ON_FILE_ERROR = 'fail_on_file_error'
K_COMMIT = 'commit'
K_DEFAULT_DB_ID = 'default_db_id'
K_START_TIME = 'start_time'

# Update All old options
K_COUNTDOWN_TIME = "countdown_time"
K_WAIT_TIME_FOR_READING = "wait_time_for_reading"
K_AUTOREBOOT = "autoreboot"
K_KEEP_USBMOUNT_CONF = "keep_usbmount_conf"


# Env
KENV_CURL_SSL = 'CURL_SSL'
KENV_COMMIT = 'COMMIT'
KENV_LOCATION_STR = 'LOCATION_STR'
KENV_DEBUG = 'DEBUG'
KENV_KEY_IGNORE_TIME = 'KEY_IGNORE_TIME'
KENV_TRANSITION_SERVICE_ONLY = 'TRANSITION_SERVICE_ONLY'

# Exit codes
EXIT_CODE_REQUIRES_EARLY_EXIT = 1
EXIT_CODE_CAN_CONTINUE = 2

@unique
class PathType(Enum):
    FILE = 0
    FOLDER = 1


# Update All old constants
UPDATE_ALL_VERSION = "2.2"
MISTER_DOWNLOADER_VERSION = "2.1"
ARCADE_ORGANIZER_INSTALLED_NAMES_TXT = "Scripts/.config/arcade-organizer/installed_names.txt"
ARCADE_ORGANIZER_INI = "Scripts/update_arcade-organizer.ini"
DOWNLOADER_URL = "https://github.com/MiSTer-devel/Downloader_MiSTer/releases/download/latest/dont_download.zip"
DOWNLOADER_INI_STANDARD_PATH = "downloader.ini"
DOWNLOADER_STORE_STANDARD_PATH = "Scripts/.config/downloader/downloader.json"
DOWNLOADER_LATEST_ZIP_PATH = "Scripts/.config/downloader/downloader_latest.zip"
TEST_UNSTABLE_SPINNER_FIRMWARE_MD5 = "b76bc57d75afce8b1040bc4d225ea3aa"
