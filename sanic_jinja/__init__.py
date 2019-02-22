from sanic.response import html
from jinja2 import Environment, PackageLoader, select_autoescape
import functools


def generate_template(package_name=None, package_path='templates'):
    if not package_name:
        raise Exception("Error: package_name is None.")

    env = Environment(loader=PackageLoader(package_name=package_name, package_path=package_path),
                      autoescape=select_autoescape(['html', 'xml', 'tpl']))

    def template(env, tpl, **kwargs):
        """
        render template
        :param tpl:
        :param kwargs:
        :return:
        """
        if not env:
            raise Exception("template doesn't init.")
        templ = env.get_template(tpl)
        return html(templ.render(kwargs))

    return functools.partial(template, env)