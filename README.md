Tutorial 1: Integrate Uploadcare widget in a few minutes
========================================================

This tutorial describes full front-end integration process
for the base case. See the video:

https://vimeo.com/103210116

Emulating HTTP Server
---------------------

To run the Simple HTTP Server, go to the root directory of this project,
and type:

    python server.py 2343

Or just this:

    make

Then type in your browser address line:

http://127.0.0.1:2343

Workaround: without HTTP Server
-------------------------------

The Simple HTTP Server requires Python to be installed in your system
(see http://python.org). If you don't have it, just replace the line in `index.html`:

    <form action="thanks.html" method="post" role="form">

with:

    <form action="http://example.com" method="post" role="form">

and open the `index.html` file.
