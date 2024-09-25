/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("fj1dj2gg49b290v")

  // remove
  collection.schema.removeField("tjjmo5nl")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "nndtzbal",
    "name": "Day_name",
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

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("fj1dj2gg49b290v")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "tjjmo5nl",
    "name": "field",
    "type": "date",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": "",
      "max": ""
    }
  }))

  // remove
  collection.schema.removeField("nndtzbal")

  return dao.saveCollection(collection)
})
