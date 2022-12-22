from django.shortcuts import render,redirect
# from django.contrib.auth import authenticate


def compute(req):
  return render(req,"Service/compute.html")

def database(req):
  return render(req,"Service/database.html")

def security(req):
  return render(req,"Service/security.html")

def network(req):
  return render(req,"Service/network.html")

def storage(req):
  return render(req,"Service/storage.html")
