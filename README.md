Tutorial 1: Integrate Uploadcare widget
=======================================

This tutorial describes full front-end integration process
for the base case, which only takes a few minutes!
    
See the video: https://vimeo.com/103210116

Emulating HTTP Server
---------------------

To run the Simple HTTP Server, go to the root directory of this project,
and type:

    python server.py 2343

Then type in your browser address line:

http://127.0.0.1:2343

Workaround: without HTTP Server
-------------------------------

The Simple HTTP Server requires Python to be installed in your system
(see http://python.org). If you don't have it, just replace the line in `index.html`:

    <form action="thanks.html" method="post" role="form">

with:

    <form action="http://example.com" method="post" role="form">

and open the `index.html` file in your browser.

Integration Steps
-----------------

1. Signup at https://uploadcare.com
2. Go to Dashboard: https://uploadcare.com/dashboard/
3. Create a new project (or select an existing one)
4. Click on "Widget" menu item
5. Scroll down to the "Integration" section
6. Copy the first code snippet into header of your HTML file (in this example it's `index.html`)
7. Copy the second snippet, and replace your file input with it. Remember to specify correct "name" attribute.
8. Reload your page!
