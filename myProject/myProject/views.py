from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
               
            )
            
            if user_type=='viewers':
                viewersProfileModel.objects.create(user=user)
                
            elif user_type=='creator':
                creatorProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")

@login_required
def addRecipePage(request):
    
    current_user=request.user
    
    if request.method=='POST':
        
        title=request.POST.get("title")
        ingredients=request.POST.get("ingredients")
        instructions=request.POST.get("instructions")
        prep_time=request.POST.get("prep_time")
        cooking_time=request.POST.get("cooking_time")
        
        total_time=request.POST.get("total_time")
        difficulty=request.POST.get("difficulty")
        nutrition=request.POST.get("nutrition")
        image=request.FILES.get("image")
    
        category=request.POST.get("category")
        Tags=request.POST.get("Tags")
        calories=request.POST.get("calories")
        
        recipe=RecipeModel(
            user=current_user,
            title=title,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time,
            cooking_time=cooking_time,
            total_time=total_time,
            Difficulty=difficulty,
            nutrition=nutrition,
            image=image,
            Category=category,
            Tag=Tags,
            calories=calories
        )
        recipe.save()
        
        return redirect("createdRecipe")
        
    return render(request,"addRecipePage.html")

@login_required
def createdRecipe(request):
    
    recipe=RecipeModel.objects.filter(user=request.user)
    
    context={
        'recipe':recipe
    }
    
    
    return render(request,"createdRecipe.html",context)

@login_required
def viewRecipe(request,recipe_id):
    recipe=RecipeModel.objects.get(id=recipe_id)
    
    context={
        'recipe':recipe
    }
    
    return render(request,"viewRecipe.html",context)

@login_required
def deleteRecipe(request,recipe_id):
    
    recipe=RecipeModel.objects.get(id=recipe_id).delete()
    
    return redirect("createdRecipe")

@login_required
def editRecipe(request,recipe_id):
    
    recipe=RecipeModel.objects.get(id=recipe_id)
    
    current_user=request.user
    
    if request.method=='POST':
        
        r_id=request.POST.get("r_id")
        title=request.POST.get("title")
        ingredients=request.POST.get("ingredients")
        instructions=request.POST.get("instructions")
        prep_time=request.POST.get("prep_time")
        cooking_time=request.POST.get("cooking_time")
        
        total_time=request.POST.get("total_time")
        difficulty=request.POST.get("difficulty")
        nutrition=request.POST.get("nutrition")
        image=request.FILES.get("image")
    
        category=request.POST.get("category")
        Tags=request.POST.get("Tags")
        calories=request.POST.get("calories")
        
        recipe=RecipeModel(
            id=r_id,
            user=current_user,
            title=title,
            ingredients=ingredients,
            instructions=instructions,
            prep_time=prep_time,
            cooking_time=cooking_time,
            total_time=total_time,
            Difficulty=difficulty,
            nutrition=nutrition,
            image=image,
            Category=category,
            Tag=Tags,
            calories=calories
        )
        recipe.save()
        
        return redirect("createdRecipe")
    
    context={
        'recipe':recipe
    }
    return render(request,"editRecipe.html",context)
    
@login_required
def recipeFeed(request):
    recipe=RecipeModel.objects.all()
    
    context={
        'recipes':recipe
    }
    
    return render(request,"recipeFeed.html",context)

@login_required
def editProfile(request):
    
    current_user=request.user
    
    if request.method=='POST':
        username=request.POST.get("username")
        email=request.POST.get("email")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        profile_pic=request.FILES.get("profile_pic")
        
        specialties=request.POST.get("specialties")
        Followers=request.POST.get("Followers")
        Achievements=request.POST.get("Achievements")
        Bio=request.POST.get("Bio")
        interests=request.POST.get("interests")
        
        current_user.username=username
        current_user.email=email
        current_user.first_name=first_name
        current_user.last_name=last_name
        current_user.profile_pic=profile_pic
        
        
        try:
            creatorProfile=creatorProfileModel.objects.get(user=current_user)
            creatorProfile.Specialties=specialties
            creatorProfile.Followers=Followers
            creatorProfile.Achievements=Achievements
            creatorProfile.Bio=Bio
            creatorProfile.save()
            current_user.save()
            
            return redirect("profilePage")
            
        except creatorProfileModel.DoesNotExist:
            creatorProfile=None
            
        try:
            viewersProfile=viewersProfileModel.objects.get(user=current_user)
            viewersProfile.Interests=interests
            viewersProfile.save()
            current_user.save()
            
            return redirect("profilePage")
            
        except viewersProfileModel.DoesNotExist:
            viewersProfile=None
        
    
    return render(request,"editProfile.html")


def recipe_search(request):
    
    query=request.GET.get("query")
    
    if query:
        recipes=RecipeModel.objects.filter(
            Q(title__icontains=query) |
            Q(Category__icontains=query) |
            Q(Tag__icontains=query)|
            Q(user__username__icontains=query)
            )
    else:
        recipes=RecipeModel.objects.none()
        
    context={
        'recipes':recipes,
        'query':query
    }
    
    return render(request,"recipe_search.html",context)
    
    
    