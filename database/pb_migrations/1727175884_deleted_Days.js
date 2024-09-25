/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("fj1dj2gg49b290v");

  return dao.deleteCollection(collection);
}, (db) => {
  const collection = new Collection({
    "id": "fj1dj2gg49b290v",
    "created": "2024-09-24 10:17:04.705Z",
    "updated": "2024-09-24 10:17:32.514Z",
    "name": "Days",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "nndtzbal",
        "name": "Day_name",
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
})
