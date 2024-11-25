/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "3aoss3oi",
    "name": "Day",
    "type": "select",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSelect": 1,
      "values": [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "3aoss3oi",
    "name": "Day",
    "type": "select",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSelect": 1,
      "values": [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri"
      ]
    }
  }))

  return dao.saveCollection(collection)
})
