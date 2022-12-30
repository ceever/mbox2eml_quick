# mbox2eml_quick

**A quick and dirty eml extractor for (thunderbird) mbox files (also finds hidden emails in mbox)**

(Partiularly for cases where emails are not displayed in Thunderbird anymore, but still contained in the mbox file!)

Copyright © 2020 Andrew Jackson (https://github.com/ceever)

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program; if not, write to the Free Software
 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston MA 02110-1301, USA.
 
---
This might not work on all mbox files, but it works on mbox files where each email starts with "From " (space required!). This seems to be the case for Thunderbird mbox files.

Particularly this program help to extract email which are not displayed in Thunderbird anymore but still stored inside the mbox file. This can be useful if you loose your files somehow but discover that your mbox files are still huge. I.e. they are just hidden but still exist.

Note, the easiest way to make sure all emails have been copied to emls is to compare the sizes of the original mbox file and the extracted emls.

---
**BUGS & REQUESTS:**

Send me an email or open a ticket on github.

---
**INSTALLATION:**
* Drop the mbox2eml_quick.py where your mbox files are, make it executable and double-click.
* Alternative run in terminal where you will receive additional information.
* Python 2 required.
