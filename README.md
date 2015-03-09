qr-tickets
==========

Encrypted QR (Quick Response) Code Tickets

This program requires Tkinter, qrcode, and Pillow (Python Image Library)
All other imports should be included in Python. (As of Python v2.7.)

This programs purpose is to take information specific to both, but seperately, the customer and supplier of the tickets. After this information is accepted, it generates an encrypted string (the algorithm can be changed.)
The string, as well as information that is relevent to the customer (for identity validation) is used to generate a QR (Quick Response) Code for rapid validation.
The information is saved in a text file as well. (This might be changed or usefull as-is in the future.)

I originally intended to only keep this for private use. However, I feel that this could be useful to others so I decided to share it.


** This software uses GNU General Public License Version 2 **
** License is included in "License.md" **
