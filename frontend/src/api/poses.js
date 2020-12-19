import axios from "axios";

async function getPoses() {
	// var results = []
	// var next = "1"

	// while(next !== null)
	// {
	// 	const response = await axios.get("/api/poses/");
	// 	results += response.data.results
	// 	next = response.data.next
	// }
	// return results;

	const response = await axios.get("/api/poses/");
	return response.data.results;
}

export default {
	getPoses,
};
