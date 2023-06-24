# AlbumDreamer
## (Click [**HERE**](https://albumdreamer.netlify.app/) to check out the demo website)


https://github.com/lucmaki/AlbumDreamer/assets/26182176/c0d0be82-0cba-4abc-bbcd-ae055b1752be

## TLDR
An AI Pipeline that employs text, images, music generation for creating musical albums for any concept of our choosing.

## Features
- **Text2Text Director for Multimodal Coherence**: A text2text model (recommended GPT4) serves as a director: analysing the concept, planning the soundscape, generating content including image and music prompts so that everything fits together.
- **Modular Director**: This director can easily be tweaked thanks to loose modular prompt templates. The user might want to input more data than just "the concept", if wants more advanced control over the creation process.
- **30s Tracks**: With MusicGen model, 30s is the maximum for the context window. Using a sliding window, we can go beyond but with lowered temporal coherence. 
- **Stylistic Visuals**: While the director controls the prompt, part of the prompt is fixed based on our configuration for consistent style. In our case, we also employed a fine-tuned text2img model + custom Lora for further stylization. 
- **Website building**: Pages can be automatically built out of album data to be served through a static website.
- **Database building**: (WIP) Pipeline feeds into an SQL database for further processing/distribution.
  
## Why?
Powerful open source models are finally accessible for the triad of "text-to-X" modalities (text, visual and audio), I sought to combine their power into a project showcasing how combining multiple modalities can create a multi-sensory narrative experience that stimulates creativity while maintaining coherence. 

For technical accomplishments: one of the main challenges for this project was consistency of quality, coherence and creativity in the face of long and multimodal generations. The project appears successful in taht regard; the results on the demo website are not cherry picked and were created with no supervisation.
