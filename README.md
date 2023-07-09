# AlbumDreamer
## (Click [**HERE**](https://albumdreamer.netlify.app/) to check out the demo website)


https://github.com/lucmaki/AlbumDreamer/assets/26182176/c0d0be82-0cba-4abc-bbcd-ae055b1752be

## TLDR
A generative AI Pipeline that employs text-to-text, text-to-image and text-to-music models for creating musical albums for any concept of our choosing. The planning phase before generating allows the album's tracks to be diverse and narratively tied.

## Features
- **Text2Text Director for Multimodal Coherence**: A text2text model (recommended GPT4) serves as a director: analysing the concept, planning the soundscape, generating content including image and music prompts so that everything fits together with a kind of narrative flow.
- **Modular Director**: This director can easily be tweaked thanks to loose modular prompt templates. The user might want to input more data than just "the concept", if wants more advanced control over the creation process.
- **30sec Tracks**: With MusicGen model, 30s is the maximum for the context window. Using a sliding window, we can go beyond but with lowered temporal coherence. 
- **Stylized Images**: We employ a fine-tuned text2img model + custom Lora + textual inversion + custom prompt, for further stylization. 
- **SQL Storage**: Pipeline generations can be stored in a SQL database with some setup.
  
## Results
For now no eval has been performed, but you can judge the demo website's albums which were not cherry picked and generated with no supervision except for the varied topics picked.

Specs wise, all models but the GPT-4 model used are open source (so, a high amount of control and customization is possible) and small enough for each to be loadable within 16GB VRAM. Also, the time to generate an album depends on hardware and whether models are preloaded. With a Nvidia V100 GPU and subtracting time to load models into memory, it takes around 5 minutes to generate an album of five tracks.

## Why?
Models are finally accessible for the triad of "text-to-X" modalities (text, visual and audio), I sought to combine their power into a project showcasing how combining multiple modalities can create a multi-sensory narrative experience that stimulates creativity while maintaining coherence.

For technical accomplishments: one of the main challenges for this project was consistency of quality, coherence and creativity in the face of long and multimodal generations. The project appears successful in that regard.
