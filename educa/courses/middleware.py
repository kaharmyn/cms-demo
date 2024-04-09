from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect

from .models import Course


def subdomain_course_middleware(get_response):
    """Course subdomain"""

    # fmt:off
    def middleware(request):
        host_parts = request.get_host().split(".")
        if len(host_parts) > 2 and host_parts[0] != "www":
            # get course subdomain
            course = get_object_or_404(Course,
                                       slug=host_parts[0])
            course_url = reverse("course_detail",
                                 args=[course.slug])
            # redirect request to course_detail
            url = "{}://{}{}".format(request.scheme,
                                     ".".join(host_parts[1:]),
                                     course_url)  # noqa:E501
            return redirect(url)
        response = get_response(request)
        return response

    return middleware
