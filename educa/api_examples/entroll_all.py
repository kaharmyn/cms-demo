import requests

username = "monore"
password = "190698ahat"
base_url = "http://127.0.0.1:8000/api/"

r = requests.get(f"{base_url}courses/")
courses = r.json()

available_courses = ", ".join([course["title"] for course in courses])
print(f"Available courses: {available_courses}")

for course in courses:
    course_id = course["id"]
    course_title = course["title"]
    r = requests.post(
        f"{base_url}courses/{course_id}/enroll/", auth=(username, password)
    )  # noqa: E501
    if r.status_code == 200:
        # request success
        print(f"Successfully enrolled in {course_title}")
