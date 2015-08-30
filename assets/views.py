from django.shortcuts import render,HttpResponse
import core
import json
# Create your views here.


def asset_report(request):
    if request.method == 'POST':
        ass_handler = core.Asset(request)
        if ass_handler.data_is_valid():
            print 'ddd'
            ass_handler.data_inject()
            #return HttpResponse(json.dumps(ass_handler.response))

        return render(request,'assets/asset_report_test.html',{'response':ass_handler.response})
        #else:
            #return HttpResponse(json.dumps(ass_handler.response))

    return HttpResponse('--test--')


def asset_report_test(request):




    return render(request,'assets/asset_report_test.html')

