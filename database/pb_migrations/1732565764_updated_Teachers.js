/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("8iphudqxe2obnzp")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "k1kcseec",
    "name": "Password",
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

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("8iphudqxe2obnzp")

  // update
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "k1kcseec",
    "name": "Password",
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
})
