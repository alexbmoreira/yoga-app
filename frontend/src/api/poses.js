import axios from "axios";

async function getPoses() {
	var records = [];
	var page = "/api/poses"

    do {
		var response = await axios.get(page);

		var next_split = (response.data.next) ? response.data.next.split("/") : null;
		page = (next_split) ? `${next_split[next_split.length - 3]}/${next_split[next_split.length - 2]}/${next_split[next_split.length - 1]}` : null;

		records = records.concat(response.data.results);
    } while (page !== null);

	return records;

	// const response = await axios.get("/api/poses/");
	// return response.data.results;
}

export default {
	getPoses,
};
