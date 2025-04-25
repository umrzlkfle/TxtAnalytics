// Try.mjs
import { scraper } from "google-maps-review-scraper";
import fs from "fs";
import { parse } from "json2csv";

const run = async () => {
  try {
    const reviews = await scraper(
      "https://www.google.com.my/maps/place/Suka+Dessert/@3.2422285,101.6476789,15z/data=!4m6!3m5!1s0x31cc47f4c5890dbd:0x19f2a665e68874fe!8m2!3d3.2414465!4d101.6493204!16s%2Fg%2F11h2c1vbtp!5m1!1e1?entry=ttu&g_ep=EgoyMDI1MDQwOS4wIKXMDSoASAFQAw%3D%3D",
      {
        sort_type: "newest",
        search_query: "",
        pages: 1,
        clean: true,
      }
    );

    if (!reviews || reviews.length === 0) {
      console.log("⚠️ No reviews found. Check the place URL or try increasing the page count.");
      return;
    }

    const csv = parse(reviews);
    fs.writeFileSync("suka_dessert_reviews.csv", csv);
    console.log("✅ Reviews saved to suka_dessert_reviews.csv");
  } catch (err) {
    console.error("❌ Error scraping reviews:", err);
  }
};

run();
