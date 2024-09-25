/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // remove
  collection.schema.removeField("qlsniawp")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "lhfqc8va",
    "name": "Group_ID",
    "type": "relation",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "collectionId": "ank945szqeli4r0",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": 1,
      "displayFields": null
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "qlsniawp",
    "name": "Group",
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
  collection.schema.removeField("lhfqc8va")

  return dao.saveCollection(collection)
})
