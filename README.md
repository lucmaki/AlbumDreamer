# AlbumDreamer
## (Click [**HERE**](https://albumdreamer.netlify.app/) to check out the demo website)


https://github.com/lucmaki/AlbumDreamer/assets/26182176/c0d0be82-0cba-4abc-bbcd-ae055b1752be

## TLDR
An AI Pipeline that employs text, images, music generation for creating musical albums for any concept of our choosing.

## Features
- **Text2Text Director for Multimodal Coherence**: A text2text model (recommended GPT4) serves as a director: planning the narrative, soundscape and generate content for image and music prompts that fit with one another.
- **Modular Director**: This director can easily be tweaked thanks to loose and modular prompt templates. The user might want to input more data than just "the concept", if wants more advanced control over the creation process.
- **30s Tracks**: With MusicGen model, 30s is the maximum for the context window. Using a sliding window, we can go beyond but with lowered temporal coherence. 
- **Stylistic Visuals**: A fine-tuned text2img model + custom Lora are utilized to create a personalized style for image generations. 
- **Website building**: Pages can be automatically built out of album data to be served through a static website.
- **Database building**: (WIP) Pipeline feeds into an SQL database for further processing/distribution.
  
## Why?
Powerful open source models are finally accessible for the triad of "text-to-X" modalities (text, visual and audio), I sought to combine their power into an artistic project showcases how combining multiple modalities can create a multi-sensory narrative experience that stimulates creativity while maintaining coherence. 

For technical accomplishments: one of the main challenges this project aimed to surpass is consistency of quality and coherence in the face of long and multimodal generations. This process was successful; the results on the demo website not being cherry picked.
