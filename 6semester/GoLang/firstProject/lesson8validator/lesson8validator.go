package lesson8validator

import "net/http"
import "github.com/go-playground/validator"

func Main() {

}

func validate(r *http.Request) error {
	var user struct {
		Username string `json:"username" validate:"required"`
		Name     string `json:"name" validate:"required"`
		Email    string `validate:"required,email"`
	}
	err := validator.New().Struct(user)
	if err != nil {
		return err
	}
	return nil
}
