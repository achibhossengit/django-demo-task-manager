from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget, label='Due Date')
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[])


    def __init__(self, *args, **kwargs):
        employees = kwargs.pop('employees', [])
        # print(employees)
        super().__init__(*args, **kwargs)
        # print(self.fields)
        self.fields['assigned_to'].choices = [(emp.id, emp.name) for emp in employees]