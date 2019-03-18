from django.shortcuts import render, get_object_or_404
from .models import Member
from savings.models import SavingAccount
from loans.models import LoanAccount,LoanIssue
from shares.models import ShareAccount

# Create your views here.

def member(request):
    template = 'members/members.html'

    members = Member.objects

    context = {
            'members': members,
            }
    
    return render(request, template, context)

def member_detail(request, mem_number):
    template = 'members/member_details.html'

    member = get_object_or_404(Member, mem_number=mem_number)
    saving_ac = get_object_or_404(SavingAccount, owner=member)
    loan_ac = get_object_or_404(LoanAccount, owner=member)
    share_ac = get_object_or_404(ShareAccount, owner=member)
    pending_loan = LoanIssue.objects.filter(account=loan_ac, status="Pending")
    approved_loan = LoanIssue.objects.filter(account=loan_ac, status="Approved")
    
    context = {
            'member': member,
            'saving_ac': saving_ac,
            'loan_ac': loan_ac,
            'share_ac': share_ac,
            'pending_loan': pending_loan,
            'approved_loan': approved_loan,
    }

    return render(request, template, context)
