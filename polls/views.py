from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#问题详情视图p3
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

#投票结果视图p3
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#投票操作视图p3
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)