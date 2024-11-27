package main

import (
	//	"encoding/json"
	"encoding/base64"
	"github.com/labstack/echo/v5"
	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
	"log"
	"net/http"
	"os"
	"os/exec"
)

func main() {

	app := pocketbase.New()

	// serves static files from the provided public dir (if exists)
	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/*", apis.StaticDirectoryHandler(os.DirFS("./pb_public"), false))
		return nil
	})

	// post image and group, return list of students and their percentege
	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		// Register new "POST /upload" route for uploading a file
		e.Router.POST("/find/:group", func(c echo.Context) error {
			group := c.PathParam("group")

			if group == "" {
				return c.String(http.StatusBadRequest, "group was not specified")
			}
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
			print(group, "\n")
			print(file.Filename, "\n\n")
			cmd := exec.Command(
				"python",
				"-X dev",
				"../server-app/face_recognition/main.py",
				"uploads/"+file.Filename,
				group,
			)
			print(group)

			output, err := cmd.Output()
			if err != nil {
				print(err)
				return c.String(http.StatusInternalServerError, "error runing the python scrips")
			}

			recognisedFacesPath := "../server-app/recognised_faces/"
			files, err := os.ReadDir(recognisedFacesPath)
			if err != nil {
				return c.String(http.StatusInternalServerError, "Error reading recognised faces folder")
			}

			var faceImages []map[string]string
			for _, file := range files {
				if !file.IsDir() {
					filePath := recognisedFacesPath + file.Name()

					// Read the file content
					imageData, err := os.ReadFile(filePath)
					if err != nil {
						return c.String(http.StatusInternalServerError, "Error reading image file: "+file.Name())
					}

					// Encode the file content in Base64
					encodedImage := base64.StdEncoding.EncodeToString(imageData)

					// Append the filename and the encoded image
					faceImages = append(faceImages, map[string]string{
						"filename": file.Name(),
						"content":  encodedImage,
					})
				}
			}

			// Create a response containing the script output and the list of recognised faces
			response := map[string]interface{}{
				"python_output":    string(output),
				"recognised_faces": faceImages,
			}

			return c.JSON(http.StatusOK, response)
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
