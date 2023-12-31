# AlbumDreamer
## (Click [**HERE**](https://albumdreamer.netlify.app/) to check out the demo website)


https://github.com/lucmaki/AlbumDreamer/assets/26182176/c0d0be82-0cba-4abc-bbcd-ae055b1752be

## TLDR
A generative AI Pipeline that employs text-to-text, text-to-image and text-to-music models for creating musical albums for any concept of our choosing. Through an AI director planning phase, the album's tracks gain cohesion between one another, with diversity and narrative flows.

## Features
- **Overarching Director**: A text2text model directs: it analyses the concept, plans the soundscape and generates prompts. All to allow coherence and narrative for the album's components.
- **Modular Director**: The director can easily be tweaked thanks to loose modular prompt templates. For example: for inputting more data than just "the concept" or using GPT-4's browsing capabilities.
- **30sec Tracks**: With MusicGen model, 30s is the maximum for the context window. Going beyond with a sliding window leads to lowered temporal coherence. 
- **Stylized Images**: We employ a fine-tuned text2img model + custom Lora + textual inversion + custom prompt, for further stylization. 
- **SQL Storage**: For mass generation with the pipeline. Requires additional setup for image and music storage.
  
## Results
You can qualitatively judge the demo website's albums which were not cherry picked and generated with no supervision except for the choice of topics.

Specs wise, all models but the GPT-4 model used are open source (so, a high amount of control and customization is possible) and small enough for each to be loadable within 16GB VRAM. Also, the time to generate an album depends on hardware and whether models are preloaded. With a Nvidia V100 GPU and subtracting time to load models into memory, it takes around 5 minutes to generate an album of five tracks.

## Why?
Models are finally accessible for the triad of "text-to-X" modalities (text, visual and audio), I aimed to combine their capabilities into a project showcasing how multiple generative modalities used together can create a multi-sensory narrative experience that's creatively stimulating and with high coherence.

For technical accomplishments: one of the main challenges for this project was consistency of quality, coherence and creativity in the face of long and multimodal generations. The project appears successful in that regard.
