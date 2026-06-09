const { getJson } = require("serpapi");

getJson(
  {
    engine: "google_lens",
    url:"https://picsum.photos/seed/picsum/200/300",
    api_key: "666154b108bd667b6469f7e1aca84d23303c28a74ba183cc0ba4c1925e6612c1",
  },
  (json) => {
    console.log(json['visual_matches']);
  },
);
