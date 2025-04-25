// runScraper.mjs
import { scraper } from "google-maps-review-scraper";

const run = async () => {
  try {
    const reviews = await scraper("https://www.google.com/maps/place/Coffee+Bean", {
      sort_type: "relevent",          // or "highest_rating", "lowest_rating"
      search_query: "string",             // can be "" or a keyword to filter
      pages: 10,                     // how many pages of reviews
      clean: false                  // set to true if you want cleaned data
    });

    console.log(reviews);
  } catch (err) {
    console.error("Error scraping reviews:", err);
  }
};

run();
