## 0.3.4 (Nov 22,2024)

- Modified the [python script]{https://github.com/BurdujaAdrian/practice_work/blob/main/user-app/pythonProject_Test-main/MainPage.py} and [start_server.bat]{https://github.com/BurdujaAdrian/practice_work/blob/main/database/start_server.bat} to use the static url from ngrok.
- Fixed the issue why the .png were not loaded in github when the 75 records were added to DB, it was not related to gitignore, but now it is fixed (https://github.com/BurdujaAdrian/practice_work/pull/15)
- Changed main.py so that embedding of faces of records from DB are not calculatead each time, a checking procedure was added to check if it was previously computed and to use it instead ()
- Solved the connection issue between backend and DB, it was due to a change of field names (https://github.com/BurdujaAdrian/practice_work/pull/12)
- Worked on researching and trying to use a different host (ngrok)

## 0.3.3 (Nov 8, 2024) 

- We added error handling to the face recognition program to avoid crashes[377a31e](https://github.com/BurdujaAdrian/practice_work/commit/377a31ea2a30695c200626a4da715e876625330e)
- Recognized faces are now moved to the front for clearer display[3247c0e](https://github.com/BurdujaAdrian/practice_work/commit/3247c0ea230979557098c5f3b83f47c15cb05958)
- Populated the database[6db71ce](https://github.com/BurdujaAdrian/practice_work/commit/6db71ce0063a5b1c528974817157eb331ba6a7d2)

## 0.3.0 (Oct 2, 2024) 

- Final version of the demo app [a2e2ca](https://github.com/BurdujaAdrian/practice_work/commit/a2e2ca41d149a99b5e19fb0419f9b3867c2ef853)


* `<function name>`: <changes to function>.



