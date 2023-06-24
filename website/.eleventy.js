module.exports = function(eleventyConfig) {
  eleventyConfig.addPassthroughCopy("albums");
  eleventyConfig.addPassthroughCopy("css");
  eleventyConfig.addPassthroughCopy("logo.png");

  eleventyConfig.addCollection("albums", function(collection) {
    return collection.getFilteredByGlob("albums.json");
  });

  return {
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      data: "_data"
    }
  };
};