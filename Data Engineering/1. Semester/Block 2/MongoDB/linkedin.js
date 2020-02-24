const { MongoClient } = require("mongodb")
const url = "mongodb://localhost:27017"

const profile1 = require("./data/linkedin/profile1.json")
const profile2 = require("./data/linkedin/profile2.json")

const options = {
	useNewUrlParser: true,
	useUnifiedTopology: true
}

const createCollection = async () => {
	return MongoClient.connect(url, options, (err, db) => {
		if (err) throw err

		console.log("connected to db")

		const dbo = db.db("linkedin")
		return dbo.createCollection("profiles", (err) => {
			if (err) throw err
			console.log("collection created")

			console.log("closing connection")
			db.close()
		})

	})
}

const insertData = async () => {
	return MongoClient.connect(url, options, (err, db) => {
		if (err) throw err

		console.log("connected to db")

		const dbo = db.db("linkedin")
		dbo.collection("profiles").insertOne(profile1, (err) => {
			if (err) throw err
			console.log("profile 1 inserted")
		})


		return dbo.collection("profiles").insertOne(profile2, (err) => {
			if (err) throw err
			console.log("profile 2 inserted")

			console.log("closing connection")
			db.close()
		})


	})
}

const queryData = async () => {
	return MongoClient.connect(url, options, (err, db) => {
		if (err) throw err

		console.log("connected to db")

		const dbo = db.db("linkedin")

		//  Gebt alle Personen mit dem Vornamen "Kane" aus
		const query = { lastName: "Kane" }
		dbo.collection("profiles").find(query).toArray((err, result) => {
			if (err) throw err
			console.log({result})
		})

		//  Gebt die Gesamtzahl an Objekten, die in der Collection gespeichert sind aus.
		dbo.collection("profiles").aggregate([ { $count: "totalNumberOfDocuments" } ]).toArray((err, result) => {
			if (err) throw err
			console.log({result})
		})

		//  Gebt alle Personen der Collection aus, für die keine "Influencer" Status gesetzt ist.
		dbo.collection("profiles").find({ "influencer" : null }).toArray((err, result) => {
			if (err) throw err
			console.log({result})
		})

		//  Gebt alle Kenntnisse/Fähigkeiten aus, die in der Collection vorkommen
		// und ermittelt wie oft die jeweilige Fähigkeit vorkommt.
		dbo.collection("profiles").aggregate([
			{"$unwind": "$skills"},
			{"$group": {
				"_id": "$skills",
				"anzahl": {"$sum": 1}
			}},

			{"$project": {
				"_id": "$_id.name",
				"anzahl": "$anzahl"
			}}
		]).toArray((err, result) => {
			if (err) throw err

			console.log({result})
		})

		//  Ermittelt die häufigste Fähigkeit, die in der Collection gespeichert ist.
		dbo.collection("profiles").aggregate([
			{"$unwind": "$skills"},
			{"$group": {
				"_id": "$skills",
				"anzahl": {"$sum": 1}
			}},
			{"$project": {
				"_id": "$_id.name",
				"anzahl": "$anzahl"
			}}
		])
			.sort({anzahl:-1})
			.limit(1)
			.toArray((err, result) => {
				if (err) throw err

				console.log({result})
			})


		//  Ermittelt die durchschnittliche Job-Verweildauer aller Personen, die in der Collection gespeichert sind.
		let output = []
		dbo.collection("profiles").aggregate([
			{"$unwind": "$professionalExperience"},
		]).forEach(function(doc){
			const {firstName, lastName, professionalExperience} = doc
			const { startYear, endYear, company } = professionalExperience
			const res = {
				name: `${firstName} ${lastName}`,
				company,
				avg: endYear ? endYear - startYear : 2020 - startYear
			}
			output.push(res)
		}).then(() => {
			const res = [... new Set(output.map(p => p.name))].reduce((acc, name) => {
				acc[name] = {}
				const experience = output.filter(e => e.name === name)
				const avgYears = experience.reduce((acc, item) => acc + item.avg, 0)
				acc[name].avgYears = avgYears / experience.length
				return acc
			}, {})
			console.log(res)
			setTimeout(() => {
				db.close()
			}, 1000)
		})
	})
}

const cleanDB = async () => {
	return MongoClient.connect(url, options, (err, db) => {
		if (err) throw err
		var dbo = db.db("linkedin")
		return dbo.collection("profiles").drop(function(err, delOK) {
			if (err) throw err
			if (delOK) console.log("Collection deleted")
			db.close()
		})
	})
}

const start = () => {
	createCollection()

	setTimeout(() => {
		insertData()
	}, 1000)

	setTimeout(() => {
		queryData()
	}, 2000)

	setTimeout(() => {
		cleanDB()
	}, 5000)
}

start()