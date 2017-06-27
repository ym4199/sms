# Create your views here.
from django.shortcuts import render
from django.views.decorators.debug import sensitive_variables
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

from utils.utils import util_api_key, util_api_secret,util_send_from_number


@sensitive_variables('api_key', 'api_secret', 'send_from_number')
def send_sms(request):
    api_key = 'NCSGLMHSQ2FTVZUA'
    api_secret = '2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F'
    send_from_number = '01029953874'

    if request.method == 'POST':
        info = request.POST

        params = dict()
        params['type'] = 'sms'
        params['to'] = info['send_to']
        params['from'] = send_from_number
        params['text'] = info['send_text']

        cool = Message(api_key, api_secret)

        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

            else:
                context = {
                    'send_to': params['to'],
                    'send_text': params['text'],
                }

                return render(request, 'sms.html', context)

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)

    else:
        context = {
            'send_from': send_from_number
        }

        return render(request, 'sms.html', context)
