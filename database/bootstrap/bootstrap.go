package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os/exec"
	"time"
)

func main() {
	// Step 1: Start Pocketbase server
	fmt.Println("Starting Pocketbase server...")
	pbCmd := exec.Command("../myapp.exe", "serve") // Adjust if necessary
	err := pbCmd.Start()
	if err != nil {
		log.Fatalf("Failed to start Pocketbase: %v", err)
	}

	// Step 2: Wait for Pocketbase to serve on localhost:8090
	waitForServer("http://localhost:8090/api/health") // Check if the server is up

	// Step 3: Start Ngrok
	fmt.Println("Starting Ngrok...")
	ngrokCmd := exec.Command("ngrok", "http", "8090")
	err = ngrokCmd.Start()
	if err != nil {
		log.Fatalf("Failed to start Ngrok: %v", err)
	}

	// Step 4: Get the public URL from Ngrok
	time.Sleep(2 * time.Second) // Allow Ngrok to initialize
	ngrokURL, err := getNgrokPublicURL()
	if err != nil {
		log.Fatalf("Failed to get Ngrok public URL: %v", err)
	}
	fmt.Printf("Ngrok public URL: %s\n", ngrokURL)
}

func waitForServer(url string) {
	for {
		resp, err := http.Get(url)
		if err == nil && resp.StatusCode == 200 {
			fmt.Println("Pocketbase is up and running!")
			return
		}
		fmt.Println("Waiting for Pocketbase to be ready...")
		time.Sleep(2 * time.Second)
	}
}

func getNgrokPublicURL() (string, error) {
	// Ngrok provides an API endpoint to fetch the tunnels
	resp, err := http.Get("http://127.0.0.1:4040/api/tunnels")
	if err != nil {
		return "", fmt.Errorf("could not get Ngrok tunnels: %v", err)
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return "", fmt.Errorf("could not read Ngrok response: %v", err)
	}

	// Parse the JSON to get the public URL
	var ngrokData map[string]interface{}
	if err := json.Unmarshal(body, &ngrokData); err != nil {
		return "", fmt.Errorf("failed to parse Ngrok JSON: %v", err)
	}

	tunnels := ngrokData["tunnels"].([]interface{})
	firstTunnel := tunnels[0].(map[string]interface{})
	publicURL := firstTunnel["public_url"].(string)

	return publicURL, nil
}
