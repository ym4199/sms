# Create your views here.
from django.shortcuts import render
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


def send_sms(request):
    if request.method == 'POST':
        info = request.POST

        api_key = "replace value"
        api_secret = "replace value"

        params = dict()
        params['type'] = 'sms'
        params['to'] = info['send_to']
        params['from'] = '010********'
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
            'send_from': '01029953874'
        }

        return render(request, 'sms.html', context)
