/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const collection = new Collection({
    "id": "verojf4b6niygsl",
    "created": "2024-11-25 21:11:14.854Z",
    "updated": "2024-11-25 21:11:14.854Z",
    "name": "Schedule_even",
    "type": "base",
    "system": false,
    "schema": [
      {
        "system": false,
        "id": "ghzshudp",
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
      },
      {
        "system": false,
        "id": "rruh1rqu",
        "name": "Day",
        "type": "select",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "maxSelect": 1,
          "values": [
            "Mon",
            "Tue",
            "Wed",
            "Thu",
            "Fri",
            "Sat"
          ]
        }
      },
      {
        "system": false,
        "id": "za6trnmc",
        "name": "Period",
        "type": "number",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "min": 1,
          "max": 7,
          "noDecimal": false
        }
      },
      {
        "system": false,
        "id": "nkgfvbsk",
        "name": "Subject",
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
        "id": "bp8mafct",
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
      },
      {
        "system": false,
        "id": "trtmltc9",
        "name": "Group_ID",
        "type": "relation",
        "required": false,
        "presentable": false,
        "unique": false,
        "options": {
          "collectionId": "ank945szqeli4r0",
          "cascadeDelete": false,
          "minSelect": null,
          "maxSelect": 1,
          "displayFields": null
        }
      },
      {
        "system": false,
        "id": "7qbqyzoj",
        "name": "Classroom",
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
  const collection = dao.findCollectionByNameOrId("verojf4b6niygsl");

  return dao.deleteCollection(collection);
})
