/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "8iphudqxe2obnzp",
    "created": "2024-09-24 10:55:27.761Z",
    "updated": "2024-09-24 10:55:27.761Z",
    "name": "Teachers",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "kzqaqsaw",
        "name": "Surname",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      },
      {
        "system": false,
        "id": "aq6ceqix",
        "name": "Name",
        "type": "text",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": null,
          "max": null,
          "pattern": ""
        }
      }
    ],
    "indexes": [],
    "listRule": null,
    "viewRule": null,
    "createRule": null,
    "updateRule": null,
    "deleteRule": null,
    "options": {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("8iphudqxe2obnzp");

  return dao.deleteCollection(collection);
})
