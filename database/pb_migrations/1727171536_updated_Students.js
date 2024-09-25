/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("4i53pyqjukl7lxi")

  // remove
  collection.schema.removeField("brfohy0d")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "s1uabzop",
    "name": "Group",
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
  const collection = dao.findCollectionByNameOrId("4i53pyqjukl7lxi")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "brfohy0d",
    "name": "Group",
    "type": "relation",
    "required": true,
    "presentable": false,
    "unique": false,
    "options": {
      "collectionId": "4i53pyqjukl7lxi",
      "cascadeDelete": false,
      "minSelect": null,
      "maxSelect": null,
      "displayFields": null
    }
  }))

  // remove
  collection.schema.removeField("s1uabzop")

  return dao.saveCollection(collection)
})
