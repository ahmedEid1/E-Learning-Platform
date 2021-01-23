<h2>TODO</h2>

- complete the content view by :
  - module_content_list URL
  - a view for deleting content

<hr>

<h2>apps</h2>
- courses
<p></p>
<hr>



---
### Technologies
- Django
- django-braces
- django-embed-video
- django-memcache-status
- Django REST framework 
- Jquery
- jQuery UI
- MemCache
  - python binding: 
      `python-memcached`
- channels
- Redis 
- channels-redis
---
# New 

## urls :
- ### `/`
    - ##### `Courses List` 
        - view : `courses/views.py#CourseListView`
        - template : `courses/course/list.html` 
        - all the courses and a list of all the subjects to only show courses belonging to this Subject
            - every subject has the number of courses it has
            - evert course card show :
                - subject the course belong to
                - number of modules in the course
                - name of the Instructor
-----
- ### accounts
    - `/login` :
        - login page
    - `/logout` :
        - logout page 
    - ##### views :
        - `django.contrib.auth`
            - `LoginView`
            - `LogoutView`
    - ##### note :
        - the templates for the two pages are overridden using :
            - `templates/registration/`
               - `login.html`
               - `logged_out.html`
---
- ### `admin` 
    - need to be a superuser to access the admin panel
    - only a superuser can add new subjects or make a user a teacher by giving them the right permission
        - a teacher can add new courses and add modules and content to the courses he owns
    - ##### views 
        - `django.contrib.admin.site.urls`
----
- ### `course/`
    - `include('courses.urls')` : 
        - all urls under the courses' app start with `course/`
  
- #### `mine/` (Login Require)
    - list of the courses the user (teacher) created
      - can edit the course, 
      - edit its modules, 
      - manging the content of a module,
      - deleting a course,
      - creating a new course,
        
    - view : `ManageCourseListView`
    - template : `courses/manage/course/list.html`
-----

   














