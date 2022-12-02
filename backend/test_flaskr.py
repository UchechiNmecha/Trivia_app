import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    #GENERATED TEST FOR "get_categories"
def test_get_categories(self):
    res = self.client().get('/categories')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["categories"])

#GENERATEED TEST FOR PAGE REQUEST EXCEEDING NUMBER OF PAGINATED CATEGORIES
def test_404_exceeding_valid_page(self):
    res = self.client().get("/categories?page=1000")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "404 page not found")

#GENERATED TEST FOR WRONG REQUEST METHOD FOR "get_categories"
def test_405_wrong_get_categories_request_method(self):
    res = self.client().patch("/categories")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "405 method not allowed")

#GENERATED TEST FOR "get_questions"
def test_get_questions(self):
    res = self.client().get("/questions")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["questions"])
    self.assertTrue(data["categories"])
    self.assertEqual(data["total_questions"], 19)

#GENERATED TEST FOR WRONG REQUEST METHOD FOR "get_questions"
def test_405_wrong_get_questions_request_method(self):
    res = self.client().patch("/questions")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "405 method not allowed")

#GENERATED TEST FOR "delete_questions"
def test_delete_questions(self):
    res = self.client().delete("/questions/11")
    data = json.loads(res.data)

    question = Question.query.filter(Question.id == 11).one_or_none()

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertEqual(data["deleted"], 11)
    self.assertEqual(question, None)

#GENERATED TEST FOR "delete_questions" ON QUESTION THAT DOES NOT EXIST
def test_422_delete_question_that_does_not_exist(self):
    res = self.client().delete("/questions/3000")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 422)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "unprocessable")

#GENERATED TEST FOR "create_questions"
def test_create_new_question(self):
    res = self.client().post("/add", json=self.new_question)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)

#GENERATED TEST FOR WRONG REQUEST METHOD FOR "create_questions"
def test_405_new_question_creation_not_allowed(self):
    res = self.client().post("/add/20", json=self.new_question)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "method not allowed")

#GENERATED TEST FOR "search_questions"
def test_search_questions(self):
    res = self.client().post("/questions/search", json={"searchTerm": "what"})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(len(data["questions"]))
    self.assertTrue(data["total_questions"])
    self.assertTrue(data["current_category"])

#GENERATED TEST FOR "search_questions" WITH WRONG METHOD
def test_405_search_questions_with_wrong_method(self):
    res = self.client().patch("/questions/search", json={"searchTerm": "what"})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "405 method not allowed")

#GENERATED TEST FOR "search_questions" NOT FOUND
def test_search_questions_not_found(self):
    res = self.client().post("/questions/search", json={"searchTerm": "asdf"})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertEqual(len(data["questions"]), 0)
    self.assertEqual(data["total_questions"], 0)
    self.assertEqual(data["current_category"], 0)

#GENERATED TEST FOR "get_category_questions"
def test_get_category_questions(self):
    res = self.client().get("/categories/2/questions")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(data["total_questions"])
    self.assertTrue(len(data["questions"]))
    self.assertEqual(len(data["current_category"], 2))

#GENERATED TEST FOR "get_category_questions" WITH WRONG METHOD
def test_405_get_category_questions_with_wrong_method(self):
    res = self.client().patch("/questions/2/questions")
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "405 method not allowed")

#GENERATED TEST FOR 'play'
def test_play(self):
    res = self.client().post("/play", json={"previous_questions": [], "quiz_category": {"id": 3, "type": "Geography"}})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)
    self.assertTrue(len(data["question"]))

#GENERATED TEST FOR "play" WITH WRONG METHOD
def test_405_play_with_wrong_method(self):
    res = self.client().patch("/play", json={"previous_questions": [], "quiz_category": {"id": 9, "type": "Astrology"}})
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 405)
    self.assertEqual(data["success"], False)
    self.assertEqual(data["message"], "405 method not allowed")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()