/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("4i53pyqjukl7lxi")

  // update
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

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("4i53pyqjukl7lxi")

  // update
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
      "maxSelect": 1,
      "displayFields": null
    }
  }))

  return dao.saveCollection(collection)
})
