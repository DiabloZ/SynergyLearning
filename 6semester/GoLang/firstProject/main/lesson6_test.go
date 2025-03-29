package main

import (
	"firstProject/lesson5"
	. "github.com/smartystreets/goconvey/convey"
	"net/mail"
	"testing"
	"time"
)

func TestGoCheck(t *testing.T) {
	Convey("TestMain", t, func() {
		Convey("Test", func() {
			So(add(2, 3), ShouldEqual, 5)
		})

		Convey("Test2", func() {
			So(add(-2, 3), ShouldEqual, 1)
		})

	})

}

func add(x, y int) int {
	return x + y
}

func TestAdd(t *testing.T) {
	if 1+1 != 2 {
		t.Errorf("1 + 1 = %d, but we need 2", 1+1)
	}
}

func TestUser(t *testing.T) {
	user2 := lesson5.User{
		ID:        3,
		Name:      "Sasdasd",
		Email:     "1@2.com",
		Password:  "SomePass",
		CreatedAt: time.Now().AddDate(0, 0, 1),
	}
	user1 := lesson5.User{
		ID:        2,
		Name:      "SomeName",
		Email:     "1@2.com",
		Password:  "SomePass",
		CreatedAt: time.Now().AddDate(0, 0, 1),
	}
	testUsers := []lesson5.User{
		{
			ID:        1,
			Name:      "Test",
			Email:     "ann@a.com",
			Password:  "some",
			CreatedAt: time.Now(),
		},
		user1,
		user2,
	}

	for _, user := range testUsers {
		if user.ID != 1 && user.ID != 2 && user.ID != 3 {
			t.Errorf("Need user with id 1 or 2, we have %d", user.ID)
		}
		var nameLen = len(user.Name)
		if nameLen < 3 || nameLen > 10 {
			t.Errorf("Name too shor or long - %d", nameLen)
		}
		_, err := mail.ParseAddress(user.Email)
		if err != nil {
			t.Errorf("User Email is not valid - %s", user.Email)
		}

	}
}
