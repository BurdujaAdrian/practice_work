/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("4i53pyqjukl7lxi")

  // remove
  collection.schema.removeField("ryfonroa")

  // remove
  collection.schema.removeField("0hbub5gh")

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
    "id": "ryfonroa",
    "name": "Group",
    "type": "text",
    "required": true,
    "presentable": false,
    "unique": false,
    "options": {
      "min": null,
      "max": null,
      "pattern": ""
    }
  }))

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "0hbub5gh",
    "name": "Year",
    "type": "number",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "min": 1,
      "max": 4,
      "noDecimal": false
    }
  }))

  // remove
  collection.schema.removeField("brfohy0d")

  return dao.saveCollection(collection)
})
