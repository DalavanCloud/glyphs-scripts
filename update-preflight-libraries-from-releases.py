#MenuTitle: Update the preflight libraries from releases (pysilfont from master) py2
# -*- coding: utf-8 -*-
__doc__="""
Update the preflight libraries from releases (pysilfont from master) py2
"""

__copyright__ = 'Copyright (c) 2018, SIL International  (http://www.sil.org)'
__license__ = 'Released under the MIT License (http://opensource.org/licenses/MIT)'
__author__ = 'Nicolas Spalinger'

# using brew and sudo we expect launchers to be put into /usr/local/bin/ and the libs in /usr/local/lib
# but if you install manually with --user you will need to add ~/Library/Python/2.7/bin to your PATH in ~/.bash_profile


import GlyphsApp
from subprocess import Popen, PIPE


def runAppleScript(scpt, args=[]):
	p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr = p.communicate(scpt)
	if stderr:
		print "AppleScript Error:"
		print stderr.decode('utf-8')
	return stdout


preflightupdate = """

tell application "Finder"

	tell application "Terminal"

		activate

		tell window 1

	        	do script "which python; python --version; python2.7 -m pip --version; sudo python2.7 -m pip uninstall --yes pysilfont glyphsLib fontTools mutatorMath ufoLib defcon fontMath; sudo python2.7 -m pip install --upgrade --no-cache-dir git+https://github.com/silnrsi/pysilfont.git@master#egg=pysilfont git+https://github.com/googlei18n/GlyphsLib.git@v2.4.0#egg=glyphsLib fontTools mutatorMath ufoLib defcon fontMath ;  psfversion "

		end tell

	end tell

end tell

tell application "Finder"
	display notification "Updating, enter your password." with title "Preflight dependencies" sound name "default"
end tell

tell application "Finder"
	display notification "Libraries versions: see output" with title "Preflight dependencies versions"
end tell

tell application "Finder"
	display notification "Watch for issues, when done close the window" with title "Installation issues"
end tell



"""

save   = runAppleScript( preflightupdate )
