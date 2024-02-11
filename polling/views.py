from django.shortcuts import render

# from django.http import Http404
from polling.models import Poll
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PollListView(ListView):
    """Django based list view"""

    model = Poll
    template_name = "polling/list.html"


class PollDetailView(DetailView):
    """Django based list detail view"""

    model = Poll
    template_name = "polling/detail.html"

    def post(self, request, *args, **kwargs):
        """post method within view class"""
        poll = self.get_object()

        if request.POST.get("vote") == "Yes":
            poll.score += 1
        else:
            poll.score -= 1
        poll.save()

        context = {"object": poll}
        return render(request, "polling/detail.html", context)


# def list_view(request):
#     """view of list of polls"""
#     context = {'polls': Poll.objects.all()}
#     return render(request, 'polling/list.html', context)
#
#
# def detail_view(request, poll_id):
#     """detailed view for each poll"""
#     try:
#         poll = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404
#
#     if request.method == "POST":
#         if request.POST.get("vote") == "Yes":
#             poll.score += 1
#         else:
#             poll.score -= 1
#         poll.save()
#
#     context = {'poll': poll}
#     return render(request, 'polling/detail.html', context)
