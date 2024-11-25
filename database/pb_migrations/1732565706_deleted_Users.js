/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("5mwwttrgfyn5lty");

  return dao.deleteCollection(collection);
}, (db) => {
  const collection = new Collection({
    "id": "5mwwttrgfyn5lty",
    "created": "2024-09-24 11:24:01.526Z",
    "updated": "2024-09-24 11:24:01.526Z",
    "name": "Users",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "zxxorygn",
        "name": "Email",
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
        "id": "me2xrlly",
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
