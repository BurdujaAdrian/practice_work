/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("8iphudqxe2obnzp")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "hei8ksnj",
    "name": "field",
    "type": "email",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "exceptDomains": null,
      "onlyDomains": null
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("8iphudqxe2obnzp")

  // remove
  collection.schema.removeField("hei8ksnj")

  return dao.saveCollection(collection)
})
