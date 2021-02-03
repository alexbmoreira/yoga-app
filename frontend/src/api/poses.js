import api from '@/api/api.service'

async function getPoses() {
  return api.get('/poses').then(response => response.data.results)
}

// async function getPoses() {
// 	var records = [];
// 	var page = "/api/poses"

//     do {
// 		var response = await axios.get(page);

// 		var next_split = (response.data.next) ? response.data.next.split("/") : null;
// 		page = (next_split) ? `${next_split[next_split.length - 3]}/${next_split[next_split.length - 2]}/${next_split[next_split.length - 1]}` : null;

// 		records = records.concat(response.data.results);
//     } while (page !== null);

// 	return records;
// }

export default {
	getPoses,
};
