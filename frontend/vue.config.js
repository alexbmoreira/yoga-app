module.exports = {
	devServer: {
		proxy: {
			"^/api": {
                target: "https://namastebuilder.herokuapp.com",
				changeOrigin: true,
			},
		},
	},
};
