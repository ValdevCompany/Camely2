package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()

	// Загрузка шаблонов из папки "templates"
	r.LoadHTMLGlob("templates/*")

	r.GET("/", func(c *gin.Context) {
		// Отрисовка шаблона "t.html" и отправка результата
		c.HTML(http.StatusOK, "template.html", nil)
	})

	r.Run(":8080")
}
