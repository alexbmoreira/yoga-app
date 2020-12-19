import axios from "axios";

async function getPoses() {
	const response = await axios.get("/api/poses");
	return response.data;
}

export default {
	getPoses,
};
