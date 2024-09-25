/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "fj1dj2gg49b290v",
    "created": "2024-09-24 10:17:04.705Z",
    "updated": "2024-09-24 10:17:04.705Z",
    "name": "Days",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "tjjmo5nl",
        "name": "field",
        "type": "date",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": "",
          "max": ""
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
  const collection = dao.findCollectionByNameOrId("fj1dj2gg49b290v");

  return dao.deleteCollection(collection);
})
