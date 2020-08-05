from pkg_resources import get_distribution

from app.views import app


def describe_spec():
    def it_contains_the_version(expect):
        request, response = app.test_client.get("/api/docs/swagger.json")
        expect(response.status) == 200
        expect(response.json["info"]["version"]) == get_distribution("memegen").version