import sys
from flask import Blueprint, request

hello = Blueprint(
	"hello",
	__name__,
)

@hello.route("/")
def index():
	return "Hello, Python"