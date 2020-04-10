'''from flask import Flask, render_template, redirect, request, url_for, Blueprint, jsonify
from data.categories import Category
from data.questions import Question
from data.users import User
from data.games import Game
from data import db_session
import requests

blueprint = Blueprint('questions_api', __name__, template_folder='templates')


@blueprint.route('/api/question/<int:question_id>',  methods=['GET'])
def get_one_question(question_id):
    session = db_session.create_session()
    questions = session.query(Question).get(question_id)
    if not questions:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'question':
                questions.to_dict(only=('id', 'text', 'category.name', 'who_add.name', 'answers', 'right_answer'))
        }
    )


@blueprint.route('/api/questions',  methods=['GET'])
def get_questions():
    session = db_session.create_session()
    questions = session.query(Question).all()
    if not questions:
        return jsonify({'error': 'Not found'})

    return jsonify(
        {
            'questions':
                [item.to_dict(only=('id', 'text', 'category.name', 'who_add.name', 'answers', 'right_answer'))
                 for item in questions]
        }
    )'''