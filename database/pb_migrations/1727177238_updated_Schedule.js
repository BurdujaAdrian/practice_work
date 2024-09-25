/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // remove
  collection.schema.removeField("azbu3ohb")

  // add
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
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "azbu3ohb",
    "name": "Day",
    "type": "text",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // remove
  collection.schema.removeField("3aoss3oi")

  return dao.saveCollection(collection)
})
