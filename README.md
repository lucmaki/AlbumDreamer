# AlbumDreamer
## (Click [**HERE**](https://albumdreamer.netlify.app/) to check out the demo website)


https://github.com/lucmaki/AlbumDreamer/assets/26182176/c0d0be82-0cba-4abc-bbcd-ae055b1752be

## TLDR
An AI Pipeline that employs text, images, music generation for creating musical albums for any concept of our choosing.

## Features
- **Multimodal Coherence through Text2Text Director**: We have a text2text model serve as director: planning the narrative, soundscape and generate content for image and music prompts that fit with one another. This director can easily be tweaked so that the user can guide the album creation process further than just "giving the concept"!
- **30s Tracks**: With MusicGen model, 30s is the maximum for the context window. Using a sliding window, we can go beyond but with lowered temporal coherence. 
- **Stylistic Visuals**: A fine-tuned text2img model + Lora are utilized to create a personalized style. 
- **Website building**: Pages can be automatically built out of album data to be served through a static website.
- **Database building**: (WIP) Pipeline feeds into an SQL database for further processing/distribution.
  
## Why?
Powerful open source models are finally accessible for the triad of "text-to-X" modalities (text, visual and audio), I sought to combine their power into an artistic project showcases how combining multiple modalities can create a multi-sensory narrative experience that stimulates creativity while maintaining coherence. 

For technical accomplishments: one of the main challenges this project aimed to surpass is consistency of quality and coherence in the face of long and multimodal generations. This process was successful; the results on the demo website not being cherry picked.
