/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "grs60uqv",
    "name": "Week_type",
    "type": "select",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSelect": 1,
      "values": [
        "Odd",
        "Even"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // remove
  collection.schema.removeField("grs60uqv")

  return dao.saveCollection(collection)
})
