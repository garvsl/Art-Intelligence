
#Inspiration:

Art Intelligence is the first-ever museum dedicated solely to art created by artificial intelligence. With Art Intelligence, you can voice your creations and watch them come to life. Art Intelligence was created for those with an imagination greater than their artistic ability; as well as those who may be unable to create art physically [ex: people with ALS, Cerebral Palsy, High on the Autism Spectrum].

#What it does:

-Generative AI - Program that can use existing content like text, audio files, or images to create new plausible content.

-Art Intelligence uses Generative AI’s text -> image specialty to generate art from a text prompt.

-The text prompt is provided via our implemented windows voice->text recognition code through JS.

-Our Dall*E API runs a text prompt through a text encoder, which is then mapped [via a model called prior] to a corresponding image encoder that captures the semantic information contained in the text encoding; an image decoder generates an image which is a visual representation of this semantic information.

-Afterwards the images are stored and uploaded to Estuary, and posted on our website.

#How we built it:

We used Python, Dalle AI (text encoding), WebSpeech API (voice/assistant), and Estuary (storing creations). We developed the site in Javascript, HTML, and CSS.

#Challenges we ran into

The Dalle API was just released and there was not enough documentation and our back-end specialist had to learn it. There were also issues with Estuary, which we had to speak to them in order to resolve.

#Accomplishments that we're proud of

This is our first hackathon for some of us, so submitting our project is something we are proud of.

#What we learned

We learned about AI image generation and how to transform voice into text, which most of us had never used before. Also, we learned how to connect front-end and back-end code and store data in Estuary. It was a great learning experience!

#What's next for AI Art Museum

We would like to perfect the system, make it more beautiful, and improve its speed.
