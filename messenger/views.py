from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import PermissionDenied
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
	msgs = Message.objects.filter(recipient=request.user)
	return render(request, 'messenger/inbox.html', {'messages_list': msgs})

@login_required
def sent(request):
	msgs = Message.objects.filter(sender=request.user)
	return render(request, 'messenger/sent.html', {'messages_list': msgs})

@login_required
def detail(request, pk):
	msg = get_object_or_404(Message, pk=pk)
	if msg.recipient != request.user and msg.sender != request.user:
		raise PermissionDenied('No tenés permiso para ver este mensaje.')
	# marcar como leído si el receptor lo abre
	if msg.recipient == request.user and not msg.is_read:
		msg.is_read = True
		msg.save(update_fields=['is_read'])
	return render(request, 'messenger/detail.html', {'message_obj': msg})

@login_required
def compose(request):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			new_msg = form.save(commit=False)
			new_msg.sender = request.user
			new_msg.save()
			messages.success(request, 'Mensaje enviado.')
			return redirect('messenger:inbox')
		else:
			messages.error(request, 'Revisá los errores.')
	else:
		form = MessageForm()
	return render(request, 'messenger/compose.html', {'form': form})
