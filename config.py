sdk_path = '/usr/lib/android-sdk'

repo_url = "https://guardianproject.info/fdroid/repo"
repo_name = "Guardian Project Official Releases"
repo_icon = "guardianproject.png"
repo_description = """
The official repository of The Guardian Project apps for use with the F-Droid
client. Applications in this repository are official binaries built by the
original application developers and signed by the same key as the APKs that
are released in the Google Play Store.
"""

# As above, but for the archive repo.
# archive_older sets the number of versions kept in the main repo, with all
# older ones going to the archive. Set it to 0, and there will be no archive
# repository, and no need to define the other archive_ values.
archive_older = 3
archive_url = "https://guardianproject.info/fdroid/archive"
archive_name = "Guardian Project Archive"
archive_icon = "guardianproject.png"
archive_description = """
The official repository of The Guardian Project apps for use with the F-Droid
client. This contains older versions of applications from the main repository.
"""

repo_maxage = 14
update_stats = True

local_copy_dir = '/media/%s/fdroid-shuffler/fdroid' % os.getenv('USER')
sync_from_local_copy_dir = True

mirrors = [
    'https://guardianproject.info/fdroid',
    'http://bdf2wcxujkg6qqff.onion/fdroid',
    'https://s3.amazonaws.com/guardianproject/fdroid',
    'https://guardianproject.s3.amazonaws.com/fdroid',
]

# these two URLs respectively:
# https://guardianproject.info/fdroid/repo
# http://bdf2wcxujkg6qqff.onion/fdroid/repo
serverwebroot = [
    'gpbuilds:/home/members/nfreitas/sites/guardianproject.info/web/fdroid',
    'fdroid@dju2peblv7upfz3q.onion:/srv/mirrors/fdroid',
]

servergitmirrors = [
    'git@gitlab.com:guardianproject/fdroid-repo',
    'git@github.com:guardianproject/fdroid-repo',
]

awsbucket = 'guardianproject'
awsaccesskeyid = os.getenv('awsaccesskeyid')
awssecretkey = os.getenv('awssecretkey')

virustotal_apikey = os.getenv('virustotal_apikey')

# slow and sometimes troublesome
#androidobservatory = True

binary_transparency_remote = 'git@github.com:guardianproject/binary_transparency_log'

