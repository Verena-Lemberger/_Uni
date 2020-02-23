const { MongoClient } = require("mongodb")
const url = "mongodb://localhost:27017"

const book1 = require("./data/linkedin/profile1.json")
const book2 = require("./data/linkedin/profile2.json")

const options = {
	useNewUrlParser: true,
	useUnifiedTopology: true
}

MongoClient.connect(url, options, (err, db) => {
	if (err) throw err

	console.log("connected to db")

	const dbo = db.db("linkedin")
	dbo.createCollection("linkedin", (err) => {
		if (err) throw err
		console.log("collection created")

	})

	dbo.collection("linkedin").insertOne(book1, (err) => {
		if (err) throw err
		console.log("profile 1 inserted")
	})


	dbo.collection("linkedin").insertOne(book2, (err) => {
		if (err) throw err
		console.log("profile 2 inserted")
		console.log("closing ...")
		db.close()
	})

	dbo.collection("linkedin").find({}).toArray(function(err, result) {
		if (err) throw err
		console.log({result})
		db.close()
	})

	/**

	 Gebt alle Personen mit dem Vornamen "Kane" aus.
	 Gebt die Gesamtzahl an Objekten, die in der Collection gespeichert sind aus.
	 Gebt alle Personen der Collection aus, für die keine "Influencer" Status gesetzt ist.
	 Gebt alle Kenntnisse/Fähigkeiten aus, die in der Collection vorkommen und ermittelt wie
	oft die jeweilige Fähigkeit vorkommt.
	 Ermittelt die häufigste Fähigkeit, die in der Collection gespeichert ist.
	 Ermittelt die durchschnittliche Job-Verweildauer aller Personen, die in der Collection gespeichert sind.

	*/

})