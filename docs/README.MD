## <u>Notes : </u>
<table>
<tbody>
<tr>
<td><b>Custom field</b></td>
<td>When you create custom model fields, make them generic. Avoid hardcoding data that depends on a specific model or field. Your field should work in any model.</td>
</tr>
<tr>
<td><b>Mixins</b></td>
<td>special kind of multiple inheritance for a class. You can use them to provide common discrete functionality that, when added to other mixins, allows you to define the behavior of a class</td>
</tr>
</tbody>
</table>

---------
- Django's authentication framework includes a permission system that allows you to assign permissions to users and groups
    - Users that have is_superuser set to True have all permissions automatically.
    

---------
-----
## creating a formset :
1.  forms.py >>>  moduleFormSet
2. views.py >>> CourseModuleUpdateView
3. urls >>> "manage_course_module"
4. templates >>> formset.html

- new stuff :
  - formsets :
    - an abstraction layer to work with multiple forms on the same page.
    
   - TemplateResponseMixin: 
        - This mixin takes charge of rendering templates and returning an HTTP response. It requires a template_name attribute that indicates the template to be rendered and provides the render_to_ response() method to pass it a context and render the template.
  
-----

- `from django.apps import apps` :
    - ex. you can use the `apps` to get a model form an app in your project
        - `apps.get_model(app_label='courses', model_name=model_name)`
-----


