import axios from "axios";

async function getPoses() {
    const response = await axios.get("/api/poses/");
	return response.data.results;
}

export default {
	getPoses,
};
