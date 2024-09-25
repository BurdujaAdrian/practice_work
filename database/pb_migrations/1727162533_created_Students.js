/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "4i53pyqjukl7lxi",
    "created": "2024-09-24 07:22:13.437Z",
    "updated": "2024-09-24 07:22:13.437Z",
    "name": "Students",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "ibn27bgl",
        "name": "Surname",
        "type": "text",
        "required": true,
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
        "id": "jguiztgv",
        "name": "Name",
        "type": "text",
        "required": true,
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
        "id": "wui6g3ca",
        "name": "Code",
        "type": "text",
        "required": true,
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
  const collection = dao.findCollectionByNameOrId("4i53pyqjukl7lxi");

  return dao.deleteCollection(collection);
})
