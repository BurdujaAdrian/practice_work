/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("4i53pyqjukl7lxi")

  // update
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

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "s1uabzop",
    "name": "Group",
    "type": "relation",
    "required": false,
    "presentable": true,
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
})
