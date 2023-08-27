from decimal import Decimal
from django.shortcuts import redirect, render
from .forms import AddDish
import json


def menu(request):
    with open("zomato/menu.json") as file:
        dishes = json.load(file, parse_float=Decimal)
        
        form = AddDish()
        
        if request.method == 'POST':
            form = AddDish(request.POST)
            if form.is_valid():
                new_dish = {
                    'dishID':len(dishes) + 1,
                    'name':form.cleaned_data['name'],
                    'price':float(form.cleaned_data['price']),
                    'available':form.cleaned_data['availability']
                }
                dishes.append(new_dish)
                with open('zomato/menu.json', 'w') as menu_file:
                    json.dump(dishes, menu_file, indent=4, default=float)
                return redirect('menu')
            else:
                form = AddDish()
    return render(request,"zomato/menu.html",{"dishes":dishes,"form":form})

def remove_dish(request, dish_id):
    with open("zomato/menu.json") as file:
        dishes = json.load(file)
        
    for dish in dishes:
        if dish['dishID'] == dish_id:
            dishes.remove(dish)
            break
        
    with open('zomato/menu.json', 'w') as menu_file:
        json.dump(dishes, menu_file, indent=4)
    return redirect('menu')