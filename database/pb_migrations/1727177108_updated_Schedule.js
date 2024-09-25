/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // remove
  collection.schema.removeField("jfizpvuq")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "4mgwn5af",
    "name": "Teacher_ID",
    "type": "relation",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "collectionId": "8iphudqxe2obnzp",
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
    "id": "jfizpvuq",
    "name": "Teacher",
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
  collection.schema.removeField("4mgwn5af")

  return dao.saveCollection(collection)
})
