from __future__ import absolute_import, unicode_literals
from django.views.generic import RedirectView, TemplateView, View
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from on_admin.users.models import User
import requests


class DashboardRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("dashboard:dashboard")


class DashboardMainView(LoginRequiredMixin, TemplateView):
    '''
    A Template View to display dashboard
    '''

    template_name = 'dashboard/dashboard.html'


    def get_context_data(self, **kwargs):
        ctx = super(DashboardMainView, self).get_context_data(**kwargs)


        ctx.update({
                'overall_status': 'OK',
                'overall_message': 'All services and hosts are up and running',
                'services': {
                            'overall_status': 'OK',
                            'count': '2 running',
                            'services':
                            [
                                {'name': 'Openfire',
                                 'status': 'Running'
                                },
                                {'name': 'Kamailio',
                                 'status': 'Running'
                                }
                            ]
                    },
                'hosts': {
                         'overall_status': 'OK',
                         'count': '1 active',
                         'hosts':
                         [
                            {'name': 'app',
                             'IP': '192.168.100.1',
                             'status': 'Active'
                            }
                         ]
                    },
                'notifications': [
                         {'Date': '22 July 2015 0715HR',
                          'Loglevel': 'Info',
                          'Message': 'All services running.'
                         },
                         {'Date': '22 July 2015 0615HR',
                          'Loglevel': 'Warning',
                          'Message': 'Openfire was restarted.'
                         },
                         {'Date': '22 July 2015 0415HR',
                          'Loglevel': 'Error',
                          'Message': 'Openfire was stopped.'
                         },

                    ]
            })
        return ctx

    def dispatch(self, *args, **kwargs):
        return super(DashboardMainView, self).dispatch(*args, **kwargs)


class DashboardManageView(LoginRequiredMixin, TemplateView):
    '''
    A Template View to display manage control
    '''

    template_name = 'dashboard/manage.html'


    def get_context_data(self, **kwargs):
        ctx = super(DashboardManageView, self).get_context_data(**kwargs)


        ctx.update({
                'services': {
                            'overall_status': 'OK',
                            'count': '3 running',
                            'services':
                            [
                                {'name': 'Openfire',
                                 'host': 'AppServer',
                                 'uptime': '1 day 17:33:23',
                                 'status': 'Running'
                                },
                                {'name': 'Kamailio',
                                 'host': 'AppServer',
                                 'uptime': '07:55:49',
                                 'status': 'Running'
                                },
                                {'name': 'FreeSwitch',
                                 'host': 'ProxyServer',
                                 'uptime': '1 week 11:23:04',
                                 'status': 'Running'
                                },

                            ]
                    },
                'hosts': {
                         'overall_status': 'OK',
                         'count': '2 active',
                         'hosts':
                         [
                            {'name': 'AppServer',
                             'IP': '192.168.100.1',
                             'status': 'Active',
                             'services_running': 2,
                             'services_stopped': 0
                            },
                            {'name': 'ProxyServer',
                             'IP': '192.168.100.2',
                             'status': 'Active',
                             'services_running': 1,
                             'services_stopped': 0
                            }
                         ]
                    }
            })
        return ctx

    def dispatch(self, *args, **kwargs):
        return super(DashboardManageView, self).dispatch(*args, **kwargs)


class DashboardUserView(LoginRequiredMixin, TemplateView):
    '''
    A Template View to display user control
    '''

    template_name = 'dashboard/user.html'


    def get_context_data(self, **kwargs):
        ctx = super(DashboardUserView, self).get_context_data(**kwargs)


        ctx.update({
                'overall_status': 'OK',
                'overall_message': 'All services and hosts are up and running',
                'services': {
                            'overall_status': 'OK',
                            'count': '2 running',
                            'services':
                            [
                                {'name': 'Openfire',
                                 'status': 'Running'
                                },
                                {'name': 'Kamailio',
                                 'status': 'Running'
                                }
                            ]
                    },
                'hosts': {
                         'overall_status': 'OK',
                         'count': '1 active',
                         'hosts':
                         [
                            {'name': 'app',
                             'IP': '192.168.100.1',
                             'status': 'Active'
                            }
                         ]
                    },
                'notifications': [
                         {'Date': '22 July, 2015',
                          'Loglevel': 'Warning',
                          'Message': 'Openfire was restarted on 22 July 2015 0615HR.'
                         }
                    ]
            })
        return ctx

    def dispatch(self, *args, **kwargs):
        return super(DashboardUserView, self).dispatch(*args, **kwargs)


class testAjaxCall(View):
    '''
    AJAX call to generate keys
    '''

    def send_simple_message(self):
        return requests.post(
            "https://api.mailgun.net/v3/wheelaccess.info/messages",
            auth=("api", "key-9a1f3b474424cca0aefff503afc697d8"),
            data={"from": "Excited User <mailgun@accessibility.place>",
                  "to": ["anduslim@gozolabs.com.com", "anduslim@gozolabs.com"],
                  "subject": "Hello",
                  "text": "Testing some Mailgun awesomness!"})

    def get(self, request):
        data = request.GET
        self.send_simple_message()

        return HttpResponse("Okay", status=200)
