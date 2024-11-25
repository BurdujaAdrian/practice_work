/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // add
  collection.schema.addField(new SchemaField({
    "system": false,
    "id": "pzwtlqwl",
    "name": "Lesson_type",
    "type": "select",
    "required": false,
    "presentable": false,
    "unique": false,
    "options": {
      "maxSelect": 1,
      "values": [
        "Course",
        "Seminar",
        "Laboratory"
      ]
    }
  }))

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("g2jtehu21syq6y3")

  // remove
  collection.schema.removeField("pzwtlqwl")

  return dao.saveCollection(collection)
})
