import axios from "axios";

async function getPoses() {
    var records = [];

    // do {
		var response = await axios.get("/api/poses/");

		records = records.concat(response.data.results);
    // } while (response.data.next !== null)

	return records

	// const response = await axios.get("/api/poses/");
	// return response.data.results;
}

export default {
	getPoses,
};
