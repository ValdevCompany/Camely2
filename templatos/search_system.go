package main

import (
	
	"net/http"
)

func main() {
	// Парсим HTML-шаблоны
	tmpl, err := template.ParseFiles("templates/index.html", "main2.css")
	if err != nil {
		panic(err)
	}

	// Устанавливаем обработчик запросов для главной страницы
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		// Используем HTML-шаблон для генерации страницы
		err := tmpl.ExecuteTemplate(w, "index.html", nil)
		if err != nil {
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			return
		}
	})

	// Устанавливаем обработчик запросов для страницы "О нас"
	http.HandleFunc("/about", func(w http.ResponseWriter, r *http.Request) {
		// Используем HTML-шаблон для генерации страницы
		err := tmpl.ExecuteTemplate(w, "about.html", nil)
		if err != nil {
			http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			return
		}
	})

	// Обработка статических файлов в каталоге "static"
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))

	// Запускаем сервер на порту 8080
	http.ListenAndServe(":8080", nil)
}
