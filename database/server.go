package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
	"os/exec"

	"github.com/labstack/echo/v5"

	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
)

func main() {
	app := pocketbase.New()

	// serves static files from the provided public dir (if exists)
	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/*", apis.StaticDirectoryHandler(os.DirFS("./pb_public"), false))
		return nil
	})

	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/api/py/hello_world", func(c echo.Context) error {
			cmd := exec.Command("python", "../server-app/demo.py")

			response, err := cmd.Output()
			if err != nil {
				return err
			}

			return c.JSON(http.StatusOK, map[string]string{"message": string(response) + " from py"})
		})
		return nil
	})

	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/api/py/lisy", func(c echo.Context) error {
			cmd := exec.Command("python", "../server-app/list.py")

			response, err := cmd.Output()
			if err != nil {
				return err
			}

			var list []string
			err = json.Unmarshal(response, &list)
			if err != nil {
				return c.JSON(http.StatusInternalServerError,
					map[string]string{
						"error": "Failed to parse response"})
			}

			return c.JSON(http.StatusOK,
				map[string]interface{}{
					"messege": list})
		})
		return nil
	})

	if err := app.Start(); err != nil {
		log.Fatal(err)
	}

	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.POST("api/py/attend/:group", func(c echo.Context) error {
			group := c.PathParam("group")
			files := todo()
			_ = group
			_ = files

			return nil

		})
		return nil
	})
}

/* template

app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
	e.Router.GET("/api/py/...", func(c echo.Context) error {

	})
	return nil
})

*/

func todo() uint8 {
	return 0
}
