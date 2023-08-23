# views.py

# from django.shortcuts import render
# from .mongodb import get_job_data
# from .forms import JobSearchForm

# myapp/views.py

from django.shortcuts import render
from .forms import JobSearchForm
from .mongodb import get_job_data
from .mongodb import get_job_search



def job_list(request):
    # Get job data from MongoDB
    job_data = get_job_data()

    # Handle job search
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            # Perform search logic based on search_query, e.g., filter job_data
            
            job_data = get_job_search(search_query)
            


    else:
        form = JobSearchForm()

    # Pass the data to the template
    return render(request, 'myapp/job_list.html', {'job_data': job_data, 'form': form})

# # views.py
# job_data = get_job_data()

def search_jobs(request):
    job_data = get_job_data()
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            
            # Process the form data and perform the search
            search_query = form.cleaned_data['search_query']
            
            # Perform the search logic using search_query
            # ...
            return render(request, 'myapp/job_list.html', {'job_data': job_data, 'form': form})
    else:
        form = JobSearchForm()
    return render(request, 'myapp/job_list.html', {'form': form})


# def job_list(request):
#     job_data = get_job_data()

#     # Create a search form instance and handle form submission
#     form = JobSearchForm(request.GET)
#     if form.is_valid():
#         search_query = form.cleaned_data['search_query']
#         if search_query:
#             job_data = job_data.filter(job_title__icontains=search_query)

#     # if request.method == 'POST':
#     #     form = JobSearchForm(request.POST)
#     #     if form.is_valid():
#     #         search_query = form.cleaned_data['search_query']
#     #         # Filter job_data based on search_query, e.g., using MongoDB queries
#     #         # Update job_data with filtered results

#     # else:
#     #     form = JobSearchForm()

#     return render(request, 'myapp/job_list.html', {'job_data': job_data, 'form': form})

