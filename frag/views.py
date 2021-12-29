from django.shortcuts import render
from . import store
# Create your views here.
def home(request):
    dictionary = {'alert':False}
    if request.method == 'POST': # form submitted
        data = request.POST
        button = data.get('action')
        if button == 'Fragment': # if fragment is clicked
            frag_type = data.get('type')
            frag_value = data.get('value')
            frag_type2 = data.get('type2')
            frag_value2 = data.get('value2')
            if frag_type2: # if mixed fragment is done
                if frag_type == 'horizontal':
                    p1, p2 = frag_value, frag_value2
                else:
                    p1, p2 = frag_value2, frag_value
                dictionary = store.mixed_fragment(p1, p2)
            else:
                if frag_type == 'horizontal': # if horizontal fragment is done
                    dictionary = store.horizontal_fragment(frag_value)
                elif frag_type == 'vertical': # if vertical fragment is done
                    dictionary = store.vertical_fragment(frag_value)
        elif button == 'Reset Database': # if reset is pressed
            dictionary = store.reset_database()
        elif button == "Mixed": # if mixed is pressed
            dictionary['mixed']=True
    # fetching all database info
    info = store.info()
    # merging dictionary
    dictionary = dictionary|info
    return render(request, 'frag/home.html',dictionary)