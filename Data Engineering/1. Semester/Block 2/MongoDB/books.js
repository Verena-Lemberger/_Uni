const { MongoClient } = require("mongodb")
const url = "mongodb://localhost:27017"

const book1 = require("./data/books/book1.json")
const book2 = require("./data/books/book2.json")

const options = {
	useNewUrlParser: true,
	useUnifiedTopology: true
}

const createCollection = async () => {
	return MongoClient.connect(url, options, (err, db) => {
		if (err) throw err

		console.log("connected to db")

		const dbo = db.db("books")
		return dbo.createCollection("books", (err) => {
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

		const dbo = db.db("books")
		dbo.collection("books").insertOne(book1, (err) => {
			if (err) throw err
			console.log("book 1 inserted")
		})


		return dbo.collection("books").insertOne(book2, (err) => {
			if (err) throw err
			console.log("book 2 inserted")

			console.log("closing connection")
			db.close()
		})


	})
}

const queryData = async () => {
	return MongoClient.connect(url, options, (err, db) => {
		if (err) throw err

		console.log("connected to db")

		const dbo = db.db("books")

		//  Gebt alle Objekte in der Collection aus.
		dbo.collection("books").find({}).toArray((err, result) => {
			if (err) throw err
			console.log({result})

		})

		//  Gebt das Buch mit der ISBN 9781449373320 aus
		let query = { "ISBN-13": 9781449373320 }
		dbo.collection("books").find(query).toArray((err, result) => {
			if (err) throw err
			console.log({result})

		})

		//  Gebt alle Bücher aus, deren Preis über $ 45,- liegt.
		query = {"ListPrice": { $gt: 45 }}
		dbo.collection("books").find(query).toArray((err, result) => {
			if (err) throw err
			console.log({result})

		})

		//  Gebt alle Bücher des "O'Reilly Media" Verlags aus, die "Martin Kleppmann" geschrieben hat.
		query = {
			Publisher: "O'Reilly Media",
			"Authors": { $in:[ "Martin Kleppmann" ] }
		}
		dbo.collection("books").find(query).toArray((err, result) => {
			if (err) throw err
			console.log({result})

		})

		//  Gebt alle Bücher von AutorInnen mit dem Vornamen "Martin" aus.
		query = {
			"Authors": { $in:[ "Martin Kleppmann" ] }
		}
		dbo.collection("books").find(query).toArray((err, result) => {
			if (err) throw err
			const res = result.filter(r => r.Authors.map(a => a.includes("Martin")))
			console.log({res})

		})

		//   Gebt alle Bücher und die jeweilige Anzahl von AutorInnen aus.
		dbo.collection("books").aggregate([
			{$unwind: "$Authors"},
			{$group: {_id: "$_id", "sum": { $sum: 1}}},
			{$group: {_id: "$_id", authors: {"$sum": "$sum"}}}
		]).toArray((err, result ) => {
			if (err) throw err
			console.log({result})

		})

		//  Gebt die Gesamtzahl an Büchern an, die in der Collection gespeichert sind.
		dbo.collection("books").aggregate([
			{ $count: "numberOfBooksStored" }
		]).toArray((err, result ) => {
			if (err) throw err
			console.log({result})
			db.close()
		})

	})
}

const cleanDB = async () => {
	return MongoClient.connect(url, options, (err, db) => {
		if (err) throw err
		var dbo = db.db("books")
		return dbo.collection("books").drop(function(err, delOK) {
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