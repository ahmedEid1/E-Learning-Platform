- formsets :
    - an abstraction layer to work with multiple forms on the same page.
    

- TemplateResponseMixin: 
  - This mixin takes charge of rendering templates and returning an HTTP response. It requires a template_name attribute that indicates the template to be rendered and provides the render_to_ response() method to pass it a context and render the template.
  
-----
## creating a formset to handle a course modules :
1.  forms.py >>>  moduleFormSet
2. views.py >>> CourseModuleUpdateView
3. urls >>> "manage_course_module"
4. templates >>> formset.html
-----