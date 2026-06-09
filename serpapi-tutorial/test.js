const {getJson} = require("serpapi");

getJson({
    engine:"google",
    q:"Mysterious Places",
    location:"India,United Kingdom,Spain,Norway",
    google_domain:"google.co.in",
    hl:"en",
    gl:"in",
    api_key:"666154b108bd667b6469f7e1aca84d23303c28a74ba183cc0ba4c1925e6612c1"
})