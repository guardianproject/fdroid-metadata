
accepted_formats = ['txt', 'yml']

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
