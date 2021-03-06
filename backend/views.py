from apps.models import App
from util.view_util import obj_to_dict, iter_to_dict, json_response


def _app_to_obj(app):
    """
    Create
    :param app:
    :return:
    :rtype: dict
    """
    result = obj_to_dict(app, ('fullname', 'description', 'icon_url',
                               'page_url', 'downloads', 'stars_percentage',
                               'votes', 'citation'))
    result['tags'] = [tag.fullname for tag in app.tags.all()]
    result['releases'] = iter_to_dict(app.releases, ('version', 'created_iso',
                                                     'release_download_url',
                                                     'works_with',
                                                     'hexchecksum', 'notes'))
    return result


def all_apps_func(request):
    """
    Gets all App objects that are active with releases

    :param request:
    :return: active App objects with releases in json format
    """
    all_apps = App.objects.filter(active=True)
    all_apps_fmt = [_app_to_obj(app) for app in all_apps if app.has_releases]
    return json_response(all_apps_fmt)
