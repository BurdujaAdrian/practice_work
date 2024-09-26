package main

import (
	//	"encoding/json"
	"github.com/labstack/echo/v5"
	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
	"log"
	"net/http"
	"os"
	//	"os/exec"
)

func main() {
	app := pocketbase.New()

	// serves static files from the provided public dir (if exists)
	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/*", apis.StaticDirectoryHandler(os.DirFS("./pb_public"), false))
		return nil
	})

	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		// Register new "POST /upload" route for uploading a file
		e.Router.POST("/upload", func(c echo.Context) error {
			// Source: Retrieve file from the request
			file, err := c.FormFile("file")
			if err != nil {
				return c.String(http.StatusBadRequest, "File not found in request")
			}

			// Open the uploaded file
			src, err := file.Open()
			if err != nil {
				return c.String(http.StatusInternalServerError, "Could not open the uploaded file")
			}
			defer src.Close()

			// Destination: Create a file on the server to save the uploaded file
			dst, err := os.Create("./uploads/" + file.Filename)
			if err != nil {
				return c.String(http.StatusInternalServerError, "Could not create destination file")
			}
			defer dst.Close()

			// Copy the uploaded file data to the destination file
			if _, err := dst.ReadFrom(src); err != nil {
				return c.String(http.StatusInternalServerError, "Error saving the file")
			}

			return c.String(http.StatusOK, "File uploaded successfully")
		}, apis.ActivityLogger(app))

		return nil
	})

	if err := app.Start(); err != nil {
		log.Fatal(err)
	}

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
