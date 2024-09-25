/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "ank945szqeli4r0",
    "created": "2024-09-24 09:50:08.413Z",
    "updated": "2024-09-24 09:50:08.413Z",
    "name": "Groups",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "241npkju",
        "name": "FAF_231",
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
  const collection = dao.findCollectionByNameOrId("ank945szqeli4r0");

  return dao.deleteCollection(collection);
})
